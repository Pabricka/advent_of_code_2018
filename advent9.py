from collections import deque, defaultdict


def winner_score(players, marbles):

    player_scores = [0 for i in range(players)]

    circle = [0, 2, 1, 3]
    current_marble_index = 3

    for turn in range(4, marbles):
        if turn % 23 == 0:
            player_scores[turn % players-1] += turn
            if current_marble_index >= 7:
                player_scores[turn % players-1] += circle.pop(current_marble_index-7)
                current_marble_index = current_marble_index-7
            elif current_marble_index < 6:
                player_scores[turn % players-1] += circle.pop(len(circle) + current_marble_index-7)
                current_marble_index = len(circle) + current_marble_index-6
            else:
                player_scores[turn % players-1] += circle.pop(len(circle))
                current_marble_index = 0
        else:
            if current_marble_index + 2 > len(circle):
                if current_marble_index == len(circle):
                    circle.insert(0, turn)
                    current_marble_index = 0
                else:
                    circle.insert(1, turn)
                    current_marble_index = 1
            else:
                circle.insert(current_marble_index+2, turn)
                current_marble_index += 2
    print("highest score: " + str(max(player_scores)))
    return max(player_scores)


def winner_score_optimized(players,marbles):

    player_scores = [0 for i in range(players)]
    circle = deque([0])

    for marble in range(1, marbles + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            player_scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    print(max(player_scores))
    return max(player_scores)


f = open("input9.txt", "r")
line = f.readline()
f.close()

p = int(line.split(" ")[0])
m = int(line.split(" ")[6])

print(line)
winner_score(p, m)
print("with 100x more marbles!")
winner_score_optimized(p, m*100)

