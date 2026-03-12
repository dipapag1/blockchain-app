from app.core.blockchain import Blockchain


def run_demo():
    blockchain = Blockchain()

    print("\n--- Blockchain created ---")
    print("Genesis block:", blockchain.chain[0].to_dict())

    print("\n--- Creating transaction ---")
    blockchain.add_transaction("Alice", "Bob", 10)

    print("Pending transactions:")
    for tx in blockchain.pending_transactions:
        print(tx.to_dict())

    print("\n--- Mining block ---")
    mined_block = blockchain.mine_pending_transactions("Miner1")
    print("New block mined:")
    print(mined_block.to_dict())

    print("\n--- Creating second transaction ---")
    blockchain.add_transaction("Bob", "Alice", 3)

    print("\n--- Mining second block ---")
    blockchain.mine_pending_transactions("Miner1")

    print("\n--- Wallet balances ---")
    print("Alice:", blockchain.get_balance("Alice"))
    print("Bob:", blockchain.get_balance("Bob"))
    print("Miner1:", blockchain.get_balance("Miner1"))

    print("\n--- Chain validation ---")
    print("Is blockchain valid?", blockchain.is_chain_valid())

    print("\n--- Full chain ---")
    for block in blockchain.chain:
        print(block.to_dict())


if __name__ == "__main__":
    run_demo()