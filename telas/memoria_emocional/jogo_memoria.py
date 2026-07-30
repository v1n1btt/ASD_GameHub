# jogo_memoria.py
import os
import random

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

from cores import COR_BOTAO, COR_DESTAQUE, COR_FUNDO_CARTAO, COR_OK, COR_TEXTO
from telas.memoria_emocional.dados_memoria import PARES, VERSO_IMGPATH
from widgets_util import cartao_arredondado, fundo_de_tela, recolorir_cartao


class CartaMemoria(Button):
    def __init__(self, par_id, imagem_frente, fallback_label, **kwargs):
        super().__init__(**kwargs)
        self.par_id = par_id
        self.imagem_frente = imagem_frente
        self.virada = False
        self.encontrada = False

        # Configurações do botão
        self.size_hint = (1, 1)
        self.background_normal = VERSO_IMGPATH
        self.background_down = VERSO_IMGPATH
        self.background_color = (1, 1, 1, 1)
        self.border = (0, 0, 0, 0)

        # Label de fallback (aparece se a imagem não existir)
        self.label_fallback = Label(
            text=fallback_label,
            font_size='18sp',
            bold=True,
            color=(0, 0, 0, 1),
            halign='center',
            valign='middle',
            size=(0, 0),
            pos=(0, 0)
        )
        self.label_fallback.bind(size=lambda w, v: setattr(w, 'text_size', w.size))
        self.add_widget(self.label_fallback)

        # Atualiza posição e tamanho do Label sempre que o botão mudar
        self.bind(pos=self._atualizar_label, size=self._atualizar_label)

        # Aplica arredondamento
        cartao_arredondado(self, COR_BOTAO)

        # Verifica existência da imagem do verso
        self._atualizar_fallback(VERSO_IMGPATH)

    def _atualizar_label(self, instance, value):
        """Centraliza o Label sobre o botão."""
        self.label_fallback.pos = (self.x, self.y)
        self.label_fallback.size = (self.width, self.height)

    def _imagem_existe(self, caminho):
        return os.path.exists(caminho)

    def _atualizar_fallback(self, caminho):
        """Mostra/esconde o fallback conforme a existência da imagem."""
        if self._imagem_existe(caminho):
            self.label_fallback.opacity = 0
        else:
            self.label_fallback.opacity = 1

    def virar(self):
        if self.encontrada:
            return
        self.virada = not self.virada
        if self.virada:
            self.background_normal = self.imagem_frente
            self.background_down = self.imagem_frente
            self._atualizar_fallback(self.imagem_frente)
        else:
            self.background_normal = VERSO_IMGPATH
            self.background_down = VERSO_IMGPATH
            self._atualizar_fallback(VERSO_IMGPATH)

    def marcar_encontrada(self):
        self.encontrada = True
        self.virada = True
        self.background_normal = self.imagem_frente
        self.background_down = self.imagem_frente
        self._atualizar_fallback(self.imagem_frente)
        recolorir_cartao(self, COR_OK)

    def resetar(self):
        self.encontrada = False
        self.virada = False
        self.background_normal = VERSO_IMGPATH
        self.background_down = VERSO_IMGPATH
        self._atualizar_fallback(VERSO_IMGPATH)
        recolorir_cartao(self, COR_BOTAO)

