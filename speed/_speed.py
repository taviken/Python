import speedtest
import enum
import os
import datetime as dt
import json
import time

file_dir = os.path.split(__file__)[0]
default_logname = 'download_speed.log'
default_path = os.path.join(file_dir, default_logname)
speed = speedtest.Speedtest()
kibibyte: int = 1024
mebibyte: int = kibibyte * kibibyte


class Units(enum.Enum):
    KIBIBYTE = kibibyte
    MEBIBYTE = mebibyte


def get_download_speed(**opts) -> "bits/s":
    res = speed.download()
    data_used = speed.results.bytes_received
    print(data_used)
    divisor = opts.get('uints', Units.MEBIBYTE)
    res /= divisor.value
    return res


def loggit(line: str, **opts) -> None:
    now = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = {now: line}
    path = opts.get('path', default_path)
    data = {}
    if os.path.exists(default_path):
        with open(path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    data.update(entry)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def main(**opts):
    delay = opts.get('delay', 600)
    while True:
        t = get_download_speed()
        loggit(line=t)
        time.sleep(delay)


if __name__ == '__main__':
    main()
