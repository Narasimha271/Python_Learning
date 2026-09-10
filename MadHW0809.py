print('-----MINI ATM-----\n')
name=input('Please enter your Name: ')
cur_bal= int(input('Current Balance: '))
action = (input(f"Choose an option (1. Deposit, 2. Withdraw, 3, Check Balance) : "))
action_1=int(action)

#How to reset action value here? 

tran_count=1
while True:
    match action_1:
        case 1: 
            cred_amount = int(input('Amount to deposit: '))
            cur_bal += cred_amount
            print ('Transaction Successful')
                                
        case 2:
            deb_amount = int(input('Amount to withdraw: '))
            while cur_bal>deb_amount:
                if deb_amount<=500:
                    cur_bal-=deb_amount  
                    print ('Transaction Successful')      
                else :
                    print('Maximum Withdrawal Limit: 500 per transaction')
                break                           

        case 3:
            cur_bal=cur_bal
            
        case _ :
            print(f"Invalid selection. Select a valid option from 1-3. \n{action}")

    print(f"\nHi {name}! \nYour balance is: {cur_bal} \nTransactions Completed: {tran_count} \nThank you for using the ATM")

    redo = input(f"Do you want to do another transaction?(Y/N): ")

    if redo.lower() == 'y':
        input(f"What do you want to do next: {action}") #How to clear the input value for action from previous transaction?
        tran_count+=1   
    elif redo.lower()=='n':
        print("Thank you for banking with us!")
        break
    else:
        print('Please enter a valid input!')
        input(f"What do you want to do next: {action}")  
    if tran_count ==5:
        print('Transaction limit reached for this session! Restart the session to try again.')
        break