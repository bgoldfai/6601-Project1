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
  print "Start:", problem.getStartState()
  
  frontier = util.Stack()
  explored = list()
  path = util.Stack()
  
  currentPosition = problem.getStartState()
  if(problem.isGoalState(currentPosition)):
    return []
  explored.append(currentPosition)
  
  for position in problem.getSuccessors(currentPosition):
    frontier.push(position)
    print "initial frontier: ", position[0]  

  while(not frontier.isEmpty()):
    
    print "At: ", currentPosition
    next = frontier.pop()
    addCurr = False
    value = next
    while(next not in problem.getSuccessors(currentPosition)):
      if path.isEmpty():
        currentPosition = problem.getStartState()
        addCurr = False
      else:
        value = path.pop()
        currentPosition = value[0]
        addCurr = True
      print "removed", currentPosition
    if addCurr:
      path.push(value)
    path.push(next)
    currentPosition = next[0]
    explored.append(currentPosition)
    
    
    if(problem.isGoalState(currentPosition)):
      print "found goal!"
      p = util.Stack()
      while(not path.isEmpty()):
         p.push(path.pop()[1])
      a = list()
      while not p.isEmpty():
        tmp = p.pop()
        print tmp
        a.append(tmp)
      return a
    
    for position in problem.getSuccessors(currentPosition):
      if(position[0] not in explored):
        frontier.push(position)
        "print position[0]"
    
  return []

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  
  currentPosition = problem.getStartState()
  if(problem.isGoalState(currentPosition)):
    return []
  
  frontier = util.Queue()
  explored = list()
  path = util.Stack()
  explored.append(currentPosition)
  
  for position in problem.getSuccessors(currentPosition):
    frontier.push(position)
    print "initial frontier: ", position[0]  

  while not frontier.isEmpty():
    
    currentPosition = frontier.pop()
    explored.append(currentPosition[0])
    print "At: ", currentPosition[0]
    path.push(currentPosition)

    for new in problem.getSuccessors(currentPosition[0]):
      if problem.isGoalState(new[0]):
        print "found goal!"
        p = util.Stack()
        p.push(currentPosition[1])
        p.push(new[1])
        current = currentPosition
        while not path.isEmpty():
          previous = current
          
          done = False
          while previous not in problem.getSuccessors(current[0]) and not done:
            if not path.isEmpty():
              current = path.pop()
            else:
              done = True
          if done:    
            print problem.getStartState()
          else:
            p.push(current[1])
            print current[1]
        
        a = list()
        while not p.isEmpty():
          tmp = p.pop()
          print tmp
          a.append(tmp)
        return a
      if new[0] not in explored:
        frontier.push(new)

  return []
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  
  currentPosition = problem.getStartState()
  if(problem.isGoalState(currentPosition)):
    return []
  
  frontier = util.PriorityQueue()
  explored = list()
  path = util.Stack()
  explored.append(currentPosition)
  
  for position in problem.getSuccessors(currentPosition):
    frontier.push(position, position[2])
    print "initial frontier: ", position[0]  

  while not frontier.isEmpty():
    
    currentPosition = frontier.pop()
    explored.append(currentPosition[0])
    
    path.push(currentPosition)

    if problem.isGoalState(currentPosition[0]):
      print "found goal!"
      p = util.Stack()
      p.push(currentPosition[1])
      current = currentPosition
      while not path.isEmpty():
        previous = current
        
        done = False
        while previous not in problem.getSuccessors(current[0]) and not done:
          print "here"
          if not path.isEmpty():
            current = path.pop()
          else:
            done = True
        if done:    
          print problem.getStartState()
        else:
          p.push(current[1])
          print current[1]
      
      a = list()
      while not p.isEmpty():
        tmp = p.pop()
        print tmp
        a.append(tmp)
      return a
    
    for new in problem.getSuccessors(currentPosition[0]):
      if new[0] not in explored:
        frontier.push(new, new[2])

  return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  
  currentPosition = problem.getStartState()
  if(problem.isGoalState(currentPosition)):
    return []
  
  frontier = util.PriorityQueue()
  explored = list()
  path = util.Stack()
  explored.append(currentPosition)
  
  for position in problem.getSuccessors(currentPosition):
    frontier.push(position, position[2]+heuristic(position[0], problem))
    print "initial frontier: ", position[0]  

  while not frontier.isEmpty():
    
    currentPosition = frontier.pop()
    explored.append(currentPosition[0])
    print "At: ", currentPosition[0]
    path.push(currentPosition)

    if problem.isGoalState(currentPosition[0]):
      print "found goal!"
      p = util.Stack()
      p.push(currentPosition[1])
      current = currentPosition
      while not path.isEmpty():
        previous = current
        
        done = False
        while previous not in problem.getSuccessors(current[0]) and not done:
          print "here"
          if not path.isEmpty():
            current = path.pop()
          else:
            done = True
        if done:    
          print problem.getStartState()
        else:
          p.push(current[1])
          print current[1]
      
      a = list()
      while not p.isEmpty():
        tmp = p.pop()
        print tmp
        a.append(tmp)
      return a
    
    for new in problem.getSuccessors(currentPosition[0]):
      if new[0] not in explored:
        frontier.push(new, new[2]+heuristic(new[0], problem))

  return []
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
