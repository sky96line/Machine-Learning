# import numpy as np

# data = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#         [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
#         [[21, 22, 23], [24, 25, 26], [27, 28, 29]]]

# def convert_1D(arr):
#     n = []
#     data = np.asarray(arr)
#     n = data.shape
#     ans = 1
#     for a in n:
#         ans *= a
#     return np.reshape(data,(ans))

# total = convert_1D(data)
# print total
import smtplib 
gmailaddress = raw_input("what is your gmail address? \n ")
gmailpassword = raw_input("what is the password for that email address? \n  ")
mailto = raw_input("what email address do you want to send your message to? \n ")
msg = raw_input("What is your message? \n ")
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , msg)
print(" \n Sent!")
mailServer.quit()