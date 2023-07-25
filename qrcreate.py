import qrcode

#taking input data and path to save from user
data = input("Enter data: ")
path = input("Name your qrcode: ")

#make the qrcode and save it in storage path
img = qrcode.make(f"{data}")
img.save(f"data/{path}.png")
