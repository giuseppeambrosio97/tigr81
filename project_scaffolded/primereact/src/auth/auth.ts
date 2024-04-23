import { AuthState } from "./types";


export function getAuthStateST(): AuthState {
    return JSON.parse(sessionStorage.getItem('authState')!);
}

export function setAuthStateST(authState: AuthState): void {
    sessionStorage.setItem('authState',JSON.stringify(authState));
}
