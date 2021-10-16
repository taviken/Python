import os
import speedtest as sp
import json
from enum import Enum
import datetime as dt
import io
import time
from ._constants import kibibyte, mibibyte, __path


class Units(Enum):
    KIBIBYTE = kibibyte
    MIBIBYTE = mibibyte


def get_download_speed(**opts):
    sptest = sp.Speedtest()
    res = sptest.download()
    dataused = sptest.results.bytes_received
    units = opts.get('units', Units.MIBIBYTE)
    return res / units.value, dataused


def logit(entry):
    if os.path.exists(__path):
        with open(__path, 'r') as f:
            try:
                data = json.load(f)
            except (json.JSONDecodeError, io.UnsupportedOperation):
                data = []
    else:
        data = []
    data.append(entry)
    with open(__path, 'w') as f:
        json.dump(data, f, indent=4)


def main(**opts):
    delay = opts.get('delay', 24 * 3600)  # defaults to every 24 hours

    while True:
        t, used = get_download_speed()
        now = dt.datetime.now().astimezone().isoformat()
        entry = {'date': now,
                 'speed': t,
                 'data_used': used}

        logit(entry)
        time.sleep(delay)
        print(entry)


if __name__ == '__main__':
    main()
