import pygame, sys
from pygame import QUIT, K_SPACE, K_RETURN, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_a, K_s, K_d, K_w, K_r, K_p
import copy

pygame.init()

'''
    Khai báo các Biến toàn cục 
'''
GRID_SIZE = 15; nxn = 15;
banco = []; NumberToWin = 5; 
player = ""; AI = ""; turn = ""; pre = (); game_over = False; LuotAI = False
# Bảng tra cứu điểm
TH = {};  
# Bảng lưu 8 hướng của 1 ô trống -> phối hợp để tra cứu điểm TH
MapPlayer = []; MapAI = [] 
# Dir lưu tọa độ các điểm có cùng Value
T_player = {}; T_Ai = {}; T_Tong = {}
# Bảng lưu "Điểm đánh giá" 4 "chiều" của 1 ô trống
ScorePlayer = []; ScoreAI = []; ScoreTong = [];
# Các hướng
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
Direc = {(-1, 0): 1, (-1, 1): 2, (0, 1): 3, (1, 1): 4, (1, 0): 5, (1, -1):6, (0, -1):7, (-1, -1):8}

# --------------------------------------------------------------------------
#               Phần khởi tạo 
GRID_SIZE = 15; nxn = 15;
banco = []; NumberToWin = 5; 
player = ""; AI = ""; turn = ""; pre = (); game_over = False; LuotAI = False
# Bảng tra cứu điểm
TH = {};  
# Bảng lưu 8 hướng của 1 ô trống -> phối hợp để tra cứu điểm TH
MapPlayer = []; MapAI = [] 
# Dir lưu tọa độ các điểm có cùng Value
T_player = {}; T_Ai = {}; T_Tong = {}
# Bảng lưu "Điểm đánh giá" 4 "chiều" của 1 ô trống
ScorePlayer = []; ScoreAI = []; ScoreTong = [];

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
Direc = {(-1, 0): 1, (-1, 1): 2, (0, 1): 3, (1, 1): 4, (1, 0): 5, (1, -1):6, (0, -1):7, (-1, -1):8}

def AddT(T: dict, value: str, x: int, y: int) -> None:
    if value not in T:
        T[value] = []
    T[value].append((x,y))

def RemoveT(T: dict, value: str, x: int, y: int) -> None:
    if value in T:
        if (x,y) in T[value]:
            T[value].remove((x, y))
        if T[value] == []:
            T.pop(value)

def taoBangDanhGia(N: int) -> list:
    matrix = [["F"] * N for _ in range(N)]
    return matrix

def Init() -> None: 
    '''
        Hàm khởi tạo giá trị ban đầu của tất cả Biến toàn cục
        Được sử dụng ghi chương trình chạy lần đầu tiên
        Và khi người chơi muốn reset bàn cờ
    
    '''

    global banco;
    global player, AI, turn,  pre, game_over, LuotAI;
    global TH, MapPlayer, MapAI, T_player, T_Ai, T_Tong, ScorePlayer, ScoreAI, ScoreTong;

    banco = [ ['.']*nxn for _ in range(nxn)]
    player = "X"; AI = "O"; turn = player; pre = (0,0,"")
    game_over = False; LuotAI = False
    
    TH.clear()
    with open("H.txt", encoding="utf-8") as inp:
        for i in range(361):
            line = inp.readline().split(";"); xau = line[0]; diem = line[1]
            TH[xau] = diem 

    MapPlayer.clear(); MapAI.clear()
    for i in range(nxn):
        MapPlayer.append( [] ); MapAI.append( [] )
        for j in range(nxn):
            MapPlayer[i].append( [0] + ["00"]*8 + ["F","F","F","F"]) 
            MapAI[i].append( [0] + ["00"]*8 + ["F","F","F","F"]) 
            if i == 0:
                MapPlayer[i][j][1] = "-1"; MapAI[i][j][1] = "-1"
            if j == nxn-1: 
                MapPlayer[i][j][3] = "-1"; MapAI[i][j][3] = "-1"
            if i == nxn-1:
                MapPlayer[i][j][5] = "-1"; MapAI[i][j][5] = "-1"
            if j == 0:
                MapPlayer[i][j][7] = "-1"; MapAI[i][j][7] = "-1"

    ScorePlayer = taoBangDanhGia(nxn); ScoreAI = taoBangDanhGia(nxn); ScoreTong = taoBangDanhGia(nxn);
    T_player = {}; T_Ai = {}; T_Tong = {}
    for i in range(nxn):
        for j in range(nxn):
            value = ScorePlayer[i][j];
            AddT(T_player, value, i, j); AddT(T_Ai, value, i, j); AddT(T_Tong, value, i, j)  

# --------------------------------------------------------------------------

def checkWin(banco: list, turn: str, x: int, y: int) -> bool:
    pass
    '''
        Hàm check Win
        Trả về True nếu "turn" Win
        Nếu không thì trả về False

    '''

def SCAN(banco: list, Map: list, turn: str, x: int, y: int, 
    ScorePlayer: list, ScoreAI: list, ScoreTong: list, 
    T_player: dict, T_Ai: dict, T_Tong: dict
    ) -> None:
    pass
    '''
        Hàm Quét các ô trống bị ảnh hưởng khi thực hiện 1 nước cờ
        Truyền tọa độ các ô trống đó và "hướng ảnh hưởng"
        vào Update_Map

    '''
    
