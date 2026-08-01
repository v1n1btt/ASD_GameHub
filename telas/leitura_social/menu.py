from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cores import COR_FUNDO_CARTAO, COR_TITULO, COR_TEXTO, COR_DESTAQUE, COR_OK
from widgets_util import cartao_arredondado, fundo_de_tela


class TelaMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raiz = FloatLayout()
        fundo_de_tela(raiz)

        caixa = BoxLayout(
            orientation="vertical",
            spacing=dp(16),
            padding=dp(26),
            size_hint=(0.86, 0.56),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
        )
        cartao_arredondado(caixa, COR_FUNDO_CARTAO)

        mia = Image(source="assets/mia.png", size_hint=(1, 0.52))#personagem que aparece no menu de entrada
        titulo = Label(
            text="Leitura Social",
            font_size="27sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1, 0.16),
        )
        subtitulo = Label(
            text="Escolha a melhor atitude em cada situação!",
            font_size="15sp",
            color=COR_TEXTO,
            size_hint=(1, 0.14),
            halign="center",
        )
        subtitulo.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        botao_iniciar=Button(
            text="Começar",
            font_size="19sp",
            bold=True,
            color=(1, 1,1,1),
            background_normal="",
            background_color=(0,0,0,0),
            size_hint=(1,0.20),
        )
        cartao_arredondado(botao_iniciar, COR_DESTAQUE)
        botao_iniciar.bind(on_release=self.ir_pra_selecao)

        botao_voltar=Button(
            text="Voltar ao menu de jogos",
            font_size="13sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(1, 0.12),
        )
        cartao_arredondado(botao_voltar,COR_OK)
        botao_voltar.bind(on_release=self.voltar_ao_menu_principal)

        caixa.add_widget(mia)
        caixa.add_widget(titulo)
        caixa.add_widget(subtitulo)
        caixa.add_widget(botao_iniciar)
        caixa.add_widget(botao_voltar)
        raiz.add_widget(caixa)
        self.add_widget(raiz)

    def ir_pra_selecao(self, *args): #dos personagens "jogáveis"
        self.manager.current="selecao"

    def voltar_ao_menu_principal(self, *args):
        self.manager.current="menu_principal"
