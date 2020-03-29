import sys
from mainui import Ui_Main
from reg import Ui_Dialog
from interface import Ui_inter
from PyQt5 import QtCore,QtWidgets,QtGui
from base64 import b64encode,b64decode
#coded by XWK 2020/3/21

acc = {}
money = {}
login_user = 0
login_psw = 0
current_user = 0

class ui(Ui_Main,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def login(self):
        global login_user,login_psw,current_user,money
        read_money()
        read_users()
        login_user = self.lineEdit_acc.text()
        login_psw = self.lineEdit_psw.text()

        if login_psw == acc.get(str(login_user)):
            current_user = login_user
            self.label_2.setText('登入成功')
            interui.label_user.setText(str(current_user))
            interui.label_balance.setText(str(money.get(current_user)))   
            interui.show()
        elif login_user =='':
            pass
        elif str(login_user) not in acc:
            self.label_2.setText('無此帳號')       
        else:
            self.label_2.setText('密碼錯誤')
        
    def open_reg(self):
        regui.show() 
    
    def reset(self):
        f = open('users.txt','w')
        f.write('')
        f.close()
        f = open('money.txt','w')
        f.write('')
        f.close()
        self.label_2.setText('清除成功')
        
class reg_ui(Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def submit(self):
        read_users()
        if self.create_acc.text() in acc:
            self.label.setText('此ID已經註冊過')
        
        else:
            if self.create_acc.text() == '' or self.create_psw.text() == '' or self.confirm_psw.text()== '':
                self.label.setText('帳號密碼不得為空')
            elif self.create_psw.text() == self.confirm_psw.text():
                user_add = add_user(self.create_acc.text(),self.create_psw.text())
                user_add.add_new_user()
                self.label.setText('註冊成功')
                self.create_acc.setText('')
                self.create_psw.setText('')
                self.confirm_psw.setText('')
            else:
                self.label.setText('兩次密碼必須相同')
        read_users()

class interface_ui(Ui_inter,QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def deposit(self):
        try:
            if int(self.lineEdit.text()) > 0:
                m = int(money[current_user])
                m += int(self.lineEdit.text())
                money[current_user] = m
                self.label_balance.setText(str(money[current_user]))
                save_money()
                self.label_status.setText('存款成功')
                self.lineEdit.setText('')
        except ValueError:
            self.label_status.setText('請輸入一個整數')


    def withdraw(self):
        try:
            if int(self.lineEdit.text()) > 0:
                m = int(money[current_user])
                m -= int(self.lineEdit.text())
                if m < 0 :
                    m += int(money[current_user])
                    self.label_status.setText('餘額不足')
                
                else:
                    money[current_user] = m
                    self.label_balance.setText(str(money[current_user]))
                    save_money()
                    self.label_status.setText('提款成功')
                    self.lineEdit.setText('')
        except ValueError:
            self.label_status.setText('請輸入一個整數')

class add_user:
    def __init__(self,a,p):
        self.a = a
        self.p = p

    def add_new_user(self):
        file = open('users.txt','a')
        file.write(encode(self.a)+','+encode(self.p)+','+'\n')
        file.close
        money[self.a] = 0
        save_money()
        read_money()

def read_users():
    global acc
    acc = {}
    r = open('users.txt','r')
    lines = r.readlines()
    for line in lines:
        list_account = line.split(',')
        try:
            acc[decode(list_account[0])] = decode(list_account[1])
        except:
            pass    
    r.close

def read_money():
    global money
    f = open('money.txt','r')
    try:
        money = eval(decode(f.read()))
    except:
        pass
    f.close

def save_money():
    f = open('money.txt','w')
    f.write(encode(str(money)))
    f.close

def encode(target):
    enc = target.encode()
    enc = b64encode(enc)
    enc = enc.decode()
    return enc

def decode(target):
    dec = target.encode()
    dec = b64decode(dec)
    dec = dec.decode()
    return dec

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    regui = reg_ui()
    interui = interface_ui()
    ui = ui()
    ui.show()
    read_users()
    read_money()
    sys.exit(app.exec_())
