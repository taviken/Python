from dataclasses import dataclass
from pathlib import Path
import json

_this_dir = Path(__file__).parent

with open(_this_dir / "modp.json", "r") as fd:
    modp_data = json.load(fd)


def _post_proc_modp(modp):
    for group_name, group in modp.items():
        for name, part in group.items():
            part = part.replace(" ", "")
            num = int(part, 16)
            group[name] = num
        modp[group_name] = group


_post_proc_modp(modp_data)


@dataclass(frozen=True)
class MODP_1024_160:
    p: int = modp_data["modp_1024_160"]["p"]
    g: int = modp_data["modp_1024_160"]["g"]
    q: int = modp_data["modp_1024_160"]["q"]


@dataclass(frozen=True)
class MODP_2048_224:
    p: int = modp_data["modp_2048_224"]["p"]
    g: int = modp_data["modp_2048_224"]["g"]
    q: int = modp_data["modp_2048_224"]["q"]


@dataclass(frozen=True)
class MODP_2048_256:
    p: int = modp_data["modp_2048_256"]["p"]
    g: int = modp_data["modp_2048_256"]["g"]
    q: int = modp_data["modp_2048_256"]["q"]
