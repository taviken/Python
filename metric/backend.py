import subprocess
import json
import os
import sys
import multimetric

_path = os.path.dirname(multimetric.__file__)
_main = os.path.join(_path, '__main__.py')

# MULTIMETRIC = 'multimetric'


def get_analyitics(source_path: str) -> dict:
    """Retrieve the analytics from a given source code path"""
    pipe = subprocess.Popen((sys.executable, _main, source_path),
                            stdout=subprocess.PIPE,
                            creationflags=subprocess.CREATE_NO_WINDOW)
    result = pipe.communicate()
    data = json.loads(result[0])
    return data
