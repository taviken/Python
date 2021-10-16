import subprocess
import json
import os
import sys
import multimetric
from collections import namedtuple

Analysis = namedtuple('Analysis', 'files overall stats')

_path = os.path.dirname(multimetric.__file__)
_main = os.path.join(_path, '__main__.py')


# MULTIMETRIC = 'multimetric'


def get_analyitics(source_path: str) -> Analysis:
    """Retrieve the analytics from a given source code path"""
    pipe = subprocess.Popen((sys.executable, _main, source_path),
                            stdout=subprocess.PIPE,
                            creationflags=subprocess.CREATE_NO_WINDOW)
    result = pipe.communicate()
    data = json.loads(result[0])
    analysis = Analysis(data['files'], data['overall'], data['stats'])
    return analysis
