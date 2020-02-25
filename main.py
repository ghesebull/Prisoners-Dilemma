from player import Player

p1 = Player(False)
p2 = Player(True)

def printTable():
    print('+-----------+-----------+-----------+')
    print('| P1  \  P2 | Cooperate |   Defect  |')
    print('+-----------+-----------+-----------+')
    print('| Cooperate | 1   \   1 | 0   \   3 |')
    print('+-----------+-----------+-----------+')
    print('|   Defect  | 3   \   0 | 2   \   2 |')
    print('+-----------+-----------+-----------+')
    print()

def printPoints():
    moves = ['C' if x == 0 else 'D' for x in p1.moves[-10:]]
    scores = [0]
    [scores.append(str(int(scores[-1]) + x)) for x in p1.points]
    scores.pop(0)
    scores = scores[-10:]
    print('+----+' + ''.join('-{}-+'.format('-' * len(str(x))) for x in scores))
    print('| P1 | ' + ' | '.join('{}{}'.format(moves[i], ' ' * (len(str(scores[i])) - 1)) for i in range(len(moves))) + ' |')
    print('+----+' + ''.join('-{}-+'.format('-' * len(str(x))) for x in scores))
    print('|    | ' + ' | '.join(scores) + ' |')
    print('+----+' + ''.join('-{}-+'.format('-' * len(str(x))) for x in scores))


    moves = ['C' if x == 0 else 'D' for x in p2.moves[-10:]]
    scores = [0]
    [scores.append(str(int(scores[-1]) + x)) for x in p2.points]
    scores.pop(0)
    scores = scores[-10:]
    print('+----+' + ''.join('-{}-+'.format('-' * len(str(x))) for x in scores))
    print('| P2 | ' + ' | '.join('{}{}'.format(moves[i], ' ' * (len(str(scores[i])) - 1)) for i in range(len(moves))) + ' |')
    print('+----+' + ''.join('-{}-+'.format('-' * len(str(x))) for x in scores))
    print('|    | ' + ' | '.join(scores) + ' |')
    print('+----+' + ''.join('-{}-+'.format('-' * len(str(x))) for x in scores))

printTable()

while (True):
    p1.makeMove()
    p2.makeMove()
    p1.addPoint(p2)
    p2.addPoint(p1)
    print()
    printTable()
    print('p1 moves: ', p1.moves[-10:])
    print('p1 points: ', p1.points[-10:])
    print('p2 moves: ', p2.moves[-10:])
    print('p2 points: ', p2.points[-10:])
    printPoints()
