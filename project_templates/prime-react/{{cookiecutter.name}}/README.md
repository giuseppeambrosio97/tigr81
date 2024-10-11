# PRIME REACT TEMPLATE

## Development stack

- [React](https://reactjs.org/)
- [Vite](https://vitejs.dev/)
- [Node.js](https://nodejs.org/en/): v20.9.0
- [nvm](https://github.com/nvm-sh/nvm)
- [Yarn](https://yarnpkg.com/)
- [TypeScript](https://www.typescriptlang.org/)
- [ESLint](https://eslint.org/)
- [Prettier](https://prettier.io/)

UI LIBRARY

- [Prime React unstayled mode](https://primereact.org/unstyled/)
- [Tailwind CSS](https://tailwindcss.com/)

### Project structure

```
├── public (also for static assets)
├── src
│   ├── assets (static assets folder)
│   ├── components (shared components)
│   ├── config (config app folder)
│   ├── pages (pages or screens)
│   ├── redux (redux store, slices, ...)
│   ├── api (api calls)
...
```

### How to run

#### Installation

##### NVM

```bash
  nvm install $(cat .nvmrc)
  nvm use
```

```bash
  yarn install
```

#### Run Project

```bash
  yarn dev
```

### Run the formatter

```bash
  yarn format
```

### Run the linter

```bash
  yarn lint
```

### Fix linting errors

```bash
  yarn lint:fix
```

### Before opening a PR

```bash
  yarn precommit
```

### Coding Conventions

- For `.ts` files, use camel case; e.g. `exampleFile.ts`
- For `.tsx` files, use pascal case; e.g. `ExampleComponent.tsx`
