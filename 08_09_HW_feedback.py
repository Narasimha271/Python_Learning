print('-----MINI ATM-----\n')
name=input('Please enter your Name: ')
cur_bal= int(input('Current Balance: '))
Options = 'Choose an option (1. Deposit, 2. Withdraw, 3, Check Balance) : '



tran_count=1
while True:
  
    if tran_count >5 :
         print(f'Max transactions are reached : {tran_count}. The session has ended.')
         break
    
    if tran_count == 1:
        User_response = int(input(Options))
    else: 
        bool_another_transaction = input(f"Do you want to do another transaction?(Y/N): ")
        if bool_another_transaction.lower() == 'y':
                    User_response = int(input(Options))
        else: 
            print("Thank you for banking with us!")
            break  

    match User_response:
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
    tran_count +=1

 
