from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

from cores import COR_TITULO, COR_TEXTO, COR_FUNDO_CARTAO, COR_SELECIONADO
from widgets_util import cartao_arredondado, recolorir_cartao


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
