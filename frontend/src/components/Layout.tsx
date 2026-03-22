import type { ReactNode } from "react";
import Navbar from "./Navbar";

function Layout({ children }: { children: ReactNode }) {
  return (
    <div style={{ padding: "20px" }}>
      <Navbar />
      {children}
    </div>
  );
}

export default Layout;