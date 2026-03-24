import hashlib
import json


def hash_block_data(block_data: dict) -> str:
    """
    Υπολογίζει SHA256 hash από τα δεδομένα ενός block.

    Η συνάρτηση μετατρέπει πρώτα το dictionary σε σταθερό JSON string
    με ταξινομημένα keys, ώστε το ίδιο ακριβώς περιεχόμενο να παράγει
    πάντα το ίδιο hash.

    Αυτό είναι πολύ σημαντικό στο blockchain, επειδή μικρή αλλαγή
    στα δεδομένα πρέπει να παράγει τελείως διαφορετικό hash.

    Args:
        block_data: Dictionary που περιέχει τα δεδομένα του block
        χωρίς να συμπεριλαμβάνει κυκλικά ή μη serializable αντικείμενα.

    Returns:
        Το SHA256 hash των δεδομένων σε hexadecimal μορφή.
    """
    block_string = json.dumps(
        block_data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")

    return hashlib.sha256(block_string).hexdigest()