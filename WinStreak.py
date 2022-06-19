#  File: WinStreak.py

#  Description: Determines the teams with the longest win streak

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue if empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)

    def __str__(self):
        s = ''
        for i in range(len(self.queue)):
            s += self.queue[i] + ' '
        return s[:-1]


# Input: players is a list of people who are playing the game
#        winners is an ordered string of the winning teams
# Output: A list of the team(s) with the longest win streak in chronological order
#         The player who has been on the team the longest should be listed first
#         Each team is represented by a string structure as follows "Player1 Player2"
def longest_win_streak(players, winners):
    # YOUR CODE HERE
    red = Queue()
    blu = Queue()
    wait = Queue()

    #print(players)

    streaks = []
    streak_index = -1
    last = 'N'

    red.enqueue(players[0])
    blu.enqueue(players[1])
    red.enqueue(players[2])
    blu.enqueue(players[3])

    for i in range(4,len(players)):
        #print(players[i])
        wait.enqueue(players[i])
    
    for w in winners:
        if w == 'R':
            if last !='R':
                last = 'R'
                streak_index+=1
                streaks.append((red.__str__(),1))
            else: #last =='R'
                cur_streak = streaks[streak_index]
                new_streak = (cur_streak[0],cur_streak[1]+1)
                streaks[streak_index] = new_streak
            
            out = blu.dequeue()
            wait.enqueue(out)
            blu.enqueue(wait.dequeue())
        if w == 'B':
            if last !='B':
                last = 'B'
                streak_index+=1
                streaks.append((blu.__str__(),1))
            else: #last =='B'
                cur_streak = streaks[streak_index]
                new_streak = (cur_streak[0],cur_streak[1]+1)
                streaks[streak_index] = new_streak

            out = red.dequeue()
            wait.enqueue(out)
            red.enqueue(wait.dequeue())
    
    #needs to return both teams
    max = 0
    streakers = [streaks[0][0]]
    for s in range(len(streaks)):
        if streaks[s][1]>streaks[max][1]:
            max = s
            streakers = []
            streakers.append(streaks[s][0])
        elif streaks[s][1]==streaks[max][1] and s != max:
            streakers.append(streaks[s][0])

    return streakers



# DO NOT MODIFY THIS METHOD
def main():
    # read number of players
    n = int(input())

    players = list(map(str, input().split()))
    # read data from standard input
    winners = input()

    # get the result from your call to flip_matrix()
    teams = longest_win_streak(players, winners)

    # print the result to standard output
    for team in teams:
        print(team)


if __name__ == "__main__":
    main()
