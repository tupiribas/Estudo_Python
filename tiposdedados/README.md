# Tipos de dados

| Descrição          | Tipo                             |
| ------------------ | -------------------------------- |
| Tipo de texto      | str                              |
| Tipos Numéricos    | int`, `float`, `complex          |
| Tipos de sequência | list`, `tuple`, `range           |
| Tipo de mapeamento | dict *(dicionário)*              |
| Tipos de conjunto  | set`,`frozenset                  |
| Tipo booleano      | bool                             |
| Tipos binários     | bytes`, `bytearray`, `memoryview |
| Nenhum Tipo        | NoneType                         |

# Detalhes

## 1. Range(inicial, fim,  intervalo)

​	Retorna uma sequência de números, inserindo o valor inicial, final e o intervalo.

## 2.  Set  (Conjunto)

​	Os conjuntos são usados para armazenar vários itens em uma única variável.

​	**Especificação** >>> Um conjunto é uma coleção *não ordenada* , **imutável** e *não tem index*

## 3. Frozenset

​	Frozen set é apenas uma versão imutável de um objeto Set.

## 4. Memoryview()

​	A função memoryview() permite acesso direto de leitura e gravação aos dados orientados a byte de um objeto sem a necessidade de copiá-lo primeiro. 

​	Isso pode gerar grandes ganhos de desempenho ao operar em objetos grandes, pois não cria uma cópia ao fatiar.
