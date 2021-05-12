import multiprocessing as mp
import time
import hashlib
import json

class Block:
    def __init__(self,data):
        self.data=data
        self.hash = None
        

def mine(block,start,stop,queue,event, key,ID):
    print(f'starting ID:{ID}')
    data=block.data
    for nonce in range(start, stop+1):
        if not event.is_set():
            data['nonce'] = nonce
            string = json.dumps(data,sort_keys=True)
            hash_ = hashlib.sha256(string.encode()).hexdigest()
            if hash_.startswith(key):
                print(f'found the nonce! ID:{ID}')
                block.data = data
                block.hash = hash_
                event.set()
                print(f'event set is: {event.is_set()}')
                queue.put(block)
                break
    print(f'finishing ID:{ID}, ended on {nonce}')
    event.set()
    print(f'event set is: {event.is_set()}\n')
    

	
def main():
    key = 'beef'
    e = mp.Event()
    b = Block({'trevor gives addison $20':'bar','nonce':0})
    q=mp.Queue()
    p1 = mp.Process(target = mine, args = (b,0,5_000_000,q,e,key,1))
    p2 = mp.Process(target = mine, args = (b,5_000_000,10_000_000,q,e,key,2))
    p3 = mp.Process(target = mine, args = (b,10_000_000,15_000_000,q,e,key,3))
    p4 = mp.Process(target = mine, args = (b,15_000_000,20_000_000,q,e,key,4))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    while not e.is_set():
        time.sleep(1)
    p1.terminate()
    p2.terminate()
    p3.terminate()
    p4.terminate()
    res = q.get(1,1)
    if res:
        print(res.data,res.hash)

if __name__ == '__main__':
    main()
