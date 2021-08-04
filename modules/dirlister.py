# _*_ coding: utf-8 _*_

import os

def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")

    return str(files)
