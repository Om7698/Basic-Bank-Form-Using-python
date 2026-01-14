balance=0.0
documents={}
def check_balance(balance):
    print(f"Your Current Balance is {balance}.")
def deposit(amount):
    global balance
    balance+= amount
    print(f"You Successfully Deposited {amount} and your current balance is {balance}")
def withdraw(amount):
    global balance
    balance-= amount
    print(f"You Successfully Withdrawn {amount} and your current balance is {balance}")
    
def check_kyc(documents):
    if len(documents) == 0:
        print("Your KYC is not completed.")
    else:
        print(f"Your KYC is up to date and Your documents {documents} avilable.")
def update_kyc(n_documents, documents):
    
    
    for i in range(n_documents):
        new_docs={}
        key = input("Enter the type of documents: ")
        value= input("Enter the Valid Data of documents: ")
        new_docs[key]=value
        if new_docs not in documents.items():
            documents.update(new_docs)
            print("We have update your Documents in our data.")
        
        else:
            print("We have already the same documents.")




 #General Information
print("\n----------------------------------")
print("Welcome to my Money my World Bank.")
print("----------------------------------\n")
while True:
    custom = input("\nEnter \"Yes\" if you need any help otherwise \"No\": ")
    if custom.upper() == "YES" :
        print("\nHow may i help you?")
        print("""
            1. Check the Balance
            2. Deposite the amount
            3. Withdraw the amount
            4. Check the KYC
            5. Update KYC
            """)
        need = (input("Enter the number between (1-5): "))
        if need == "1":
            check_balance(balance)
        elif need == "2":
            amount= float(input("Enter the amount for Deposite: "))
            if amount >0:
                deposit(amount)
            else:
                print("You Entered Invalid Value. Sorry!")
        elif need == "3":
            amount=float(input("Enter the amount for Withdraw: "))
            if amount>0 and amount<balance:
                withdraw(amount)
            else:
                print("You Entered Invalid Vlaue, It can not be withdraw. Sorry!")
        elif need == "4":
            check_kyc(documents)
        elif need == "5":
            n_documents = int(input("Enter the Documents number that you want to be add: "))
            update_kyc(n_documents, documents)
        else:
            print("You Entered Invalid Number. Sorry!")

    else:
        print("Thanks for using my money my World Bank.")
        break



