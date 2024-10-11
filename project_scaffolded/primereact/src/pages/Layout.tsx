import { Outlet, useNavigate } from "react-router-dom";
import { Sidebar } from "primereact/sidebar";
import { Menu } from "primereact/menu";
import { Button } from "primereact/button";
import { useState } from "react";
import { buttonDefaultPt } from "@/defaultPt";

export default function Layout() {
  const [visible, setVisible] = useState(false);
  const navigate = useNavigate();

  const menuItems = [
    {
      label: "Home",
      items: [
        {
          label: "Home Page",
          icon: "pi pi-home",
          command: () => {
            navigate("/home");
          },
        },
        {
          label: "POC Page",
          icon: "pi pi-code",
          command: () => {
            navigate("/poc");
          },
        },
        {
          label: "Logout",
          icon: "pi pi-sign-out",
          command: () => {
            navigate("/login");
          },
        },
      ],
    },
  ];

  return (
    <>
      {/* Sidebar with the Menu */}
      <Sidebar visible={visible} onHide={() => setVisible(false)}>
        <div className="flex flex-col gap-3">
          <h2 className="text-center font-bold">Menu</h2>
          {/* Menu component from PrimeReact */}
          <Menu model={menuItems} className="w-full min-w-full" />
        </div>
      </Sidebar>

      {/* Button to toggle the sidebar */}
      <Button
        icon="pi pi-bars"
        size="large"
        className="top-0 left-0 ml-2 mt-2"
        
        style={{ position: "fixed" }}
        
        onClick={() => setVisible(true)}
        pt={buttonDefaultPt}
      />

      {/* Header Section */}
      <header className="text-white flex justify-center font-bold text-2xl p-5 bg-primary mb-2">
        Application Header
      </header>

      {/* Main content area */}
      <main className="flex flex-col w-full mb-5">
        {/* Outlet renders the current route component */}
        <Outlet />
      </main>
    </>
  );
}
