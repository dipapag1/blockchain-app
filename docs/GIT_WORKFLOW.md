# GIT_WORKFLOW.md

## Στόχος

Να υπάρχει καθαρή, ασφαλής και ελεγχόμενη ροή ανάπτυξης χωρίς να χαθεί η συνοχή του project.

---

## Branches που χρησιμοποιούνται

- `main`
- `test`
- `member1`
- `member2`
- `member3`

---

## Ρόλος κάθε branch

### main
Το τελικό σταθερό branch του project.

Περιέχει μόνο κώδικα που:
- έχει ελεγχθεί
- έχει δοκιμαστεί
- είναι έτοιμος για παρουσίαση / παράδοση

### test
Ενδιάμεσο branch για integration.

Χρησιμοποιείται για:
- συνένωση κομματιών από τα member branches
- έλεγχο ότι backend / frontend / core συνεργάζονται σωστά
- δοκιμές πριν το τελικό merge στο main

### member1
Branch ανάπτυξης του core blockchain.

### member2
Branch ανάπτυξης του FastAPI backend.

### member3
Branch ανάπτυξης του React frontend.

---

## Βασική ροή εργασίας

1. Κάθε μέλος δουλεύει μόνο στο branch του.
2. Κάνει μικρά, καθαρά commits.
3. Ο team lead κάνει review.
4. Το κομμάτι περνά πρώτα στο `test`.
5. Γίνονται integration checks.
6. Όταν όλα δουλεύουν σωστά, γίνεται merge στο `main`.

---

## Κανόνες commit messages

Τα commit messages πρέπει να είναι σύντομα και σαφή.

### Σωστά παραδείγματα
- `Add Block model`
- `Implement proof of work`
- `Add transaction endpoint`
- `Connect dashboard to backend`
- `Create balance page`

### Λάθος παραδείγματα
- `update`
- `fix`
- `last changes`
- `final`
- `code`
- `work done`

---

## Κανόνες merge

- Δεν γίνεται merge απευθείας στο `main` χωρίς έλεγχο.
- Κάθε merge πρέπει να αφορά συγκεκριμένο και λογικό κομμάτι.
- Δεν γίνεται merge μισοτελειωμένου feature.
- Αν ένα feature σπάει άλλο κομμάτι, επιστρέφει για διόρθωση.

---

## Τι ελέγχεται πριν το merge στο test

- Ο κώδικας είναι στο σωστό αρχείο;
- Είναι μέσα στο scope του project;
- Είναι καθαρός και αναγνώσιμος;
- Δεν έχει duplicated logic;
- Δεν σπάει τη δομή του project;
- Δεν προσθέτει περιττή πολυπλοκότητα;

---

## Τι ελέγχεται πριν το merge στο main

- Το backend τρέχει σωστά
- Το frontend επικοινωνεί σωστά με το backend
- Το core blockchain δουλεύει σωστά
- Το mining λειτουργεί
- Τα balances υπολογίζονται σωστά
- Τα βασικά routes απαντούν σωστά
- Το project είναι παρουσιάσιμο

---

## Προτεινόμενη συχνότητα συγχρονισμού

- Συχνά μικρά commits
- Συχνό review
- Συχνές μικρές συνενώσεις στο `test`
- Όχι μεγάλα merges της τελευταίας στιγμής