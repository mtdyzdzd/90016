#!/usr/bin/env python3
"""Generate Sprint 2 school-location evidence files from the official CSV."""

from __future__ import annotations

import csv
import html
import math
import sys
import urllib.request
from pathlib import Path


SOURCE_CSV_URL = (
    "https://www.education.vic.gov.au/Documents/about/research/datavic/"
    "dv402-SchoolLocations2025.csv"
)

MELBOURNE_CONNECT_LAT = -37.8001
MELBOURNE_CONNECT_LON = 144.9643
SPRINT2_WP_GO_MAPS_MAP_ID = "2"

REQUIRED_AREAS = {
    "Inner Eastern Melbourne",
    "North Eastern Melbourne",
    "Outer Eastern Melbourne",
    "Western Melbourne",
    "Southern Melbourne",
}

OUTPUT_COLUMNS = [
    "School_No",
    "School_Name",
    "Education_Sector",
    "School_Type",
    "Address_Line_1",
    "Address_Town",
    "Address_Postcode",
    "Region",
    "Area",
    "LGA_Name",
    "X",
    "Y",
    "Distance_km_from_Melbourne_Connect",
    "Map_Category_Sector",
    "Map_Category_Type",
    "Map_Category_Area",
    "Map_Category_Suburb",
    "Website_For_Popup",
    "Logo_Image_URL",
    "Logo_Status_For_Popup",
]

WPGMZA_IMPORT_COLUMNS = [
    "id",
    "map_id",
    "address",
    "description",
    "pic",
    "link",
    "icon",
    "lat",
    "lng",
    "anim",
    "title",
    "infoopen",
    "category",
    "approved",
    "retina",
    "Custom Field:Education Sector",
    "Custom Field:School Type",
    "Custom Field:Area",
    "Custom Field:Suburb",
    "Custom Field:Nearest Six Secondary",
    "Custom Field:Distance from Melbourne Connect",
]

CATEGORY_MODEL_COLUMNS = [
    "Filter_Group",
    "Filter_Value",
    "Recommended_WP_Go_Maps_Setup",
]

NEAREST_WEBSITES = {
    "University High School": "https://unihigh.vic.edu.au/",
    "Academy of Mary Immaculate": "https://www.academy.vic.edu.au/",
    "Simonds Catholic College": "https://www.sccmelb.catholic.edu.au/",
    "Holmes Grammar School": "https://www.holmesgrammar.vic.edu.au/",
    "Ozford College": "https://ozford.edu.au/",
    "Princes Hill Secondary College": "https://www.phsc.vic.edu.au/",
}

NEAREST_LOGOS = {
    "University High School": (
        "https://unihigh.vic.edu.au/wp-content/uploads/2021/12/"
        "cropped-UHS_new.png"
    ),
    "Academy of Mary Immaculate": (
        "https://www.academy.vic.edu.au/wp-content/uploads/2024/08/"
        "Layer_1.png"
    ),
    "Simonds Catholic College": (
        "https://sccmelb.s3.ap-southeast-2.amazonaws.com/uploads/Logos/"
        "Simonds-Crest-Blue-words-UPDATED.png?v=1619158555"
    ),
    "Holmes Grammar School": (
        "https://cdn.prod.website-files.com/678d9ca358a88efae5ca716e/"
        "67902137aa4fe63ad74179f9_Holmes%20Grammar%20School%20Logo_Horizontal.png"
    ),
    "Ozford College": (
        "https://ozford.edu.au/media/images/"
        "OIHE_new_logo_260505_002847_page-0001.original.jpg"
    ),
    "Princes Hill Secondary College": (
        "https://www.phsc.vic.edu.au/wp-content/uploads/2024/08/"
        "logo-type-colour.png"
    ),
}


def haversine_km(lat_a: float, lon_a: float, lat_b: float, lon_b: float) -> float:
    radius_km = 6371.0088
    phi_a = math.radians(lat_a)
    phi_b = math.radians(lat_b)
    delta_phi = math.radians(lat_b - lat_a)
    delta_lam = math.radians(lon_b - lon_a)
    term = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi_a) * math.cos(phi_b) * math.sin(delta_lam / 2) ** 2
    )
    return radius_km * 2 * math.atan2(math.sqrt(term), math.sqrt(1 - term))


