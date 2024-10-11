import { Button } from "primereact/button";
import { Menu } from "primereact/menu";
import { Sidebar } from "primereact/sidebar";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { PageKey } from "../HomePage";
import { Role } from "@/auth";
import { useDispatch } from "react-redux";
import { buttonDefaultPt } from "@/defaultPt";

type SideMenuProps = {
  setPageToShow: (pagetoShow: PageKey) => void;
  role: Role;
};

function SideMenu(props: SideMenuProps) {
  const [visible, setVisible] = useState(false);
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const MENU_ITEM = [
    {
      label: "Home",
      items: [
        {
          label: "Home Page",
          icon: "pi pi-home",
          command: () => {
            props.setPageToShow("home");
          },
        },
        {
          label: "Your POC",
          icon: "pi pi-code",
          command: () => {
            props.setPageToShow("poc");
          },
        },
        {
          label: "Logout",
          icon: "pi pi-sign-out",
          command: async () => {
            navigate("/login");
          },
        },
      ],
    },
  ];


  return (
    <>
      <Sidebar visible={visible} onHide={() => setVisible(false)}>
        <div className="flex flex-col gap-3">
          <h2 className="text-center font-bold">Menu</h2>
          <Menu className="w-full min-w-full" model={MENU_ITEM} />
        </div>
      </Sidebar>
      <Button
        icon="pi pi-bars"
        size="large"
        className="top-0 left-0 ml-2 mt-2"
        {% raw %}
        style={{
          position: "fixed",
        }}
        {% endraw %}
        onClick={() => setVisible(true)}
        pt={buttonDefaultPt}
      />
    </>
  );
}

export default SideMenu;
