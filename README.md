# ASD_GameHub

Plataforma Android com jogos educativos voltados para crianças com Transtorno do Espectro Autista (TEA), desenvolvida como parte da Atividade Extensionista Curricular **Software para a Sociedade (S2S)** da USP.

---

## Pré-requisitos

- Python 3.14 (recomendado)
- Kivy 2.3.1
- Buildozer

---

## Guia de Instalação do Buildozer (Ubuntu 26.04)

### 1. Instale as dependências do Buildozer

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip \
python3-virtualenv autoconf libtool pkg-config zlib1g-dev \
libncurses5-dev libncursesw5-dev libtinfo6 cmake libffi-dev \
libssl-dev automake autopoint gettext
```

### 2. Instale o Rust

```bash
curl https://sh.rustup.rs -sSf | sh
```

Adicione a seguinte linha em ~/.bashrc se já não existir:

```bash
. "$HOME/.cargo/env"
```

### 3. Configure o ambiente Python

Recomenda-se utilizar um ambiente virtual para evitar conflitos entre dependências do projeto e do sistema:

```bash
sudo apt update
sudo apt install python3.14-venv
python3.14 -m venv venv_p4a_develop
source venv_p4a_develop/bin/activate
```

### 4. Instale o Buildozer

```bash
pip install git+https://github.com/kivy/buildozer
pip install legacy-cgi setuptools cython==0.29.34
```

---

## Criando um arquivo .apk

Se o ambiente virtual Python ainda não estiver ativo, ative-o:

```bash
source venv_p4a_develop/bin/activate
```

Note que esta etapa deve ser repetida sempre que um novo terminal for aberto.

Por fim, execute o comando de build:

```bash
buildozer -v android debug
```

A primeira compilação será demorada, pois o Buildozer irá fazer o download do Android SDK, NDK e outras ferramentas necessárias para o processo.
O arquivo .apk gerado se encontrará na pasta

```bash
./bin/leiturasocial-1.0-arm64-v8a_armeabi-v7a-debug.apk
```
