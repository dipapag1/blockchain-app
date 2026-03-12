import time

from app.core.block import Block
from app.core.transaction import Transaction
from app.core.utils import hash_block_data


class Blockchain:
    """
    Απλή εκπαιδευτική υλοποίηση blockchain.
    """

    def __init__(self, difficulty: int = 4, mining_reward: float = 50) -> None:
        """
        Αρχικοποιεί το blockchain.

        Args:
            difficulty: Πόσα αρχικά μηδενικά απαιτούνται στο hash.
            mining_reward: Η αμοιβή του miner για κάθε νέο block.
        """
        self.chain = []
        self.pending_transactions = []
        self.difficulty = difficulty
        self.mining_reward = mining_reward

        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Δημιουργεί και προσθέτει το genesis block στο chain.
        """
        genesis_block = Block(
            index=0,
            timestamp=time.time(),
            transactions=[],
            previous_hash="0"
        )
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Επιστρέφει το τελευταίο block του chain.

        Returns:
            Block: Το τελευταίο block.
        """
        return self.chain[-1]

    def calculate_hash(self, block: Block) -> str:
        """
        Υπολογίζει το hash ενός block.

        Args:
            block: Το block για το οποίο υπολογίζεται το hash.

        Returns:
            str: Το SHA256 hash του block.
        """
        block_data = {
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": [
                tx.to_dict() if hasattr(tx, "to_dict") else tx
                for tx in block.transactions
            ],
            "previous_hash": block.previous_hash,
            "nonce": block.nonce
        }

        return hash_block_data(block_data)

    def proof_of_work(self, block: Block) -> str:
        """
        Εκτελεί proof of work μέχρι το hash να ξεκινά με τα απαιτούμενα μηδενικά.

        Args:
            block: Το block που γίνεται mine.

        Returns:
            str: Το έγκυρο mined hash.
        """
        required_prefix = "0" * self.difficulty

        while True:
            hash_value = self.calculate_hash(block)

            if hash_value.startswith(required_prefix):
                return hash_value

            block.nonce += 1

    def add_transaction(self, sender: str, receiver: str, amount: float) -> Transaction:
        """
        Προσθέτει μία νέα συναλλαγή στις pending transactions.

        Args:
            sender: Ο αποστολέας.
            receiver: Ο παραλήπτης.
            amount: Το ποσό.

        Returns:
            Transaction: Η συναλλαγή που προστέθηκε.

        Raises:
            ValueError: Αν τα δεδομένα της συναλλαγής είναι μη έγκυρα.
        """
        if not sender or not receiver:
            raise ValueError("Sender and receiver are required.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        transaction = Transaction(sender=sender, receiver=receiver, amount=amount)
        self.pending_transactions.append(transaction)
        return transaction

    def add_block(self, block: Block) -> Block:
        """
        Κάνει mining και προσθέτει ένα block στο chain.

        Args:
            block: Το block προς προσθήκη.

        Returns:
            Block: Το block που προστέθηκε.
        """
        block.previous_hash = self.get_latest_block().hash
        block.hash = self.proof_of_work(block)
        self.chain.append(block)
        return block

    def mine_pending_transactions(self, miner_address: str) -> Block:
        """
        Δημιουργεί νέο block από τις pending transactions και δίνει reward στον miner.

        Args:
            miner_address: Το wallet address του miner.

        Returns:
            Block: Το νέο mined block.

        Raises:
            ValueError: Αν δεν υπάρχουν pending transactions ή αν λείπει miner address.
        """
        if not miner_address:
            raise ValueError("Miner address is required.")

        if not self.pending_transactions:
            raise ValueError("There are no pending transactions to mine.")

        reward_transaction = Transaction(
            sender="SYSTEM",
            receiver=miner_address,
            amount=self.mining_reward
        )

        block_transactions = self.pending_transactions.copy()
        block_transactions.append(reward_transaction)

        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=block_transactions,
            previous_hash=self.get_latest_block().hash
        )

        mined_block = self.add_block(new_block)
        self.pending_transactions = []

        return mined_block

    def get_balance(self, address: str) -> float:
        """
        Υπολογίζει το balance ενός wallet από όλες τις συναλλαγές του chain.

        Args:
            address: Το wallet address.

        Returns:
            float: Το τελικό balance.
        """
        balance = 0.0

        for block in self.chain:
            for transaction in block.transactions:
                tx = transaction.to_dict() if hasattr(transaction, "to_dict") else transaction

                if tx["receiver"] == address:
                    balance += tx["amount"]

                if tx["sender"] == address:
                    balance -= tx["amount"]

        return balance

    def is_chain_valid(self) -> bool:
        """
        Ελέγχει αν το blockchain είναι έγκυρο.

        Returns:
            bool: True αν το chain είναι valid, αλλιώς False.
        """
        for index in range(1, len(self.chain)):
            current_block = self.chain[index]
            previous_block = self.chain[index - 1]

            recalculated_hash = self.calculate_hash(current_block)

            if current_block.hash != recalculated_hash:
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            if not current_block.hash.startswith("0" * self.difficulty):
                return False

        return True
    
    def add_transaction(self, sender: str, receiver: str, amount: float) -> Transaction:
    """
    Προσθέτει μία νέα συναλλαγή στις pending transactions.

    Args:
        sender: Ο αποστολέας.
        receiver: Ο παραλήπτης.
        amount: Το ποσό.

    Returns:
        Transaction: Η συναλλαγή που προστέθηκε.

    Raises:
        ValueError: Αν τα δεδομένα είναι μη έγκυρα ή αν το υπόλοιπο δεν επαρκεί.
    """
    if not sender or not receiver:
        raise ValueError("Sender and receiver are required.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if sender != "SYSTEM":
        sender_balance = self.get_balance(sender)
        if sender_balance < amount:
            raise ValueError("Insufficient balance.")

    transaction = Transaction(sender=sender, receiver=receiver, amount=amount)
    self.pending_transactions.append(transaction)
    return transaction