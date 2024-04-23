import { Provider } from "react-redux";
import LoginPage from "@/pages/login/LoginPage";
import PocPage from "@/pages/poc/PocPage";
import { HashRouter as Router, Route, Routes } from "react-router-dom";
import store from "@/redux/store";
import HomePage from "@/pages/home/HomePage";

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="w-screen h-screen">
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/home" element={<HomePage />} />
            <Route path="/" element={<LoginPage />} />
          </Routes>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
