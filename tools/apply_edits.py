import json
import sys
from pathlib import Path

paper_root = Path(sys.argv[1])
edits_dir = Path(sys.argv[2])
src_root = paper_root / "paper-server" / "src" / "minecraft" / "java"

if not src_root.is_dir():
    print(f"source root not found: {src_root}")
    sys.exit(1)

failed = False
applied = 0

for edit_file in sorted(edits_dir.glob("*.json")):
    spec = json.loads(edit_file.read_text(encoding="utf-8"))
    target = src_root / spec["file"]
    if not target.is_file():
        print(f"[{edit_file.name}] missing file: {spec['file']}")
        failed = True
        continue
    text = target.read_text(encoding="utf-8")
    for index, item in enumerate(spec["replace"]):
        count = text.count(item["old"])
        if count != 1:
            print(f"[{edit_file.name}] edit #{index} in {spec['file']}: expected 1 match, found {count}")
            failed = True
            continue
        text = text.replace(item["old"], item["new"], 1)
        applied += 1
    target.write_text(text, encoding="utf-8")

print(f"applied {applied} edits")
sys.exit(1 if failed else 0)
