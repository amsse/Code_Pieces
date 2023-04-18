'''
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings.
Each match is represented by a string in the format "x:y", where
x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns
the number of points our team (x) got in the championship by the
rules given above.

'''

def points(games):
    count = 0
    for score in games:
        res = score.split(':')  # formats the scorecard
        if res[0]>res[1]:  # win
            count += 3
        elif res[0] == res[1]:  # draw
            count += 1
    return count

# test
#games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
#points(games)


'''

def points(games):
    result = 0
    for item in games:
	    result += 3 if item[0] > item[2] else 0     
	    result += 1 if item[0] == item[2] else 0
    return result
    
'''


############### ONE LINER ################
#
#
#    def points(a):
#        return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))
#
#
##########################################