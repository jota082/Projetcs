## Nome: Jônathas Nobre Moura Mat: 538799

import turtle
import random
import winsound

winsound.PlaySound('mar.wav',winsound.SND_ASYNC)
turtle.register_shape('garrafa.gif')
turtle.register_shape('tartaruga.gif')
turtle.register_shape('tartaruga2.gif')
turtle.register_shape('tartaruga3.gif')         #música e fotos utilizadas
turtle.register_shape('tartaruga4.gif')
turtle.register_shape('vida.gif')
turtle.register_shape('alga.gif')
turtle.title('ANYA ESCAPE')  # nome na barra de titulo

xx = 300
yy = 300        
vv = 12
pt = 0
life = 3
def score ():
    sc = turtle.Turtle()
    sc.hideturtle()
    sc.color('Black')
    sc.speed(0)
    sc.penup()
    sc.setposition(110, 300)
    sc.pendown()
    sc.write(('Score:'), font=('Courier', 15, 'italic'))
score()

pts = turtle.Turtle()
pts.penup()
pts.hideturtle()
pts.setposition(210,301)
pts.write(pt, font=('Courier', 14 ))

janela = turtle.Screen()  ##criando a interface gráfica
janela.bgpic('fundo.gif')
caneta = turtle.Turtle() ##criando o quadrado
caneta.hideturtle()
caneta.speed(0)

def quadrado ():
    caneta.color('SteelBlue')
    caneta.pensize(5)
    caneta.up()
    caneta.goto(-xx, yy)
    caneta.down()
    for i in range(4):  ##criar o quadrado
        caneta.forward(2 * xx)
        caneta.right(90)

quadrado()
tartaruga = turtle.Turtle()  ##criar a tartaruga
tartaruga.speed(0)

def canto (elemento):
    lugar = ['cima','esquerda','direita','baixo'][random.randint(0,3)]
    if lugar == 'cima':
        posicao = random.randint(-300,300)
        elemento.goto(posicao,yy - 35)
    elif lugar =='esquerda':
        posicao = random.randint(-300, 300)
        elemento.goto(posicao, xx - 35)
    elif lugar == 'direita':
        posicao = random.randint(-300, 300)
        elemento.goto(posicao, xx - 35)
    elif lugar == 'baixo':
        posicao = random.randint(-300, 300)
        elemento.goto(posicao, yy - 35)

def algaAnda ():
    alga.forward(10)
    if alga.xcor() > xx - 16 :
        alga.setheading(random.randint(90, 270))
    elif alga.xcor() < -xx + 16:
        alga.setheading([random.randint(0,90),random.randint(270,360)][random.randint(0,1)])
    elif alga.ycor() > yy - 40 :
        alga.setheading(random.randint(180, 360))
    elif alga.ycor() < -yy + 40:
        alga.setheading(random.randint(0,180))
    turtle.ontimer(algaAnda, 1000 // 24)
    distx = tartaruga.xcor() - alga.xcor()
    disty = tartaruga.ycor() - alga.ycor()

    if distx > -40 and distx < 40 and disty > -50 and disty < 50:
        global pt
        global pts
        pt += 100
        pts.clear()
        pts.write(pt, font=('Courier', 14))
        canto(alga)

alga = turtle.Turtle() ##cria a alga
alga.speed(0)
alga.shape('alga.gif')
alga.penup()
canto(alga)
alga.setheading(random.randint(0,360))
algaAnda()

def turt ():
    tartaruga.penup()
    tartaruga.shape('tartaruga.gif')

turt()
def cima():
    tartaruga.setheading(90)
    tartaruga.shape('tartaruga.gif')
    if tartaruga.ycor() < yy - 36:
        tartaruga.forward(vv)
def baixo():
    tartaruga.setheading(270)
    tartaruga.shape('tartaruga3.gif')
    if tartaruga.ycor() > - yy + 36:
        tartaruga.forward(vv)
def esquerda():
    tartaruga.setheading(180)
    tartaruga.shape('tartaruga4.gif')
    if tartaruga.xcor() > -xx + 37:
        tartaruga.forward(vv)
def direita():
    tartaruga.setheading(0)
    tartaruga.shape('tartaruga2.gif')
    if tartaruga.xcor() < xx - 37:
        tartaruga.forward(vv)
def teclas():
    turtle.onkeypress(cima, 'Up')
    turtle.onkeypress(baixo, 'Down')
    turtle.onkeypress(esquerda, 'Left')
    turtle.onkeypress(direita, 'Right')
    turtle.listen()

vida1 = turtle.Turtle()
vida2 = turtle.Turtle()
vida3 = turtle.Turtle()
vida1.speed(0)
vida2.speed(0)
vida3.speed(0)
vida1.left(90)
vida2.left(90)
vida3.left(90)
vida1.penup()
vida2.penup()
vida3.penup()
vida1.shape('vida.gif')
vida2.shape('vida.gif')
vida3.shape('vida.gif')
vida1.goto(-290,320)
vida2.goto(-270,320)
vida3.goto(-250,320)
teclas()

def garrafaAnda ():
    garrafa.forward(15)
    if garrafa.xcor() > xx - 16:
        garrafa.setheading(random.randint(90, 270))
    elif garrafa.xcor() < -xx + 16:
        garrafa.setheading([random.randint(0, 90), random.randint(270, 360)][random.randint(0, 1)])
    elif garrafa.ycor() > yy - 30:
        garrafa.setheading(random.randint(180, 360))
    elif garrafa.ycor() < -yy + 30:
        garrafa.setheading(random.randint(0, 180))
    janela.ontimer(garrafaAnda, 1000 // 24)
    distx2 = tartaruga.xcor() - garrafa.xcor()
    disty2 = tartaruga.ycor() - garrafa.ycor()
    if distx2 > -40 and distx2 < 40 and disty2 > -50 and disty2 < 50:
        canto(garrafa)
        global life
        global vida1
        global vida2
        global vida3
        life -= 1
        if life == 2:
            vida3.hideturtle()
        elif life == 1:
            vida2.hideturtle()
        elif life == 0:
            turtle.bye()

garrafa = turtle.Turtle() ##cria a garrafa
garrafa.speed(0)
garrafa.penup()
garrafa.shape('garrafa.gif')
canto(garrafa)
garrafa.setheading(random.randint(0,360))
garrafaAnda()

janela.tracer(0)
while True:
    janela.update()