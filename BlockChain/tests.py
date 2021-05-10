import unittest
import BlockChain as bc


class TestBlockChain(unittest.TestCase):

    def setUp(self) -> None:
        self.chain = bc._BlockChain()

    def test_adding_transaction(self):
        transaction = ['alice gives bob $20']
        self.chain.add_new_transaction('alice gives bob $20')
        self.chain.mine()
        block = self.chain.last_block
        self.assertEqual(transaction, block.transactions)

    def test_adding_mulltiple_transactions(self):
        transactions = ['alice gives bob $30', 'bob gives alice herpes']
        for transaction in transactions:
            self.chain.add_new_transaction(transaction)
        self.chain.mine()
        block = self.chain.last_block
        self.assertEqual(transactions, block.transactions)


if __name__ == "__main__":
    unittest.main()
