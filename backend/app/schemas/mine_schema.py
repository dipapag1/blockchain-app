from pydantic import BaseModel, Field

from app.schemas.block_schema import BlockResponse


class MineRequest(BaseModel):
    """
    Schema εισόδου για mining request.

    Χρησιμοποιείται από το POST /api/mine endpoint ώστε
    να δηλωθεί ποιος miner θα λάβει το reward.
    """

    miner_address: str = Field(..., min_length=1, description="Το address του miner.")


class MineResponse(BaseModel):
    """
    Schema response για mining endpoint.

    Περιέχει:
    - μήνυμα επιτυχίας
    - το νέο block που δημιουργήθηκε μετά το mining
    """

    message: str
    block: BlockResponse