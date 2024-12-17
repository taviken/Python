import os
from pathlib import Path
import pickle
from tkinter import filedialog
from datetime import datetime

__version__ = "0.0.1"

_this_dir = Path(__file__).parent
_session_file = _this_dir / "session.dat"

allowed_suffixes = (".mkv",)


def create_log(names: iter, log_path: Path):
    now = datetime.now()

    full_path = (
        log_path
        / f"Movie List {now.year}{now.month}{now.day}_{now.hour}_{now.minute}.log"
    )

    with open(full_path, "w") as fp:
        for name in sorted(names):
            print(name, file=fp)
            # fp.write(name)


def get_names() -> iter:
    files = [f for f in os.listdir(_this_dir) if os.path.isfile(f)]
    files = filter(lambda x: Path(x).suffix in allowed_suffixes, files)
    return files


def get_write_dir() -> Path:
    given_dir = filedialog.askdirectory()
    return Path(given_dir)


def load_session() -> dict:
    if not os.path.exists(_session_file):
        Path(_session_file).touch()
        data = {}
    else:
        try:
            with open(_session_file, "rb") as fp:
                data = pickle.load(fp)
        except EOFError:
            data = {}
    return data


def save_session(save_data: dict):
    with open(_session_file, "wb") as fp:
        # breakpoint()
        pickle.dump(save_data, fp, protocol=pickle.HIGHEST_PROTOCOL)


def main():
    data = load_session()

    log_path = data.get("log_path")
    if log_path is None:
        log_path = get_write_dir()

    names = get_names()

    breakpoint()
    create_log(names, log_path)
    breakpoint()

    data.update({"log_path": log_path, "version": __version__})
    save_session(data)


if __name__ == "__main__":
    main()
