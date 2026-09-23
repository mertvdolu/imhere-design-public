# Asset provenance / v1.0

## Approved design

Theme, Geist, logo and UI wording: Cream & Ink v2.2, repository commit `f3dbd40bdedad4ec0b3ed06f38b72d1c1cfcebf2`. Existing design package files were read, not changed. The font licence is included as `assets/OFL.txt`. Both logo SVGs retain the exact source bytes.

`build.py` composes representative viewport layouts from the approved catalog and the approved main-screen experience: request intent selection, Nearby, Connections, writable chat and own profile. It uses native-sized coordinate canvases as **design renders**, not screenshots of a running Flutter build. Store marketing headlines live outside the app frame and are not new app localisation keys. Product behaviour is unchanged.

## Fictional data

Maya and Alex are invented adults. Their names, occupations, interests and conversation are sample data. Panels are independent fixture scenes, not one account's continuous session. No live service, personal data or real user was accessed. Profile age/gender are hidden in these fixtures; occupation is visible.

The two portraits were made with the built-in `image_gen` tool, without source photos or identity references. Original PNGs are preserved. JPEGs are export encodings of those same images for compact vector embedding; no identity alteration was made. Full prompts are in `IMAGEGEN-PROMPTS.json`. Visible artwork disclosure: `Fictional profiles · Illustrative content`.

## Map

`assets/map-ready-ios.svg` and `assets/map-ready-android.svg` are exact copies of the approved v2.2 `map-ready` EN / 100% fixtures. No map data was fetched. The base geometry is a schematic catalog illustration; colour areas are illustrative fixed aggregates. This is explicitly labelled `Illustrative map · Not live data`. The required OpenStreetMap/OpenFreeMap attribution and source OpenMapTiles attribution remain visible. No personal pin, person count or distance is present. The displayed time belongs to the sample snapshot, not a people count.

## Publication boundary

Native capture comparison is outstanding and stated in `DELIVERY.json` and the handoff. Final store submission must accurately match the released build. Where needed, replace the screen viewport with a native capture of the same fictional fixture; retain headline composition, disclosure and map attribution. No stores were modified by this design task.
