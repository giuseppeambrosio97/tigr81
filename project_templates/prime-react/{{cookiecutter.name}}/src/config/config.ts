import dev from './configDev';
import local from './configLocal';
import localBe from './configLocalBe';

const config = {
    local: local,
    localBe: localBe,
    dev: dev,
};

const ENV: Environment = import.meta.env.VITE_APP_ENVIRONMENT as Environment;


export default config[ENV || 'local'];
