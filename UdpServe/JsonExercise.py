import json

json_string = '{"Name":"Move Cars","Address":"MagleGaardsvej 2","Cars":[{"Brand":"BMW","Model":"330e","Color":"Green","Mileage":45721},{"Brand":"VW","Model":"Golf","Color":"Red","Mileage":20},{"Brand":"Ford","Model":"Galaxy","Color":"Black","Mileage":124326}],"Employees":[{"Name":"Move","Salary":1000000,"MonthsEmployed":28,"JobAreas":["President","Mechanic"]},{"Name":"Not Move","Salary":100,"MonthsEmployed":13,"JobAreas":["Vice-President","Mechanic"]}]}'

# Deserialize JSON string into a dictionary
data = json.loads(json_string)

# Access the color of the second car
print(data["Cars"][1]["Color"])
