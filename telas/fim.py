from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cores import COR_FUNDO_CARTAO, COR_TITULO, COR_TEXTO, COR_IDEAL
from widgets_util import cartao_arredondado, fundo_de_tela


class TelaFim(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raiz = FloatLayout()
        fundo_de_tela(raiz)

        caixa=BoxLayout(
            orientation="vertical",
            spacing=dp(14),
            padding=dp(26),
            size_hint=(0.86, 0.56),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
        )
        cartao_arredondado(caixa,COR_FUNDO_CARTAO)

        self.avatar = Image(size_hint=(1, 0.48))
        self.titulo = Label(
            text="Você concluiu todas as situações!",
            font_size="19sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1,0.18),
            halign="center",
        )
        self.titulo.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        self.resultado=Label(
            text="",
            font_size="15sp",
            color=COR_TEXTO,
            size_hint=(1, 0.16),
            halign="center",
        )
        self.resultado.bind(size=lambda w,v: setattr(w,"text_size",w.size))

        botao_de_novo=Button(
            text="Jogar novamente",
            font_size="16sp",
            bold=True,
            color=(1,1,1,1),
            background_normal="",
            background_color=(0,0,0,0),
            size_hint=(1,0.18),
        )
        cartao_arredondado(botao_de_novo,COR_IDEAL)
        botao_de_novo.bind(on_release=self.jogar_novamente)

        caixa.add_widget(self.avatar)
        caixa.add_widget(self.titulo)
        caixa.add_widget(self.resultado)
        caixa.add_widget(botao_de_novo)
        raiz.add_widget(caixa)
        self.add_widget(raiz)

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        self.avatar.source = app.personagem["imagem"]
        self.titulo.text = f"{app.personagem['nome']} concluiu todas as situações!"
        self.resultado.text = (
            f"Você fez {app.pontuacao_ideal} de 15 escolhas ideais.\nCada tentativa é um aprendizado!"
        )

    def jogar_novamente(self, *args):
        self.manager.current = "selecao"
