# -*- coding:utf-8 -*-

import time
import subprocess

def main():
    source_file = "./full_targetids.txt"
    target_dir = './'

    flag = 0
    name = 1
    datalist = []
    start = int(time.time())

    with open(source_file,'r') as fsource:
        for line in fsource:
            flag += 1
            datalist.append(line)
            if flag == 30000:
                with open(target_dir+"ycl"+str(name),"w+") as f_target:
                    for data in datalist:
                        f_target.write(data)
                cmd = "nohup python video_comment.py {0} &".format("ycl"+str(name))
                cmd = cmd.split(" ")
                chlid = subprocess.Popen(cmd)
                print name
                name += 1
                flag = 0
                datalist = []
    
    with open(target_dir + 'ycl' + str(name),"w+") as f_target:
        for data in datalist:
            f_target.write(data)
        cmd = "nohup python video_comment.py {0} &".format("ycl"+str(name))
        cmd = cmd.split(" ")
        chlid = subprocess.Popen(cmd)

    print int(time.time()) - start

if __name__ == "__main__":
    main()
