# fim_memoria.py
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from cores import COR_DESTAQUE, COR_FUNDO_CARTAO, COR_OK, COR_TEXTO, COR_TITULO
from widgets_util import cartao_arredondado, fundo_de_tela


class TelaFimMemoria(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.raiz = FloatLayout()
        fundo_de_tela(self.raiz)

        # Cartão central
        self.cartao = BoxLayout(
            orientation="vertical",
            spacing=dp(16),
            padding=dp(26),
            size_hint=(0.86, 0.60),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
        )
        cartao_arredondado(self.cartao, COR_FUNDO_CARTAO)

        # Título
        self.titulo = Label(
            text="Fim de jogo!",
            font_size="27sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1, 0.20),
        )

        # Estatísticas (serão atualizadas em on_pre_enter)
        self.label_estatisticas = Label(
            text="",
            font_size="16sp",
            color=COR_TEXTO,
            size_hint=(1, 0.15),
            halign="center",
            valign="middle",
        )
        self.label_estatisticas.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        # Mensagem de desempenho
        self.label_mensagem = Label(
            text="",
            font_size="17sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(1, 0.40),
            halign="center",
            valign="middle",
        )
        self.label_mensagem.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        # Botão voltar ao menu
        self.botao_voltar = Button(
            text="Voltar ao menu do jogo",
            font_size="17sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(1, 0.20),
        )
        cartao_arredondado(self.botao_voltar, COR_DESTAQUE)
        self.botao_voltar.bind(on_release=self.voltar_ao_menu)

        self.cartao.add_widget(self.titulo)
        self.cartao.add_widget(self.label_estatisticas)
        self.cartao.add_widget(self.label_mensagem)
        self.cartao.add_widget(self.botao_voltar)

        self.raiz.add_widget(self.cartao)
        self.add_widget(self.raiz)

    def on_pre_enter(self, *args):
        """Atualiza as informações ao entrar na tela."""
        app = App.get_running_app()
        memoria = app.memoria
        pares = memoria.get("pontuacao", 0)
        tentativas = memoria.get("tentativas", 0)
        total_pares = 30  # 10 rodadas * 3 pares

        self.label_estatisticas.text = f"Pares encontrados: {pares} de {total_pares}\nTentativas: {tentativas}"
        self.label_mensagem.text = self._mensagem_desempenho(pares, total_pares)

    def _mensagem_desempenho(self, pares, total):
        """Retorna uma mensagem encorajadora baseada no número de pares encontrados."""
        if pares == total:
            return "Perfeito! Você encontrou todos os pares! Parabéns!"
        elif pares >= total * 0.8:  # 80% ou mais
            return "Excelente! Você encontrou quase todos os pares!"
        elif pares >= total * 0.5:  # 50% ou mais
            return "Muito bem! Você encontrou a maioria dos pares! Continue assim!"
        else:
            return "Que bom que você jogou! Cada tentativa é um aprendizado. Continue se divertindo!"

    def voltar_ao_menu(self, *args):
        """Retorna ao menu principal do jogo da memória."""
        # Navega para o menu (o estado será resetado ao clicar em "Jogar" novamente)
        self.manager.current = "menu_memoria"