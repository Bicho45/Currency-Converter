import os, time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def convertFromTo(convertFrom, convertTo):
    if convertFrom == convertTo:
        return 1.0
    else:
        return convertTo * convertFrom

def program():
    CURRENCY = {
        'LB' : 90,
        'USD': 1.0,
        'EUR': 0.85,
        'EGP': 30.9,
        'RMB': 6.5,
    }
    accept = "Y"
    while accept == "Y":
        print("Welcome to 'Currency Converter':")
        print('''
        ||====================================================================||
        ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
        ||(100)==================| Bachir RESERVE NOTE |================(100)||
        ||\\$//        ~         '------========--------'                \\$//||
        ||<< /        /$\              // ____ \\                         \ >>||
        ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
        ||<<|        \\ //           || <||  >\  ||                        |>>||
        ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
        ||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
        ||>>|  12                     *\\/___\_//*   1989                  |<<||
        ||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
        ||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
        ||(100)===================  ONE HUNDRED DOLLARS =================(100)||
        ||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
        ||====================================================================||
        --------------------------------------------------------------------------------
        ''')
        print("{")
        for c in CURRENCY:
            print(f"{c} : {CURRENCY[c]}")
        print("}")
        #print(CURRENCY)
        currencyChoose = input("Choose a currency to convert from: ").upper()
        amount = float(input("Enter the amount: "))
        confirm = input(f"You entered {amount} {currencyChoose}. Confirm? (Y/N): ").capitalize()
        if confirm == "Y":
            clear()
            convert = input("Choose a currency to convert to: ").upper()
            time.sleep(2)
            print("Analyzing your request... Please wait.")
            time.sleep(2)
            print(f"Checking for {convert}'s best rates available ...... Please wait.")
            time.sleep(2)
            print(f"Getting a discount price for {currencyChoose} ...... Please wait.")
            if currencyChoose in CURRENCY:
                clear()
                print(f"Preparing the deal from {currencyChoose} to {convert} .... Please wait.")
                time.sleep(2)
                cft = convertFromTo(CURRENCY[convert], CURRENCY[currencyChoose]) # EGP 3% USD
                print(f"Exchange Rate: 1 {currencyChoose} = {cft} {convert}")
                time.sleep(2)
                print(f"{amount} {currencyChoose} is equal to {round(amount/cft, 2)} {convert}")
                time.sleep(1)
                accept = input("Do you accept this transaction? (Y/N): ").capitalize()
                if accept == "Y":
                    program()
                elif accept == "N":
                    print("Transaction Canceled.")
                    if(input("Do you want to perform another conversion? (Y/N)").upper() == "Y"):
                        program()
                    else:
                        print("Exiting...")
                        time.sleep(1)
                        break
            else:
                print("Invalid currency. Conversion canceled.")
                time.sleep(2)
                program()
        elif confirm == "N":
            program()

program()
