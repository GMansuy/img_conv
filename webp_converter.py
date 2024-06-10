from PIL import Image
import os

def load_images() :
    extensions = ('.png', '.jpg', '.jpeg')
    try:
        list_of_images = os.listdir('./images')
        images = list()

        for image in list_of_images:
            if image.endswith(extensions):
                images.append(image)

        return(images)
    except:
        pass

def convert_to_webp(img_name) :
    
    index_extension = img_name.rfind('.')
    if (-1 == index_extension):
        print("Error")
        return
    output = 'webp/' + img_name[:index_extension] + '.webp'

    img_path = 'images/' + img_name 
    img_rgb = Image.open(img_path).convert("RGB")
    img_rgb.save(output, 'webp')

# images = load_images()

# for img in images :
#     convert_to_webp(img)