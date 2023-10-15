
from PIL import Image
d1 = Image.open('pic2.jpeg')
d2 = Image.open('pic3.jpeg')
d3 = Image.open('pic4.jpeg')
d4 = Image.open('pic5.jpeg')
d5 = Image.open('pic6.jpeg')
d = {'8 Марта': d1, '23 Февраля': d2, 'День Рождения': d3, 'Новый год': d4, 'Рождество': d5}

a=input("Введите праздник: ")
img = d[a]
img.show()