from PIL import Image,ImageFont,ImageDraw

img = Image.open('white.png')#create and open an white inmage
font=ImageFont.truetype("Lato-BlackItalic.ttf",24) #select font to be used


draw = ImageDraw.Draw(img)# pass the image  
text= "HEY BUDDY"

draw.text((0,150),text,(0,0,0),font=font)#co ordinates are given first then the string then the rgb values and finally the font drawn
img.save("text.png")
