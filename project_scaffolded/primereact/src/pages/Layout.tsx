import { Outlet } from "react-router-dom";
import SidebarMenu from "@/components/SidebarMenu";
import ThemeSwitcher from "@/components/ThemeSwitcher";

export default function Layout() {
  return (
    <>
      {/* Header Section */}
      <header className="text-white flex justify-between items-center font-bold text-2xl p-3 bg-primary mb-2">
        <SidebarMenu />
        <h2>Application Header</h2>
        <ThemeSwitcher />
      </header>

      {/* Main content area */}
      <main className="flex flex-col w-full mb-5">
        {/* Outlet renders the current route component */}
        <Outlet />
      </main>
    </>
  );
}
