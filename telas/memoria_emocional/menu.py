# menu_memoria.py
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cores import COR_FUNDO_CARTAO, COR_TITULO, COR_TEXTO, COR_DESTAQUE, COR_OK
from widgets_util import cartao_arredondado, fundo_de_tela


class TelaMenuMemoria(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raiz = FloatLayout()
        fundo_de_tela(raiz)

        caixa = BoxLayout(
            orientation="vertical",
            spacing=dp(16),
            padding=dp(26),
            size_hint=(0.86, 0.50),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
        )
        cartao_arredondado(caixa, COR_FUNDO_CARTAO)

        titulo = Label(
            text="Jogo da Memória",
            font_size="27sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1, 0.30),
        )
        subtitulo = Label(
            text="Encontre os pares de imagens!",
            font_size="15sp",
            color=COR_TEXTO,
            size_hint=(1, 0.20),
            halign="center",
        )
        subtitulo.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        botao_jogar = Button(
            text="Jogar",
            font_size="19sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(1, 0.25),
        )
        cartao_arredondado(botao_jogar, COR_DESTAQUE)
        botao_jogar.bind(on_release=self.ir_para_jogo)

        botao_voltar = Button(
            text="Voltar ao menu de jogos",
            font_size="13sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(1, 0.15),
        )
        cartao_arredondado(botao_voltar, COR_OK)
        botao_voltar.bind(on_release=self.voltar_ao_menu_principal)

        caixa.add_widget(titulo)
        caixa.add_widget(subtitulo)
        caixa.add_widget(botao_jogar)
        caixa.add_widget(botao_voltar)
        raiz.add_widget(caixa)
        self.add_widget(raiz)

    def ir_para_jogo(self, *args):
        # Inicializa o estado do jogo antes de navegar
        app = App.get_running_app()
        app.memoria = {
            "rodada_atual": 0,          # 0 a 9
            "cartas_atuais": [],        # lista de 6 cartas (dicionários) para a rodada
            "cartas_reveladas": [],     # lista de índices das cartas atualmente viradas (máx 2)
            "pares_encontrados": [],    # não se aplica se forem únicas? Ajustar conforme mecânica
            "tentativas": 0,            # ou outro contador
            "pontuacao": 0,             # ex: acertos
            "estado_jogo": "aguardando" # ou "revelando", "verificando", etc.
        }
        self.manager.current = "jogo_memoria"

    def voltar_ao_menu_principal(self, *args):
        self.manager.current = "menu_principal"
