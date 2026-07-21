from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cores import COR_FUNDO_CARTAO, COR_TITULO, COR_TEXTO, COR_IDEAL, COR_OK, COR_DESTAQUE
from widgets_util import cartao_arredondado, fundo_de_tela
from componentes import BotaoJogo


class TelaMenuPrincipal(Screen):
    """Primeira tela do app: o jogador escolhe entre os 3 minigames disponíveis."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raiz = FloatLayout()
        fundo_de_tela(raiz)

        caixa = BoxLayout(
            orientation="vertical",
            spacing=dp(16),
            padding=dp(26),
            size_hint=(0.88, 0.72),
            pos_hint={"center_x": 0.5, "center_y": 0.53},
        )
        cartao_arredondado(caixa, COR_FUNDO_CARTAO)

        titulo=Label(
            text="Escolha um jogo",
            font_size="28sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1,0.14),
        )
        subtitulo=Label(
            text="Treine habilidades sociais brincando!",
            font_size="14sp",
            color=COR_TEXTO,
            size_hint=(1,0.10),
            halign="center",
        )
        subtitulo.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        cartao1 = BotaoJogo(
            "Leitura Social",
            "Escolha a melhor atitude em cada situação",
            COR_IDEAL,
            "menu",
            size_hint=(1, 0.24),
        )
        cartao2 = BotaoJogo(
            "jogo 2",
            "nome tela game 2",
            COR_OK,
            "jogo2",
            size_hint=(1, 0.24),
        )
        cartao3 = BotaoJogo(
            "jogo 3",
            "nome tela game 3",
            COR_DESTAQUE,
            "jogo3",
            size_hint=(1, 0.24),
        )
        for cartao in (cartao1, cartao2, cartao3):
            cartao.parent_tela = self

        caixa.add_widget(titulo)
        caixa.add_widget(subtitulo)
        caixa.add_widget(cartao1)
        caixa.add_widget(cartao2)
        caixa.add_widget(cartao3)
        raiz.add_widget(caixa)
        self.add_widget(raiz)

    def ir_para_jogo(self, nome_tela):
        self.manager.current = nome_tela
