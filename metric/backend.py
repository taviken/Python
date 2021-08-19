import subprocess
import json

MULTIMETRIC = 'multimetric'


def get_analyitics(source_path: str) -> dict:
    """Retrieve the analytics from a given source code path"""
    pipe = subprocess.Popen((MULTIMETRIC, source_path),
                            stdout=subprocess.PIPE,
                            creationflags=subprocess.CREATE_NO_WINDOW)
    result = pipe.communicate()
    data = json.loads(result[0])
    return data
