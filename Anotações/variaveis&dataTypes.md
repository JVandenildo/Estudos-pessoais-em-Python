# Variáveis e Data Types

Variáveis são usadas para armazenar informações usadas e manipuladas no programa de computador. Elas também são uma maneira de rotular dados com um nome descritivo, dessa maneira o programa se torna mais legível para quem ler. É útil pensar as variáveis como containers que armazenam informações. As variáveis se comportam como se fossem o valor a que se referem.

## Criando variáveis

A primeira maneira de criar uma variável em Python é atribui-la um valor usando o operador de atribuição. Sintaxe:

```python
nome_descritivo = valor
```

Na sintaxe acima, o nome da variável fica a esquerda, o operador de atribuição (`=`), seguido pelo valor que se deseja atribuir a variável em questão. O valor neste constructo pode ser qualquer objeto Python, incluindo string, números, listas, dicionários, ou mesmo objetos customizados. Exemplos de variáveis em Python:

```python
palavra = "Python"
numero = 42
coeficiente = 2.87
frutas = ["laranja", "manja", "uva"]
ordinais = { 1: "primeiro", 2: "segundo", 3: "terceiro" }

class UmaClasseCustomizada: pass
instance = UmaClasseCustomizada()
```

No exemplo acima, foram definidos variáveis atribuindo valores a seus nomes. Os primeiros cinco exemplos incluem variáveis que se referem a diferentes tipos nativos. O último exemplo mostra que variáveis podem se referir a objetos customizados como uma instância de uma classe.

## Data Types não básicos

- **Listas**: em comparação, é como arrays de tamanho dinâmico, declarados em outras linguagens (vetores em C++ e ArrayList em Java). Listas não precisam ser sempre homogêneas, o que torna uma ferramenta interessante no Python;
- **Tupla**: uma tupla é uma coleção de objetos de Python separados por vírgulas. Em algumas maneiras, uma tupla é semelhante a uma lista em termos de indexamento, objetos aninhados, e repetição, a diferença é que tuplas são imutáveis;
- **Set**: um Set é uma coleção desordenada de data type que é iterável, mutável, e não possui elementos duplicados. A classe set do Python representa a noção matemática de um conjunto;
- **Dicionário**: em Python, Dicionário é uma coleção ordenada (desde a versão 3.7) de valores, usados para armazenar os valores dos dados como um map, que, diferente de outros data types que armazenam somente um único valor como um elemento, Dicionários em Python armazenam pares chave:valor. Chave:valor é providenciado no dicionário para torná-lo mais otimizado.

## Typecasting

O processo de converter o valor de um data type (integer, string, float, etc.) para outro data type é chamado de conversão de tipo. Python tem dois tipos de conversão: Implícita e Explícita.

## Referências

### Referências em artigos (variáveis e data types)

- "[Variables in Python: Usage and Best Practices](https://realpython.com/python-variables/)" no site [realpython.com/](https://realpython.com/);
- "[Python Variables](https://www.w3schools.com/python/python_variables.asp)" no site [w3schools.com/](https://www.w3schools.com/);
- "[Python's Assignment Operator: Write Robust Assignments](https://realpython.com/python-assignment-operator/)" no site [realpython.com/](https://realpython.com/);
- "[Basic Data Types in Python: A Quick Exploration](https://realpython.com/python-data-types/)" no site [realpython.com/](https://realpython.com/);
- "[Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)" no site [w3schools.com/](https://www.w3schools.com/);
- "[Python for Beginners: Data Types](https://thenewstack.io/python-for-beginners-data-types/)" no site [thenewstack.io/](https://thenewstack.io/);
- "[Tuples vs Lists vs Sets in Python](https://jerrynsh.com/tuples-vs-lists-vs-sets-in-python/)" no site [jerrynsh.com/](https://jerrynsh.com/);
- "[Python for Beginners: Lits](https://thenewstack.io/python-for-beginners-lists/)" no site [thenewstack.io/](https://thenewstack.io/);
- "[Python for Beginners: When and How to Use Tuples](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/)" no site [thenewstack.io/](thenewstack.io/);
- "[Python Type Conversion](https://www.programiz.com/python-programming/type-conversion-and-casting)" no site [programiz.com/](https://www.programiz.com/).

### Referências em vídeos (variáveis e data types)

- [Playlist](https://youtube.com/playlist?list=PLBlnK6fEyqRhN-sfWgCU1z_Qhakc1AGOn&si=gT2ct0CbQ87AOSEq) do canal [@nesoacademy](https://www.youtube.com/@nesoacademy);
- "[Difference Between List, Tuple, Set and Dictionary in Python](https://youtu.be/n0krwG38SHI?si=LdcHDycy7d2kuEIL)" do canal [@KindsonTheTechPro](https://www.youtube.com/@KindsonTheTechPro).
