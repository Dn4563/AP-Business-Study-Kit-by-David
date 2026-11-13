# AP Business Study Kit by David Noskow

Live site (once Pages is on): https://dn4563.github.io/AP-Business-Study-Kit-by-David/

Built the same way as David's other kits: content files in `content/`, the shared engine in `core/` (copied from Study-Hub-by-David/kit-core), and one built `index.html`. Don't edit `index.html` by hand.

## Add a unit
1. Make a folder such as `content/unit-03/` with `cards.md`, `asks.json`, `watch.md`, `trees.md`, `guide.json`, `scenarios.json` and `practice.json`. The formats are in `core/README.md`; `content/unit-01/` is a full example.
2. Add the unit to `units` in `content/course.json`, with `"learnMix": true` and `"recall": true` (every unit after the first).
3. Build and test (below), then add the unit to the Study Hub's `courses.json`.

## Build and test
Node 18 or newer. The first time, run `npm install`. After every change run `npm test`: it parses the content, builds `index.html` and clicks through every tab. To update the engine, clone Study-Hub-by-David next to this repo and run `npm run sync-core`.

## Publish
Merge into `main`, then turn on Pages once: Settings → Pages → Deploy from a branch → `main` / `(root)`.

See `CLAUDE.md` for how units should be built.

Study kit engine by David Noskow (`core/LICENSE`).
