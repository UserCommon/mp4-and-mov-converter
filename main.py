import os

def main():
    print("Choose 1 or 2.")
    print("1. Convert .mp4 to .mov")
    print("2. Convert .mov to .mp4")

    a = int(input())

    print("Input path of file")

    path = input()

    if a == 1:
        os.system("ffmpeg -i {path}.mp4 -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov {path}.mov".format(path=path))
    else:
        os.system("ffmpeg -i {path}.mov {path}.mp4".format(path=path))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Wrong input, please type again.")
        main()