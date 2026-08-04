weight=float(input("Enter your weight(KG)"))
height=float(input("Enter your height(M)"))

def calculate_BMI(weight,height):
    return weight/(height**2)


def condition_BMI():
    if calculate_BMI(weight,height)<18:
        return "Low weight!"
    elif 18<=calculate_BMI(weight,height)<=25:
        return "Normal weight"
    else:
        return "Over weight"
    
def main():
    print(condition_BMI())

if __name__=="__main__":
    main()