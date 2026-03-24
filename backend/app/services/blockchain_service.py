from app.core.blockchain import Blockchain


blockchain = Blockchain()


def create_transaction(sender: str, receiver: str, amount: float) -> dict:
    """
    Δημιουργεί μία νέα συναλλαγή μέσω του core blockchain engine.

    Η συνάρτηση αυτή αποτελεί μέρος του service layer και αναλαμβάνει
    να καλέσει το αντίστοιχο core method, επιστρέφοντας serializable
    δεδομένα κατάλληλα για χρήση από τα API routes.

    Args:
        sender: Ο αποστολέας της συναλλαγής.
        receiver: Ο παραλήπτης της συναλλαγής.
        amount: Το ποσό της συναλλαγής.

    Returns:
        dict: Τα δεδομένα της συναλλαγής σε dictionary μορφή.

    Raises:
        ValueError: Αν η συναλλαγή είναι άκυρη ή δεν υπάρχει επαρκές balance.
    """
    transaction = blockchain.add_transaction(sender, receiver, amount)
    return transaction.to_dict()


def mine_block(miner_address: str) -> dict:
    """
    Κάνει mining όλων των pending transactions.

    Η συνάρτηση καλεί το core mining logic και επιστρέφει
    το νέο block σε serializable μορφή.

    Args:
        miner_address: Το address που θα λάβει το mining reward.

    Returns:
        dict: Το νέο mined block σε dictionary μορφή.

    Raises:
        ValueError: Αν το mining δεν μπορεί να εκτελεστεί.
    """
    block = blockchain.mine_pending_transactions(miner_address)
    return block.to_dict()


def get_chain() -> list[dict]:
    """
    Επιστρέφει όλη την αλυσίδα σε serializable μορφή.

    Returns:
        list[dict]: Λίστα από blocks σε dictionary μορφή.
    """
    return [block.to_dict() for block in blockchain.chain]


def get_balance(address: str) -> float:
    """
    Υπολογίζει το confirmed balance ενός address.

    Args:
        address: Το address του οποίου θέλουμε το υπόλοιπο.

    Returns:
        float: Το επιβεβαιωμένο balance του address.
    """
    return blockchain.get_balance(address)


def validate_chain() -> bool:
    """
    Ελέγχει αν η αλυσίδα είναι έγκυρη.

    Returns:
        bool: True αν το chain είναι valid, αλλιώς False.
    """
    return blockchain.is_chain_valid()


def get_latest_block() -> dict:
    """
    Επιστρέφει το τελευταίο block της αλυσίδας.

    Returns:
        dict: Το τελευταίο block σε dictionary μορφή.
    """
    return blockchain.get_latest_block().to_dict()