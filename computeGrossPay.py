import random

company = input("Enter your company name:").strip()

while True:
    try:
        hours = float(input("Enter hours: ").strip())
        if hours >= 0:
            try:
                rate = float(input("Enter rate: ").strip())
                if rate >= 0:
                    try:
                        if hours > 40:
                            #(baseline amount) + (extra hours) * (rate * 1.5 increase)
                            over_pay = (40 * rate) + (hours - 40) * (rate * 1.5)
                            print("Company:", company)
                            print("Hours:", hours)
                            print("Rate:", rate)
                            print("**********************************")
                            print("Your document number is:", random.randint(1000,2000))
                            print("Your", company, "gross pay is", round(over_pay,2), "dollars")
                        else:
                            pay = float(hours * rate)
                            print("Company:", company)
                            print("Hours:", hours)
                            print("Rate:", rate)
                            print("**********************************")
                            print("Your document number is:", random.randint(1000,2000))
                            print("Your", company, "gross pay is", round(pay,2), "dollars")
    
                    except:
                        print('Error, please enter a valid numeric input. Try again!')

            except:
               print('Error, please enter numeric input. Try again!')
                      
    except:
        print('Error, please enter numeric input. Try again!')
