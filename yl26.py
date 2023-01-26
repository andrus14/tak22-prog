sales = {
    "Johnver": {
        "revenue": {
            "tea": 190,
            "coffee": 325,
            "water": 682,
            "milk": 829
        },
        "expenses": {
            "tea": 120,
            "coffee": 300,
            "water": 50,
            "milk": 67
        }
    },
    "Vanston": {
        "revenue": {
            "tea": 140,
            "coffee": 19,
            "water": 14,
            "milk": 140
        },
        "expenses": {
            "tea": 65,
            "coffee": 10,
            "water": 299,
            "milk": 254
        }
    }
}

for employee_name, employee_sales  in sales.items():
    print(employee_name)

    comission = 0
    for drink_name, drink_value in employee_sales['revenue'].items():
        profit = drink_value - employee_sales['expenses'][drink_name]
        if profit > 0:
            print('Kasum on pos', profit * 0.062)
            comission += profit * 0.062
    
    print(comission)
