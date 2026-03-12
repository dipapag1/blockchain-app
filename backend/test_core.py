from app.core.blockchain import Blockchain


def run_demo():
    blockchain = Blockchain()

    print("\n--- Blockchain created ---")
    print("Genesis block:", blockchain.chain[0].to_dict())

    print("\n--- Funding Alice ---")
    blockchain.add_transaction("SYSTEM", "Alice", 50)
    funding_block = blockchain.mine_pending_transactions("Miner1")
    print("Funding block mined:")
    print(funding_block.to_dict())

    print("\n--- Creating transaction ---")
    blockchain.add_transaction("Alice", "Bob", 10)
    print("Pending transactions:")
    for tx in blockchain.pending_transactions:
        print(tx.to_dict())

    print("\n--- Mining block ---")
    new_block = blockchain.mine_pending_transactions("Miner1")
    print("New block mined:")
    print(new_block.to_dict())

    print("\n--- Checking balances ---")
    print("Alice balance:", blockchain.get_balance("Alice"))
    print("Bob balance:", blockchain.get_balance("Bob"))
    print("Miner1 balance:", blockchain.get_balance("Miner1"))

    print("\n--- Validating chain ---")
    print("Is blockchain valid?", blockchain.is_chain_valid())


if __name__ == "__main__":
    run_demo()