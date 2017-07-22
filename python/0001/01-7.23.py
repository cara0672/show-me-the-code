__author__ =  'CARA'

from PIL import Image,ImageFont,ImageDraw
im = Image.open("image.jpg")  
fnt = ImageFont.truetype("simfang.ttf",20) 
draw = ImageDraw.Draw(im) 
draw.text((190,0),"4",font = fnt,fill = "red")
im.save("123.jpg")
