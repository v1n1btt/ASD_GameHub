from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cenarios import CENARIOS, REACOES_IMG
from cores import COR_FUNDO_CARTAO, COR_TEXTO, COR_DESTAQUE, COR_BOTAO
from widgets_util import cartao_arredondado, recolorir_cartao, fundo_de_tela


class TelaCenario(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.raiz = FloatLayout()
        fundo_de_tela(self.raiz)

        # barra de progresso simples no topo
        self.rotulo_progresso = Label(
            text="",
            font_size="13sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(0.86, 0.04),
            pos_hint={"center_x": 0.5, "top": 0.985},
        )
        self.raiz.add_widget(self.rotulo_progresso)

        #cartão com o avatar do jogador e texto da situação atual
        self.cartao_situacao = BoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            padding=dp(14),
            size_hint=(0.9, 0.28),
            pos_hint={"center_x": 0.5, "top": 0.93},
        )
        cartao_arredondado(self.cartao_situacao,COR_FUNDO_CARTAO)

        self.avatar_pequeno = Image(size_hint=(0.32, 1))
        self.texto_situacao = Label(
            text="",
            font_size="15sp",
            color=COR_TEXTO,
            size_hint=(0.68, 1),
            halign="left",
            valign="middle",
        )
        self.texto_situacao.bind(size=lambda w, v: setattr(w, "text_size", w.size))
        self.cartao_situacao.add_widget(self.avatar_pequeno)
        self.cartao_situacao.add_widget(self.texto_situacao)
        self.raiz.add_widget(self.cartao_situacao)

        # área das opções (botões)
        self.caixa_opcoes = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            padding=dp(6),
            size_hint=(0.9, 0.40),
            pos_hint={"center_x": 0.5, "y": 0.06},
        )
        self.raiz.add_widget(self.caixa_opcoes)

        # cartão de feedback e da reação do coleguinha npc
        self.cartao_feedback = BoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            padding=dp(14),
            size_hint=(0.9, 0.34),
            pos_hint={"center_x": 0.5, "y": -0.4},  #começa fora da tela
        )
        cartao_arredondado(self.cartao_feedback,COR_FUNDO_CARTAO)

        coluna_reacao = BoxLayout(orientation="vertical", size_hint=(0.32, 1), spacing=dp(4))
        self.imagem_reacao = Image(size_hint=(1, 0.78))
        self.texto_reacao = Label(
            text="",
            font_size="11.5sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(1, 0.22),
            halign="center",
            valign="middle",
        )
        self.texto_reacao.bind(size=lambda w, v: setattr(w, "text_size", w.size))
        coluna_reacao.add_widget(self.imagem_reacao)
        coluna_reacao.add_widget(self.texto_reacao)

        coluna_texto =BoxLayout(orientation="vertical",size_hint=(0.68,1),spacing=dp(8))
        self.texto_feedback=Label(
            text="",
            font_size="14.5sp",
            color=COR_TEXTO,
            halign="left",
            valign="middle",
            size_hint=(1, 0.7),
        )
        self.texto_feedback.bind(size=lambda w, v: setattr(w, "text_size", w.size))
        self.botao_continuar = Button(
            text="Continuar",
            font_size="15sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(1, 0.3),
        )
        cartao_arredondado(self.botao_continuar,COR_DESTAQUE)
        self.botao_continuar.bind(on_release=self.proximo_cenario)
        coluna_texto.add_widget(self.texto_feedback)
        coluna_texto.add_widget(self.botao_continuar)
        self.cartao_feedback.add_widget(coluna_reacao)
        self.cartao_feedback.add_widget(coluna_texto)
        self.raiz.add_widget(self.cartao_feedback)

        self.add_widget(self.raiz)

    def on_pre_enter(self, *args):
        self.carregar_cenario()

    def carregar_cenario(self):
        app = App.get_running_app()
        cenario = CENARIOS[app.indice_cenario]

        self.rotulo_progresso.text = f"Situação {app.indice_cenario + 1} de {len(CENARIOS)}"
        self.texto_situacao.text = cenario["situacao"]
        self.avatar_pequeno.source = app.personagem["imagem"]

        # esconde o feedback e mostra as opções de novo
        self.cartao_feedback.pos_hint={"center_x":0.5,"y":-0.5}
        self.caixa_opcoes.opacity=1
        self.caixa_opcoes.disabled=False

        self.caixa_opcoes.clear_widgets()
        for escolha in cenario["escolhas"]:
            botao = Button(
                text=escolha["texto"],
                font_size="14.5sp",
                bold=True,
                color=(1,1,1,1),
                background_normal="",
                background_color=(0,0,0,0),
                halign="center",
                valign="middle",
            )
            botao.bind(size=lambda w, v: setattr(w, "text_size", w.size))
            cartao_arredondado(botao, COR_BOTAO)
            botao.bind(on_release=lambda inst, esc=escolha: self.escolher(esc))
            self.caixa_opcoes.add_widget(botao)

    def escolher(self, escolha): #AQUI ESTÃO OS NÍVEIS DAS ESCOLHAS - errado e certo estão, obviamente, ocultos do user, isso pq o intuito do jogo é não pressionar ele por ter resultados "corretos", mas sim mostrar que há outras formas de reagir que podem ser melhores
        app = App.get_running_app()
        if escolha["nivel"]=="ideal":
            app.pontuacao_ideal += 1
            prefixo="Ótima escolha!\n"
        else:
            prefixo="Boa tentativa!\n"

        self.texto_feedback.text=prefixo+escolha["feedback"]
        self.imagem_reacao.source=REACOES_IMG[escolha["reacao"]]
        self.texto_reacao.text=escolha["reacao_texto"]

        recolorir_cartao(self.cartao_feedback,COR_FUNDO_CARTAO)

        # esconde opções e mostra feedback
        self.caixa_opcoes.disabled = True
        self.caixa_opcoes.opacity = 0
        self.cartao_feedback.pos_hint = {"center_x": 0.5, "y": 0.06}

    def proximo_cenario(self, *args):
        app = App.get_running_app()
        app.indice_cenario += 1
        if app.indice_cenario >= len(CENARIOS):
            self.manager.current="fim"
        else:
            self.carregar_cenario()
