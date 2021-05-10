import hashlib
import json
import time
from collections import namedtuple

_hash = hashlib.sha256
_block_data = namedtuple('_block_data', ['index', 'data', 'timestamp', 'previous_hash', 'nonce'])


class Block:
    def __init__(self, index: int, data: "hashable object", timestamp: float, previous_hash: str, **options):
        self._hash_method = options.get('hash', 'sha256')
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.hash}'
    
    @property
    def asdict(self) -> dict:
        return {'index': self.index,
                'data': self.data,
                'timestamp': self.timestamp,
                'previous_hash': self.previous_hash,
                'nonce': self.nonce}

    @property
    def block_string(self) -> str:
        string = json.dumps(self.asdict, sort_keys=True)
        return string

    @property
    def hash(self) -> str:
        block_string = self.block_string
        digest = _hash
        return _hash(block_string.encode()).hexdigest()

    def increment_nonce(self) -> None:
        self._nonce += 1


class BlockChain: pass


class _Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = None

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.hash}'

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return _hash(block_string.encode()).hexdigest()


class _BlockChain:
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = _Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def proof_of_work(block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        prepend = '0' * _BlockChain.difficulty
        while not computed_hash.startswith(prepend):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    @staticmethod
    def is_valid_proof(block, block_hash):
        return (block_hash.startswith('0' * _BlockChain.difficulty) and
                block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = _Block(index=last_block.index + 1,
                           transactions=self.unconfirmed_transactions,
                           timestamp=time.time(),
                           previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index
