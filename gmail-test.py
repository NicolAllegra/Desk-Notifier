import RPi.GPIO as GPIO, feedparser, time
import os
DEBUG = 1

USERNAME = "lucanicoltlm"     # just the part before the @ sign, add yours here
PASSWORD = "Ciao1234"     # password of your email
prec=0
NEWMAIL_OFFSET = 1        # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 1      # check mail every 60 seconds

while True:

    newmails = feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"]
    #print "email:"+ str(newmails)
    #print "email:"+ str(prec)

    if (prec<newmails):
        #bash='flite -voice slt -t "Have you 24 new mail from Gmail"'
        bash='flite -voice slt -t "Have you "'+ newmails +'" new mail from Gmail"'
        #print "email:"+ str(newmails)
        #bash="flite -voice slt -f ciao.txt"
        os.system(bash)
        prec=newmails;
        
    time.sleep(MAIL_CHECK_FREQ)
    