class TelaJogoMemoria(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.raiz = FloatLayout()
        fundo_de_tela(self.raiz)

        # --- Barra de informações (topo) ---
        self.barra_info = BoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            padding=dp(10),
            size_hint=(0.9, 0.08),
            pos_hint={"center_x": 0.5, "top": 0.98},
        )
        cartao_arredondado(self.barra_info, COR_FUNDO_CARTAO)

        self.label_rodada = Label(
            text="Rodada 1/10",
            font_size="14sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(0.4, 1),
            halign="left",
            valign="middle",
        )
        self.label_pontuacao = Label(
            text="Pares: 0",
            font_size="14sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(0.3, 1),
            halign="center",
            valign="middle",
        )
        self.label_tentativas = Label(
            text="Tentativas: 0",
            font_size="14sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(0.3, 1),
            halign="right",
            valign="middle",
        )

        self.barra_info.add_widget(self.label_rodada)
        self.barra_info.add_widget(self.label_pontuacao)
        self.barra_info.add_widget(self.label_tentativas)
        self.raiz.add_widget(self.barra_info)

        # --- Botão de voltar ---
        self.botao_voltar = Button(
            text="< Voltar",
            font_size="12sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(0.15, 0.05),
            pos_hint={"x": 0.02, "top": 0.92},
        )
        cartao_arredondado(self.botao_voltar, COR_OK)
        self.botao_voltar.bind(on_release=self.voltar_ao_menu)
        self.raiz.add_widget(self.botao_voltar)

        # --- Grade de cartas ---
        self.grade = GridLayout(
            cols=2,
            spacing=dp(12),
            padding=dp(8),
            size_hint=(0.9, 0.55),
            pos_hint={"center_x": 0.5, "center_y": 0.50},
        )
        cartao_arredondado(self.grade, COR_FUNDO_CARTAO)
        self.raiz.add_widget(self.grade)

        # --- Cartão de feedback (aparece quando rodada termina) ---
        self.cartao_feedback = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=dp(16),
            size_hint=(0.8, 0.25),
            pos_hint={"center_x": 0.5, "y": -0.4},  # Começa fora da tela
        )
        cartao_arredondado(self.cartao_feedback, COR_FUNDO_CARTAO)

        self.label_feedback = Label(
            text="",
            font_size="16sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(1, 0.6),
            halign="center",
            valign="middle",
        )
        self.label_feedback.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        self.botao_proximo = Button(
            text="Próxima Rodada",
            font_size="15sp",
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(1, 0.4),
        )
        cartao_arredondado(self.botao_proximo, COR_DESTAQUE)
        self.botao_proximo.bind(on_release=self.proxima_rodada)

        self.cartao_feedback.add_widget(self.label_feedback)
        self.cartao_feedback.add_widget(self.botao_proximo)
        self.raiz.add_widget(self.cartao_feedback)

        self.add_widget(self.raiz)

        # Estado interno
        self.cartas = []
        self.primeira_carta = None
        self.segunda_carta = None
        self.aguardando_verificacao = False
        self.pares_encontrados_rodada = 0

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        if not hasattr(app, 'memoria') or app.memoria["rodada_atual"] >= 10:
            app.iniciar_jogo_memoria()
        self.carregar_rodada()

    def carregar_rodada(self):
        app = App.get_running_app()
        memoria = app.memoria
        rodada = memoria["rodada_atual"]

        self.label_rodada.text = f"Rodada {rodada + 1}/10"
        self.label_pontuacao.text = f"Pares: {memoria['pontuacao']}"
        self.label_tentativas.text = f"Tentativas: {memoria['tentativas']}"

        pares_selecionados = random.sample(PARES, 3)
        cartas_temp = []
        for par in pares_selecionados:
            cartas_temp.append({"par_name": par["nome"], "par_id": par["id"], "imagem": par["lado_a"]})
            cartas_temp.append({"par_name": par["nome"], "par_id": par["id"], "imagem": par["lado_b"]})
        random.shuffle(cartas_temp)

        memoria["cartas_atuais"] = cartas_temp
        memoria["pares_encontrados"] = []
        memoria["cartas_reveladas"] = []

        self.grade.clear_widgets()
        self.cartas = []
        self.primeira_carta = None
        self.segunda_carta = None
        self.aguardando_verificacao = False
        self.pares_encontrados_rodada = 0

        for dados in cartas_temp:
            carta = CartaMemoria(fallback_label=dados["par_name"], par_id=dados["par_id"], imagem_frente=dados["imagem"])
            carta.bind(on_release=self.clicar_carta)
            self.grade.add_widget(carta)
            self.cartas.append(carta)

        self.cartao_feedback.pos_hint = {"center_x": 0.5, "y": -0.4}

    def clicar_carta(self, carta):
        if self.aguardando_verificacao:
            return
        if carta.virada or carta.encontrada:
            return

        carta.virar()

        if self.primeira_carta is None:
            self.primeira_carta = carta
        elif self.segunda_carta is None:
            self.segunda_carta = carta
            self.aguardando_verificacao = True
            app = App.get_running_app()
            app.memoria["tentativas"] += 1
            self.label_tentativas.text = f"Tentativas: {app.memoria['tentativas']}"
            self.verificar_pares()

    def verificar_pares(self):
        if self.primeira_carta.par_id == self.segunda_carta.par_id:
            self.primeira_carta.marcar_encontrada()
            self.segunda_carta.marcar_encontrada()
            app = App.get_running_app()
            app.memoria["pontuacao"] += 1
            self.label_pontuacao.text = f"Pares: {app.memoria['pontuacao']}"
            self.pares_encontrados_rodada += 1
            self.primeira_carta = None
            self.segunda_carta = None
            self.aguardando_verificacao = False

            if self.pares_encontrados_rodada == 3:
                self.finalizar_rodada()
        else:
            Clock.schedule_once(self.desvirar_cartas, 0.8)

    def desvirar_cartas(self, dt):
        if self.primeira_carta and not self.primeira_carta.encontrada:
            self.primeira_carta.virar()
        if self.segunda_carta and not self.segunda_carta.encontrada:
            self.segunda_carta.virar()
        self.primeira_carta = None
        self.segunda_carta = None
        self.aguardando_verificacao = False

    def finalizar_rodada(self):
        app = App.get_running_app()
        rodada = app.memoria["rodada_atual"]
        if rodada == 9:
            self.label_feedback.text = "Parabéns! Você completou todas as rodadas!"
            self.botao_proximo.text = "Ver Resultado"
        else:
            self.label_feedback.text = f"Rodada {rodada + 1} concluída!"
            self.botao_proximo.text = "Próxima Rodada"
        self.cartao_feedback.pos_hint = {"center_x": 0.5, "y": 0.15}

    def proxima_rodada(self, *args):
        app = App.get_running_app()
        app.memoria["rodada_atual"] += 1
        if app.memoria["rodada_atual"] >= 10:
            self.manager.current = "fim_memoria"
        else:
            self.carregar_rodada()

    def voltar_ao_menu(self, *args):
        self.manager.current = "menu_memoria"
