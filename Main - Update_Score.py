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

def Init() -> None:
    pass
    '''
        Hàm khởi tạo giá trị ban đầu của tất cả Biến toàn cục
        Được sử dụng ghi chương trình chạy lần đầu tiên
        Và khi người chơi muốn reset bàn cờ
    
    '''

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
    if turn == player:
        matrix = ScorePlayer; T_matrix = T_player
    else: 
        matrix = ScoreAI; T_matrix = T_Ai

    if (dx, dy) in [ (1, 0), (1, -1), (0, -1), (-1, -1) ]:
        xau = Map[x][y][Direc[(dx, dy)]] + "X" + Map[x][y][Direc[(-dx, -dy)]]   
    elif (dx, dy) in [ (-1, 0),(-1, 1),  (0, 1), ( 1, 1 ) ]:
        xau = Map[x][y][Direc[(-dx, -dy)]] +  "X" + Map[x][y][Direc[(dx, dy)]]
    k = Direc[(dx, dy)]
    if k > 4:
        k -= 4
    Map[x][y][8 + k] = TH[xau]

    oldScore = matrix[x][y]
    m = [Map[x][y][9],Map[x][y][10],Map[x][y][11],Map[x][y][12]]; m.sort();
    if m[0] == m[1] == "C":
        m[0] = "B"
    elif m[0] == m[1] == "D":
        m[0] = "C"

    Map[x][y][0] = "".join(m)

    newScore = Map[x][y][0];
    RemoveT(T_matrix, matrix[x][y], x, y); matrix[x][y] = newScore; AddT(T_matrix, matrix[x][y], x, y)
    
    RemoveT(T_Tong, ScoreTong[x][y], x, y);
    tong = ScorePlayer[x][y] + ScoreAI[x][y]; tong = list(tong); tong.sort(); ScoreTong[x][y] = "".join(tong[:4])
    AddT(T_Tong, ScoreTong[x][y], x, y);
    

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

def game_loop():
    pass
    '''
        Phần giao diện pygame
        Sử dụng các hàm trên, gọi các hàm, trả kết quả lên màn hình game
    '''