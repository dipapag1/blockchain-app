class Transaction:
    """
    Αναπαριστά μία συναλλαγή στο blockchain.

    Μία συναλλαγή περιγράφει τη μεταφορά ενός ποσού από έναν sender
    σε έναν receiver.

    Σε αυτή την απλή εκπαιδευτική υλοποίηση:
    - δεν υπάρχουν ψηφιακές υπογραφές,
    - δεν υπάρχουν wallets/public keys,
    - και το validation είναι βασικό.

    Παρ' όλα αυτά, η κλάση οργανώνει σωστά τη δομή των συναλλαγών
    ώστε να μπορεί αργότερα να επεκταθεί.
    """

    def __init__(self, sender: str, receiver: str, amount: float) -> None:
        """
        Δημιουργεί μία νέα συναλλαγή.

        Args:
            sender: Η διεύθυνση ή το όνομα αυτού που στέλνει το ποσό.
            receiver: Η διεύθυνση ή το όνομα αυτού που λαμβάνει το ποσό.
            amount: Το ποσό της συναλλαγής.

        Raises:
            ValueError: Αν sender/receiver είναι κενά ή αν το amount
            δεν είναι θετικός αριθμός.
        """
        if not sender or not receiver:
            raise ValueError("Sender and receiver are required.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.sender = sender
        self.receiver = receiver
        self.amount = float(amount)

    def to_dict(self) -> dict:
        """
        Μετατρέπει τη συναλλαγή σε dictionary.

        Αυτό είναι χρήσιμο για:
        - hashing block δεδομένων,
        - serialization,
        - logging/debugging,
        - και εμφάνιση μέσω API.

        Returns:
            Dictionary με sender, receiver και amount.
        """
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
        }