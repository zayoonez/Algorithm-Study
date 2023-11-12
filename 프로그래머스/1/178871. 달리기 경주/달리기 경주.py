def solution(players, callings):
    rankDict = {player : i for i, player in enumerate(players)}

    for call in callings :
        # players를 바꿔조야되니까
        # call의 지금 rank
        rank = rankDict[call] #3
        # kai, poe 자리 변경 / kai 3 poe 2 <-> kai2 poe3
        
        rankDict[players[rank-1]] = rank
        rankDict[players[rank]] = rank-1
        
        players[rank], players[rank-1] = players[rank-1], players[rank]
        
        
    return players