from account import Account;
from time import sleep;
import pickle;
import os;

appVersion: str = "1.0";

class PasswordManager():
    # Properties
    AccountList: list;

    # Init
    def __init__(self):
        self.AccountList = [];
        self.load();
        self.mainMenu(True);

    # Main Menu
    def mainMenu(self, firstCall: bool):
        if(firstCall):
            print("\n\nWelcome to Password Manager v" + appVersion);
            firstCall = False;
        
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
                self.save();
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
                self.save();
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
        if(len(self.AccountList) > 0):
            for i in range(0, len(self.AccountList)):
                if(i == 0):
                    print("\n\n0. Return");
                print("\n" + str(i + 1) + ". " + self.AccountList[i].Name);
            try:
                selectedAcc: int = int(input("\nSelection: ")) - 1;
            except:
                print("\nWrong input.");
                self.show();
            if(selectedAcc == -1):
                return;

            sleep(1);

            print("\n\nName: " + self.AccountList[selectedAcc].Name + " PW: " + self.AccountList[selectedAcc].Password);
            print("\n0. OK");
            print("\n1. Modify");
            print("\n2. Delete");
            print("\nSelection: ");
            selection: str = input();

            if(selection == "0"):
                self.show();
            elif(selection == "1"):
                self.modify(selectedAcc);
            elif(selection == "2"):
                self.delete(selectedAcc);
        else:
            print("\n\nNo accdata.");
    
    # modifying accdata
    def modify(self, accIndex: int):
            print("\n\nModify: 1. Name\n        2. Password");
            modSel: str = input("\nSelection: ");
            if(modSel == "1"):
                newName: str = input("\n\nNew name: ");
                self.AccountList[accIndex].Name = newName;
            elif(modSel == "2"):
                newPassword1: str = input("\n\nNew password: ");
                newPassword2: str = input("\n\nRepeat password: ");
                if(newPassword1 == newPassword2):
                    self.AccountList[accIndex].Password = newPassword1;
                else:
                    print("\nPasswords don't match.");
                    self.modify(accIndex);
            else:
                print("\n\nWrong input.");
                self.modify(accIndex);
            self.save();
            print("\nAccount modified!");

    # delete accdata
    def delete(self, accIndex: int):
        self.AccountList.remove(self.AccountList[accIndex]);
        self.save();
        print("\nAccount deleted.");

    # save accdata    
    def save(self):
        savePath: str = os.getcwd() + "\\userdata\\";
        fileName: str = "acclistdata.dat";
        filePath: str = savePath + fileName;
        if(not os.path.exists(savePath)):
            os.mkdir(savePath);

        with open(filePath, "wb") as f:
            pickle.dump(self.AccountList, f);

    # load accdata
    def load(self):
        savePath: str = os.getcwd() + "\\userdata\\";
        fileName: str = "acclistdata.dat";
        filePath: str = savePath + fileName;
        if(not os.path.exists(savePath)):
            os.mkdir(savePath);
        
        if(os.path.exists(filePath)):
             with open(filePath, "rb") as f:
                self.AccountList = pickle.load(f);
        else:
            return;