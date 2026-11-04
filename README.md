Mint
===========

Vanilla-first, performance-focused fork of [PaperMC/Paper](https://github.com/PaperMC/Paper) for Minecraft 26.3.

This repository holds only Mint's own changes. The build downloads Paper at the commit pinned in `PAPER_COMMIT`, copies `overlay/` over it (new classes and resources), applies Paper's patches, applies the exact-match edits from `edits/*.json` to the patched sources, and builds the Paperclip jar.

Edit file format:

    {"file": "net/minecraft/server/level/ChunkMap.java", "replace": [{"old": "exact text, must occur once", "new": "replacement"}]}

The `Inspect Source` workflow exports chosen classes from the patched tree as an artifact.
