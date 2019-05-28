from PIL import Image,ImageDraw, ImageFont
image = Image.new('RGB',(1000,900),(255,255,255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)

import random
#import qrcode
import datetime
import os
os.system("ID card generator ")
d_date = datetime.datetime.now()
format_date = d_date.strftime(" %d -%m-%Y \t\t ID card generator \t \t ")
print('****************************************************************')
print(format_date)
print('****************************************************************')
# name

(x,y) = (50,50)

stuname = input("enter your full name : ")
color = 'rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf' , size = 60)
draw.text((x,y),stuname,fill= color,font=font)

#unique id number

(x,y) = (600,75)
idno = random.randint(1000000,9000000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)


(x, y) = (50, 350)
message = input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)

(x, y) = (250, 350)
message = input('Enter Your Age: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)



(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)


(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
color = 'rgb(255, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)



(x, y) = (50, 650)
message = input('Enter Your Mobile Number: ')
temp=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)


(x, y) = (50, 750)
message = input('Enter Your Address: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)

image.save(str(stuname)+'.jpg')
#img = qrcode.make(str(company)+str(idno))   # this info. is added in QR code, also add other things
#img.save(str(idno)+'.bmp')

"""
til = Image.open(stuname+'C:\Users\Shivangi Sharma\Pictures\2010-01.jpg')
im = Image.open(str(idno)+'C:\Users\Shivangi Sharma\Pictures\2010-01.jpg') #25x25
til.paste(im,(600,350))
til.save(stuname+'C:\Users\Shivangi Sharma\Pictures\2010-01.jpg')

print(('\n\n\nYour ID Card Successfully created in a PNG file '+stuname+'C:\Users\Shivangi Sharma\Pictures\2010-01.jpg'))
"""
eval(input('\n\nPress any key to Close program...'))















