import smtplib as s
import json


ob = s.SMTP('smtp.gmail.com','587')
ob.ehlo()
ob.starttls()

with open("data.json",'r') as data:
    data = data.read();
    
data = json.loads(data)
email = data['email']
password = data['password']

ob.login(email,password)
subject = "test python code"
body = "I am interested in AI Ml Using python"
massage = f"Subject:{subject}\n\n{body}"
listadd = ["abhishekmalu14@gmail.com"]
ob.sendmail('abhimahesh49@gmail.com',listadd,massage)
print("----Emails sended----")
ob.quit()
