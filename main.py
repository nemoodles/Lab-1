from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
def factorial(starting_number: int):
    if starting_number == 0:
        return {"return": False}

    result = 1
    number = starting_number

    while number > 1:
        result *= number
        number -= 1

    return {"starting_number": starting_number, "factorial": result}

#result = result * number 
# result = 1 * 5 = 5 
# number = number - 1
# number = 5 - 1 = 4

# result = 5 * 4 = 20
# number = 4 - 1 = 3

# result = 5 * 3 = 15
# number = 3 - 1 = 2

# result = 5 * 2 = 10
# number = 2 - 1 = 1

# result = 5 * 1 = 5
# number = 1 - 1 = 0