def normalise_suburb(value: str) -> str:
    value = (value or "").strip()
    return value.title() if value.isupper() else value


def download_rows() -> list[dict[str, str]]:
    request = urllib.request.Request(
        SOURCE_CSV_URL,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        text = response.read().decode("utf-8-sig")
    return list(csv.DictReader(text.splitlines()))


def reduce_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for row in rows:
        if row.get("School_Status") != "O":
            continue
        if row.get("Area") not in REQUIRED_AREAS:
            continue

        lon = float(row["X"])
        lat = float(row["Y"])
        name = row["School_Name"]
        distance = haversine_km(
            MELBOURNE_CONNECT_LAT,
            MELBOURNE_CONNECT_LON,
            lat,
            lon,
        )

        output.append(
            {
                "School_No": row["School_No"],
                "School_Name": name,
                "Education_Sector": row["Education_Sector"],
                "School_Type": row["School_Type"],
                "Address_Line_1": row["Address_Line_1"],
                "Address_Town": normalise_suburb(row["Address_Town"]),
                "Address_Postcode": row["Address_Postcode"],
                "Region": row["Region"],
                "Area": row["Area"],
                "LGA_Name": row["LGA_Name"],
                "X": row["X"],
                "Y": row["Y"],
                "Distance_km_from_Melbourne_Connect": f"{distance:.2f}",
                "Map_Category_Sector": row["Education_Sector"],
                "Map_Category_Type": row["School_Type"],
                "Map_Category_Area": row["Area"],
                "Map_Category_Suburb": normalise_suburb(row["Address_Town"]),
                "Website_For_Popup": NEAREST_WEBSITES.get(name, ""),
                "Logo_Image_URL": NEAREST_LOGOS.get(name, ""),
                "Logo_Status_For_Popup": (
                    "Required for nearest-six secondary school"
                    if name in NEAREST_WEBSITES
                    else ""
                ),
            }
        )
    return sorted(output, key=lambda item: (item["Area"], item["School_Name"]))


def nearest_secondary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    secondary = [row for row in rows if row["School_Type"] == "Secondary"]
    nearest = sorted(
        secondary,
        key=lambda item: float(item["Distance_km_from_Melbourne_Connect"]),
    )[:6]
    return [
        {
            **row,
            "Marker_Popup_Requirement": (
                "Add official school logo image and website link in marker popup."
            ),
        }
        for row in nearest
    ]


def popup_description(row: dict[str, str]) -> str:
    lines = [
        ("Education sector", row["Education_Sector"]),
        ("School type", row["School_Type"]),
        ("Area", row["Area"]),
        ("Suburb", row["Address_Town"]),
        ("Distance from Melbourne Connect", f"{row['Distance_km_from_Melbourne_Connect']} km"),
    ]
    if row["Website_For_Popup"]:
        lines.append(("Website", row["Website_For_Popup"]))
    return "".join(
        f"<div><strong>{html.escape(label)}:</strong> {html.escape(value)}</div>"
        for label, value in lines
    )


def wpgmza_marker_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for row in rows:
        nearest_six = "Yes" if row["School_Name"] in NEAREST_WEBSITES else "No"
        output.append(
            {
                "id": str(900000 + int(row["School_No"])),
                "map_id": SPRINT2_WP_GO_MAPS_MAP_ID,
                "address": ", ".join(
                    part
                    for part in [
                        row["Address_Line_1"],
                        row["Address_Town"],
                        row["Address_Postcode"],
                    ]
                    if part
                ),
                "description": popup_description(row),
                "pic": row["Logo_Image_URL"],
                "link": row["Website_For_Popup"],
                "icon": "",
                "lat": row["Y"],
                "lng": row["X"],
                "anim": "0",
                "title": row["School_Name"],
                "infoopen": "0",
                "category": "",
                "approved": "1",
                "retina": "0",
                "Custom Field:Education Sector": row["Education_Sector"],
                "Custom Field:School Type": row["School_Type"],
                "Custom Field:Area": row["Area"],
                "Custom Field:Suburb": row["Address_Town"],
                "Custom Field:Nearest Six Secondary": nearest_six,
                "Custom Field:Distance from Melbourne Connect": (
                    row["Distance_km_from_Melbourne_Connect"]
                ),
            }
        )
    return output


def category_model_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    groups = [
        ("Education Sector", sorted({row["Education_Sector"] for row in rows})),
        ("School Type", sorted({row["School_Type"] for row in rows})),
        ("Area", sorted({row["Area"] for row in rows})),
        ("Suburb", sorted({row["Address_Town"] for row in rows})),
        ("Nearest Six Secondary", ["Yes", "No"]),
    ]
    output = []
    for group, values in groups:
        for value in values:
            output.append(
                {
                    "Filter_Group": group,
                    "Filter_Value": value,
                    "Recommended_WP_Go_Maps_Setup": (
                        "Create as marker custom-field option and enable filtering "
                        "in WP Go Maps Marker Fields settings."
                    ),
                }
            )
    return output


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_evidence(path: Path, reduced: list[dict[str, str]], nearest: list[dict[str, str]]) -> None:
    areas = sorted({row["Area"] for row in reduced})
    school_types = sorted({row["School_Type"] for row in reduced})
    sectors = sorted({row["Education_Sector"] for row in reduced})
    nearest_lines = "\n".join(
        f"- {row['School_Name']} ({row['Distance_km_from_Melbourne_Connect']} km)"
        for row in nearest
    )
    path.write_text(
        "\n".join(
            [
                "# Sprint 2 Data Evidence",
                "",
                f"Source CSV: {SOURCE_CSV_URL}",
                "",
                f"Reduced record count: {len(reduced)}",
                "",
                "Required areas included:",
                *[f"- {area}" for area in areas],
                "",
                f"Education sectors: {', '.join(sectors)}",
                f"School types: {', '.join(school_types)}",
                "",
                "Six closest secondary schools to Melbourne Connect:",
                nearest_lines,
                "",
                "Generation script: `Sprint_2/etc/generate_sprint2_school_outputs.py`",
                "WP Go Maps marker import file: `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv`",
                f"WP Go Maps import target used for historical import evidence: map ID {SPRINT2_WP_GO_MAPS_MAP_ID}",
                "WP Go Maps filter model file: `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv`",
                "",
                "WP Go Maps import reference: https://www.wpgmaps.com/help/docs/importing-files/",
                "The import file sets `approved` to `1` and uses `Custom Field:<name>` headers for Sprint 2 filter fields.",
                "",
                "The current accepted live page does not bulk-render all 913 WP Go Maps markers by default. As recorded in the final 11 May live-verification note, the user-facing Sprint 2 page uses an editable Gutenberg shell plus a controlled school-map widget that reads the reduced data, controls marker density from Melbourne Connect at 1 km, supports search/filter behaviour, and keeps the Sprint 1 map baseline protected.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    reduced_path = base_dir / "S2_Reduced_School_Locations_2025.csv"
    nearest_path = base_dir / "S2_Nearest_Secondary_Schools.csv"
    wpgmza_import_path = base_dir / "S2_WPGoMaps_Marker_Import.csv"
    category_model_path = base_dir / "S2_WPGoMaps_Filter_Model.csv"
    evidence_path = base_dir / "S2_Data_Evidence.md"

    reduced = reduce_rows(download_rows())
    nearest = nearest_secondary_rows(reduced)

    write_csv(reduced_path, reduced, OUTPUT_COLUMNS)
    write_csv(nearest_path, nearest, OUTPUT_COLUMNS + ["Marker_Popup_Requirement"])
    write_csv(wpgmza_import_path, wpgmza_marker_rows(reduced), WPGMZA_IMPORT_COLUMNS)
    write_csv(category_model_path, category_model_rows(reduced), CATEGORY_MODEL_COLUMNS)
    write_evidence(evidence_path, reduced, nearest)

    print(f"Wrote {len(reduced)} reduced school records to {reduced_path}")
    print(f"Wrote {len(nearest)} nearest secondary records to {nearest_path}")
    print(f"Wrote WP Go Maps marker import rows to {wpgmza_import_path}")
    print(f"Wrote WP Go Maps filter model rows to {category_model_path}")
    print(f"Wrote evidence notes to {evidence_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
