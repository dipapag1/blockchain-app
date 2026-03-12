import time

from app.core.block import Block
from app.core.transaction import Transaction
from app.core.utils import hash_block_data


class Blockchain:
    """
    Απλή εκπαιδευτική υλοποίηση blockchain.

    Η κλάση αυτή είναι υπεύθυνη για:
    - τη διατήρηση της αλυσίδας των blocks,
    - τη διαχείριση των pending transactions,
    - τον υπολογισμό hashes,
    - το proof of work,
    - το mining,
    - την επικύρωση της αλυσίδας,
    - και τον υπολογισμό υπολοίπων.

    Πρόκειται για simplified blockchain model, κατάλληλο για
    εκπαιδευτικό project και κατανόηση της βασικής λογικής.
    """

    def __init__(self, difficulty: int = 4, mining_reward: float = 50) -> None:
        """
        Αρχικοποιεί το blockchain.

        Με τη δημιουργία του blockchain:
        - ορίζεται η δυσκολία του proof of work,
        - ορίζεται το reward του miner,
        - δημιουργούνται τα storage lists,
        - και προστίθεται το genesis block.

        Args:
            difficulty: Πόσα αρχικά μηδενικά πρέπει να έχει το hash
                για να θεωρηθεί έγκυρο στο proof of work.
            mining_reward: Το reward που θα λαμβάνει ο miner
                κάθε φορά που γίνεται mining.

        Raises:
            ValueError: Αν η δυσκολία είναι αρνητική ή το reward μη θετικό.
        """
        if difficulty < 0:
            raise ValueError("Difficulty cannot be negative.")
        if mining_reward <= 0:
            raise ValueError("Mining reward must be greater than zero.")

        self.chain: list[Block] = []
        self.pending_transactions: list[Transaction] = []
        self.difficulty = difficulty
        self.mining_reward = float(mining_reward)

        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Δημιουργεί το genesis block.

        Το genesis block είναι το πρώτο block της αλυσίδας και
        δεν έχει πραγματικό προηγούμενο block, άρα το previous_hash
        τίθεται σε "0".

        Μετά τη δημιουργία του, περνά και αυτό από proof of work,
        ώστε να ακολουθεί τους ίδιους κανόνες εγκυρότητας
        με τα υπόλοιπα blocks.
        """
        genesis_block = Block(
            index=0,
            timestamp=time.time(),
            transactions=[],
            previous_hash="0",
        )
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Επιστρέφει το τελευταίο block της αλυσίδας.

        Returns:
            Το πιο πρόσφατο block του blockchain.
        """
        return self.chain[-1]

    def calculate_hash(self, block: Block) -> str:
        """
        Υπολογίζει το hash ενός block.

        Για τον υπολογισμό του hash λαμβάνονται υπόψη μόνο τα δεδομένα
        που πρέπει να καθορίζουν μοναδικά το block:
        - index
        - timestamp
        - transactions
        - previous_hash
        - nonce

        Το ίδιο το πεδίο `hash` δεν συμπεριλαμβάνεται στον υπολογισμό,
        γιατί διαφορετικά θα δημιουργούσε κυκλική εξάρτηση.

        Args:
            block: Το block του οποίου θέλουμε να υπολογίσουμε το hash.

        Returns:
            Το SHA256 hash του block σε hexadecimal μορφή.
        """
        block_data = {
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": [
                tx.to_dict() if hasattr(tx, "to_dict") else tx
                for tx in block.transactions
            ],
            "previous_hash": block.previous_hash,
            "nonce": block.nonce,
        }
        return hash_block_data(block_data)

    def proof_of_work(self, block: Block) -> str:
        """
        Εκτελεί τον αλγόριθμο proof of work για ένα block.

        Η λογική είναι η εξής:
        - Υπολογίζουμε hash για το block.
        - Αν το hash ξεκινά με τόσα μηδενικά όσα ορίζει η δυσκολία,
          τότε το block θεωρείται mined.
        - Διαφορετικά αυξάνουμε το nonce και ξαναδοκιμάζουμε.

        Με αυτόν τον τρόπο η εύρεση έγκυρου block απαιτεί υπολογιστική
        προσπάθεια, κάτι που αποτελεί βασική ιδέα των blockchain
        που χρησιμοποιούν proof of work.

        Args:
            block: Το block που θέλουμε να εξορύξουμε.

        Returns:
            Το έγκυρο hash που ικανοποιεί τη δυσκολία.
        """
        required_prefix = "0" * self.difficulty

        while True:
            hash_value = self.calculate_hash(block)

            if hash_value.startswith(required_prefix):
                return hash_value

            block.nonce += 1

    def get_pending_outgoing_amount(self, address: str) -> float:
        """
        Υπολογίζει το σύνολο των εξερχόμενων pending συναλλαγών
        μιας διεύθυνσης.

        Αυτό είναι απαραίτητο για να μην μπορεί κάποιος χρήστης να
        δημιουργήσει πολλές pending συναλλαγές που συνολικά ξεπερνούν
        το πραγματικό διαθέσιμο υπόλοιπό του.

        Παράδειγμα:
        Αν κάποιος έχει 40 coins και δημιουργήσει pending transaction 30,
        δεν πρέπει να του επιτραπεί να δημιουργήσει και δεύτερη pending
        transaction 20 πριν γίνει mining.

        Args:
            address: Η διεύθυνση/χρήστης που ελέγχουμε.

        Returns:
            Το άθροισμα όλων των pending ποσών που στέλνει η διεύθυνση.
        """
        total = 0.0

        for transaction in self.pending_transactions:
            tx = transaction.to_dict() if hasattr(transaction, "to_dict") else transaction
            if tx["sender"] == address:
                total += tx["amount"]

        return total

    def add_transaction(self, sender: str, receiver: str, amount: float) -> Transaction:
        """
        Προσθέτει μία νέα συναλλαγή στις pending transactions.

        Πριν προστεθεί η συναλλαγή γίνεται έλεγχος:
        - ότι sender και receiver υπάρχουν,
        - ότι το ποσό είναι θετικό,
        - και ότι ο sender έχει αρκετό διαθέσιμο balance.

        Εξαίρεση αποτελεί ο sender "SYSTEM", ο οποίος χρησιμοποιείται
        για reward ή αρχική διανομή ποσών και δεν ελέγχεται ως προς balance.

        Args:
            sender: Ο αποστολέας της συναλλαγής.
            receiver: Ο παραλήπτης της συναλλαγής.
            amount: Το ποσό που μεταφέρεται.

        Returns:
            Το αντικείμενο Transaction που δημιουργήθηκε και μπήκε στα pending.

        Raises:
            ValueError: Αν τα δεδομένα είναι άκυρα ή δεν υπάρχει επαρκές balance.
        """
        if not sender or not receiver:
            raise ValueError("Sender and receiver are required.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if sender != "SYSTEM":
            available_balance = self.get_balance(sender) - self.get_pending_outgoing_amount(sender)
            if available_balance < amount:
                raise ValueError("Insufficient balance.")

        transaction = Transaction(sender=sender, receiver=receiver, amount=amount)
        self.pending_transactions.append(transaction)
        return transaction

    def add_block(self, block: Block) -> Block:
        """
        Προσθέτει ένα νέο block στην αλυσίδα αφού πρώτα το ολοκληρώσει.

        Πριν το block προστεθεί:
        - συνδέεται με το hash του τελευταίου block,
        - περνά από proof of work,
        - αποκτά τελικό hash,
        - και τέλος αποθηκεύεται στην αλυσίδα.

        Args:
            block: Το block που θα προστεθεί.

        Returns:
            Το ίδιο block, πλέον ολοκληρωμένο και αποθηκευμένο.
        """
        block.previous_hash = self.get_latest_block().hash
        block.hash = self.proof_of_work(block)
        self.chain.append(block)
        return block

    def mine_pending_transactions(self, miner_address: str) -> Block:
        """
        Κάνει mining όλων των pending transactions.

        Η διαδικασία είναι:
        1. Ελέγχεται αν υπάρχει miner address.
        2. Ελέγχεται αν υπάρχουν pending transactions.
        3. Προστίθεται reward transaction προς τον miner.
        4. Δημιουργείται νέο block με όλες τις pending συναλλαγές.
        5. Το block εξορύσσεται με proof of work.
        6. Προστίθεται στην αλυσίδα.
        7. Οι pending transactions μηδενίζονται.

        Args:
            miner_address: Η διεύθυνση που θα λάβει το mining reward.

        Returns:
            Το block που μόλις έγινε mined.

        Raises:
            ValueError: Αν λείπει το miner address ή δεν υπάρχουν pending transactions.
        """
        if not miner_address:
            raise ValueError("Miner address is required.")

        if not self.pending_transactions:
            raise ValueError("There are no pending transactions to mine.")

        reward_transaction = Transaction(
            sender="SYSTEM",
            receiver=miner_address,
            amount=self.mining_reward,
        )

        block_transactions = self.pending_transactions.copy()
        block_transactions.append(reward_transaction)

        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=block_transactions,
            previous_hash=self.get_latest_block().hash,
        )

        mined_block = self.add_block(new_block)
        self.pending_transactions = []

        return mined_block

    def get_balance(self, address: str) -> float:
        """
        Υπολογίζει το confirmed balance μιας διεύθυνσης.

        Το balance υπολογίζεται διατρέχοντας όλα τα blocks της αλυσίδας:
        - αν η διεύθυνση είναι receiver, το ποσό προστίθεται,
        - αν η διεύθυνση είναι sender, το ποσό αφαιρείται.

        Η μέθοδος αυτή λαμβάνει υπόψη μόνο συναλλαγές που έχουν ήδη
        γίνει mined και βρίσκονται στο chain, όχι τις pending.

        Args:
            address: Η διεύθυνση/χρήστης του οποίου θέλουμε το υπόλοιπο.

        Returns:
            Το επιβεβαιωμένο υπόλοιπο της διεύθυνσης.
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
        Ελέγχει αν ολόκληρη η αλυσίδα είναι έγκυρη.

        Οι βασικοί έλεγχοι είναι:
        - το genesis block να έχει previous_hash = "0",
        - το stored hash κάθε block να ταιριάζει με το recalculated hash,
        - κάθε block να δείχνει σωστά στο hash του προηγούμενου block,
        - και κάθε hash να ικανοποιεί το proof of work difficulty.

        Αν οποιοδήποτε block έχει αλλοιωθεί μετά τη δημιουργία του,
        ο έλεγχος θα αποτύχει.

        Returns:
            True αν η αλυσίδα είναι έγκυρη, αλλιώς False.
        """
        if not self.chain:
            return False

        genesis_block = self.chain[0]

        if genesis_block.previous_hash != "0":
            return False

        if genesis_block.hash != self.calculate_hash(genesis_block):
            return False

        if not genesis_block.hash.startswith("0" * self.difficulty):
            return False

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