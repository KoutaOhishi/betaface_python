#!/usr/bin/env python
#coding:utf-8
import requests
import base64


api_key = "d45fd466-51e2-4701-8da8-04351c872236"
api_secret = "171e8465-f548-401d-b63b-caf0dc28df5f"
image_file_path = "/home/rg26/Desktop/betaface_module/face.jpg"

def image_encoder(image_file_path):
    with open(image_file_path, "rb") as f:
        data = f.read()

    return base64.b64encode(data)

def get_img_uid(image_file_path):
    img_data = image_encoder(image_file_path)
    url = "http://betafaceapi.com/service.svc/UploadNewImage_File"
    param = {
        "api_key" : api_key,
        "api_secret" : api_secret,
        #"detection_flags" : ,
        "imagefile_data" : img_data,
        "original_filename" : "face.jpg"
    }

    res = requests.post(url, data=param)
    #print res
    r =  str(res.text)
    img_uid = r[r.index("<img_uid>")+9:r.index("</img_uid>")]
    return img_uid

def get_img_info(img_uid):
    param = {
        "api_key" : api_key,
        "api_secret" : api_secret,
        "img_uid" : img_uid
    }

    url = "http://betafaceapi.com/service.svc/GetImageInfo"

    res = requests.post(url, data=param)
    print res

    return res.text


def main():
    img_uid = get_img_uid(image_file_path)
    img_info = get_img_info(img_uid)

    print img_info




if __name__ == "__main__":
    #print image_encoder(image_file_path)
    main()