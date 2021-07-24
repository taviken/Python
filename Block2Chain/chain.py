import block
import datetime as dt


class BlockChain:
    def __init__(self):
        self._chain = [block.create_genesis()]

    def __len__(self):
        return len(self._chain)

    def __iter__(self):
        for block in self._chain:
            yield block

    @property
    def chain(self):
        return self._chain

    @property
    def lastBlock(self):
        return self._chain[-1]

    def addBlock(self, data):
        self._chain.append(block.Block(dt.datetime.now(), self.lastBlock.hash, data))

    def replaceChain(self, new_chain):
        if len(new_chain) <= len(self):
            return
        elif not self.isValidChain(new_chain):
            return
        else:
            self._chain = new_chain.chain

    def isValidChain(self, other_chain):
        for block in other_chain:

