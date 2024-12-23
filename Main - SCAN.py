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

def SCAN(banco: list, Map: list, turn: str, x: int, y: int, ScorePlayer: list, ScoreAI: list, ScoreTong: list, T_player: dict, T_Ai: dict, T_Tong: dict) -> None:
    pass
    '''
        Hàm Quét các ô trống bị ảnh hưởng khi thực hiện 1 nước cờ
        Truyền tọa độ các ô trống đó và "hướng ảnh hưởng"
        vào Update_Map

    '''
    global directions;
    for dx, dy in directions:
        h = []; trang = 1; i = 1
        while True:
            new_x = x + dx * i; new_y = y + dy * i
            if 0 <= new_x < nxn and 0 <= new_y < nxn:
                giatri = banco[new_x][new_y]
                if giatri == turn:
                    if trang == 1:
                        trang = 0
                if giatri == ".":
                    trang -= 1;
                    Update_Map(banco, Map, turn, new_x, new_y, -dx, -dy, ScorePlayer, ScoreAI, ScoreTong, T_player, T_Ai,  T_Tong)
                    if trang == -1:
                        break
                if giatri != turn and giatri != ".":
                    break
            else:
                break
            i += 1
    
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

def game_loop():
    pass
    '''
        Phần giao diện pygame
        Sử dụng các hàm trên, gọi các hàm, trả kết quả lên màn hình game
    '''