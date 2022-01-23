#!/usr/bin/env python
import os
import sys


def help(name: str):
    print("Sup!")
    print('You need to write: {name} "FILENAME.mp4"'.format(name=name))
    print("Then ffmpeg will convert your mp4 to mov for usage in davinci resolve!")


def main():
    args = sys.argv
    name = args[0]
    path = args[1]
    
    if path == "--help" or path == "-h":
        help(name)
    else:
        mov_path = path.replace(".mp4", ".mov")
        os.system("ffmpeg -i {path} -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov {mov_path}".format(path=path, mov_path=mov_path))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Wrong input, please type again.")
        main()
