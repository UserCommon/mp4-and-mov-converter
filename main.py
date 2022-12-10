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
    path = args[1].lower()

    if path == "--help" or path == "-h":
        help(name)
    elif path[-4::] == ".mp4":
        mov_path = path.replace(".mp4", ".mov")
    elif path[-4::] == ".mov":
        mov_path = path.replace(".mov", ".mp4")
    else:
        print("File must be mp4 or mov!")
        exit(1)
    os.system(
        "ffmpeg -i {path} -acodec pcm_s24le -vcodec copy {mov_path}".format(path=path, mov_path=mov_path))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Wrong input, please type again.")
        main()
