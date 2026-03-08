# FUNCTIONS.md

## Σκοπός

Το αρχείο αυτό περιγράφει τις βασικές συναρτήσεις και μεθόδους που αναμένονται στο project, μαζί με τον ρόλο τους.

Δεν αποτελεί τελικό implementation, αλλά λειτουργεί ως κοινός οδηγός για όλη την ομάδα.

---

# Backend Core

## Block

### __init__(index, timestamp, transactions, previous_hash)
Δημιουργεί ένα block με:
- index
- timestamp
- transactions
- previous_hash
- nonce
- hash

---

## Transaction

### __init__(sender, receiver, amount)
Δημιουργεί μία συναλλαγή με:
- sender
- receiver
- amount

### to_dict()
Επιστρέφει τη συναλλαγή σε μορφή dictionary για εύκολη αποθήκευση / εμφάνιση / serialization.

---

## Blockchain

### __init__()
Αρχικοποιεί:
- chain
- pending_transactions
- mining_reward
- difficulty

και δημιουργεί το genesis block.

### create_genesis_block()
Δημιουργεί το πρώτο block του blockchain.

### calculate_hash(block)
Υπολογίζει το SHA256 hash ενός block.

### proof_of_work(block)
Εκτελεί mining αλλάζοντας το nonce μέχρι το hash να ξεκινά με τον απαιτούμενο αριθμό μηδενικών.

### add_transaction(sender, receiver, amount)
Προσθέτει νέα συναλλαγή στις pending transactions.

### mine_pending_transactions(miner_address)
Δημιουργεί νέο block από τις pending transactions, κάνει mining και προσθέτει reward transaction για τον miner.

### add_block(block)
Προσθέτει block στο chain μετά τον απαραίτητο έλεγχο και το mining.

### get_balance(address)
Υπολογίζει το balance ενός wallet σαρώνοντας όλες τις συναλλαγές του chain.

### get_latest_block()
Επιστρέφει το τελευταίο block της αλυσίδας.

### is_chain_valid()
Ελέγχει:
- αν τα hashes είναι σωστά
- αν τα previous_hash ταιριάζουν
- αν τηρείται το proof of work

---

# Backend API

## Routes

### GET /chain
Επιστρέφει όλο το blockchain.

### GET /pending
Επιστρέφει τις pending transactions.

### POST /transactions
Προσθέτει νέα συναλλαγή.

### POST /mine
Κάνει mining των pending transactions.

### GET /balance/{wallet}
Επιστρέφει το balance ενός wallet.

### GET /validate
Επιστρέφει αν το chain είναι έγκυρο.

---

# Frontend

## Dashboard
Εμφανίζει:
- blocks
- γενική εικόνα chain
- κατάσταση συστήματος

## Transactions page
Επιτρέπει:
- δημιουργία transaction
- εμφάνιση pending transactions

## Mine page
Επιτρέπει:
- mining
- εμφάνιση αποτελέσματος mining

## Balances page
Επιτρέπει:
- αναζήτηση wallet
- εμφάνιση balance