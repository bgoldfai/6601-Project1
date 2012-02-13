# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  print "ahahaha"
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  start = [problem.getStartState()]
  seenpositions = []
  currentpositions = [start]
  allLocs=[]
  found=False
  goalLoc=[]
  while currentpositions and not found:
    nextpositions = []
    for p in currentpositions:
      #print "next:"+str(nextpositions)
      #print "Current:"+str(currentpositions)
      #print "p:"+str(p)
      visited=p[0]
      seenpositions.append(visited)
      #print "Visited:"+str(visited)
      #print "Seen:"+str(seenpositions)
      succ = problem.getSuccessors(visited)
      #print "succ:"+str(succ)
      for np in succ:
        #print np[0]
        if np[0] in seenpositions: 
          continue
        if problem.isGoalState(np[0]) is True:
          #print "FoundSolution"+str(np)
          found=True
          goalLoc=np[0]
          cur = [list(np),visited]
          allLocs.append(cur)
          break
        #print "haha"
        nextpositions.append(np)
        cur = [list(np),visited]
        allLocs.append(cur)
    currentpositions = nextpositions
  moves=[]
  k=0
  if not found:
    print "No solution exists"
  else:
    #cur=allLocs.pop()
    while allLocs:
      cur=allLocs.pop()
      if cur[0][0] == goalLoc:
        #print cur
        if cur[0][1][0]=='W':
          moves.append(w)
        if cur[0][1][0]=='E':
          moves.append(e)
        if cur[0][1][0]=='N':
          moves.append(n)
        if cur[0][1][0]=='S':
          moves.append(s)
        break
    while allLocs:
      prev=allLocs.pop()
      #	print prev
      if cur[1]==prev[0][0]:
        cur=prev
        if prev[0][1][0]=='W':
          moves.append(w)
        if prev[0][1][0]=='E':
          moves.append(e)
        if prev[0][1][0]=='N':
          moves.append(n)
        if prev[0][1][0]=='S':
          moves.append(s)
        #print prev
  move=list(moves)
  move.reverse()
  print str(move)
  return move
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
