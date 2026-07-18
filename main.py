import os
os.environ.setdefault("KIVY_NO_ARGS","1")

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.utils import platform
from cenarios import CENARIOS, PERSONAGENS, REACOES_IMG

#paleta de cores pastel

COR_FUNDO_CARTAO=(1,0.99,0.97,0.97)     
COR_TEXTO=(0.20,0.16,0.14,1)             
COR_TITULO=(0.42,0.20,0.55,1)            
COR_BOTAO=(0.55,0.72,0.95,1)             
COR_BOTAO_TEXTO=(0.08,0.14,0.30,1)       
COR_IDEAL =(0.38,0.78,0.53,1)             
COR_IDEAL_TEXTO=(0.06,0.28,0.15,1)
COR_OK=(0.55,0.72,0.95,1)                
COR_OK_TEXTO=(0.08,0.14,0.30,1)
COR_DESTAQUE=(0.98,0.65,0.35,1)          
COR_SELECIONADO=(0.98,0.80,0.30,1)       

COR_REACAO = {
    "feliz":(0.38,0.78,0.53,1),
    "triste":(0.65, 0.72,0.92,1),
    "assustado":(0.80,0.68,0.92,1),
    "bravo":(0.98, 0.62,0.45,1),
    "neutro":(0.75,0.78,0.82,1),
    "pensativo":(0.55,0.72,0.95,1),
}

#FORMATO DA TELA REDIMENSIONADO CORRETAMENTE
if platform not in ("android","ios"):
    Window.size = (390, 760)


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





# -------------------------------------Tela de menu principal (escolha de jogo)--------------------------------------

class BotaoJogo(BoxLayout):
    """Cartão clicável que representa um dos 3 jogos no menu principal."""

    def __init__(self, titulo, subtitulo, cor, nome_tela, **kwargs):
        super().__init__(orientation="vertical", spacing=dp(4), padding=dp(14), **kwargs)
        self.nome_tela = nome_tela
        cartao_arredondado(self, cor)

        rotulo_titulo = Label(
            text=titulo,
            font_size="17sp",
            bold=True,
            color=COR_TITULO,
            size_hint=(1, 0.6),
            halign="center",
            valign="middle",
        )
        rotulo_titulo.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        rotulo_subtitulo = Label(
            text=subtitulo,
            font_size="12.5sp",
            color=COR_TEXTO,
            size_hint=(1, 0.4),
            halign="center",
            valign="middle",
        )
        rotulo_subtitulo.bind(size=lambda w, v: setattr(w, "text_size", w.size))

        self.add_widget(rotulo_titulo)
        self.add_widget(rotulo_subtitulo)

        # faixa colorida de destaque à esquerda do cartão, só um detalhe visual
        self._cor_detalhe = cor

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent_tela.ir_para_jogo(self.nome_tela)
            return True
        return super().on_touch_down(touch)


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


# -------------------------------------Tela de menu inicial--------------------------------------

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





# # -------------------------------------Tela de seleção de personagem--------------------------------------

class BotaoPersonagem(BoxLayout):
    #botão que é clicável para selecionar o personagem

    def __init__(self, personagem, tela_selecao, **kwargs):
        super().__init__(orientation="vertical", padding=dp(8), spacing=dp(4), **kwargs)
        self.personagem=personagem
        self.tela_selecao=tela_selecao

        cartao_arredondado(self, COR_FUNDO_CARTAO)

        self.foto=Image(source=personagem["imagem"], size_hint=(1, 0.8))
        self.nome_label = Label(
            text=personagem["nome"],
            font_size="14sp",
            bold=True,
            color=COR_TEXTO,
            size_hint=(1, 0.2),
        )
        self.add_widget(self.foto)
        self.add_widget(self.nome_label)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.tela_selecao.selecionar(self.personagem)
            return True
        return super().on_touch_down(touch)

    def marcar_selecionado(self, selecionado):
        cor = COR_SELECIONADO if selecionado else COR_FUNDO_CARTAO
        recolorir_cartao(self, cor)


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






# # -------------------------------------Tela de cenário (situação social e escolhas mais a reação do NPC)--------------------------------------

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





# -------------------------------------Tela final--------------------------------------

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


# -------------------------------------App principal--------------------------------------

class LeituraSocialApp(App):
    def build(self):
        self.title="Leitura Social"
        self.personagem=PERSONAGENS[0]
        self.indice_cenario=0
        self.pontuacao_ideal=0

        gerenciador=ScreenManager(transition=FadeTransition(duration=0.25))
        gerenciador.add_widget(TelaMenuPrincipal(name="menu_principal"))
        gerenciador.add_widget(TelaMenu(name="menu"))
        gerenciador.add_widget(TelaSelecao(name="selecao"))
        gerenciador.add_widget(TelaCenario(name="cenario"))
        gerenciador.add_widget(TelaFim(name="fim"))
        gerenciador.add_widget(TelaOUTROGAME(
            "jogo 2",
            "game 2",
            name="jogo2",
        ))
        gerenciador.add_widget(TelaOUTROGAME(
            "jogo 3",
            "game 3",
            name="jogo3",
        ))
        gerenciador.current="menu_principal"
        return gerenciador

    def reiniciar_jogo(self):
        self.indice_cenario=0
        self.pontuacao_ideal=0


if __name__ == "__main__":
    LeituraSocialApp().run()