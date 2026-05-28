from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # Crear imagen 256x256
    img = Image.new('RGB', (256, 256), color=(20, 30, 50))
    draw = ImageDraw.Draw(img)

    # Dibujar circulo naranja
    draw.ellipse((20, 20, 236, 236), fill=(255, 120, 0))
    draw.ellipse((40, 40, 216, 216), fill=(20, 30, 50))

    try:
        font = ImageFont.truetype("arialbd.ttf", 60)
    except:
        font = ImageFont.load_default()

    text = "CSC"
    draw.text((65, 95), text, fill="white", font=font)

    # Guardar en varios formatos
    img.save('app_icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32)])
    img.save('logo.png', format='PNG')
    print("app_icon.ico y logo.png creados!")

if __name__ == "__main__":
    create_icon()
