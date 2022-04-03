# powerplant-coding-challenge

## Requirements

You need to have `Python 3.8+` installed. `flask` will be installed alongside the setup of the virtual environment.

## Setting up a Virtual Environment (Windows)

Open cmd on the same directory as the project and type the following:
```
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
```
This will create a virtual environment, activate it and install all the requirements needed.

## Running the application (Windows)

To run the application, type:
```
python main.py
```

To send payloads and test the application, open a new cmd on the same directory as the project and type the following:
```
curl -X POST -d @example_payloads/payload1.json -H "Content-Type: application/json" http://localhost:8888/productionplan
```
With this command you will send payload `payload1.json`, so if you want to send a different one, just replace that line with the desired payload.
