# TEAM_RULES.md

## Σκοπός έργου

Το project είναι ένα εκπαιδευτικό blockchain / cryptocurrency prototype για πανεπιστημιακή εργασία.

Η υλοποίηση πρέπει να παραμείνει:
- απλή
- καθαρή
- beginner-friendly
- εύκολη στην παρουσίαση και επεξήγηση

Δεν στοχεύουμε σε production-ready σύστημα.

---

## Τεχνολογίες έργου

- Python
- FastAPI
- React
- SHA256 hashing
- simple proof of work

---

## Το project πρέπει να περιλαμβάνει

- blockchain
- blocks
- transactions
- mining
- wallet balances
- REST API
- μικρό React frontend

---

## Το project ΔΕΝ πρέπει να περιλαμβάνει

- smart contracts
- peer-to-peer networking
- authentication / login systems
- microservices
- databases υψηλής πολυπλοκότητας
- advanced cryptography
- distributed nodes
- websocket architecture
- άσχετα επιπλέον features

---

## Βασικές αρχές ανάπτυξης

1. Κάθε αρχείο έχει μία ξεκάθαρη ευθύνη.
2. Δεν γράφουμε business logic σε λάθος layer.
3. Ο κώδικας πρέπει να είναι μικρός, καθαρός και αναγνώσιμος.
4. Όλες οι βασικές συναρτήσεις πρέπει να έχουν docstrings.
5. Δεν προσθέτουμε νέα αρχεία ή φακέλους χωρίς συμφωνία ομάδας.
6. Δεν αλλάζουμε τη δομή του project χωρίς έγκριση του team lead.
7. Προτιμάμε την απλότητα από την “εντύπωση”.
8. Ό,τι υλοποιείται πρέπει να μπορεί να εξηγηθεί εύκολα στην παρουσίαση.

---

## Κανόνες συνεργασίας

- Το `main` παραμένει πάντα σταθερό.
- Το `test` χρησιμοποιείται για integration και δοκιμές πριν το τελικό merge.
- Κάθε μέλος δουλεύει στο δικό του branch.
- Κανένα merge δεν γίνεται χωρίς review.
- Όλα τα commits πρέπει να έχουν καθαρά και περιγραφικά μηνύματα.
- Δεν σβήνουμε ή μετακινούμε αρχεία χωρίς ενημέρωση της ομάδας.

---

## Branches

- `main` → τελικό και σταθερό branch
- `test` → branch ελέγχου / ενοποίησης
- `member1` → core blockchain development
- `member2` → FastAPI backend / routes / schemas
- `member3` → React frontend

---

## Ρόλοι ομάδας

### Member 1
Υπεύθυνος για:
- core blockchain
- block
- transaction
- hashing
- proof of work
- validation
- wallet balance logic

### Member 2
Υπεύθυνος για:
- FastAPI setup
- routes
- request/response schemas
- backend integration

### Member 3
Υπεύθυνος για:
- React frontend
- pages
- components
- API communication από frontend

---

## Ορισμός “σωστού παραδοτέου”

Κάθε κομμάτι θεωρείται ολοκληρωμένο όταν:
- δουλεύει
- είναι μέσα στο scope
- είναι γραμμένο στο σωστό αρχείο
- έχει καθαρή ονοματοδοσία
- έχει docstrings όπου χρειάζεται
- δεν σπάει τη συνολική αρχιτεκτονική