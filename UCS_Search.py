'''
@author: Parth Patel
'''
from State import State
from Node import Node
import queue
from TreePlot import TreePlot
    

def UcsSearch():
    """
    This method performs A* search
    """
    
    #create queue
    pqueue = queue.PriorityQueue()
    
    #create root node
    initialState = State()
    root = Node(initialState, None)
    
    #show the search tree explored so far
    #treeplot = TreePlot()
    #treeplot.generateDiagram(root, root)
    
    #add to priority queue
    pqueue.put((root.heuristic, root))
    
    #check if there is something in priority queue to dequeue
    while not pqueue.empty(): 
        
        #dequeue nodes from the priority Queue
        _, currentNode = pqueue.get()
        
        #remove from the fringe
        currentNode.fringe = False
        
        #check if it has goal State
        print ("-- dequeue --", currentNode.state.place)
        
        #check if this is goal state
        if currentNode.state.checkGoalState():
            print ("reached goal state")
            #print the path
            print ("----------------------")
            print ("Path")
            currentNode.printPath()
            
            #show the search tree explored so far
            #treeplot = TreePlot()
            #treeplot.generateDiagram(root, currentNode)
            break
            
        #get the child nodes 
        childStates = currentNode.state.successorFunction()
        # to remove parent
        if currentNode.depth !=0 and currentNode.parent.state.place in childStates:
            childStates.remove(currentNode.parent.state.place)


        for childState in childStates:
            
            childNode = Node(State(childState), currentNode)
            
            #add to tree and queue
            pqueue.put((childNode.heuristic, childNode))
            
        #show the search tree explored so far
        treeplot = TreePlot()
        treeplot.generateDiagram(root, currentNode)
        
                
    #print tree
    print ("----------------------")
    print ("Tree")
    root.printTree()
    
UcsSearch()