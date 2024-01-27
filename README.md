# contexta360 Assignment

## About The Project
This project contains both a frontend and backend application to display factorials on a web application, arranged by timestamp.

The frontend uses Vue.js to expose a web application which communicates directly to a backend server utilising Flask. The frontend displays a web application using HTML and Javascript, that allows you to submit a factorial number n and a timestamp to the backend server. The frontend application will then display each factorial result in order of timestamp on the web application. 

In regards the backend server, this exposes two endpoints, one for submitting a factorial n (/submit_reading). This endpoint will accept a factorial number "n" and a timestamp as inputs and then store the result in internal memory. 

The second endpoint will retrieve all the results of the factorial calculation (/get_factorials). This endpoint will retrieve all store factorial numbers submitted and calculate the factorial result for each. Once each of these factorial results have been calculated, then it will be returned to the frontend server where it will be arranged in order of timestamp.

### Built With
* [Vue.js]
* [Docker]
* [Flask]

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
It is recommended that you use a python virtual environment for this project in other to manage you dependencies.

Please ensure you have the following install on your system before starting this project.

* npm
* python
* pip

## Frontend (Locally)
Steps to setup the frontend application locally.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/chrishayes058/contexta360.git
   ```
2. Go to frontend directory
    ```
    cd frontend
    ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Run the dev environment 
    ```
    npm run dev
    ```

The frontend application should be accessible on http://localhost:5173/ 

## Backend (Locally)
Steps to setup backend locally.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/chrishayes058/contexta360.git
   ```
2. Install dependencies via pip
    ```
    pip install --upgrade pip
    pip install --no-cache-dir -r requirements.txt
    ```
3. Run the flask server.
    ```
    python backend/main.py
    ```


## Run Application via Docker
If you do not want to set everything up locally, you can also choose to run the entire application via docker. 

Please ensure you have both Docker and docker-compose installed for this. 

```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

Since the frontend uses http-server in the dockerfile, the frontend can then be accessed via the following URL: http://localhost:8080/
