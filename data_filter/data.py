from enum import IntEnum
import pandas as pd

# from pandas.core.frame import DataFrame

ID = "id"
FORMAT = "%Y-%m-%d %H:%M:%S"


class modes(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4


data = [
    {ID: modes.A.value, "timestamp": "2026-06-27 07:53:13"},
    {ID: "event1", "timestamp": "2026-06-27 07:53:14"},
    {ID: modes.B.value, "timestamp": "2026-06-27 07:53:15"},
    {ID: "event2", "timestamp": "2026-06-27 07:53:16"},
    {ID: modes.C.value, "timestamp": "2026-06-27 07:53:17"},
]


def get_intervals(data: dict):

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format=FORMAT)

    df["end_time"] = df["timestamp"].shift(-1)
    df["end_time"] = df["end_time"].fillna(pd.Timestamp.now())

    # df["duration"] = df["end_time"] - df["timestamp"]
    df = df.rename(columns={"timestamp": "start_time"})

    recs = df.to_dict(orient="records")

    return recs
