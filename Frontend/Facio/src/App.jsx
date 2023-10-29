import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Landing } from "./components/Landing";
import { Uploading } from "./components/Uploading";
import { Support } from "./components/Support";
import { About } from "./components/About";
import { Services } from "./components/Services";
import { Header } from "./components/Header"; // Make sure to import the Header component

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/Uploading" element={<Uploading />} />
        <Route path="/Support" element={<Support />} />
        <Route path="/About" element={<About />} />
        <Route path="/Services" element={<Services />} />
      </Routes>
    </Router>
  );
}

export default App;
