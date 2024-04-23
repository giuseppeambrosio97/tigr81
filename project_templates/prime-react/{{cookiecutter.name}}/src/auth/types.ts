export enum Role {
    ADMIN = "ADMIN",
    GUEST = "GUEST"
}

export type AuthState = {
    accessToken: string | null;
    userName: string | null;
    role: Role | null;
}