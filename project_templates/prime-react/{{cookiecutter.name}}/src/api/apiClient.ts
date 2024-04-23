import { getAuthStateST } from "@/auth";
import config from "@/config/config";
import axios from "axios";

const axiosInstance = axios.create({
    baseURL: config.backend.baseUrl,
});

axiosInstance.interceptors.request.use(config => {
    const authState = getAuthStateST();

    config.headers.Authorization = `Bearer ${authState.accessToken}`;
    return config;
}, error => {
    return Promise.reject(error);
});

export default axiosInstance;