# Detecção de Velocidade (Speed Detection)

Gabriel Teixeira Mesquita

Orientador: Prof. Dr. Marco Túlio Alves Rodrigues

## Tecnologias utilizadas

* Python 3.6.8
* PIP 9.0.1

### Instalação Python

Instalar o python pela interface de apt-get é muito simples, basta executar os seguintes comandos:

`$ sudo apt-get update `

`$ sudo apt-get upgrade python3 `

`$ sudo apt-get install python3 `

Verifica se o python3 foi instalado corretamente:

```
$ python3 -V
Python 3.6.8
```

---

### Instalação PIP

O PIP é um gerenciador de pacotes python, neste projeto, é necessário instalar algumas dependências,
o PIP vai conseguir facilitar a instalação destes.

Para fazer a instalação, execute os seguintes comandos no terminal:

`$ sudo apt install python-pip `

Verifica se o PIP3 foi instalado corretamente:

```
$ pip --version
pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)
```

---

### Instalação IDE

No meu caso, usei o PyCharm como IDE, mas você pode usar qualquer um.
Existem duas formas de fazer a instalação, a primeira é baixando o pacote diretamente:

`$ sudo tar xfz pycharm-*.tar.gz -C /opt/`

`$ cd /opt/pycharm-*/bin`

`$ ./pycharm.sh`

Ou voce pode fazer a instalação via snap:

`$ sudo snap install pycharm-community --classic `

---

### Configuração VMs

Antes de começar, é bom criar um ambiente virtual para fazer a instalação dos pacotes na versão
correta do projeto, isso para tentar ao máximo, não poluir o seu pc com pacotes e dependências variadas.

Com isso, execute os comandos para instalar o python-venv:

`$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev `

`$ sudo apt install -y python3-venv `

Com o python-venv instalado, crie o seu ambiente virtual proximo ao clone deste repositório (não dentro dele)

`$ python3 -m venv myEnv `

Ao executar este comando, verifique se a pasta ficou assim:

`$ ls myEnv `

![ls MyEnv result](https://user-images.githubusercontent.com/11557379/65373036-2eaa8e00-dc4e-11e9-9d37-ef9df69acb56.png)

---

### Ativar Python Ambiente Virtual

Para ativar, execute:

`$ source myEnv/bin/activate `

![VM activate](https://user-images.githubusercontent.com/11557379/65373048-5a2d7880-dc4e-11e9-9c0f-ebcc71e3404d.png)

Para desativar, execute:

`$ deactivate `

---

### Instalação dependências

Com o ambiente virtual ativado, execute no terminal:

`$ pip install -r requirements.txt `

---

## [Speed detection - Docs](https://github.com/fnoquiq/speed-detection-docs)
