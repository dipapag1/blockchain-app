from fastapi import APIRouter, HTTPException

from app.schemas.balance_schema import BalanceResponse
from app.schemas.block_schema import BlockResponse
from app.schemas.mine_schema import MineRequest, MineResponse
from app.schemas.response_schema import BlockchainResponse, ValidationResponse
from app.schemas.transaction_schema import TransactionCreate, TransactionResponse
from app.services import blockchain_service


router = APIRouter(prefix="/api", tags=["Blockchain"])


@router.post("/transactions", response_model=TransactionResponse)
def create_transaction(payload: TransactionCreate) -> TransactionResponse:
    """
    Δημιουργεί μία νέα συναλλαγή και την προσθέτει στις pending transactions.

    Το endpoint δέχεται sender, receiver και amount μέσω request body.
    Η πραγματική επιχειρησιακή λογική εκτελείται στο service layer.

    Args:
        payload: Τα δεδομένα της συναλλαγής που έρχονται από το request.

    Returns:
        TransactionResponse: Η συναλλαγή που δημιουργήθηκε μαζί με μήνυμα επιτυχίας.

    Raises:
        HTTPException: Αν τα δεδομένα είναι άκυρα ή δεν υπάρχει επαρκές balance.
    """
    try:
        transaction = blockchain_service.create_transaction(
            sender=payload.sender,
            receiver=payload.receiver,
            amount=payload.amount,
        )
        return TransactionResponse(
            message="Transaction added successfully.",
            transaction=transaction,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/mine", response_model=MineResponse)
def mine_block(payload: MineRequest) -> MineResponse:
    """
    Κάνει mining όλων των pending transactions και δημιουργεί νέο block.

    Το endpoint απαιτεί miner address, ώστε το reward της εξόρυξης
    να καταλήξει στον σωστό παραλήπτη.

    Args:
        payload: Τα δεδομένα του miner που έρχονται από το request body.

    Returns:
        MineResponse: Πληροφορίες για το νέο mined block.

    Raises:
        HTTPException: Αν δεν υπάρχουν pending transactions ή λείπει miner address.
    """
    try:
        block = blockchain_service.mine_block(payload.miner_address)
        return MineResponse(
            message="Block mined successfully.",
            block=block,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/chain", response_model=BlockchainResponse)
def get_blockchain() -> BlockchainResponse:
    """
    Επιστρέφει ολόκληρη την αλυσίδα των blocks.

    Το endpoint αυτό είναι χρήσιμο για:
    - debugging,
    - οπτικοποίηση της αλυσίδας,
    - έλεγχο του ιστορικού των συναλλαγών.

    Returns:
        BlockchainResponse: Το συνολικό chain και το μήκος του.
    """
    chain = blockchain_service.get_chain()
    return BlockchainResponse(
        length=len(chain),
        chain=chain,
    )


@router.get("/balance/{address}", response_model=BalanceResponse)
def get_balance(address: str) -> BalanceResponse:
    """
    Επιστρέφει το confirmed balance ενός address.

    Το balance υπολογίζεται από mined συναλλαγές που βρίσκονται ήδη
    στο blockchain και όχι από pending συναλλαγές.

    Args:
        address: Το wallet address του οποίου θέλουμε το υπόλοιπο.

    Returns:
        BalanceResponse: Το address και το υπολογισμένο balance.

    Raises:
        HTTPException: Αν το address είναι κενό.
    """
    if not address.strip():
        raise HTTPException(status_code=400, detail="Address is required.")

    balance = blockchain_service.get_balance(address)
    return BalanceResponse(
        address=address,
        balance=balance,
    )


@router.get("/validate", response_model=ValidationResponse)
def validate_chain() -> ValidationResponse:
    """
    Ελέγχει αν η αλυσίδα είναι έγκυρη.

    Η εγκυρότητα βασίζεται στους ελέγχους:
    - σωστό hash ανά block,
    - σωστή σύνδεση previous_hash,
    - τήρηση proof of work.

    Returns:
        ValidationResponse: Το αποτέλεσμα του validation.
    """
    is_valid = blockchain_service.validate_chain()
    return ValidationResponse(
        is_valid=is_valid,
    )


@router.get("/latest-block", response_model=BlockResponse)
def get_latest_block() -> BlockResponse:
    """
    Επιστρέφει το τελευταίο block της αλυσίδας.

    Είναι χρήσιμο endpoint όταν θέλουμε γρήγορα να δούμε
    το πιο πρόσφατο mined block χωρίς να ζητήσουμε ολόκληρο το chain.

    Returns:
        BlockResponse: Το τελευταίο block της αλυσίδας.
    """
    block = blockchain_service.get_latest_block()
    return BlockResponse(**block)