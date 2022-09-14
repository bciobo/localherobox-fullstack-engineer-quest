# LocalHeroBox Fullstack code challenge

Backend & Frontend stack providing a simple `orders` API and a small web-app
to interact with, filter and present order information from that API.

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

**Recommended tools**

* [pyenv](https://github.com/pyenv/pyenv)

## Frontend Requirements

* Node.js (with `npm`).

**Recommended tools**

* [nvm](https://github.com/nvm-sh/nvm)
* 
## Run

### Backend

* Start the stack with Docker Compose:

```bash
docker-compose up -d
```

* See README inside backend folder for details on how to run in development mode 

### Frontend

**Setup**
1. go to `frontend/` folder
2. run `make install`

**Start React dev server**
1. go to parent folder `cd ../`
2. start the app in the development mode `make run-react`

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.