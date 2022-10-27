def main():
    # Checks to see what your investment will be after ten years
    # in an compound account.
    investment = eval(input("What is your start investment: "))

    apr = eval(input("What is the annual interest rate: "))

    for i in range(10):
        investment = investment * (1 + apr)
    
    print("total amount after ten years: " + str(investment))

main()
