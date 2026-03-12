from app.core.transaction import Transaction


def test_transaction_to_dict():
    """
    Ελέγχει ότι ένα Transaction object
    μετατρέπεται σωστά σε dictionary.
    """
    transaction = Transaction("Alice", "Bob", 10)

    assert transaction.sender == "Alice"
    assert transaction.receiver == "Bob"
    assert transaction.amount == 10
    assert transaction.to_dict() == {
        "sender": "Alice",
        "receiver": "Bob",
        "amount": 10,
    }