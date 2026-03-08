# ARCHITECTURE.md

## Γενική περιγραφή

Το project είναι ένα απλό εκπαιδευτικό blockchain prototype με backend σε Python / FastAPI και frontend σε React.

Η αρχιτεκτονική του είναι σκόπιμα απλή ώστε να είναι:
- εύκολη στην κατανόηση
- εύκολη στην ανάπτυξη από ομάδα
- εύκολη στην παρουσίαση σε πανεπιστημιακή εργασία

---

## Βασικά υποσυστήματα

Το project χωρίζεται σε 3 βασικά μέρη:

1. Core Blockchain Logic
2. REST API Backend
3. React Frontend

---

## 1. Core Blockchain Logic

Το core περιέχει όλη τη βασική λογική του blockchain:

- block structure
- transactions
- hashing
- proof of work
- mining
- wallet balances
- chain validation

Το core ΔΕΝ πρέπει να γνωρίζει τίποτα για:
- HTTP
- routes
- frontend
- UI

---

## 2. REST API Backend

Το backend εκθέτει το core μέσω REST API.

Ρόλος του:
- να λαμβάνει requests
- να καλεί τη λογική του blockchain
- να επιστρέφει JSON responses

Το backend ΔΕΝ πρέπει να ξαναγράφει το blockchain logic.

---

## 3. React Frontend

Το frontend παρέχει απλή διεπαφή χρήστη.

Ρόλος του:
- να εμφανίζει τα δεδομένα
- να στέλνει requests στο backend
- να επιτρέπει αλληλεπίδραση με transactions / mining / balances

Το frontend ΔΕΝ πρέπει να περιέχει blockchain logic.

---

## Ροή δεδομένων

### Προσθήκη συναλλαγής
Frontend → FastAPI route → Blockchain.add_transaction() → response

### Mining
Frontend → FastAPI route → Blockchain.mine_pending_transactions() → νέο block → response

### Έλεγχος balance
Frontend → FastAPI route → Blockchain.get_balance(wallet) → response

### Προβολή chain
Frontend → FastAPI route → Blockchain.chain → response

---

## Αρχιτεκτονική επιπέδων

### Core layer
Περιέχει:
- `block.py`
- `transaction.py`
- `blockchain.py`
- `utils.py`

### API layer
Περιέχει:
- `main.py`
- `routes.py`
- `schemas/`
- `services/`

### Presentation layer
Περιέχει:
- React pages
- React components
- api service calls

---

## Γιατί επιλέχθηκε αυτή η αρχιτεκτονική

Η αρχιτεκτονική αυτή επιλέχθηκε γιατί:
- διαχωρίζει καθαρά τις ευθύνες
- επιτρέπει ομαδική εργασία χωρίς σύγχυση
- κρατά τον κώδικα απλό και ελεγχόμενο
- αποφεύγει περιττή πολυπλοκότητα
- ταιριάζει σε εκπαιδευτικό project

---

## Εκτός scope

Η αρχιτεκτονική δεν περιλαμβάνει:
- peer-to-peer nodes
- distributed consensus μεταξύ κόμβων
- smart contracts
- login / users
- production security
- microservices
- databases υψηλής πολυπλοκότητας

---

## Βασική τεχνική ιδέα

Κάθε νέο block:
- περιέχει συναλλαγές
- συνδέεται με το προηγούμενο μέσω `previous_hash`
- αποκτά hash μέσω SHA256
- εξορύσσεται μέσω απλού proof of work

Έτσι προκύπτει μία αλυσίδα blocks που μπορεί να ελεγχθεί για ακεραιότητα.