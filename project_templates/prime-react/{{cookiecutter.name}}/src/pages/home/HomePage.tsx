import { useState } from "react";
import SideMenu from "./components/SideMenu";
import { getAuthStateST } from "@/auth";
import PocPage from "../poc/PocPage";

export type PageKey = "pocs" | "home";

type PageItem = {
  title: string;
  element: JSX.Element;
};

type Pages = {
  [key in PageKey]: PageItem;
};

const KEY_TO_PAGE: Pages = {
  pocs: {
    title: "Your POC Page",
    element: <PocPage />,
  },
  home: {
    title: "Home Page",
    element: <PocPage />,
  },
};

export default function HomePage() {
  const [pageToShow, setPageToShow] = useState<PageKey>("home");

  const authState = getAuthStateST();

  if (!authState.accessToken || !authState.role || !authState.userName) {
    return;
  }

  return (
    <div className="flex justify-content-center w-full h-full">
      <SideMenu role={authState.role} setPageToShow={setPageToShow} />
      <div className="flex flex-col w-full mb-5">
        <h2 className="text-white flex items-center justify-center font-bold text-2xl min-h-16 bg-primary p-5">
          {{cookiecutter.home_page_title}}
        </h2>
        <h2 className="flex items-center justify-center text-2xl min-h-16">
          {KEY_TO_PAGE[pageToShow].title}
        </h2>
        <div className="w-full h-full overflow-y-auto scrollbar max-h-[80%]">
          {KEY_TO_PAGE[pageToShow].element}
        </div>
      </div>
    </div>
  );
}
