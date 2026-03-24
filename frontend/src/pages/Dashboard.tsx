import { useEffect, useState } from "react";
import { getChain, validateChain } from "../services/api";
import type { Block } from "../types/blockchain";
import BlockCard from "../components/BlockCard";

function Dashboard() {
  const [blocks, setBlocks] = useState<Block[]>([]);
  const [chainLength, setChainLength] = useState<number>(0);
  const [isValid, setIsValid] = useState<boolean | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadDashboard = async () => {
      try {
        setLoading(true);
        setError(null);

        const [chain, validation] = await Promise.all([
          getChain(),
          validateChain(),
        ]);

        setChainLength(chain.length);
        setBlocks(chain.chain);
        setIsValid(validation.is_valid);
      } catch (err) {
        console.error("Dashboard load error:", err);
        setError("Failed to load blockchain data.");
      } finally {
        setLoading(false);
      }
    };

    loadDashboard();
  }, []);

  return (
    <div>
      <h1 className="page-title">Dashboard</h1>

      {loading && <div className="card">Loading blockchain data...</div>}
      {error && <div className="card message-error">{error}</div>}

      {!loading && !error && (
        <>
          <div className="dashboard-grid">
            <div className="card">
              <h3>Chain Length</h3>
              <p>{chainLength}</p>
            </div>

            <div className="card">
              <h3>Validation</h3>
              <p className={isValid ? "message-success" : "message-error"}>
                {isValid ? "Valid Blockchain" : "Invalid Blockchain"}
              </p>
            </div>
          </div>

          {blocks.map((block) => (
            <BlockCard key={block.index} block={block} />
          ))}
        </>
      )}
    </div>
  );
}

export default Dashboard;