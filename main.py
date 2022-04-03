from flask import Flask, request, jsonify, json

"""
The payload contains 3 types of data:
load: The load is the amount of energy (MWh) that need to be generated during one hour.

fuels: based on the cost of the fuels of each powerplant, the merit-order can be determined which is the starting point for deciding which powerplants should be switched on and how much power they will deliver. Wind-turbine are either switched-on, and in that case generate a certain amount of energy depending on the % of wind, or can be switched off.
gas(euro/MWh): the price of gas per MWh. Thus if gas is at 6 euro/MWh and if the efficiency of the powerplant is 50% (i.e. 2 units of gas will generate one unit of electricity), the cost of generating 1 MWh is 12 euro.
kerosine(euro/Mwh): the price of kerosine per MWh.
co2(euro/ton): the price of emission allowances (optionally to be taken into account).
wind(%): percentage of wind. Example: if there is on average 25% wind during an hour, a wind-turbine with a Pmax of 4 MW will generate 1MWh of energy.

powerplants: describes the powerplants at disposal to generate the demanded load. For each powerplant. is specified:
name:
type: gasfired, turbojet or windturbine.
efficiency: the efficiency at which they convert a MWh of fuel into a MWh of electrical energy. Wind-turbines do not consume 'fuel' and thus are considered to generate power at zero price.
pmax: the maximum amount of power the powerplant can generate.
pmin: the minimum amount of power the powerplant generates when switched on.
"""

powerdict = {
  "gasfired": "gas(euro/MWh)",
  "turbojet": "kerosine(euro/MWh)",
  "windturbine": "wind(%)"
}

app = Flask(__name__)

@app.route("/")
def main_page():
  return "Power Plant Coding Challenge!"

@app.route('/productionplan', endpoint='productionplan', methods=['POST'])
def production_plan():
    payload = request.get_json()
    response = solve(payload)
    return jsonify(response)

def solve(payload):
    #get load data
    load = payload["load"]

    #calculate prices for each powerplant
    payload = calculate_prices(payload)
    powerplants = payload["powerplants"]
    
    #get merit order
    merit_order(powerplants)
    
    #allocate power to the different powerplants
    data = allocate_power(load, payload)
    return data

#calculate fuel prices for each powerplant
def calculate_prices(payload):
    for powerplant in payload["powerplants"]:
        if(powerplant["type"] == "windturbine"):
            powerplant["price"] = 0
        else:
            powerplant["price"] = payload["fuels"][powerdict [powerplant["type"]] ]  / powerplant["efficiency"]
    return payload
    
def merit_order(powerplants):
    return powerplants.sort(key=lambda x: x["price"])

def allocate_power(load, payload):
    #At any moment in time, all available powerplants need to generate the power to exactly match the load.
    powerplants = payload["powerplants"]
    data = []
    p = 0

    for powerplant in powerplants:
        if(load == 0):
            p = 0

        #if pmin is higher than the remaining load, we need to change the power output from the previous powerplant so that we have "pmin" load remaining
        elif(load < powerplant["pmin"]):
            diff = abs(powerplant["pmin"] - load)
            data[-1]["p"] -= diff
            load += diff
            p = powerplant["pmin"]

        else:
            if(powerplant["type"] == "windturbine"):
                p = powerplant["pmax"] * payload["fuels"]["wind(%)"] / 100.0
            else:
                p = powerplant["pmax"] if load >= powerplant["pmax"] else load

        p = round(p,1)  
        load = abs(load - p)
        data.append({"name" : powerplant["name"], "p" : p})
    
    return data

def main():
    app.run(host="0.0.0.0", port=8888)

if __name__ == '__main__':
    main()
