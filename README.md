# Conecte 4

Conecte 4 é uma implementação em Python do popular jogo de tabuleiro "Conecte 4", feita como uma atividade da disciplina de Redes De Computadores da Universidade Federal Fluminense, ministrada pelo docente Flavio Luiz Seixas. Este programa permite dois jogadores competirem online em um tabuleiro virtual utilizando comunicação por socket.

![gamedemo](https://github.com/user-attachments/assets/cb774f5d-4769-4340-b5e0-0a4399594bbe)

## Descrição Geral

O jogo segue as regras clássicas de Conecte 4:
- Dois jogadores se alternam fazendo jogadas.
- Cada jogador escolhe uma coluna para colocar sua peça ("X" ou "O").
- O objetivo é alinhar quatro peças consecutivas horizontalmente, verticalmente ou diagonalmente.

O programa utiliza comunicação em rede para conectar os dois jogadores. Um jogador atua como "anfitrião" (host), enquanto o outro se conecta como cliente.

## Funcionalidades
- Interface baseada em texto para exibição do tabuleiro e interação com os jogadores.
- Suporte à comunicação por sockets para conectar dois jogadores remotamente.
- Verificação automática de vitórias, empates e jogadas válidas.

## Requisitos
- Python 3.x
- Conexão à internet ou rede local (LAN) para os dois jogadores

## Instalação
1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/Disklo/conecte-4-socket
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd conecte4
   ```

3. Certifique-se de que o Python 3.x está instalado na sua máquina.

## Como Executar

### 1. Jogador Host (Anfitrião):
1. Execute o programa:
   ```bash
   python conecte4.py
   ```

2. Escolha a opção `h` (hospedar) quando solicitado.
3. O programa exibirá o endereço IP que o outro jogador deve usar para se conectar.

### 2. Jogador Cliente:
1. Execute o programa:
   ```bash
   python conecte4.py
   ```

2. Escolha a opção `c` (conectar) quando solicitado.
3. Insira o endereço IP fornecido pelo anfitrião.

### 3. Jogando o Jogo:
- Após ambos os jogadores se conectarem, o jogo começa automaticamente.
- O anfitrião faz a primeira jogada.
- Escolha uma coluna digitando um número de 0 a 6.
- O jogo continua até que um jogador vença ou o tabuleiro fique cheio (empate).

## Exemplo de Execução

**Demonstração em vídeo:**
<a href="https://youtu.be/XLPcaX2UlVs">https://youtu.be/XLPcaX2UlVs</a>

**Interface do Tabuleiro:**
```
. . . . . . .
. . . . . . .
. . . . . . .
. . . X . . .
. . O X . . .
X O O X . . .
0 1 2 3 4 5 6
```
- Cada linha representa uma fileira do tabuleiro.
- Os números na parte inferior representam as colunas disponíveis para jogadas.

**Mensagens:**
- "É seu turno!" indica que é hora de jogar.
- "Aguardando o oponente..." informa que é a vez do adversário.
- Mensagens de vitória, derrota ou empate aparecem automaticamente ao final do jogo.

## Autor
Criado por:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Disklo" title="Perfil de Disklo">
        <img src="https://avatars.githubusercontent.com/u/24628410?v=4" width="100px;" alt="Foto de Disklo"/><br>
        <sub>
          <b>Disklo (Rafael Lucio)</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/caioffnascimento" title="Caio Nascimento">
        <img src="https://avatars.githubusercontent.com/u/112733099?v=4" width="100px;" alt="Foto de Caio"/><br>
        <sub>
          <b>Caioffnascimento</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## Licença
Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
