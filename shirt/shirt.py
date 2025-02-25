import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if check_arg_ends(sys.argv[1], sys.argv[2]):
            try:
                merge_img(sys.argv[1], "shirt.png", sys.argv[2])
            except FileNotFoundError:
                sys.exit("Could not find the image file")


def check_arg_ends(str1, str2):
    formats = ["jpg", "jpeg", "png"]
    str_rest1, end1 = str1.split(".")
    str_rest2, end2 = str2.split(".")
    if end1.lower() in formats and end2.lower() in formats:
        if end1.lower() == end2.lower():
            return True
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")

def merge_img(img1, img2, out):
    before = Image.open(img1)
    shirt = Image.open(img2)
    size = shirt.size
    before = ImageOps.fit(before, size)
    before.paste(shirt, box = (0, 0), mask = shirt)
    before.save(out, format=None)

if __name__ == "__main__":
    main()


