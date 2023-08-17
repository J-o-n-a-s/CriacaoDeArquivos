from time import sleep
from tkinter.filedialog import askdirectory

if __name__ == '__main__':
    print(
        '\n'
        + '*' * 80
        + '\nPor gentileza, selecione o diretório para a criação dos arquivos.\n'
        + '*' * 80
    )

    sleep(2)

    caminho = askdirectory()

    print(f'O diretório selecionado foi "{caminho}".\n' + '*' * 80)

    while True:
        erro = False
        prefixo = input(
            'Digite um prefixo para o nome dos arquivos:\n> '
        ).strip()

        if len(prefixo) != 0:
            for caracter in prefixo:
                if caracter in '\/|<>*:"?':
                    erro = True
                    print(
                        '-' * 80
                        + '\n >>> Prefixo inválido! Tente novamente.\n'
                        + '-' * 80
                    )
                    break

        if not erro:
            print('*' * 80)
            break

    while True:
        quantidade = input('Quantos arquivos deseja criar?\n> ')

        if quantidade.isdecimal() and not quantidade == 0:
            print('*' * 80)
            quantidade = int(quantidade)
            break
        else:
            print(
                '-' * 80
                + '\n >>> Valor digitado inválido! Tente novamente.\n'
                + '-' * 80
            )

    zeros_esquerda = False

    if quantidade > 1:
        while True:
            resposta = (
                input('Completar numeração com zeros a esquerda? [S/N]\n> ')
                .strip()
                .upper()[0]
            )

            if resposta in 'SN':
                print('*' * 80)
                zeros_esquerda = True if resposta == 'S' else False
                break
            else:
                print(
                    '-' * 80
                    + '\n >>> Resposta inválida! Tente novamente.\n'
                    + '-' * 80
                )

    while True:
        erro = False
        extensao = (
            input(
                'Digite a extensão do arquivo sem o ponto e com 2 à 4 caracteres.\n> '
            )
            .strip()
            .lower()
        )

        for caracter in extensao:
            if caracter in '\/|<>*:"?' or 2 > len(extensao) > 4:
                erro = True
                print(
                    '-' * 80
                    + '\n >>> Extensão do arquivo inválida! Tente novamente.\n'
                    + '-' * 80
                )
                break

        if not erro:
            print('*' * 80)
            break

    while True:
        nome_interno = '#' * len(str(quantidade)) if zeros_esquerda else '#'
        confirmar = (
            input(
                f'Os arquivos {quantidade} terão os seguintes nomes {prefixo}{nome_interno}.{extensao}, confirma? [S/N]\n> '
            )
            .strip()
            .upper()[0]
        )

        if confirmar not in 'SN':
            print(
                '-' * 80
                + '\n >>> Confirmação inválida! Tente novamente.\n'
                + '-' * 80
            )
        else:
            print('*' * 80)
            break

    if confirmar == 'N':
        print(
            'Por gentileza, refaça a configuração da forma correta. Até mais!\n'
            + '*' * 80
        )
    else:
        print('Por gentileza, aguarde. Criando os arquivos...')

        nome_arquivo = ''

        for contador in range(1, quantidade + 1):
            try:
                if zeros_esquerda:
                    nome_arquivo = (
                        caminho
                        + '/'
                        + prefixo
                        + ('0' * len(str(quantidade)) + str(contador))[
                            -len(str(quantidade)) :
                        ]
                        + '.'
                        + extensao
                    )
                else:
                    nome_arquivo = (
                        caminho
                        + '/'
                        + prefixo
                        + str(contador)
                        + '.'
                        + extensao
                    )
                arquivo = open(nome_arquivo, 'r+')
            except FileNotFoundError:
                arquivo = open(nome_arquivo, 'w+')

            arquivo.close()

            sleep(0.01)

            print(f'Arquivo "{nome_arquivo}" criado com sucesso.')

        print(
            '*' * 80
            + '\nTodos arquivos criados com sucesso! Até mais!\n'
            + '*' * 80
            + '\n'
        )

    sleep(3)
