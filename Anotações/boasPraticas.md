# Boas Práticas em Python

## Boas práticas para nomear variáveis

Os nomes de variáveis devem sempre ser descritivos que claramente explicam o propósito da variável. Exemplos:

```python
temperatura = 25
masa = 54.5
mensagem = "Olá, programador!"
```

Alguns pontos a serem evitados:

- Nomes genéricos como `variable`, `dado` ou `valor`. Esses nomes genéricos podem funcionar para exemplos pequenos, mas não são descritivos o suficiente para códigos de produção;
- Letras únicas. Variáveis nomeadas com uma letra só pode ser difícil de entender o que ela significa, tornando o código difícil de ler, especialmente quando se usa com expressões com nomes similares. Algumas exceções a isso são
  - índices de listas;
    É bastante comum usar letras como `i`, `j` e `k` para representar índices.
  - pontos de coordenadas.
    Comum usar `x`, `y`, e `z`.
- Abreviações. É interessante usar nomes completos por ser mais legível e claro. Contudo, em caso de abreviações já conhecidas por todos o uso é compressível. Exemplo:

  ```python
    cmd = "python -m pip list" # cmd é comumente abreviação para "command"
    msg = "Olá, programador!" # msg é comumente abreviação para "message"
  ```

Muitas vezes é preciso múltiplas palavras para montar um nome de variável descritivo. E o nome de variável com algumas palavras pode ser difícil de ler, dependendo de como seja construído esse nome. Exemplo:

```python
quantidadedegraduandos =200
```

No exemplo acima a variável é meio difícil de ler, tem que prestar atenção nos limites das palavras para fazer sentido.
As práticas mais comuns para nomear variáveis com múltiplas palavras são:

- Snake case: palavras em minúsculo são separadas por underline. Por exemplo: `quantidade_de_graduandos`.

## Referências

### Referências em artigo

- "[Variables in Python: Usage and Best Practices](https://realpython.com/python-variables/#best-practices-for-naming-variables)" de [realpython](https://realpython.com/).

### Referências em vídeo
