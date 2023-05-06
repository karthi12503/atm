import random
# opening console
global usr_storage
usr_storage = {}
global amount
amount = 0
while True:
    print("HEY ! WELCOME TO ATM")
    print('''
             1.NEW USER PIN GENERATION
             2.BALANCE
             3.CASH WITHDRAWEL
             4.CASH DEPOSIT
             5.QUIT
         ''')
    choise = int(input("ENTER YOUR CHOISE : "))
    match choise:
            case 1:
                # PIN GENERATION
                class pin_gen:
                    def __init__(self,id,pin):
                        self.id = id
                        self.pin = pin
                    def otp_gen(self):
                        return random.randint(1000,9999)
                        
                    def otp_verify(self,sotp,rotp):
                        if sotp == rotp:
                            print("otp verified")
                        else:
                            print("otp wrong")
                    def pin_update(self,id,pin,phone,acc_no,amount):
                             usr_storage.update({id:{"PIN":pin,"phone_n0":phone,"Account_no":acc_no,"AMOUNT":amount}})              
                print("NEW USER PIN GENERATION")
                id = int(input("ENTER YOUR PREFERED ID : "))
                pin = int(input("ENTER YOUR PREFERED PIN : "))
                obj = pin_gen(id,pin)
                phone = input('ENTER THE PHONE NUMBER : ')
                acc_no = input("ENTER THE ACCOUNT NUMBER : ")
                sotp = obj.otp_gen()
                print(sotp)
                rotp = int(input("ENTER THE OTP : "))
                obj.otp_verify(sotp,rotp)
                obj.pin_update(id,pin,phone,acc_no,amount)
                print("pin updated")
            case 2:
                #balance
                id1 = int(input("ENTER YOUR ID : "))
                try:
                    print(f"YOUR BALANCE IS {usr_storage[id1]['AMOUNT']}")
                except KeyError:
                    print("HEY ! YOU HAVE ENTERED WRONG ID")
            case 3:
                #cash withdrawel
                print("CASH WITHDRAWEL")
                id3 = int(input("ENTER YOUR ID : "))
                if id3 in usr_storage:
                    amount_with = int(input("ENTER THE AMOUNT : "))
                    if amount_with <= usr_storage[id3]["AMOUNT"]:
                        usr_storage[id3]["AMOUNT"] = usr_storage[id3]["AMOUNT"] - amount_with
                        print(f"HEY TAKE YOUR AMOUNT ${amount_with}")
                    else:
                        print("YOU DO NOT HAVE SUFFICIENT BALANCE !!!")
                else:
                    print("IT SEEMS THAT YOU DO NOT HAVE ID ! CREATE IT FIRST")
                    
                    
            case 4:
                #cash deposit
                print("CASH DEPOSIT")
                id2 = int(input("ENTER YOUR ID : "))
                if id2 in usr_storage:
                    amount_dep = int(input("ENTER THE AMOUNT : "))
                    usr_storage[id2]["AMOUNT"] = amount_dep
                    print("YOUR AMOUNT SUCCESSFULY DEPOSITED !")
                else:
                    print("IT SEEMS THAT YOU DO NOT HAVE ID ! CREATE IT FIRST")
            case 5:
                print("THANKS FOR USING (^__^)")
                break
                
