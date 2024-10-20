import { Outlet } from "react-router-dom";
import SidebarMenu from "@/components/SidebarMenu";
import ThemeSwitcher from "@/components/ThemeSwitcher";

export default function Layout() {
  return (
    <>
      {/* SidebarMenu component with the Sidebar and Menu */}
      <SidebarMenu />
      <ThemeSwitcher />

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
