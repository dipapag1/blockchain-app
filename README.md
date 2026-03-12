# Educational Blockchain API

Ένα εκπαιδευτικό backend project blockchain, υλοποιημένο με **Python** και **FastAPI**.  
Το project περιλαμβάνει τον βασικό πυρήνα ενός blockchain συστήματος, όπως blocks, transactions, hashing, proof of work, mining, validation, balance calculation, καθώς και REST API endpoints για αλληλεπίδραση με το σύστημα.

---

## Features

- Block class
- Transaction class
- Blockchain class
- SHA256 hashing
- Proof of Work
- Mining mechanism
- Chain validation
- Balance calculation
- Overspending protection
- FastAPI REST API
- Pydantic schemas
- Service layer
- Core tests
- Route tests
- Auto-generated API documentation

---

## Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── block.py
│   │   ├── blockchain.py
│   │   ├── transaction.py
│   │   └── utils.py
│   │
│   ├── schemas/
│   │   ├── balance_schema.py
│   │   ├── block_schema.py
│   │   ├── mine_schema.py
│   │   ├── response_schema.py
│   │   └── transaction_schema.py
│   │
│   ├── services/
│   │   └── blockchain_service.py
│   │
│   ├── tests/
│   │   └── test_routes.py
│   │
│   └── main.py
│
├── requirements.txt
├── test_core.py
└── README.md


## Developer Documentation

Για οδηγίες εγκατάστασης και συνεργασίας δείτε:

docs/GUIDE.md