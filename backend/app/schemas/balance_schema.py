from pydantic import BaseModel


class BalanceResponse(BaseModel):
    """
    Schema response για balance endpoint.

    Επιστρέφει το address που ζητήθηκε και
    το υπολογισμένο confirmed balance του.
    """

    address: str
    balance: float