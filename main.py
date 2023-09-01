import sys
from PIL import Image

def main(input_filenames):

    images = [Image.open(f) for f in input_filenames]

    thresh = 110

    fn = lambda x : 255 if x > thresh else 0

    r_images = [f.convert('L').point(fn, mode='1') for f in images]

    r_images[0].save("result.pdf", resolution=100.0, save_all=True, append_images=r_images[1:])

if __name__ == "__main__":
    main(sys.argv[1:])
