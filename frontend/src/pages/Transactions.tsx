import TransactionForm from "../components/TransactionForm";

interface TransactionsProps {
  onSuccess: () => void;
}

function Transactions({ onSuccess }: TransactionsProps) {
  return (
    <div>
      <h1 className="page-title">Transactions</h1>
      <TransactionForm onSuccess={onSuccess} />
    </div>
  );
}

export default Transactions;