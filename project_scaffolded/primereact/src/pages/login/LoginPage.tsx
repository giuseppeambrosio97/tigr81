import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import { FormEvent, useRef, useState } from "react";
import { Image } from "primereact/image";
import { useNavigate } from "react-router-dom";
import { loginUser } from "@/api/login";
import { Toast } from "primereact/toast";
import { setAuthStateST } from "@/auth";
import { buttonDefaultPt } from "@/defaultPt";

const LOGIN_ERROR_LIFE_TIME = 1500;

function LoginPage() {
  const navigate = useNavigate();
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [loginFailed, setLoginFailed] = useState(false);

  const toastRef = useRef<Toast>(null);

  const showLoginFailedToast = () => {
    toastRef.current!.show({
      severity: "error",
      summary: "Authentication Failed",
      detail: "Username or password incorrect",
      life: LOGIN_ERROR_LIFE_TIME,
    });
  };

  const handleLogin = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const tokenData = await loginUser({
        userName,
        password,
      });
      setAuthStateST({
        userName,
        accessToken: tokenData.accessToken,
        role: tokenData.role,
      });
      navigate("/home");
    } catch (error) {
      setLoginFailed(true);
      setTimeout(() => {
        setLoginFailed(false);
      }, LOGIN_ERROR_LIFE_TIME);
      showLoginFailedToast();
    }
  };

  return (
    <div className="flex justify-center p-4 md:p-8 lg:p-12 md:mt-16">
      <Toast ref={toastRef} />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-20 max-w-[90%] md:max-w-[60%] lg:max-w-[50%] xl:max-w-[40%]">
        {/* Image Section */}
        <div className="flex justify-center">
          <Image
            src="https://raw.githubusercontent.com/giuseppeambrosio97/tigr81/develop/assets/5142438-cute-baby-tigre-vettoriale.jpg"
            alt="POC login logo"
            className="w-full h-auto max-w-xs md:max-w-sm lg:max-w-md"
          />
        </div>

        {/* Form Section */}
        <div className="flex items-center justify-center">
          <form
            onSubmit={handleLogin}
            className="flex flex-col gap-4 w-full"
          >
            {/* Username Field */}
            <div className="flex flex-col gap-2">
              <label
                htmlFor="username"
                className={`block text-sm font-medium ${
                  loginFailed ? "text-red-500" : "text-gray-700"
                }`}
              >
                Username
              </label>
              <InputText
                id="username"
                value={userName}
                onChange={(e) => setUserName(e.target.value)}
                className={`mt-1 block w-full p-2 border ${
                  loginFailed ? "border-red-500" : "border-gray-300"
                } rounded-md`}
              />
            </div>

            {/* Password Field */}
            <div className="flex flex-col gap-2">
              <label
                htmlFor="password"
                className={`block text-sm font-medium ${
                  loginFailed ? "text-red-500" : "text-gray-700"
                }`}
              >
                Password
              </label>
              <InputText
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className={`mt-1 block w-full p-2 border ${
                  loginFailed ? "border-red-500" : "border-gray-300"
                } rounded-md`}
              />
            </div>

            {/* Login Button */}
            <Button
              label="Login"
              type="submit"
              className="w-full p-2 mt-1 border border-gray-300 rounded-md"
              pt={buttonDefaultPt}
            />
          </form>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
