import picamera
from time import sleep
from subprocess import call
from os import remove

print("about to take a video")
with picamera.PiCamera() as camera:
    
    a = input("Please, name a file:\n")
    b = int(input("Please, set up a recording time:\n"))
    camera.resolution = (1280, 720)
    
    print("RECORDING !")
    camera.start_recording("/home/pi/Desktop/Photos/" + a + ".h264")
    sleep(b)
    camera.stop_recording()
    
print("Video taken")
print("We are going to convert the video")
command = "MP4Box -add /home/pi/Desktop/Photos/" + a + ".h264 /home/pi/Desktop/Photos/" + a + ".mp4"
call([command], shell = True)
remove("/home/pi/Desktop/Photos/" + a + ".h264")
print("Video converted")


