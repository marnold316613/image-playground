import sys
import os
from PIL import Image

# grab arguments
if len(sys.argv)>2:
 original_folder = sys.argv[1]
 output_folder = sys.argv[2]
else:
  print("no arguments passed")


# if new folder exists
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

# loop thru folder and then convert and save into new folder
for filename in os.listdir(original_folder):
  img = Image.open(f'{original_folder}{filename}')
  clean_name=os.path.splitext(filename)[0]
  img.save(f'{output_folder}{clean_name}.png',"png")
