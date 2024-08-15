# Pythonicness e Empacotamento

Escrever um código limpo e de fácil entendimento é muito importante. Uma maneira de fazê-lo é por Python Zen.

## Sumário

1. [Python Zen](#python-zen);
   1. [PEP (Python Enhancement Proposals)](#pep-python-enhancement-proposals).
2. [Bibliotecas de Terceiros](#bibliotecas-de-terceiros);
3. [Empacotamento](#empacotamento).
   1. [Empacotamento para usuários](#empacotamento-para-usuários).

## Python Zen

O Zen do Python é uma maneira de se guiar nas boas práticas. É usado a linha a seguir para acessar o Python Zen.

```python
import this
```

Resultado:

```text
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

> [!HINT]
> Algumas linhas no Python Zen podem precisar de mais explicação.</span>

- **_Explicit is better than implicit_**: é melhor soletrar exatamente o que seu código está fazendo. É por isso que adicionar uma _string_ numérica a uma _integer_ requer conversão explícita, ao invés de acontecer atrás da cortina, como acontece em outras linguagens.
- **_Flat is better than nested_**: estruturas bastante ninhadas (listas de listas, de listas, e assim por diante…) deveria ser evitada.
- **_Errors should never pass silently_**: em geral, quando um erro ocorre, deveria ter a saída para informar o erro, ao invés de ignorá-lo.
- **_There should be one -- and preferably only one -- obvious to do it_**: referência e contradiz a filosofia da linguagem Perl que deveria ter mais de uma maneira de fazê-lo.

### PEP (Python Enhancement Proposals)

As PEP, Propostas de Aprimoramento do Python, são sugestões para melhorias na linguagem, feitas por desenvolvedores Python experientes.
PEP 8, por exemplo, é um guia de estilo no assunto de escrita de códigos legíveis. Ele contém um números de condutas em referências a nomeação de variáveis, que estão resumidas aqui:

- módulos deveriam ter nomes curtos e todas letras minúsculas;
- nomes de classes deveriam ser no estilo CamelCase;
- a maioria dos nomes das variáveis e funções deveria ser minúsculas_com_underline;
- constantes (variáveis que nunca mudam seu valor) deveriam ser maiúsculas_com_underline;
- nomes que entrariam em conflito com palavras chave do Python (como '`class`' ou '`if`') deveriam ter _underline_ à direita.

PEP 8 também recomenda usar espaços em branco em volta dos operadores e depois de vírgulas para aumentar a legibilidade. Contudo, espaços em branco não deveriam ser usados demais. Por exemplo, evitar ter qualquer espaço em branco logo depois de parênteses, colchetes ou chaves.
Outras sugestões da PEP 8 incluem:

- linhas deveriam ser mais longas que 80 caracteres;
- '`from module import *`' deveria ser evitado;
- deveria haver apenas uma declaração por linha.

É sugerido também usar espaços, ao invés do _tab_, para indentar. Contudo, em alguns casos, isso é questão de preferência pessoal. Se você usar espaços, somente 4 por linha. É mais importante escolher um e ficar até o final do programa.
O conselho mais importante na PEP é ignorá-la quando for necessário. Não se incomode com seguir sugestões da PEP quando causaria ao seu código ser menos legível; inconsistência com o código ao redor; ou sem compatibilidade com versões anteriores. Contudo, seguir a PEP 8 terá uma grande melhoria na qualidade do código.
Algumas outras PEPs notáveis que cobrem estilo de código:

- PEP 20: O Python Zen;
- PEP 257: Style Conventions para Docstrings.

## Bibliotecas de Terceiros

A biblioteca padrão do Python, contém uma funcionalidade extensiva. Contudo, algumas atividades requerem o uso de bibliotecas de terceiros. Algumas bibliotecas conhecidas são:

- **[django](https://www.djangoproject.com/)**: é a _framework_ para _web_ escrita em Python mais usada, Django dá suporte para websites que incluem [Instagram](https://instagram.com) e [Disqus](https://disqus.com). Tem vários recursos úteis, e qualquer _feature_ que falte é por pacotes de extensão.
- **[CherryPy](https://cherrypy.dev/)** e **[Flask](https://flask.palletsprojects.com/en/3.0.x/)** são também _frameworks_ para _web_ bem populares. Para dissecar dados de websites, a biblioteca BeautifulSoup é bem útil, e acaba dando resultados melhores que construir o próprio dessecador com expressões regulares.

Enquanto o Python oferece módulos para acessar sites de forma programática, como o [urllib](http://docs.python.org/3/library/urllib.html), eles são um tanto pesados para usar. As solicitações de biblioteca de terceiros facilitam muito o uso de solicitações HTTP.
Um número de módulos de terceiros estão disponíveis para computação científica e matemática usando o Python.

- O módulo **matplotlib** permite criar grafos baseados em dados no Python;
- O módulo **[Numpy](https://numpy.org/)** permite o uso de arrays multidimensionais que são mais rápidos que a solução nativa do Python de listas aninhadas. Também contém funções para performar operações matemáticas, como transformações de matrix em arrays.
- A biblioteca **[SciPy](https://scipy.org/)** contém numerosas extensões para a funcionalidade do NumPy.

Python pode ser usado para desenvolvimento de jogos. Normalmente, é usado como uma linguagem de script para jogos escritos em outras linguagens, mas pode ser usado para jogos em si. Para jogos 3D, a biblioteca **Panda3D** pode ser usada. Para jogos 2D, uma escolha é **pygame**.
Outros exemplos de bibliotecas de terceiros:

1. [Pandas](https://pandas.pydata.org/);
2. [Librosa](https://librosa.org/);
3. [IPython](https://ipython.org/project.html);
4. [plotly](https://plotly.com/python/);
5. [Bottle](https://bottlepy.org/docs/dev/);
6. [Pyramid](https://pypi.org/project/pyramid/);
7. [request3](https://pypi.org/project/request3/);
8. [Beautiful Soup4](https://pypi.org/project/beautifulsoup4/);
9. [Selenium](https://pypi.org/project/selenium/);
10. [lxml](https://pypi.org/project/lxml/);
11. [Scrapy3](https://pypi.org/project/Scrapy3/);
12. OpenCV;
13. Mahotas;
14. SimpleTK;
15. Scikit;
    1. [image](https://scikit-image.org/);
    2. [learn](https://scikit-learn.org/stable/index.html).
16. TensorFlow;
17. Keras;
18. Theano;
19. PyTorch;
20. Splinter;
21. Robot;
22. Behave;
23. PyUnit;
24. PyTest;
25. Kivy;
26. Kivy;
27. Tkinter;
28. WxPython;
29. PyGui;
30. PySide;
31. PyGlet;
32. PyOpenGL;
33. Arcade.

## Empacotamento

Em Python o termo empacotamento refere a colocar módulos que foram escritos em um formato padrão, para que outros programadores possam instalar e usá-los com facilidade. Isso envolve o uso de módulos **setuptools** e **distutils**.
O primeiro passo no empacotamento é organizar arquivos existentes corretamente. Colocar todos os arquivos que se quer em uma biblioteca no mesmo lugar que o diretório parental. Este diretório deveria conter um arquivo chamado **init**.py, que pode estar em branco mas deve estar presente no diretório.
Este diretório vai em outro diretório contendo o readme e license, assim como um arquivo importante chamado setup.py.
Exemplo de estrutura do diretório:

```text
Usuario/
 LICENSE.txt
 README.txt
 setup.py
 usuario/
  __init__.py
  programa.py
  programa2.py
```

Pode-se colocar quantos arquivos de _script_ no diretório que forem necessários.
O próximo passo no empacotamento é escrever o arquivo setup.py.
Ele contém informações necessárias para reunir o pacote para que seja carregado no **PyPi** e instalado com **pip** (nome, versão, etc.).
Exemplo de arquivo setup.py:

```python
from distutils.core import setup

setup(
   name = 'LipSliteris',
   version = '0.1dev',
   packages = ['monte',],
   license = 'MIT',
   long_description = open('README.txt').read()
)
```

Depois de criar o arquivo setup.py, carregue-o no PyPi, ou use a linha de comando para criar uma distribuição binária (um instalador executável).
Construir uma distribuição de código-fonte, é usado a linha de comando para navegar até o diretório contendo setup.py, e rodar o comando python setup.py sdist. Rodas python setup.py bdist ou, para Windows, python setup.py bdist_wininst para construir uma distribuição binária.
Use "python setup.py register", seguido por "python setup.py sdist upload" para carregar um pacote.
Finalmente, instale um pacote com "python setup.py install".

### Empacotamento para usuários

Nem todos usuários de computador que não são programadores têm Python instalado. Portanto, é interessante empacotar scripts como arquivos executáveis para a plataforma, como os sistemas operacionais Windows ou Mac.
Para Windows, várias ferramentas estão disponíveis para a conversão de scripts para executáveis. Por exemplo, **py2exe**, pode ser usado para empacotar um script de Python, junto com as bibliotecas que são requeridas, em um único executável. **PyInstaller** e **cx_Freeze** tem o mesmo propósito.
Para Macs, tem o **py2app**, **PyInstaller** ou **cx_Freeze**.
