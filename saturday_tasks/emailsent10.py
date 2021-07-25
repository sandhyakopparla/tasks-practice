import smtplib
li=[]
n=int(input("enter the no."))
for i in range(n):
    element=int(input("enter the number"))
    li.append(element)
print(li)
even=[]
odd=[]
for i in range(len(li)):
    if(li[i]%2==0):
        even.append(li[i])
    else:
        odd.append(li[i])
print(even)
print(odd)
messages = ' '.join([str(elem) for elem in even])
print(messages)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("practicedigital12@gmail.com","sandhya9@9")
connection.sendmail("practicedigital12@gmail.com","gulshankumar060699@gmail.com",messages)
print("message is successfully send")
connection.quit()




    


