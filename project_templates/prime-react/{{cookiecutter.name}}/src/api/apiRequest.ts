import { AxiosResponse } from 'axios';
import axiosInstance from './apiClient';

export enum RequestMethod {
    GET = 'get',
    POST = 'post',
    PATCH = 'patch',
    DELETE = 'delete',
}

export const apiRequest = async <T = any, U = AxiosResponse<T>>(
    method: RequestMethod,
    endpoint: string,
    data?: T,
): Promise<U> => {

    try {
        const response = await axiosInstance({
            method,
            url: endpoint,
            data,
        });
        return response.data as U;
    } catch (error) {
        console.error(`Error in API request: ${error}`);
        throw error;
    }
};
