export const formatTimestamp = (timestamp: number): string => {
  const date = new Date(timestamp * 1000);
  if (isNaN(date.getTime())) {
    return "Invalid date";
  }
  return date.toLocaleString("el-GR");
};

export const shortenHash = (hash: string, start = 10, end = 10): string => {
  if (!hash) return "-";
  if (hash.length <= start + end) return hash;
  return `${hash.slice(0, start)}...${hash.slice(-end)}`;
};