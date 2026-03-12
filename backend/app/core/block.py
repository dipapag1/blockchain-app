from __future__ import annotations

from typing import Any


class Block:
    """
    Αναπαριστά ένα block του blockchain.

    Κάθε block περιέχει:
    - έναν αύξοντα αριθμό θέσης (index),
    - τη χρονική στιγμή δημιουργίας του (timestamp),
    - τη λίστα συναλλαγών που περιλαμβάνει,
    - το hash του προηγούμενου block,
    - ένα nonce που χρησιμοποιείται στο proof of work,
    - και το τελικό hash του block.

    Το block από μόνο του είναι ένα container δεδομένων.
    Η δημιουργία του hash και η επικύρωσή του γίνονται από την Blockchain class.
    """

    def __init__(
        self,
        index: int,
        timestamp: float,
        transactions: list,
        previous_hash: str,
        nonce: int = 0,
        hash_value: str = "",
    ) -> None:
        """
        Αρχικοποιεί ένα νέο block.

        Args:
            index: Η θέση του block μέσα στην αλυσίδα.
            timestamp: Η χρονική στιγμή δημιουργίας του block.
            transactions: Η λίστα των συναλλαγών που περιέχονται στο block.
            previous_hash: Το hash του προηγούμενου block της αλυσίδας.
            nonce: Αριθμός που μεταβάλλεται κατά το proof of work.
            hash_value: Το τελικό hash του block, αν είναι ήδη γνωστό.
        """
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = hash_value

    def to_dict(self) -> dict[str, Any]:
        """
        Μετατρέπει το block σε dictionary.

        Η μέθοδος αυτή χρησιμοποιείται για serialization, debugging
        και ευκολότερη εμφάνιση των δεδομένων του block.

        Αν κάποια transactions είναι αντικείμενα που διαθέτουν `to_dict()`,
        μετατρέπονται και αυτές σε dictionaries ώστε το τελικό αποτέλεσμα
        να είναι πλήρως serializable.

        Returns:
            Dictionary με όλα τα βασικά δεδομένα του block.
        """
        serialized_transactions = [
            tx.to_dict() if hasattr(tx, "to_dict") else tx
            for tx in self.transactions
        ]

        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": serialized_transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash,
        }