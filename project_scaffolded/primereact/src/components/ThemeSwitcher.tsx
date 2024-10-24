import { PrimeReactContext } from 'primereact/api';
import { Button } from 'primereact/button';
import { useContext, useState } from 'react';

export default function ThemeSwitcher() {
    const { changeTheme } = useContext(PrimeReactContext);
    const [mode, setMode] = useState('light');

    const isLightMode = mode === 'light';

    const onSwitchTheme = () => {
        const newMode = isLightMode ? 'dark' : 'light';
        changeTheme!(`lara-${mode}-green`, `lara-${newMode}-green`, 'app-theme', () =>
            setMode(isLightMode ? 'dark' : 'light')
        );
    };
    return (
        <Button
            icon={`pi ${isLightMode ? 'pi-sun' : 'pi-moon'}`}
            raised
            rounded
            onClick={onSwitchTheme}
        />
    );
}
