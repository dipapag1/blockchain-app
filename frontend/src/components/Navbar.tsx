import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <div className="navbar">
      <NavLink to="/">Dashboard </NavLink>
      <NavLink to="/transactions">Transactions </NavLink>
      <NavLink to="/mine">Mine</NavLink>
    </div>
  );
}

export default Navbar;