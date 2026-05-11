# Sprint 2 Data Evidence

Source CSV: https://www.education.vic.gov.au/Documents/about/research/datavic/dv402-SchoolLocations2025.csv

Reduced record count: 913

Required areas included:
- Inner Eastern Melbourne
- North Eastern Melbourne
- Outer Eastern Melbourne
- Southern Melbourne
- Western Melbourne

Education sectors: Catholic, Government, Independent
School types: Language, Pri/Sec, Primary, Secondary, Special

Six closest secondary schools to Melbourne Connect:
- University High School (0.86 km)
- Academy of Mary Immaculate (0.97 km)
- Simonds Catholic College (1.20 km)
- Holmes Grammar School (1.33 km)
- Ozford College (1.67 km)
- Princes Hill Secondary College (1.85 km)

Generation script: `Sprint_2/etc/generate_sprint2_school_outputs.py`
WP Go Maps marker import file: `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv`
WP Go Maps target map ID: 2
WP Go Maps filter model file: `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv`

WP Go Maps import reference: https://www.wpgmaps.com/help/docs/importing-files/
The import file sets `approved` to `1` and uses `Custom Field:<name>` headers for Sprint 2 filter fields.
