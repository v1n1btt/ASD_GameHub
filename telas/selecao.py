from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cenarios import PERSONAGENS
from cores import COR_FUNDO_CARTAO, COR_TITULO, COR_IDEAL
from widgets_util import cartao_arredondado, fundo_de_tela
from componentes import BotaoPersonagem


class TelaSelecao(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cartoes = []

        raiz = FloatLayout()
        fundo_de_tela(raiz)

        painel = BoxLayout(
            orientation="vertical",
            spacing=dp(14),
            padding=dp(18),
            size_hint=(0.92, 0.86),
            pos_hint={"center_x": 0.5, "center_y": 0.52},
        )
        cartao_arredondado(painel,COR_FUNDO_CARTAO)

        titulo = Label(
            text="Escolha seu personagem",
            font_size="19sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1, 0.10),
        )

        grade = GridLayout(cols=3, spacing=dp(10), size_hint=(1, 0.70))
        for personagem in PERSONAGENS:
            cartao = BotaoPersonagem(personagem, self)
            self.cartoes.append(cartao)
            grade.add_widget(cartao)

        self.botao_confirmar = Button(
            text="Jogar!",
            font_size="18sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(1, 0.16),
            disabled=True,
            opacity=0.5,
        )
        cartao_arredondado(self.botao_confirmar, COR_IDEAL)
        self.botao_confirmar.bind(on_release=self.confirmar)

        painel.add_widget(titulo)
        painel.add_widget(grade)
        painel.add_widget(self.botao_confirmar)
        raiz.add_widget(painel)
        self.add_widget(raiz)

    def selecionar(self, personagem):
        app=App.get_running_app()
        app.personagem=personagem
        for cartao in self.cartoes:
            cartao.marcar_selecionado(cartao.personagem["id"] == personagem["id"])#simples seleção por ID
        self.botao_confirmar.disabled = False #permite apertar o botao de confirmar
        self.botao_confirmar.opacity = 1

    def confirmar(self, *args):
        app = App.get_running_app()
        app.reiniciar_jogo()
        self.manager.current = "cenario"
