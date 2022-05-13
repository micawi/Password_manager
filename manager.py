from account import Account;
from pickle import dump, load;
from time import sleep;
import os;

appVersion: str = "1.0";

class PasswordManager():
    # Properties
    AccountList: list;

    # Init
    def __init__(self):
        self.AccountList = [];

    # Main Menu
    def mainMenu(self, firstCall: bool):
        if(firstCall):
            print("\n\nWelcome to Password Manager v" + appVersion);
        
        while(True):
            # Show options
            print("\n\n1. Show accounts/passwords");
            print("\n\n2. New account/password");
            print("\n\n3. Exit");
            selection: str = input("\nSelection: ");
            sleep(1);

            # Get into suboptions
            if(selection == "1"):
                self.show(); 
            elif(selection == "2"):
                self.genAccount();
            elif(selection == "3"):
                print("\n\nGOODBYE!");
                sleep(1);
                exit();                            
    
    # Get inputs and gen acc
    def genAccount(self):
        # Get inputs
        print("\n\nAccount name: ");
        name: str = input();
        print("\nPassword: ");
        pw1: str = input();
        print("\nRepeat password: ");
        pw2: str = input();

        sleep(1);

        # gen Account
        if(pw1 == pw2):
            print("\n\nSave account? Y/N: ");
            answer: str = input();
            if(answer == "Y"):
                newAcc = Account(name, pw1);
                self.AccountList.append(newAcc);
            elif(answer == "N"):
                return;
            else:
                print("\nWrong input.");
                self.genAccount();
        else:
            print("\n\nPasswords do not match.");
            self.genAccount();
    
    # Show accounts/passwords
    def show(self):
        for i in range(0, len(self.AccountList)):
            if(i == 0):
                print("\n\n0. Return");
            else:
                print("\n" + str(i) + " " + self.AccountList[i].Name);
        selectedAcc: int = int(input("\nSelection: ")) - 1;