import os

from telas.memoria_emocional.fim_memoria import TelaFimMemoria
from telas.memoria_emocional.jogo_memoria import TelaJogoMemoria
from telas.memoria_emocional.menu import TelaMenuMemoria
os.environ.setdefault("KIVY_NO_ARGS","1")

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.utils import platform

from telas.menu_principal import TelaMenuPrincipal
from telas.leitura_social.cenarios import CENARIOS, PERSONAGENS, REACOES_IMG
from telas.leitura_social.menu import TelaMenu
from telas.leitura_social.selecao import TelaSelecao
from telas.leitura_social.cenario import TelaCenario
from telas.fim import TelaFim
from telas.outro_jogo import TelaOUTROGAME
import random

QUANTIDADE_CENARIOS_POR_PARTIDA = 10

#FORMATO DA TELA REDIMENSIONADO CORRETAMENTE
if platform not in ("android","ios"):
    Window.size = (390, 760)


# -------------------------------------App principal--------------------------------------

class LeituraSocialApp(App):
    def build(self):
        self.title="Leitura Social"
        self.personagem=PERSONAGENS[0]
        self.indice_cenario=0
        self.pontuacao_ideal=0

        gerenciador=ScreenManager(transition=FadeTransition(duration=0.25))
        gerenciador.add_widget(TelaMenuPrincipal(name="menu_principal"))

        # Leitura Social
        gerenciador.add_widget(TelaMenu(name="menu"))
        gerenciador.add_widget(TelaSelecao(name="selecao"))
        gerenciador.add_widget(TelaCenario(name="cenario"))
        gerenciador.add_widget(TelaFim(name="fim"))

        # Memória Emocional
        gerenciador.add_widget(TelaMenuMemoria(name="menu_memoria"))
        gerenciador.add_widget(TelaJogoMemoria(name="jogo_memoria"))
        gerenciador.add_widget(TelaFimMemoria(name="fim_memoria"))

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
        self.cenarios_da_partida = random.sample(CENARIOS,min(QUANTIDADE_CENARIOS_POR_PARTIDA,len(CENARIOS))) #isso aleatoriza os cenários levados ao user



if __name__ == "__main__":
    LeituraSocialApp().run()
