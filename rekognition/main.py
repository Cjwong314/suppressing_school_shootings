import cv2
import time
import boto3
import json
import os
from twilio.rest import Client

starttime = time.time()


def take_photo(pic,  port=0, ramp_frames=30, x=1280, y=720):  
    camera = cv2.VideoCapture(port)
 #Camera Resolution
    camera.set(3, x)
    camera.set(4, y)
 # Adjust camera lighting
    for i in range(ramp_frames):
        temp = camera.read()
    retval, im = camera.read()
 #Takes Photo
    cv2.imwrite(pic,im)
    print("photo" + str(pic) + "taken")

#Removes Photo
    del(camera)

def upload_photo(pic):
    s3 = boto3.resource('s3')
    # s3.meta.client.upload_file('/Users/cjwong/Desktop/solving_school_shootings/'+str(pic), 'gun-rekognition', str(pic))
    s3.meta.client.upload_file(str(pic), 'gun-rekognition', str(pic))
    print("photo uploaded")

def text_sender():
    account_sid = "ACa12d9736c34520b6c1abdf0c627de173"
    auth_token = "2eba35dd5d96cf06efdbada2f4a63eb8"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Hello from Chris",
    from_="+18559373996",
    to="+17207572144"
    )
    print(message.sid)

def detect_labels(pic, bucket):

    session = boto3.Session()
    client = session.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':pic}},
    MaxLabels=10)

    print('Detected labels for ' + pic)
    print()
    for label in response['Labels']:
        print("Label: " + label['Name'])
        print("Confidence: " + str(label['Confidence']))
        print("Instances:")
#This is where it checks to see if there is a gun in the image
        if label['Name'] == "Gun":
            print("Gun Detected")
            text_sender()
            exit()

        print("Parents:")
        for parent in label['Parents']:
            print(" " + parent['Name'])

        print("Aliases:")
        for alias in label['Aliases']:
            print(" " + alias['Name'])

            print("Categories:")
        for category in label['Categories']:
            print(" " + category['Name'])
            print("----------")
            print()

    if "ImageProperties" in str(response):
        print("Background:")
        print(response["ImageProperties"]["Background"])
        print()
        print("Foreground:")
        print(response["ImageProperties"]["Foreground"])
        print()
        print("Quality:")
        print(response["ImageProperties"]["Quality"])
        print()

    return len(response['Labels'])


def main():
    current_time = time.ctime()
    pic = 'webcamphoto' + str(current_time) + '.jpg'
    bucket = 'gun-rekognition'
    take_photo(pic)
    upload_photo(pic)
    label_count = detect_labels(pic, bucket)
    print("Labels detected: " + str(label_count))
    
    
    

while (True): 
    main()

    time.sleep(5 - ((time.time() - starttime) % 5))