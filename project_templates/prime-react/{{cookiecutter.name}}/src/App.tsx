import { Provider } from "react-redux";
import { HashRouter as Router, Route, Routes } from "react-router-dom";
import store from "@/redux/store";
import HomePage from "@/pages/home/HomePage";
import PocPage from "@/pages/poc/PocPage";
import LoginPage from "@/pages/login/LoginPage";
import Layout from "./pages/Layout";

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="w-screen h-screen">
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            
            {/* Layout Route */}
            <Route element={<Layout />}>
              <Route path="/home" element={<HomePage />} />
              <Route path="/poc" element={<PocPage />} />
            </Route>

            {/* Default Route */}
            <Route path="/" element={<LoginPage />} />
          </Routes>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
