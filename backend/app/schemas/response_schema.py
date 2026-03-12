from pydantic import BaseModel

from app.schemas.block_schema import BlockResponse


class BlockchainResponse(BaseModel):
    """
    Schema response για endpoint που επιστρέφει όλο το blockchain.

    Περιέχει:
    - το συνολικό μήκος της αλυσίδας
    - τη λίστα όλων των blocks
    """

    length: int
    chain: list[BlockResponse]


class ValidationResponse(BaseModel):
    """
    Schema response για endpoint validation.

    Επιστρέφει μόνο το αποτέλεσμα του ελέγχου εγκυρότητας
    της αλυσίδας.
    """

    is_valid: bool