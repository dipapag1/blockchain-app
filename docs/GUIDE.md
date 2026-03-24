
# Developer Setup & Git Workflow Guide

---

## 1. Clone Repository

git clone <REPOSITORY_URL>
cd Blockchain-project/backend

---

## 2. Δημιουργία Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

Linux / macOS:
python3 -m venv venv
source venv/bin/activate

---

## 3. Εγκατάσταση Requirements

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

---

## 4. Έλεγχος ότι το Project λειτουργεί

Run Tests:
python -m pytest -q

Run API:
uvicorn app.main:app --reload

API Docs:
http://127.0.0.1:8000/docs

---

## 5. Git Workflow

Δεν κάνουμε ποτέ push απευθείας στο main.

Workflow:
pull main / pull test
create branch
implement feature
run tests
commit
push branch
open pull request
review
merge

---

## 6. Create Feature Branch

git checkout main
git pull origin main
git checkout -b feature/my-feature-name

---

## 7. Daily Workflow

Check changes:
git status

Add files:
git add .

Commit:
git commit -m "add mining route tests"

Push:
git push origin feature/my-feature-name

---

## 8. Pull Request

1. Push branch
2. Open Pull Request
3. Add description
4. Wait for review

Example title:
Add route tests for transaction and mining endpoints

---

## 9. Before Every Push

python -m pytest -q

---

## 10. Update Branch With Main

git checkout main
git pull origin main
git checkout feature/my-feature-name
git merge main

---

## 11. Commit Message Guidelines

Good examples:
add blockchain service layer
add transaction schema
fix balance validation bug
add route tests
update documentation

Avoid:
fix
stuff
changes
update

---

## 12. Complete Setup Example

git clone <REPOSITORY_URL>
cd Blockchain-project/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload

---

## 13. Project Goal

Educational blockchain backend implementation including:
- blockchain core engine
- transactions
- mining
- proof of work
- chain validation
- REST API
- automated tests
