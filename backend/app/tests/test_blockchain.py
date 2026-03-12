import pytest

from app.core.blockchain import Blockchain


def test_genesis_block_created():
    """
    Ελέγχει ότι με τη δημιουργία του blockchain
    παράγεται σωστά το genesis block.
    """
    blockchain = Blockchain()

    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].index == 0
    assert blockchain.chain[0].previous_hash == "0"


def test_add_transaction_requires_existing_balance():
    """
    Ελέγχει ότι μία κανονική συναλλαγή μπορεί να προστεθεί
    μόνο αν ο sender έχει επαρκές balance.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 40)
    blockchain.mine_pending_transactions("Miner1")

    blockchain.add_transaction("Alice", "Bob", 10)

    assert len(blockchain.pending_transactions) == 1
    assert blockchain.pending_transactions[0].sender == "Alice"


def test_add_transaction_insufficient_balance_raises():
    """
    Ελέγχει ότι απορρίπτεται συναλλαγή όταν δεν υπάρχει balance.
    """
    blockchain = Blockchain()

    with pytest.raises(ValueError, match="Insufficient balance"):
        blockchain.add_transaction("Alice", "Bob", 10)


def test_mine_pending_transactions():
    """
    Ελέγχει ότι το mining προσθέτει block στην αλυσίδα
    και καθαρίζει τις pending transactions.
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
    Ελέγχει ότι τα balances υπολογίζονται σωστά
    μετά από mined συναλλαγές.
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
    Ελέγχει ότι μία σωστή αλυσίδα θεωρείται valid.
    """
    blockchain = Blockchain()

    blockchain.add_transaction("SYSTEM", "Alice", 20)
    blockchain.mine_pending_transactions("Miner1")

    assert blockchain.is_chain_valid() is True