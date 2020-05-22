# Frontend Directory Overview

### Main Directory
-   package.json    - Object all project dependencies. New modules installed via npm.
-   vue.config.js   - Object containing all vue specific configuration, in this case Vuetify.
-   babel.config.js - Object responsible for the Babel JS compiler config. Handles backwards JS compatibility.
-   eslint.js       - Object responible for code linting config.
-   public          - Holds index.html, a template that, during build, is injected with assets from src.
-   src             - Holds all app logic.

### src
-   Assets          - Handles all static assets.
-   Components      - Reusable Vue instances, this folder holds the core app logic seperated into logical components.
-   Plugins         - Plugins add global level functionality, in this case Vuetify.
-   Router          - Configuration for routing multi-page apps.

-   [Vue Config Docs](https://cli.vuejs.org/config/)
-   [Vue Components](https://vuejs.org/v2/guide/components.html)

## Project setup
-   Clone repo
-   Install dependancies ``npm install``
-   Run locally ``npm run dev``
-   Run linting service ``npm run lint``
