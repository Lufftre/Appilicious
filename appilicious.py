from PIL import Image
import hashlib
import colorsys
import os

phones = [["ludde",[10,18,13,3,6,10,7],"",[101,101,26,43,128,148]],
		["micke",[20, 6, 2, 8, 10, 2, 8, 7],"m_",[122,122,31,52,152,176]]]
	
phone = phones[1]

screens = phone[1]
prefix = phone[0]
icon_w,icon_h,start_x,start_y,pad_x,pad_y = phone[3]

def sortColors(colors):
	colors.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb[1]))

	return colors[:]


def parse_image(row,col,img,screen):
		x, y = start_x + pad_x * col, start_y + pad_y * row
		slice_bit = img.crop((x, y, x + icon_w, y + icon_h))
		hashlib.md5(slice_bit.tobytes())
		filename = 'out/{:1d}_{:02d}.png'.format(screen,col + row*4)
		
		slice_bit.save(filename)
		return filename


def main():

	if not os.path.exists("out"):
		os.makedirs("out")
	icons = []

	for screen in range(len(screens)):
		img = Image.open("res/{}/bild{}.jpg".format(prefix,screen))
		for row in range(5):
			for col in range(4):
				if(screens[screen] > (col+row * 4)):
					filename = parse_image(row,col,img,screen)
					icons.append(filename)

	colors = []
	for icon in icons:
		img = Image.open(icon)
		img.thumbnail((1,1), Image.ANTIALIAS)
		colors.append([icon,img.getpixel((0,0))])


	colors = sortColors(colors)
	
	html = "<html><body>"
	for i, color in enumerate(colors):
	  html += '<div style="background-color: rgba({},{},{},1)"><img src="{}"></div>'.format(color[1][0],color[1][1],color[1][2],color[0])

	with open("icons.html", 'w') as f:
		f.write(html)


if __name__ == "__main__":
	main()
