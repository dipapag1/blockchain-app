import { Routes, Route, Navigate } from "react-router-dom";
import { useState } from "react";
import Layout from "./components/Layout";
import Dashboard from "./pages/Dashboard";
import Transactions from "./pages/Transactions";
import Mine from "./pages/Mine";

function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  const triggerRefresh = () => {
    setRefreshKey((prev) => prev + 1);
  };

  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Dashboard refreshKey={refreshKey} />} />
        <Route
          path="/transactions"
          element={<Transactions onSuccess={triggerRefresh} />}
        />
        <Route
          path="/mine"
          element={<Mine onSuccess={triggerRefresh} />}
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Layout>
  );
}

export default App;