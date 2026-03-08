# FILE_RESPONSIBILITIES.md

## Σκοπός

Το αρχείο αυτό ορίζει τον ρόλο κάθε αρχείου του project.

Κάθε μέλος πρέπει να γράφει μόνο το περιεχόμενο που ανήκει στο συγκεκριμένο αρχείο.

Δεν μεταφέρουμε λογική σε λάθος σημείο και δεν προσθέτουμε άσχετο κώδικα.

---

# ROOT

## .gitignore
Περιέχει αρχεία και φακέλους που δεν πρέπει να ανεβαίνουν στο Git.

## README.md
Κεντρική περιγραφή του project:
- τι είναι
- τεχνολογίες
- setup
- βασικά features
- πώς τρέχει

---

# DOCS

## ARCHITECTURE.md
Περιγράφει τη συνολική αρχιτεκτονική του project.

## TEAM_RULES.md
Περιγράφει κανόνες συνεργασίας και scope.

## GIT_WORKFLOW.md
Περιγράφει branches, commits, merge flow.

## FUNCTIONS.md
Περιγράφει τις βασικές functions / methods / endpoints.

## API_SPEC.md
Περιγράφει τα endpoints, request bodies και responses του backend.

## FRONTEND_PAGES.md
Περιγράφει τις σελίδες και τα βασικά UI στοιχεία του frontend.

## TESTING.md
Περιγράφει τι tests πρέπει να γίνουν και τι ελέγχουμε.

## PRESENTATION_NOTES.md
Περιγράφει βασικά σημεία που θα παρουσιαστούν στην τελική εργασία.

## FILE_RESPONSIBILITIES.md
Περιγράφει τον ρόλο κάθε αρχείου του project.

---

# BACKEND

## backend/README.md
Τοπικό README μόνο για το backend:
- εγκατάσταση
- dependencies
- τρόπος εκτέλεσης

## backend/requirements.txt
Όλα τα Python dependencies του backend.

## backend/run.py
Απλό entry point για εύκολη εκκίνηση του backend.

---

# BACKEND / APP

## backend/app/__init__.py
Αρχείο package initialization. Δεν περιέχει business logic.

## backend/app/main.py
Δημιουργία FastAPI app και σύνδεση routes.

Δεν περιέχει core blockchain logic.

---

# BACKEND / API

## backend/app/api/__init__.py
Package init file.

## backend/app/api/routes.py
Όλα τα REST API routes.

Περιέχει:
- route definitions
- λήψη request data
- κλήση service/core logic
- response επιστροφή

Δεν περιέχει:
- proof of work implementation
- hash generation logic
- μεγάλα business rules

---

# BACKEND / CORE

## backend/app/core/__init__.py
Package init file.

## backend/app/core/block.py
Ορισμός της κλάσης Block και μόνο.

## backend/app/core/transaction.py
Ορισμός της κλάσης Transaction και μόνο.

## backend/app/core/blockchain.py
Η βασική λογική του blockchain:
- chain
- pending transactions
- genesis block
- proof of work
- mining
- validation
- balances

## backend/app/core/utils.py
Βοηθητικές συναρτήσεις όπως hashing ή serialization helpers.

Δεν περιέχει state του blockchain.

---

# BACKEND / SCHEMAS

## backend/app/schemas/__init__.py
Package init file.

## backend/app/schemas/transaction_schema.py
Schema για request/response σχετικό με transactions.

## backend/app/schemas/mine_schema.py
Schema για mining requests / mining responses.

## backend/app/schemas/balance_schema.py
Schema για balance responses.

## backend/app/schemas/block_schema.py
Schema για block serialization / response μορφή.

## backend/app/schemas/response_schema.py
Γενικά response models για σταθερή μορφή απαντήσεων.

---

# BACKEND / SERVICES

## backend/app/services/__init__.py
Package init file.

## backend/app/services/blockchain_service.py
Ενδιάμεση πρόσβαση στο blockchain instance.

Χρησιμοποιείται ώστε τα routes να μη χειρίζονται απευθείας όλη τη λογική.

Δεν ξαναγράφει το core logic.

---

# BACKEND / TESTS

## backend/app/tests/__init__.py
Package init file.

## backend/app/tests/test_block.py
Tests για την κλάση Block.

## backend/app/tests/test_transaction.py
Tests για την κλάση Transaction.

## backend/app/tests/test_blockchain.py
Tests για το blockchain core:
- genesis
- hashing
- mining
- validation
- balances

## backend/app/tests/test_routes.py
Tests για τα API routes.

---

# BACKEND / DATA

## backend/data/.gitkeep
Κρατά τον φάκελο data στο repository.

---

# FRONTEND

## frontend/README.md
Τοπικό README μόνο για το frontend:
- setup
- install
- run instructions

## frontend/package.json
Dependencies και scripts του frontend.

## frontend/tsconfig.json
Ρυθμίσεις TypeScript.

## frontend/vite.config.ts
Ρυθμίσεις Vite.

---

# FRONTEND / PUBLIC

## frontend/public/.gitkeep
Κρατά τον φάκελο public στο repository.

---

# FRONTEND / SRC

## frontend/src/main.tsx
Frontend entry point.

## frontend/src/App.tsx
Κεντρικό component / routing / layout setup.

## frontend/src/index.css
Βασικά global styles.

---

# FRONTEND / PAGES

## frontend/src/pages/Dashboard.tsx
Κεντρική εικόνα του blockchain:
- blocks
- overview
- κατάσταση chain

## frontend/src/pages/Transactions.tsx
Σελίδα συναλλαγών:
- form δημιουργίας
- pending transactions list

## frontend/src/pages/Mine.tsx
Σελίδα mining:
- mine button
- αποτέλεσμα mining
- miner input αν χρειάζεται

## frontend/src/pages/Balances.tsx
Σελίδα ελέγχου balance wallet.

---

# FRONTEND / COMPONENTS

## frontend/src/components/Layout.tsx
Κοινό layout σελίδων.

## frontend/src/components/Navbar.tsx
Πλοήγηση μεταξύ σελίδων.

## frontend/src/components/BlockCard.tsx
Εμφάνιση ενός block.

## frontend/src/components/TransactionForm.tsx
Form για νέα συναλλαγή.

## frontend/src/components/PendingTransactions.tsx
Εμφάνιση pending transactions.

## frontend/src/components/MinePanel.tsx
UI για mining action και αποτέλεσμα.

## frontend/src/components/BalanceCard.tsx
Εμφάνιση balance wallet.

---

# FRONTEND / SERVICES

## frontend/src/services/api.ts
Όλες οι κλήσεις προς το FastAPI backend.

Δεν περιέχει UI code.

---

# FRONTEND / TYPES

## frontend/src/types/blockchain.ts
TypeScript types/interfaces για:
- Block
- Transaction
- Balance response
- API response structures

---

# FRONTEND / UTILS

## frontend/src/utils/format.ts
Μικρές βοηθητικές functions μορφοποίησης:
- dates
- hash preview
- numbers

Δεν περιέχει business logic.

---

# GITHUB

## .github/PULL_REQUEST_TEMPLATE.md
Template για pull request περιγραφή:
- τι άλλαξε
- ποια αρχεία επηρεάζει
- τι δοκιμάστηκε
- τι πρέπει να ελεγχθεί