# Sprint 2 Site Maintenance Security Check - 11 May 2026

## Purpose

This note records the safety check completed after the live page was restored to the Sprint 1 Gutenberg / WP Go Maps component baseline and before further Sprint 2 school-map work continued. It is a historical 11 May maintenance checkpoint. The final 11 May live-verification record documents the later accepted Sprint 2 school-map widget.

## Maintenance Checks

| Check | Result | Evidence |
| ----- | ------ | -------- |
| Temporary local diagnostic service | Closed for this Sprint 2 task | After shutdown, any remaining `8765` listener was identified as an unrelated local service, not the Sprint 2 diagnostic helper. No further action was taken against the unrelated service. |
| Browser diagnostic overlays | Cleared | The WP Go Maps admin page was reloaded, which removed the transient labels from the page DOM. |
| Live content persistence | No unintended persistent update found at this checkpoint | The live public page still showed the component-style Sprint 1 baseline at the maintenance checkpoint: site header, Gutenberg content, WP Go Maps map, and five stored formal markers. A later 11 May follow-up published and verified the controlled Sprint 2 school-map widget. |
| Marker write safety | Protected by server permissions | A direct WP Go Maps marker write attempt returned HTTP 403, so no test marker or school marker was saved through that route. |
| Formal repository | Unchanged during this maintenance check | The formal repository was not edited during this maintenance check. Later Sprint 2 artefact updates record the accepted live school-map widget and QA evidence. |

## Maintenance Rule Going Forward

- Continue Sprint 2 site work through WordPress admin UI, WP Go Maps plugin-supported import/export, and locally generated CSV/JSON evidence files.
- Do not use browser-injected helper code to create, update, or delete site content.
- Keep the local WP Go Maps backup as a rollback asset before any future bulk import, but do not include raw backup JSON in the formal evidence set.
- Keep US-05 to US-07 open until live search/list behaviour, filters, and nearest-six popup checks are verified through the safer maintenance path. This happened later on 11 May through the controlled school-map widget, so the final live-verification record accepts US-05 to US-07 while US-09 remains open.
