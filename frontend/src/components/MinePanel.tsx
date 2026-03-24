import React, { useState } from "react";
import { mineBlock } from "../services/api";

function MinePanel() {
  const [minerAddress, setMinerAddress] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleMine = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    setLoading(true);
    setMessage(null);
    setError(null);

    try {
      const res = await mineBlock({
        miner_address: minerAddress,
      });

      setMessage(
        `${res.message} New block #${res.block.index} created successfully.`
      );
      setMinerAddress("");
    } catch (err: unknown) {
      console.error("Mine error:", err);
      setError("Failed to mine block.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h3>Mine Pending Transactions</h3>

      <form onSubmit={handleMine}>
        <input
          value={minerAddress}
          onChange={(e) => setMinerAddress(e.target.value)}
          placeholder="Miner address"
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Mining..." : "Mine Block"}
        </button>
      </form>

      {message && <p className="message-success">{message}</p>}
      {error && <p className="message-error">{error}</p>}
    </div>
  );
}

export default MinePanel;