import webbrowser
print("Thanks For Using Insta Scrapper")
donate = input("Do you want to support us by donation? (Enter yes/no): ")
if donate == "yes":
    print("Your small amount also helps a lot Thanks!")
    webbrowser.open('https://commerce.coinbase.com/checkout/44cfcf8a-0bdd-4b01-9c79-1c4c02369adb')
else:
    print("Bye, Have a good day")
