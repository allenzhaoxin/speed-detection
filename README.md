# Detecção de Velocidade (Speed Detection)

Gabriel Teixeira Mesquita

Orientador: Prof. Dr. Marco Túlio Alves Rodrigues

## Resultados dos Testes

| **Velocidade Real** 	| **Teste 1** 	| **Teste 2** 	|
|:-------------------:	|:-----------:	|:-----------:	|
|     **60 KM/H**     	|    78 KM/H   	|    84 KM/H   	|
|     **80 KM/H**     	|   105 KM/H   	|   100 KM/H   	|
|     **100 KM/H**    	|   117 KM/H  	|   114 KM/H   	|

### Exemplos reais e experimentais de testes:

Teste controlado a 60 km/h:

![GIF 60km-h - Day 1](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/teste_controlado_60_day1.gif)
![GIF 60km-h - Day 2](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/teste_controlado_60_day2.gif)

Teste controlado a 80 km/h:

![GIF 80km-h - Day 1](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/teste_controlado_80_day1.gif)
![GIF 80km-h - Day 2](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/teste_controlado_80_day2.gif)

Teste controlado a 100 km/h:

![GIF 100km-h - Day 1](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/teste_controlado_100_day1.gif)
![GIF 100km-h - Day 2](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/teste_controlado_100_day2.gif)

---

## Metodologia

# Deteção

![GIF 100km-h - Day 2](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/metodologia-1.gif)

# Assimilação

![GIF 100km-h - Day 2](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/metodologia-2.gif)

# Cálculo

![GIF 100km-h - Day 2](https://github.com/fnoquiq/speed-detection/blob/master/resource/gifs/metodologia-3.gif)

---

## Tecnologias utilizadas

* Python 3.6.8
* PIP 9.0.1

### Dependências

* OpenCV 4.1
* Dlib 19.18
* Cmake 3.13
* Numpy 1.16

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

Com o ambiente virtual ativado, entre no projeto speed-detection e execute no terminal:

`$ pip install -r requirements.txt`

Portanto recomendamos instalar as dependências desta forma:

`$ pip install -r requirements.txt --verbose`

O processo de instalação da dependência DLIB pode ser bastante demorado e caso não use a tag `-- verbose`, a instalação pode passar uma sensação de travamento.

---

## [Mais documentações](https://github.com/fnoquiq/speed-detection-docs/blob/master/TCC_II___Gabriel_Mesquita___UIT.pdf)
