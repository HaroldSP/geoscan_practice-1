import picamera

print("about to take a picture")
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    a = input("Please, name a file:\n")
    camera.capture("/home/pi/Desktop/Photos/" + a + ".jpg")
print("Picture taken")
