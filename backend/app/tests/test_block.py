from app.core.block import Block


def test_block_creation():
    """
    Ελέγχει ότι ένα block δημιουργείται σωστά
    και ότι όλα τα βασικά πεδία του αποθηκεύονται σωστά.
    """
    block = Block(
        index=1,
        timestamp=123456.0,
        transactions=[],
        previous_hash="abc123"
    )

    assert block.index == 1
    assert block.timestamp == 123456.0
    assert block.transactions == []
    assert block.previous_hash == "abc123"
    assert block.nonce == 0
    assert block.hash == ""