# -*- coding:utf-8 -*-

import requests
import re
import os
import time

basic_path = os.path.abspath("")
img_path = basic_path + "/imagepath/"
def path_check(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

def get_pic(contents):
    key_srcs = re.findall('data-src=".*.jpeg',contents)
    keys = [tmp.split("image/")[1].split("/")[0] for tmp in key_srcs ]
    name_srcs = re.findall('alt=".*',contents)
    names = [tmp.split('="')[1].split('"')[0] for tmp in name_srcs ]
    for index,key in enumerate(keys):
        jpeg_url = "https://s3.qingbuyaohaixiu.com/image/{0}.jpeg".format(key)
        jpeg = requests.get(jpeg_url)
        file_name = img_path+names[index]
        while os.path.exists(file_name+'.jpeg'):
            file_name = file_name+'1'
        with open(file_name+'.jpeg','wb') as jpeg_file:
            jpeg_file.write(jpeg.content)
        #time.sleep(1)

def main():
    path_check(img_path)
    basic_url = "https://qingbuyaohaixiu.com"
    first_request = requests.get(basic_url)
    pages = re.findall("page=\d+",first_request.content)
    maxpage = max([int(tmp.split("=")[1]) for tmp in pages])
    
    get_pic(first_request.content)
    
    for page in range(2,maxpage+1):
        req_url = basic_url + "?page=" + str(page)
        contents = requests.get(req_url)
        get_pic(contents.content)
        #time.sleep(1)

if __name__ == "__main__":
    begin=int(time.time())
    main()
    time_cost = int(time.time()) - begin
    time_fo = open(basic_path+"/time","w")
    time_fo.write(str(time_cost))
    time_fo.close()
