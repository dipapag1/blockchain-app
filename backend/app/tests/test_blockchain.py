import pytest

from app.core.blockchain import Blockchain


def test_genesis_block_created():
    """
    Ελέγχει ότι με τη δημιουργία του Blockchain
    δημιουργείται αυτόματα και το genesis block.
    """
    blockchain = Blockchain()

    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].index == 0
    assert blockchain.chain[0].previous_hash == "0"


def test_add_transaction_requires_existing_balance():
    """
    Ελέγχει ότι μία κανονική συναλλαγή μπορεί να προστεθεί
    μόνο όταν ο sender έχει ήδη διαθέσιμο balance.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 40)
    blockchain.mine_pending_transactions("Miner1")

    blockchain.add_transaction("Alice", "Bob", 10)

    assert len(blockchain.pending_transactions) == 1
    assert blockchain.pending_transactions[0].sender == "Alice"


def test_add_transaction_insufficient_balance_raises():
    """
    Ελέγχει ότι αν ένας χρήστης δεν έχει αρκετό balance,
    η προσθήκη συναλλαγής αποτυγχάνει με ValueError.
    """
    blockchain = Blockchain()

    with pytest.raises(ValueError, match="Insufficient balance"):
        blockchain.add_transaction("Alice", "Bob", 10)


def test_pending_outgoing_amount_prevents_overspending_before_mining():
    """
    Ελέγχει ότι το σύστημα λαμβάνει υπόψη και τις pending
    outgoing συναλλαγές ώστε να αποφεύγεται overspending.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 40)
    blockchain.mine_pending_transactions("Miner1")

    blockchain.add_transaction("Alice", "Bob", 30)

    with pytest.raises(ValueError, match="Insufficient balance"):
        blockchain.add_transaction("Alice", "Charlie", 20)


def test_mine_pending_transactions():
    """
    Ελέγχει ότι το mining:
    - δημιουργεί νέο block,
    - αδειάζει τις pending transactions,
    - και αυξάνει το μήκος της αλυσίδας.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 25)
    blockchain.mine_pending_transactions("Miner1")

    blockchain.add_transaction("Alice", "Bob", 10)
    mined_block = blockchain.mine_pending_transactions("Miner1")

    assert len(blockchain.chain) == 3
    assert mined_block.index == 2
    assert len(blockchain.pending_transactions) == 0


def test_get_balance():
    """
    Ελέγχει ότι το balance κάθε χρήστη υπολογίζεται σωστά
    με βάση τις mined συναλλαγές της αλυσίδας.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 40)
    blockchain.mine_pending_transactions("Miner1")

    blockchain.add_transaction("Alice", "Bob", 15)
    blockchain.mine_pending_transactions("Miner1")

    assert blockchain.get_balance("Alice") == 25
    assert blockchain.get_balance("Bob") == 15
    assert blockchain.get_balance("Miner1") == 100


def test_chain_validation():
    """
    Ελέγχει ότι μία σωστά δομημένη αλυσίδα
    αναγνωρίζεται ως έγκυρη.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 20)
    blockchain.mine_pending_transactions("Miner1")

    assert blockchain.is_chain_valid() is True


def test_chain_validation_fails_when_data_is_tampered():
    """
    Ελέγχει ότι αν αλλοιωθούν δεδομένα σε ήδη mined block,
    η επικύρωση της αλυσίδας αποτυγχάνει.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 20)
    blockchain.mine_pending_transactions("Miner1")

    blockchain.chain[1].transactions[0].amount = 999

    assert blockchain.is_chain_valid() is False