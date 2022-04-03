# powerplant-coding-challenge
# Setup (Windows)

## Requirements

You need to have `Python 3.8+` and `flask` installed. `flask` will be installed alongside the setup of the virtual environment.

## Getting the Repository

To get the repository, open cmd and type the following:

```
git clone https://github.com/tiagoalexs/powerplant-coding-challenge
```
This will clone the repository listed in this URL.

Alternatively to get the repository you can use `Github Desktop` and do the following:
- `File` -> `Clone Repository` -> Select `URL` option -> Insert `https://github.com/tiagoalexs/powerplant-coding-challenge` into `Repository URL` and click `Clone`

## Setting up a Virtual Environment 

After cloning the repository, enter the project directory by typing:
```
cd powerplant-coding-challenge/
```

Then while on the same directory as the project type the following:
```
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
```
This will create a virtual environment, activate it and install all the requirements needed.

## Running the application

To run the application, type:
```
python main.py
```

To send payloads and test the application, open a new cmd on the same directory as the project and type the following:
```
curl -X POST -d @example_payloads/payload1.json -H "Content-Type: application/json" http://localhost:8888/productionplan
```
With this command you will send the payload `payload1.json`, so if you want to send a different one, just replace that line with the desired payload.
