import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import { RiBodyScanLine } from "react-icons/ri";
const NavLink = ({ to, children }) => (
  <Link to={to} className="mr-4 cursor-pointer">
    {children}
  </Link>
);

NavLink.propTypes = {
  to: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
};

export function Header() {
  return (
    <header className="bg-gray-800 text-white py-4">
      <div className="container mx-auto flex items-center justify-between">
        <div className="flex items-center">
          <RiBodyScanLine className="mr-2" size={24} />
          <span className="text-xl font-bold">Facio</span>
        </div>
        <div className="flex items-center">
          <NavLink to="/">Landing</NavLink>
          <NavLink to="/about">About</NavLink>
          <NavLink to="/services">Services</NavLink>
          <NavLink to="/support">Support</NavLink>
          <NavLink to="/uploading">Uploading</NavLink>
        </div>
      </div>
    </header>
  );
}
