from PIL import Image
from pathlib import Path
import sys

ASCII_CHARS = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
MAX_BRIGHTNESS_VALUE = 255


def get_img_file_path() -> Path:
    if len(sys.argv) == 1:
        return Path(input('Enter a path to the image you want to transform: '))
    else:
        return Path(sys.argv[1])
    
def get_pixel_matrix(path: Path):
    try:
        with Image.open(path) as im:
            print('Image successfully loaded!')
            print(f'Image format: {im.format}')
            print(f'Image size: {im.size[0]}x{im.size[1]}')
            return im.load(), im.size[0], im.size[1]
    except FileNotFoundError:
        print('Could not find that file: ', path)
        quit()

def get_transform_method() -> str:
    available_methods = [
        'average',
        'minmax',
        'luminosity'
    ]

    if len(sys.argv) < 2 or sys.argv[2] not in available_methods:
        while True:
            print('Choose a brightness mapping method:')
            print('- average')
            print('- minmax')
            print('- luminosity')
            method = input('Type in chosen method: ').strip().lower()
            if method not in available_methods:
                print('Invalid method. Please try again')
            else:
                return method
    else:
        return sys.argv[2]
    
def get_brightness_invert() -> bool:
    if len(sys.argv) < 3:
        print('Would you like to invert brightness? y/n')
        if input() == 'y':
            return True
        else:
            return False
    else:
        return bool(int(sys.argv[3]))

def get_pixel_brightness(pixel: tuple, method: str) -> int:
    method = method.lower()

    if method == 'average':
        return round(sum(pixel) / 3)
    elif method == 'minmax':
        return round((min(pixel) + max(pixel)) / 2)
    elif method == 'luminosity':
        return round(0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2])

def transform_pixel_to_ascii(pixel: tuple, method: str, invert: bool) -> str:
    brightness = get_pixel_brightness(pixel, method)
    if invert:
        brightness = abs(brightness - MAX_BRIGHTNESS_VALUE)
    
    i = round(brightness / MAX_BRIGHTNESS_VALUE * (len(ASCII_CHARS) - 1))
    if not(0 <= i < len(ASCII_CHARS)):
        print(i, brightness)
    return ASCII_CHARS[i]

def write_ascii_img_to_file(path: Path, width: int, height: int, pixel_matrix, method: str, invert_brightness: bool):

    with open(path, 'w') as file:
    
        for i in range(height):
            for j in range(width):
                file.write(transform_pixel_to_ascii(pixel_matrix[j, i], method, invert_brightness) * 3)
            file.write('\n')

        print('Image successfully transformed: ', path)

def main():

    img_file_path = get_img_file_path()
    pixel_matrix, img_width, img_height = get_pixel_matrix(img_file_path)
    transform_method = get_transform_method()
    invert_brightness = get_brightness_invert()
    
    ascii_img_file_path = img_file_path.stem + '-ascii.txt'
    write_ascii_img_to_file(ascii_img_file_path, img_width, img_height, pixel_matrix, transform_method, invert_brightness)

    #im.show()

if __name__ == '__main__':
    main()