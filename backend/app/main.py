from fastapi import FastAPI

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