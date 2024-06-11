from PIL import Image
import os
from decimal import Decimal, ROUND_DOWN
from img_class import IMG_FILE
from colorama import Fore, Style

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'
    return escape_mask.format(parameters, uri, label)


def get_image_size(path) :
    size_in_bytes = os.path.getsize(path)
    size_in_kb = Decimal(str(size_in_bytes / 1024)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
    return size_in_kb

def convert_to_webp(img_name) :
    
    index_extension = img_name.rfind('.')
    if (-1 == index_extension):
        print("Error")
        return
    webp_name = img_name[:index_extension] + '.webp'
    output = 'webp/' + webp_name

    img_path = 'images/' + img_name 
    img_rgb = Image.open(img_path).convert("RGBA")
    img_rgb.save(output, 'webp')

    return webp_name


def load_images() :
    extensions = ('PNG', 'JPG', 'JPEG')
    try:
        list_of_images = os.listdir('./images')
        images = list()

        for image in list_of_images:
            try :
                image_format = Image.open(os.path.curdir + '/images/' + image).format
                if image_format in extensions:
                    webp_name = convert_to_webp(image)
                    image_size = get_image_size(os.path.curdir + '/images/' + image)
                    webp_size = get_image_size(os.path.curdir + '/webp/' + webp_name)
                    images.append(IMG_FILE(image, image_format, image_size, webp_size, webp_name))
            except :
                print ('Image : ', image, 'cannot be converted !')

        column_width = 60
        print(Style.BRIGHT + '\nRecommended conversions : \n')

        header = ("Image Name", "Base Size (KB)", "Webp Size (KB)", "Link")
        print(f"{header[0]:<{column_width}}{header[1]:<{column_width}}{header[2]:<{column_width}}{header[3]:<{column_width}}")
        print('-' * (column_width * 4))

        potential_savings = 0

        for img in images:
            if (img.size > img.webp_size) :
                potential_savings += img.size - img.webp_size
                print(f"{Fore.CYAN + img.filename:<{column_width}} \
                {Fore.RED + str(img.size):<{column_width}} \
                {Fore.GREEN + str(img.webp_size):<{column_width}} \
                {Fore.YELLOW + link('file:///home/gabriel/img_conv/webp/' + img.webp_name) :<{column_width}}\n")

        print(Fore.RESET + "Potential savings : ", potential_savings, 'KB\n')
        return(images)
    except:
        pass


# images = load_images()