def Update_Map(banco: list, Map: list, turn: str, x: int, y: int, 
    dx: int, dy: int, ScorePlayer: list, ScoreAI: list, ScoreTong: list, 
    T_player: dict, T_Ai: dict, T_Tong: dict) -> None:
    pass
    '''
        Hàm Cập nhật lại thông tin về hướng bị ảnh hưởng cho ô trống
        Truyền thông tin tới Update_Score

    '''

def Update_Score(banco: list, Map: list, turn: str, x: int, y: int, 
    dx: int, dy: int, ScorePlayer: list, ScoreAI: list, ScoreTong: list, 
    T_player: dict, T_Ai: dict, T_Tong: dict) -> None:
    pass
    '''
        Hàm Tính lại điểm đánh giá cho ô trống theo hướng bị ảnh hưởng
        Cập nhật Các bảng đánh giá ScorePlayer, ScoreAI, ScoreTong
            và Các từ điển lưu vị trí T_player, T_Ai, T_Tong

    '''
    

def AI_move() -> tuple[int, int]:
    pass
    '''
        Hàm trả về tọa độ (x,y) AI lựa chọn dựa theo UuTien_move() và minimax()
    
    '''

def UuTien_move(T_Ai: dict, T_player: dict) -> tuple[int, int]:
    pass
    '''
        Hàm xét các trường hợp chắc chắn cần đi
        Nếu không nằm trong các trường hợp chắc chắn -> (-1, -1)

    '''

def minimax(Board: list, isMaximizing: bool, depth: int, alpha: int, beta: int, 
    Score_Player: list, Score_AI: list, Score_Tong: list, 
    Tplayer: dict, TAi: dict, TTong: dict, 
    Map_Player: list, Map_AI: list, x: int = -1, y: int = -1) -> tuple[int, int]:
    pass
    '''
        Hàm tính toán minimax kết hợp với 1 loạt dữ liệu đánh giá có sẵn
        Trả về tọa độ của ô có điểm cao nhất

    '''

# --------------------------------------------------------------------------
#                   Phần khởi chạy, duy trì game
def game_loop():
    global ScorePlayer, ScoreAI, ScoreTong, T_Ai, T_player, T_Tong, MapPlayer, MapAI, banco, game_over, turn, LuotAI;
    while True:
        draw_board(); draw_XO(banco); 
        # draw_numbers()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not LuotAI:
                x_mouse, y_mouse = pygame.mouse.get_pos(); row, col = y_mouse // SQUARE_SIZE, x_mouse // SQUARE_SIZE
                if event.button == 1:
                    if banco[row][col] == '.':
                        banco[row][col] = player; Update_Pre(row, col, player)
                        RemoveT(T_player, ScorePlayer[row][col], row, col); RemoveT(T_Ai, ScoreAI[row][col], row, col); RemoveT(T_Tong, ScoreTong[row][col], row, col);
                        ScorePlayer[row][col] = "-1"; ScoreAI[row][col] = "-1"; ScoreTong[row][col] = "-1"
                        if checkWin(banco, player, row, col):
                            game_over = True; 
                            break
                        SCAN(banco, MapPlayer, player, row, col, ScorePlayer, ScoreAI, ScoreTong, T_player, T_Ai,  T_Tong);
                        SCAN(banco, MapAI, AI, row, col, ScorePlayer, ScoreAI, ScoreTong, T_player, T_Ai,  T_Tong);
                        LuotAI = True

            if LuotAI and not game_over:
                draw_board(); draw_XO(banco); # draw_numbers()
                (x, y) = AI_move()
                banco[x][y] = AI; Update_Pre(x, y, AI)
                RemoveT(T_player, ScorePlayer[x][y], x, y); RemoveT(T_Ai, ScoreAI[x][y], x, y); RemoveT(T_Tong, ScoreTong[x][y], x, y)
                ScorePlayer[x][y] = "-1"; ScoreAI[x][y] = "-1"; ScoreTong[x][y] = "-1"
                if checkWin(banco, AI, x, y):
                    game_over = True; turn = AI;
                    break
                SCAN(banco, MapPlayer, player, x, y, ScorePlayer, ScoreAI, ScoreTong, T_player, T_Ai,  T_Tong);
                SCAN(banco, MapAI, AI, x, y, ScorePlayer, ScoreAI, ScoreTong, T_player, T_Ai,  T_Tong);
                LuotAI = False;

            if event.type == KEYDOWN:
                if (event.key == K_r):
                    Init()

        if game_over:
            font = pygame.font.Font(None, 74)
            if turn == AI:
                winner_text = font.render(f'{turn} wins!', True, (255, 0, 0))
            else:
                winner_text = font.render(f'{turn} wins!', True, (0, 255, 0))
            Comment_1 = font.render('Press "R" to reset', True, (0, 0, 255))
            screen.blit(winner_text, (WINDOW_WIDTH // 2 - winner_text.get_width() // 2, WINDOW_HEIGHT // 2 - winner_text.get_height() // 2))
            screen.blit(Comment_1, (WINDOW_WIDTH // 2 - Comment_1.get_width() // 2, WINDOW_HEIGHT // 2 - Comment_1.get_height() // 2 + 50))

        pygame.display.flip()

Init();
game_loop()
# --------------------------------------------------------------------------
