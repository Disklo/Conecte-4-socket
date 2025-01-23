import socket
import threading
import sys
import os

# Função para criar o tabuleiro do jogo Conecte 4
def create_board():
    # Retorna uma matriz 6x7 preenchida com pontos (representando espaços vazios)
    return [["." for _ in range(7)] for _ in range(6)]

# Função para exibir o tabuleiro no terminal
def print_board(board):
    # Imprime cada linha do tabuleiro e os índices das colunas
    for row in board:
        print(" ".join(row))
    print("0 1 2 3 4 5 6")

# Verifica se a jogada em uma coluna é válida
def is_valid_move(board, column):
    # A jogada é válida se a célula no topo da coluna estiver vazia
    return board[0][column] == "."

# Realiza a jogada no tabuleiro
def make_move(board, column, piece):
    # Percorre as linhas da coluna de baixo para cima e preenche a primeira célula vazia
    for row in reversed(board):
        if row[column] == ".":
            row[column] = piece
            return

# Verifica se um jogador venceu
def check_winner(board, piece):
    # Verifica combinações horizontais, verticais e diagonais que resultam em vitória

    # Horizontais
    for row in range(6):
        for col in range(4):  # Limita o alcance para evitar ultrapassar as bordas
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Verticais
    for row in range(3):  # Limita a altura para evitar ultrapassar as bordas
        for col in range(7):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Diagonais positivas (\)
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Diagonais negativas (/)
    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False

# Verifica se o tabuleiro está cheio
def board_full(board):
    # Retorna True se todas as células estiverem ocupadas
    return all(cell != "." for row in board for cell in row)

# Limpa o terminal para exibir o estado atualizado do jogo
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lida com mensagens recebidas do outro jogador
def handle_peer_connection(sock, board, turn_lock):
    while True:
        data = sock.recv(1024).decode()  # Recebe os dados enviados pelo peer
        if not data:
            print("Conexão encerrada pelo outro jogador.")
            sys.exit()

        # Atualiza o tabuleiro e libera o turno
        updated_board = eval(data)
        for i in range(6):
            board[i] = updated_board[i]
        turn_lock[0] = True

# Função principal que gerencia o jogo
def main():
    print("Bem-vindo ao Conecte 4!")
    mode = input("Digite 'h' para hospedar ou 'c' para conectar-se a um jogo: ").strip().lower()

    board = create_board()  # Inicializa o tabuleiro
    turn_lock = [mode == 'h']  # Define quem joga primeiro (host)

    if mode == 'h':
        # Configura o servidor para hospedar o jogo
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", 12345))  # Liga o socket à porta 12345
        server.listen(1)  # Aguarda conexão
        host_ip = socket.gethostbyname(socket.gethostname())
        print(f"Seu IP para conexão: {host_ip}")
        print("Aguardando conexão do outro jogador...")
        conn, addr = server.accept()  # Aceita a conexão
        print(f"Jogador conectado: {addr}")
        peer = conn
    elif mode == 'c':
        # Conecta ao servidor do host
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = input("Digite o IP do anfitrião: ").strip()
        peer.connect((host, 12345))  # Conecta ao host
        print("Conectado ao anfitrião!")
    else:
        print("Opção inválida.")
        sys.exit()

    # Inicia uma thread para receber mensagens do peer
    threading.Thread(target=handle_peer_connection, args=(peer, board, turn_lock), daemon=True).start()

    player_piece = "X" if mode == 'h' else "O"  # Define a peça do jogador
    opponent_piece = "O" if mode == 'h' else "X"  # Define a peça do oponente

    while True:
        if turn_lock[0]:  # Verifica se é o turno do jogador
            clear_terminal()
            print_board(board)

            if check_winner(board, opponent_piece):  # Verifica se o oponente venceu
                print("O oponente venceu! Fim de jogo.")
                break

            if board_full(board):  # Verifica empate
                print("Empate! O tabuleiro está cheio.")
                break

            # Turno do jogador
            print("É seu turno!")
            while True:
                try:
                    col = int(input("Escolha uma coluna (0-6): "))
                    if 0 <= col <= 6 and is_valid_move(board, col):
                        break
                    else:
                        print("Movimento inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Tente novamente.")

            make_move(board, col, player_piece)  # Realiza a jogada
            clear_terminal()
            print_board(board)
            turn_lock[0] = False
            print("Aguarde. É o turno do oponente.")

            if check_winner(board, player_piece):  # Verifica vitória do jogador
                clear_terminal()
                print_board(board)
                print("Você venceu! Fim de jogo.")
                peer.sendall(str(board).encode())
                break

            peer.sendall(str(board).encode())  # Envia o estado do tabuleiro ao peer
        else:
            # Aguarda o turno do oponente
            if not hasattr(main, "waiting_message_printed"):
                print("Aguardando o oponente...")
                main.waiting_message_printed = True

# Executa o jogo
if __name__ == "__main__":
    main()