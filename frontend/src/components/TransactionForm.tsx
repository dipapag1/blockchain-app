import { useState } from "react";
import axios from "axios";
import { createTransaction } from "../services/api";

interface TransactionFormProps {
  onSuccess: () => void;
}

function TransactionForm({ onSuccess }: TransactionFormProps) {
  const [sender, setSender] = useState("");
  const [receiver, setReceiver] = useState("");
  const [amount, setAmount] = useState(1);

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault();

  setLoading(true);
  setMessage(null);
  setError(null);

  const payload = {
    sender: sender.trim(),
    receiver: receiver.trim(),
    amount: Number(amount),
  };

  console.log("TRANSACTION PAYLOAD:", payload);

  try {
    const res = await createTransaction(payload);

    setError(null);
    setMessage(res.message);

    setSender("");
    setReceiver("");
    setAmount(1);

    onSuccess();
  } catch (err: unknown) {
    setMessage(null);

    if (axios.isAxiosError(err)) {
      console.error("Transaction error:", err);
      console.error("Response data:", err.response?.data);
      console.error("Status:", err.response?.status);

      setError(
        err.response?.data?.detail ||
          err.response?.data?.message ||
          "Failed to create transaction"
      );
    } else {
      console.error("Unexpected error:", err);
      setError("Failed to create transaction");
    }
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="card">
      <h3>Create Transaction</h3>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Sender</label>
          <input
            value={sender}
            onChange={(e) => setSender(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Receiver</label>
          <input
            value={receiver}
            onChange={(e) => setReceiver(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Amount</label>
          <input
            type="number"
            min="1"
            value={amount}
            onChange={(e) => setAmount(Number(e.target.value))}
            required
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? "Sending..." : "Send Transaction"}
        </button>
      </form>

      {message && <p className="message-success">{message}</p>}
      {error && <p className="message-error">{error}</p>}
    </div>
  );
}

export default TransactionForm;