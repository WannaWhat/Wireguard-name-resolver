from pathlib import Path
from pprint import pprint
from sys import argv

root_path = Path(argv[0]).parent


def find(path: Path, suffix: str) -> [str]:
    out = []
    for _p in path.iterdir():
        if _p.is_file():
            if _p.suffix == suffix:
                out.append(_p)
        elif _p.is_dir():
            out.extend(find(_p, suffix))
    return out


output = find(root_path, ".xml")
output = list(map(lambda x: str(x.relative_to(root_path)), output))
print(output)
