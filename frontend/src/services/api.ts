import axios from "axios";
import type {
  BlockchainResponse,
  ValidationResponse,
  TransactionCreatePayload,
  TransactionResponse,
  MineRequestPayload,
  MineResponse,
} from "../types/blockchain";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getChain = async (): Promise<BlockchainResponse> => {
  const response = await api.get("/api/chain");
  return response.data;
};

export const validateChain = async (): Promise<ValidationResponse> => {
  const response = await api.get("/api/validate");
  return response.data;
};

export const createTransaction = async (
  payload: TransactionCreatePayload
): Promise<TransactionResponse> => {
  const response = await api.post("/api/transactions", payload);
  return response.data;
};

export const mineBlock = async (
  payload: MineRequestPayload
): Promise<MineResponse> => {
  const response = await api.post("/api/mine", payload);
  return response.data;
};

export default api;