from PIL import Image
import requests
from io import BytesIO

def create_ascii(img_url):
  try:
    response = requests.get(img_url)
    pic = Image.open(BytesIO(response.content))
  except:
    return 'Please enter a valid URL for an image'
  width, height = pic.size
  aspect_ratio = height / width
  new_width = 110
  new_height = int(aspect_ratio * new_width)
  img = pic.resize((new_width, new_height))
  img = img.convert('L')
  pixels = img.getdata()
  chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']
  count = len(chars)
  new_pixels = [chars[int(((count-1)*pixel)/256)] for pixel in pixels] 
  new_pixels = ''.join(new_pixels)
  new_pixels_count = len(new_pixels)
  ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
  return ascii_image

if __name__ == '__main__':
  print(create_ascii('google.com'))
  print(create_ascii('https://www.google.com/'))
  art = create_ascii('https://images.pexels.com/photos/5302784/pexels-photo-5302784.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
  for line in art:
    print(line)