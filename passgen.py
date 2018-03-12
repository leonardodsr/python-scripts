import string
import random
import os
import smtplib
import sys

def pass_gen(size=18, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def sendemail(from_addr, to_addr_list, subject, message, login, password, smtpserver = 'smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)    
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

valor = pass_gen()
usuario = str(sys.argv)
senha = str(sys.argv)
content = 'Root Password!! \nUser: root\nPassword: ' + valor
sendemail(usuario, 'leonardo.sr.92@gmail.com', 'Root Password', str(content),str(usuario), str(senha))




