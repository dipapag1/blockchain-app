import type { Block } from "../types/blockchain";
import { formatTimestamp, shortenHash } from "../utils/format";
interface Props {
  block: Block;
}

function BlockCard({ block }: Props) {
  return (
    <div className="card">
      <h3>Block #{block.index}</h3>

      <div className="block-meta">
        <div>
          <strong>Timestamp:</strong> {formatTimestamp(block.timestamp)}
        </div>

        <div>
          <strong>Hash:</strong> {shortenHash(block.hash)}
        </div>

        <div>
          <strong>Previous Hash:</strong> {shortenHash(block.previous_hash)}
        </div>

        <div>
          <strong>Nonce:</strong> {block.nonce}
        </div>

        <div>
          <strong>Transactions:</strong> {block.transactions.length}
        </div>
      </div>
    </div>
  );
}

export default BlockCard;