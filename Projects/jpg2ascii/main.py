# jpg to ascii
# approach: measuring the darkness/brightness of a pixel and
# find the most fitting equivalent to an ASCII character
from PIL import Image
from time import sleep
import subprocess
import os


def get_ascii_brightness():
    # ratio: white / black -> avoiding 1/0
    ratios = []
    image = Image.open(os.path.dirname(__file__) + '\\asc\\ascii.png')
    for char in range(95):
        character = image.crop((char * 8, 0, (char + 1) * 8, 12))
        # character.save("ASCII_{}".format(char + 32), "PNG")

        black, white = 0, 0
        for pixel in character.getdata():
            if pixel == (0, 0, 0):
                black += 1
            else:
                white += 1

        ratios.append(white / black)

    return ratios


def get_image_brightness(filename):
    image = Image.open(filename)
    size = image.size
    re_x, re_y = size[0] - size[0] % 8, size[1] - size[1] % 12
    image.resize((re_x, re_y))

    image_brightness = []

    for y in range(0, re_y, 12):
        for x in range(0, re_x, 8):
            pixels = image.crop((x, y, x + 8, y + 12))
            pixels = pixels.convert("RGB")

            brightness = 0
            for pixel in pixels.getdata():
                brightness += sum(pixel)

            # 73440 = 3 (RGB average) * 96(pixel amount) * 255(average)
            image_brightness.append(brightness / 73440)
    return image_brightness


def convert_image(ascii_brightness, image_brightness):
    image = []

    for ratio in image_brightness:
        asc_i = 0
        delta_bright = float("inf")

        for i in range(len(ascii_brightness)):
            delta = abs(ratio - ascii_brightness[i])

            if delta < delta_bright:
                delta_bright = delta
                asc_i = i

        image.append(str(chr(asc_i + 32)))
    return image


def clear(time=0):
    sleep(time)
    subprocess.call("cls", shell=True)


def main():
    try:
        filename = input("Enter your filename: ")
        size = Image.open(filename).size
    except Exception as e:
        print("It seems to be something wrong with your file name. Try again!", "\n", e, "\n")
        clear(2)
        return main()

    ascii_brightness = get_ascii_brightness()
    image_brightness = get_image_brightness(filename)

    mode = input("save in text file? (y/n): ").lower()
    negative = input("negative? (y/n): ")
    negative = True if negative == "y" else False

    clear()
    if mode == 'n':
        if negative:
            image = convert_image(list(map(lambda x: 1 - x, ascii_brightness)), image_brightness)
        else:
            image = convert_image(ascii_brightness, image_brightness)

        for i in range(len(image)):
            if i % ((size[0] - size[0] % 8) // 8) == 0:
                print("\n" + image[i], end="")
            else:
                print(image[i], end="")
        input()

    elif mode == 'y':
        if negative:
            image = convert_image(ascii_brightness, image_brightness)
        else:
            image = convert_image(list(map(lambda x: 1 - x, ascii_brightness)), image_brightness)

        with open("jpg2ascii_text.txt", 'w') as f:
            for i in range(len(image)):
                if i % ((size[0] - size[0] % 8) // 8) == 0:
                    f.write("\n" + image[i])
                else:
                    f.write(image[i])
    else:
        print("srsly? - you can't even press a damn key right?\n")
        clear(1)
        return main()

if __name__ == '__main__':
    main()
