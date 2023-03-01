import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file('/Users/cjwong/Desktop/solving_school_shootings/webcamphotoTue Feb 28 16:30:05 2023.jpg', 'gun-rekognition', 'webcamphotoTue Feb 28 16:30:05 2023.jpg')