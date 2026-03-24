from fastapi.testclient import TestClient

from app.main import app
from app.services.blockchain_service import blockchain


client = TestClient(app)


def reset_blockchain_state() -> None:
    """
    Επαναφέρει την κατάσταση του shared blockchain instance.

    Το service layer χρησιμοποιεί ένα global Blockchain object.
    Για να είναι ανεξάρτητα τα route tests, αδειάζουμε chain
    και pending transactions και ξαναδημιουργούμε genesis block
    πριν από κάθε βασικό test scenario.
    """
    blockchain.chain = []
    blockchain.pending_transactions = []
    blockchain.create_genesis_block()


def test_root_endpoint():
    """
    Ελέγχει ότι το root endpoint απαντά σωστά
    και επιβεβαιώνει ότι το API λειτουργεί.
    """
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Blockchain API is running."


def test_create_transaction_and_mine_flow():
    """
    Ελέγχει ολόκληρη τη βασική ροή του API:

    1. Χρηματοδότηση της Alice από το SYSTEM
    2. Mining του funding block
    3. Δημιουργία κανονικής συναλλαγής Alice -> Bob
    4. Mining δεύτερου block
    5. Έλεγχος balances
    """
    reset_blockchain_state()

    response_fund = client.post(
        "/api/transactions",
        json={
            "sender": "SYSTEM",
            "receiver": "Alice",
            "amount": 50
        }
    )
    assert response_fund.status_code == 200
    assert response_fund.json()["transaction"]["receiver"] == "Alice"

    response_mine_1 = client.post(
        "/api/mine",
        json={"miner_address": "Miner1"}
    )
    assert response_mine_1.status_code == 200
    assert response_mine_1.json()["block"]["index"] == 1

    response_tx = client.post(
        "/api/transactions",
        json={
            "sender": "Alice",
            "receiver": "Bob",
            "amount": 10
        }
    )
    assert response_tx.status_code == 200
    assert response_tx.json()["transaction"]["sender"] == "Alice"

    response_mine_2 = client.post(
        "/api/mine",
        json={"miner_address": "Miner1"}
    )
    assert response_mine_2.status_code == 200
    assert response_mine_2.json()["block"]["index"] == 2

    response_balance_alice = client.get("/api/balance/Alice")
    response_balance_bob = client.get("/api/balance/Bob")
    response_balance_miner = client.get("/api/balance/Miner1")

    assert response_balance_alice.status_code == 200
    assert response_balance_bob.status_code == 200
    assert response_balance_miner.status_code == 200

    assert response_balance_alice.json()["balance"] == 40.0
    assert response_balance_bob.json()["balance"] == 10.0
    assert response_balance_miner.json()["balance"] == 100.0


def test_chain_endpoint():
    """
    Ελέγχει ότι το endpoint του chain επιστρέφει σωστά
    το μήκος της αλυσίδας και τη λίστα των blocks.
    """
    reset_blockchain_state()

    response = client.get("/api/chain")

    assert response.status_code == 200
    assert response.json()["length"] == 1
    assert isinstance(response.json()["chain"], list)
    assert response.json()["chain"][0]["index"] == 0


def test_validate_endpoint():
    """
    Ελέγχει ότι το validate endpoint επιστρέφει
    True για μία σωστή αλυσίδα.
    """
    reset_blockchain_state()

    response = client.get("/api/validate")

    assert response.status_code == 200
    assert response.json()["is_valid"] is True


def test_latest_block_endpoint():
    """
    Ελέγχει ότι το endpoint latest-block επιστρέφει
    το πιο πρόσφατο block της αλυσίδας.
    """
    reset_blockchain_state()

    response = client.get("/api/latest-block")

    assert response.status_code == 200
    assert response.json()["index"] == 0
    assert response.json()["previous_hash"] == "0"


def test_create_transaction_with_insufficient_balance():
    """
    Ελέγχει ότι το API απορρίπτει συναλλαγή όταν ο sender
    δεν έχει αρκετό confirmed διαθέσιμο balance.
    """
    reset_blockchain_state()

    response = client.post(
        "/api/transactions",
        json={
            "sender": "Alice",
            "receiver": "Bob",
            "amount": 10
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient balance."


def test_mine_without_pending_transactions():
    """
    Ελέγχει ότι το API απορρίπτει αίτημα mining
    όταν δεν υπάρχουν pending transactions.
    """
    reset_blockchain_state()

    response = client.post(
        "/api/mine",
        json={"miner_address": "Miner1"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "There are no pending transactions to mine."