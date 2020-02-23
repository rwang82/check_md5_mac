# coding: utf-8
import os
import sys
import struct
import binascii
import subprocess

MD5_RECORD_L = []
MD5_RECORD_R = []

class md5info:
    def __init__(self, fname, md5):
        self.fname = fname
        self.md5 = md5

def get_fname_md5(d, records):
    for root,dirs,fs in os.walk(d):
        for f in fs:
            fullpath = os.path.join(root, f)
            #cmd='md5 {} |awk \'{print $4}\''.format(fullpath) 
            cmd='md5 {} |awk \'{}\''.format(fullpath, '{print $4}') 
            #print('cmd:{}'.format(cmd))
            p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            out,err = p.communicate()
            for line in out.splitlines():
                info = md5info(f, line)
                records.append(info)

def do_compare(recordsL, recordsR):
    for idxL, md5InfoL in enumerate(recordsL):
        #print('idxL:{} {} {}'.format(idxL, md5InfoL.fname, md5InfoL.md5))
        for idxR, md5InfoR in enumerate(recordsR):
            if md5InfoL.md5 == md5InfoR.md5:
                print('md5:{} {} {}'.format(md5InfoL.md5, md5InfoL.fname, md5InfoR.fname ))

if '__main__' == __name__:
    get_fname_md5('./left', MD5_RECORD_L)
    get_fname_md5('./right', MD5_RECORD_R)
    do_compare(MD5_RECORD_L, MD5_RECORD_R)
    




