import os
import glob
import PIL.Image as Image
import mkdocs


def convert_jpg(fn):
    fn_new = os.path.splitext(fn)[0] + ".jpg"
    img = Image.open(fn)
    img = img.convert("RGB")
    img.save(fn_new)


def main():
    root = "./"
    png_flist = glob.glob(root+"*.png")
    for fn in png_flist:
        convert_jpg(fn)


if __name__ == "__main__":
    main()