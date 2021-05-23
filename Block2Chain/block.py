import json
import datetime
import hashlib


class Block:
    def __init__(self,
                 timestamp: datetime.datetime,
                 prev_hash: str,
                 data: object,
                 validator=None,
                 signature=None):
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.data = data
        self.validator = validator
        self.signature = signature
        self._hash = None

    @property
    def asdict(self) -> dict:
        return {'timestamp': self.timestamp,
                'prev_hash': self.prev_hash,
                'data': self.data,
                'validator': self.validator,
                'signature': self.signature}

    @property
    def toJson(self) -> str:
        return json.dumps(self.asdict)

    @property
    def hash(self):
        return self._hash

    def __hash(self):
        self._hash = hashlib.sha256(self.toJson.encode()).hexdigest()


def create_genesis():
    return Block(timestamp=datetime.datetime.now(),
                 prev_hash='----',
                 data="In the beginning was the word, and the word was not null string terminated",
                 validator=None,
                 signature=None)
