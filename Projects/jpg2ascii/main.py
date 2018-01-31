# jpg to ascii
# approach: measuring the darkness/brightness of an area of pixels (8x12) and
# find the most fitting equivalent to an ASCII character
# https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.tell
#
# How to extract frames from GIFs:
# https://gist.github.com/BigglesZX/4016539
# https://gist.github.com/revolunet/848913
from PIL import Image
from time import sleep
import subprocess
import os


def get_ascii_brightness():
    # ratio: white / black -> avoiding 1/0
    ratios = []
    image = Image.open(os.path.dirname(__file__) + '\\bin\\asc\\ascii.png')

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


def extract_frames(filename):
    frame = Image.open(filename)
    current_path = os.path.dirname(__file__)
    count = 0
    current_frame = frame.convert("RGBA")

    while frame:
        current_frame.save(current_path + '\\bin\\temp\\' + "{}.png".format(count + 1), "PNG")
        current_frame = Image.alpha_composite(current_frame, frame.convert("RGBA"))
        count += 1
        try:
            frame.seek(count)
        except EOFError:
            break

    return [current_path + "/bin/temp/" + str(i) + ".png" for i in range(1, count + 1)]


def paint(image, size):
    for i in range(len(image)):
        if i % ((size[0] - size[0] % 8) // 8) == 0:
            print("\n" + image[i], end="")
        else:
            print(image[i], end="")


def paint_in_file(image, size):
    with open("jpg2ascii_text.txt", 'w') as f:
        for i in range(len(image)):
            if i % ((size[0] - size[0] % 8) // 8) == 0:
                f.write("\n" + image[i])
            else:
                f.write(image[i])


def delete_files():
    current_dir = os.path.dirname(__file__)
    file_list = os.listdir(current_dir + "/bin/temp/")

    for file in file_list[:]:
        os.remove(current_dir + "/bin/temp/" + file)


def clear(time=0.0):
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

    mode = input("save in text file? (y/n): ").lower()
    negative = True if input("negative? (y/n): ") == "y" else False
    negative = not negative if mode == 'y' else negative

    ascii_brightness = get_ascii_brightness()

    if negative:
        ascii_brightness = list(map(lambda x: 1 - x, ascii_brightness))

    if filename.split(".")[1] == "gif":
        files = extract_frames(filename)
        file_count = 0
        image_brightnesses = [get_image_brightness(file) for file in files]
        images = [convert_image(ascii_brightness, brightness) for brightness in image_brightnesses]
        delete_files()
        while True:
            clear(0.05)  # 0.05s is merely a arbitrary time span, since i couldn't manage to extract the fps of a gif
            paint(images[file_count], size)
            if file_count < len(files) - 1:
                file_count += 1
            else:
                file_count = 0
    else:
        image = convert_image(ascii_brightness, get_image_brightness(filename))
        clear()
        if mode == 'n':
            paint(image, size)
            input("Press any key to continue...")
            return main()

        elif mode == 'y':
            paint_in_file(image, size)
        else:
            print("srsly? - you can't even press a damn key right? - sigh...\n")
            clear(1)
            return main()

if __name__ == '__main__':
    main()
