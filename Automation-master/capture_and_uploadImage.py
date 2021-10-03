import cv2
import dropbox
import time
import random

start_time = time.time()

def upload_file(img_name):
    access_token = "dVp9Uak3cmMAAAAAAAAAATEp44tVhERP9Fm8EkNoiHcyzuCw9dvCaJR2qPeJAsKP"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded!")