import json
import multiprocessing as mp

_cores = mp.cpu_count()


def _mine(block, nonces, key, hasher, event: mp.Event, queue: mp.Queue):
    for nonce in nonces:
        if event.is_set():
            break
        hash_ = hash_block(block, nonce, hasher)
        if hash_.startswith(key):
            event.set()
            queue.put((nonce, hash_))
    return None, None


def hash_block(block, nonce, hasher) -> str:
    data = block.asdict
    data['nonce'] = nonce
    block_string = json.dumps(data, sort_keys=True).encode()
    return hasher(block_string).hexdigest()


def multi_mine(block, key, hasher):
    event = mp.Event()
    nonce_set = _get_nonces(1_000_000)
    processes = [mp.Process(target=_mine, args=(block, nonces, key, hasher, event)) for nonces in nonce_set]


def _get_nonces(size):
    start = 0
    end = size
    while True:
        yield start, end
        start += size
        end += size
