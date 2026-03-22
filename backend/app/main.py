<<<<<<< HEAD
=======
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router


app = FastAPI(
    title="Educational Blockchain API",
    description=(
        "REST API για ένα εκπαιδευτικό blockchain project. "
        "Υποστηρίζει δημιουργία συναλλαγών, mining, έλεγχο υπολοίπου, "
        "προβολή της αλυσίδας και validation."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def root() -> dict:
    """
    Βασικό endpoint ελέγχου λειτουργίας του API.

    Χρησιμοποιείται ως απλό health check ώστε να μπορεί
    κάποιος χρήστης ή tester να επιβεβαιώσει ότι η εφαρμογή
    είναι ενεργή και απαντά κανονικά.

    Returns:
        dict: Μήνυμα επιβεβαίωσης ότι το API λειτουργεί.
    """
    return {
        "message": "Blockchain API is running."
    }


app.include_router(router)
>>>>>>> 98d54ff (Apothikeuse to bc project)
