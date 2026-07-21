from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.image import Image


def cartao_arredondado(widget,cor):
    #Desenha um fundo arredondado (fica com aquele efeito de cartão)"""
    with widget.canvas.before:
        Color(*cor)
        widget._bg = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[dp(18)])
    widget.bind(
        pos=lambda w, v: setattr(w._bg, "pos", w.pos),
        size=lambda w, v: setattr(w._bg, "size", w.size),
    )


def recolorir_cartao(widget,cor,raio=18):
    #Troca a cor de fundo de um cartão já existente de acordo com a interação do user
    widget.canvas.before.clear()
    with widget.canvas.before:
        Color(*cor)
        widget._bg=RoundedRectangle(
            pos=widget.pos, size=widget.size, radius=[dp(raio)]
        )


def fundo_de_tela(raiz):
    #adiciona o fundo da sala de aula
    fundo=Image(
        source="assets/fundo_sala.png",
        fit_mode="fill",
        size_hint=(1,1),
        pos_hint={"x": 0, "y": 0},
    )
    raiz.add_widget(fundo)
    return fundo
