
# --------------------------------------------------------------------------
#           Phần Áp dụng giải thuật MiniMax
diemABC = {"A": 100000, "B": 10000, "C": 1000, "D": 100, "E": 10, "F": 0}
def DiemBanCo(Tudien):
    # Tổng điểm của Bàn cờ là tổng điểm của tất cả các giá trị đã đánh giá trong danh sách
    e = 0; 
    for key in Tudien:
        diem_key = 0
        for j in key: # j: A B C D E F 
            diem_key += diemABC[j]
        e += diem_key*len(Tudien[key])
    return e

def minimax(Board, isMaximizing, depth, alpha, beta, Score_Player, Score_AI, Score_Tong, Tplayer, TAi, TTong, Map_Player, Map_AI, x = -1, y = -1):
    
    if depth == 0:
        if isMaximizing:
            T_tancong = T_player; T_phongthu = TAi
        else:
            T_tancong = TAi; T_phongthu = T_player
        result = DiemBanCo(T_tancong) - DiemBanCo(T_phongthu)
        return result, None

    # -------------------------------------------------------------------------------------
    # Khối lấy ra N_o giá trị có "điểm đánh giá" cao nhất <=> nước đi khả thi nhất
    N_o = 5
    list_Best = []
    T = list(TTong.keys()); T.sort()
    for i in T:
        if i[0] == "A" or i[0] == "B":
            list_Best = TTong[i]
            break
        list_Best += TTong[i]
        if len(list_Best) > N_o:
            break
    list_Best = list_Best[:N_o]
    # -------------------------------------------------------------------------------------

    if isMaximizing:
        maxVal = float('-inf');
        best_move = list_Best[0]
        for (x, y) in list_Best:
            Board[x][y] = AI;
            if checkWin(Board, AI, x, y):
                Val = 10000000
                Board[x][y] = "."
                maxVal = max(Val, maxVal); best_move = (x, y)
                break
            # -------------------------------------------------------------------------------------
            # Khối cập nhật, duy trì "data đánh giá"
            Board1 = Board.copy();  
            Score_Player1 = copy.deepcopy(Score_Player); Score_AI1 = copy.deepcopy(Score_AI); Score_Tong1 = copy.deepcopy(Score_Tong); Tplayer1 = copy.deepcopy(Tplayer); TAi1 = copy.deepcopy(TAi); TTong1 = copy.deepcopy(TTong); Map_Player1 = copy.deepcopy(Map_Player); Map_AI1 = copy.deepcopy(Map_AI);
            RemoveT(Tplayer1, Score_Player1[x][y], x, y); RemoveT(TAi1, Score_AI1[x][y], x, y); RemoveT(TTong1, Score_Tong1[x][y], x, y)
            SCAN(Board1, Map_Player1, player, x, y, Score_Player1, Score_AI1, Score_Tong1, Tplayer1, TAi1,  TTong1);
            SCAN(Board1, Map_AI1, AI, x, y, Score_Player1, Score_AI1, Score_Tong1, Tplayer1, TAi1,  TTong1);
            # -------------------------------------------------------------------------------------
            Val, move = minimax(Board1, False, depth-1, alpha, beta, Score_Player1, Score_AI1, Score_Tong1, Tplayer1, TAi1, TTong1, Map_Player1, Map_AI1, x, y)
            Board[x][y] = "."

            if Val > maxVal:
                maxVal = Val; best_move = (x, y)
            
            alpha = max(alpha, Val)
            if beta <= alpha:
                break

        return maxVal, best_move

    else:
        minVal = float('inf');
        best_move = list_Best[0]
        for (x, y) in list_Best:
            Board[x][y] = player;
            if checkWin(Board, player, x, y):
                Val = -10000000
                Board[x][y] = "."
                minVal = min(Val, maxVal); best_move = (x, y)
                break
            # -------------------------------------------------------------------------------------
            # Khối cập nhật, duy trì "data đánh giá"
            Board1 = Board.copy();  
            Score_Player1 = copy.deepcopy(Score_Player); Score_AI1 = copy.deepcopy(Score_AI); Score_Tong1 = copy.deepcopy(Score_Tong); Tplayer1 = copy.deepcopy(Tplayer); TAi1 = copy.deepcopy(TAi); TTong1 = copy.deepcopy(TTong); Map_Player1 = copy.deepcopy(Map_Player); Map_AI1 = copy.deepcopy(Map_AI);
            RemoveT(Tplayer1, Score_Player1[x][y], x, y); RemoveT(TAi1, Score_AI1[x][y], x, y); RemoveT(TTong1, Score_Tong1[x][y], x, y)
            SCAN(Board1, Map_Player1, player, x, y, Score_Player1, Score_AI1, Score_Tong1, Tplayer1, TAi1,  TTong1);
            SCAN(Board1, Map_AI1, AI, x, y, Score_Player1, Score_AI1, Score_Tong1, Tplayer1, TAi1,  TTong1);
            # -------------------------------------------------------------------------------------
            Val, move = minimax(Board1, True, depth-1, alpha, beta, Score_Player1, Score_AI1, Score_Tong1, Tplayer1, TAi1, TTong1, Map_Player1, Map_AI1, x, y)
            
            Board[x][y] = "."

            if Val < minVal:
                minVal = Val; best_move = (x, y)

            beta = min(beta, Val)
            if beta <= alpha:
                break

        return minVal, best_move

def UuTien_move(T_Ai, T_player):
    c = ""; d = ""
    for a in T_Ai:
        if a[0] == "A":        # Thắng "ngay" được THÌ thắng luôn
            return T_Ai[a][0] 
        if a[0] == "B":
            c = a     
    # Nếu không thắng được luôn:        
    for b in T_player:                 
        if b[0] == "A":        # Chặn nước thắng "ngay" của player             
            return T_player[b][0]
    # Nếu đối thủ không thắng ngay được: 
    if c != "":                # Tạo nước thắng "ở lượt sau" được thì tạo luôn
        return T_Ai[c][0]
    return (-1, -1)

def AI_move():
    (x, y) = UuTien_move(T_Ai, T_player)
    if (x, y) != (-1, -1):
        return (x, y)

    Board = banco.copy(); 
    # deepcopy rất rất nhiều "data"
    Score_Player = copy.deepcopy(ScorePlayer); Score_AI = copy.deepcopy(ScoreAI); Score_Tong = copy.deepcopy(ScoreTong); Tplayer = copy.deepcopy(T_player); TAi = copy.deepcopy(T_Ai); TTong = copy.deepcopy(T_Tong); Map_Player = copy.deepcopy(MapPlayer); Map_AI = copy.deepcopy(MapAI);
    
    best_score, best_move = minimax(Board, True, 3,  float('-inf'), float('inf'), Score_Player, Score_AI, Score_Tong, Tplayer, TAi, TTong, Map_Player, Map_AI)
    #print(best_score, flush = True)
    return best_move
# --------------------------------------------------------------------------
