import shutil


def copiar_imagem(nome_imagem, novo_nome):
    shutil.copy(nome_imagem, novo_nome)

# Ler o arquivo de texto contendo os nomes
with open('nomes.txt', 'r') as arquivo:
    nomes = arquivo.read().splitlines()

# Nome da imagem original
nome_imagem_original = 'imagem_original.png'

# Copiar a imagem para cada nome da lista
for nome in nomes:
    novo_nome_imagem = f'{nome}.png'  # Nome da imagem com o nome correspondente
    copiar_imagem(nome_imagem_original, novo_nome_imagem)

print('Imagens copiadas com sucesso.')
