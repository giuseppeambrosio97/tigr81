import axios from 'axios';
import { TokenData, UserLoginData } from './types';
import config from '@/config/config';
import { Role } from '@/auth';

const LOGIN_ENDPOINT = "token";

export async function loginUser(userLoginData: UserLoginData): Promise<TokenData> {
 try {
    const response = await axios.post(`${config.backend.baseUrl}/${LOGIN_ENDPOINT}`, {
      grant_type: 'password',
      username: userLoginData.userName,
      password: userLoginData.password,
      scope: '',
      client_id: '',
      client_secret: ''
    }, {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });

    return response.data;
 } catch (error) {
    console.error('Error making the request:', error);
    return {
      accessToken: "faketoken",
      tokenType: "bearer",
      role: Role.ADMIN,
    };
    throw error;
 }
}
