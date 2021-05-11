import json
import multiprocessing as mp

_cores = mp.cpu_count()


def _mine(block, nonces, key, hasher, event: mp.Event):
    for nonce in nonces:
        if event.is_set():
            break
        hash_ = hash_block(block, nonce, hasher)
        if hash_.startswith(key):
            event.set()
            return nonce, hash_
    return None, None


def hash_block(block, nonce, hasher) -> str:
    data = block.asdict
    data['nonce'] = nonce
    block_string = json.dumps(data, sort_keys=True).encode()
    return hasher(block_string).hexdigest()


def multi_mine(block, key, hasher):
    event = mp.Event()
    nonce_set = _gen_nonces(_cores)
    processes = [mp.Process(target=_mine, args=(block, nonces, key, hasher, event)) for nonces in nonce_set]



def _gen_nonces(cores):
    raise NotImplementedError
