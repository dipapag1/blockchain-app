from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    """
    Schema εισόδου για δημιουργία νέας συναλλαγής.

    Χρησιμοποιείται από το POST /api/transactions endpoint
    για να κάνει validation στα δεδομένα του request body.
    """

    sender: str = Field(..., min_length=1, description="Το address του αποστολέα.")
    receiver: str = Field(..., min_length=1, description="Το address του παραλήπτη.")
    amount: float = Field(..., gt=0, description="Το ποσό της συναλλαγής.")


class TransactionData(BaseModel):
    """
    Schema αναπαράστασης μίας συναλλαγής.

    Χρησιμοποιείται σε responses όταν θέλουμε να επιστρέψουμε
    τα δεδομένα μίας συναλλαγής με σταθερή μορφή.
    """

    sender: str
    receiver: str
    amount: float


class TransactionResponse(BaseModel):
    """
    Schema response για endpoint δημιουργίας συναλλαγής.

    Περιέχει:
    - μήνυμα επιτυχίας
    - τα δεδομένα της συναλλαγής που προστέθηκε
    """

    message: str
    transaction: TransactionData