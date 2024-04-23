import { Role } from "@/auth";


export type UserLoginData = {
    userName: string;
    password: string;
}

export type TokenData = {
    accessToken: string;
    tokenType: string;
    role: Role;
}