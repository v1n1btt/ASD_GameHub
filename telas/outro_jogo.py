from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cores import COR_FUNDO_CARTAO, COR_TITULO, COR_TEXTO, COR_DESTAQUE
from widgets_util import cartao_arredondado, fundo_de_tela

# -------------------------------------OUTROS JOGOS--------------------------------------
#ADICIONEM AQUI

class TelaOUTROGAME(Screen):

    def __init__(self, titulo_jogo, descricao, **kwargs):
        super().__init__(**kwargs)
        raiz = FloatLayout()
        fundo_de_tela(raiz)

        caixa = BoxLayout(
            orientation="vertical",
            spacing=dp(14),
            padding=dp(26),
            size_hint=(0.86, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
        )
        cartao_arredondado(caixa,COR_FUNDO_CARTAO)

        titulo=Label(
            text=titulo_jogo,
            font_size="20sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1, 0.3),
            halign="center",
        )
        titulo.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        texto = Label(
            text=descricao,
            font_size="14.5sp",
            color=COR_TEXTO,
            size_hint=(1, 0.36),
            halign="center",
            valign="middle",
        )
        texto.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        botao_voltar=Button(
            text="Voltar ao menu de jogos",
            font_size="20sp",
            bold=True,
            color=(1,1,1,1),
            background_normal="",
            background_color=(0,0,0,0),
            size_hint=(1,0.24),
        )
        cartao_arredondado(botao_voltar,COR_DESTAQUE)
        botao_voltar.bind(on_release=self.voltar_ao_menu_principal)

        caixa.add_widget(titulo)
        caixa.add_widget(texto)
        caixa.add_widget(botao_voltar)
        raiz.add_widget(caixa)
        self.add_widget(raiz)

    def voltar_ao_menu_principal(self, *args):
        self.manager.current = "menu_principal"
