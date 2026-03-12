from pydantic import BaseModel

from app.schemas.transaction_schema import TransactionData


class BlockResponse(BaseModel):
    """
    Schema αναπαράστασης block σε API response.

    Περιέχει όλα τα βασικά πεδία ενός block:
    - index
    - timestamp
    - transactions
    - previous_hash
    - nonce
    - hash
    """

    index: int
    timestamp: float
    transactions: list[TransactionData]
    previous_hash: str
    nonce: int
    hash: str