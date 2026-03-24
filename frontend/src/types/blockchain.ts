export interface Transaction {
  sender: string;
  receiver: string;
  amount: number;
}

export interface Block {
  index: number;
  timestamp: number;
  transactions: Transaction[];
  previous_hash: string;
  nonce: number;
  hash: string;
}

export interface BlockchainResponse {
  length: number;
  chain: Block[];
}

export interface ValidationResponse {
  is_valid: boolean;
}

export interface TransactionCreatePayload {
  sender: string;
  receiver: string;
  amount: number;
}

export interface TransactionResponse {
  message: string;
  transaction: Transaction;
}

export interface MineRequestPayload {
  miner_address: string;
}

export interface MineResponse {
  message: string;
  block: Block;
}