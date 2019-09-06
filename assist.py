# coding=gbk


import os
import subprocess
import time

def download_enw_from_google_scholar():
    # 辅助下载Google scholar
    f = r'C:\Users\ly\OneDrive\project01\JGR\reference_modified.txt'
    fr = open(f,'r')
    lines = fr.readlines()
    for line in lines:
        url = 'https://scholar.google.com/scholar?hl=zh-CN&as_sdt=0%2C5&q=*+*+*+*+*+*+*&btnG='
        url = list(url)
        line = line.split('\n')[0]
        print(line)
        line = line.split()
        if len(line) > 0:
            for i in range(7):
                ind = url.index('*')
                url[ind] = line[i]
        # print(''.join(url))
        cmd = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -d '+'"'+''.join(url)+'"'
        subprocess.call(cmd)


def import_enw():
    # 自动导入endnote
    fdir = r'C:\Users\ly\Desktop\gs\\'
    flist = os.listdir(fdir)
    for f in flist:
        cmd = '"'+fdir+f+'"'
        os.system(cmd)
        time.sleep(5)

# if __name__ == '__main__':
#     import_enw()
