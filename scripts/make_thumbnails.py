import glob
import json
import os
import sys

from PIL import Image

os.chdir(os.path.dirname(os.path.realpath(__file__)))

img_width = int(sys.argv[1])
img_height = int(img_width * 9 / 16)
jpeg_quality = int(sys.argv[2]) if len(sys.argv) > 2 else 95

input_dir = "..\\themes"
output_dir = f"../src/resources"

for theme_dir in glob.glob(f"{input_dir}/**"):
    print(f"<- {theme_dir}")

    with open(f"{theme_dir}/theme.json", 'r') as fileobj:
        theme_config = json.load(fileobj)
    theme_name = os.path.basename(theme_dir)

    light_image_id = theme_config.get("dayHighlight") or theme_config["dayImageList"][len(theme_config["dayImageList"]) // 2]
    light_image_filename = theme_config["imageFilename"].replace("*", str(light_image_id))
    dark_image_id = theme_config.get("nightHighlight") or theme_config["nightImageList"][len(theme_config["nightImageList"]) // 2]
    dark_image_filename = theme_config["imageFilename"].replace("*", str(dark_image_id))

    img1 = Image.open(f"{theme_dir}/{light_image_filename}")
    img2 = Image.open(f"{theme_dir}/{dark_image_filename}")

    img2.paste(img1.crop((0, 0, img1.width // 2, img1.height)))
    img2.thumbnail((img_width, img_height))
    img2.save(f"{output_dir}/{theme_name}_thumbnail.jpg", quality=jpeg_quality)

print(f"-> {output_dir}")
