#!/usr/bin/env python
#coding:utf-8
import requests
import base64
import xml.etree.ElementTree as ET
import xmltodict
import json

API_KEY = "d45fd466-51e2-4701-8da8-04351c872236"
API_SECRET = "171e8465-f548-401d-b63b-caf0dc28df5f"

def image_encoder(image_file_path):
    """
        画像データをbase64形式にエンコードする
    """
    with open(image_file_path, "rb") as f:
        data = f.read()

    return base64.b64encode(data)

def get_img_uid(image_file_path):
    """
        img_uidを取得する関数
    """
    img_data = image_encoder(image_file_path)

    param = {
        "api_key" : API_KEY,
        "api_secret" : API_SECRET,
        #"detection_flags" : ,
        "imagefile_data" : img_data,
        "original_filename" : "face.jpg"
    }

    res = requests.post("http://betafaceapi.com/service.svc/UploadNewImage_File", data=param)
    dict = xmltodict.parse(res.content)
    #print json.dumps(dict, indent=1)

    img_uid = dict["BetafaceImageResponse"]["img_uid"]

    return img_uid

def get_img_info(img_uid):
    """
        顔の特徴を辞書型で返す
    """
    param = {
        "api_key" : API_KEY,
        "api_secret" : API_SECRET,
        "img_uid" : img_uid
    }

    res = requests.post("http://betafaceapi.com/service.svc/GetImageInfo", data=param)
    dict = xmltodict.parse(res.content)
    #print json.dumps(dict, indent=1)
    tags = dict["BetafaceImageInfoResponse"]["faces"]["FaceInfo"]["tags"]

    face_info = {}
    for i in range(len(tags["TagInfo"])):
        face_info[tags["TagInfo"][i]["name"]] = tags["TagInfo"][i]["value"]

    return face_info


def main():
    image_file_path = "/home/rg26/Desktop/betaface_module/face.jpg"
    img_uid = get_img_uid(image_file_path)
    img_info = get_img_info(img_uid)

    print img_info


if __name__ == "__main__":
    main()