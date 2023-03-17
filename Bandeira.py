from PIL import Image, ImageDraw, ImageOps

blue = (0, 56, 168)
red = (206, 17, 38)
white = (255, 255, 255)

largura = 1000
altura = 500

imagem = Image.new('RGB', (largura, altura), white)
desenho = ImageDraw.Draw(imagem)
divisor = altura//2

desenho.rectangle(((0, 0), (largura, divisor)), fill=blue)
desenho.rectangle(((0, divisor), (largura, altura)), fill=red)

faixa = altura/2

largura_triangulo, altura_triangulo = 2*largura/5, altura
eixo_x, eixo_y = 0, altura / 2 - altura_triangulo / 2
desenho.polygon([(eixo_x, eixo_y),
                 (eixo_x + largura_triangulo, eixo_y + altura_triangulo / 2),
                 (eixo_x, eixo_y + altura_triangulo)],
                fill='white')

imagem.show()
revert = ImageOps.invert(imagem)
revert.show()
