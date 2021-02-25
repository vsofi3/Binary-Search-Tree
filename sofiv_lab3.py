"""
Lab 3
Author: Sofi Vinas
Date: 21 February 2021
Description: BST Implementation
Notes:
    1) Created a helper function _find to return the node with the desired ticketID
    2) Other functions implemented with the help of Jared Hall's pseudocode from office hours
"""
from mealticket import *

#============================== Aux Classes ====================================
class Sentinel():
    """This class builds the Sentinel nodes"""

    def __init__(self):
        """The constructor for the Sentinel class"""
        self._key = None
        self._value = None
        self._leftChild = None
        self._rightChild = None
        self._parent = None

    def isSentinel(self):
        """ This method makes it easy to check if a given node is a Sentinel"""
        return True

class Node():
    """ This class implements a node for the BST. """
    def __init__(self, ticket):
        """
        Description: The constructor for the Node class.
        Inputs: A valid MealTicket (input validation should be done by insert)
        """
        self._parent = Sentinel() #was Sentinel()
        self._leftChild = Sentinel()
        self._rightChild = Sentinel()
        self._value = ticket
        self._key = ticket.ticketID

    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        returnValue = "Node: {}\n".format(self._key)
        returnValue += "Parent: {}\n".format(self._parent._key)
        returnValue += "Left Child: {}\n".format(self._leftChild._key)
        returnValue += "Right Child: {}\n".format(self._rightChild._key)
        return returnValue

    def isSentinel(self):
        """ A helper method for figureing out if a node is a Sentinel """
        return False

    #Accessor Methods
    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        """
        return self._parent

    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        """
        return self._rightChild

    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        """
        return self._leftChild

    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the MealTicket.
        """
        return self._value

    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Input: A Node() reference.
        """
        self._parent = node

    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Input: A Node() reference.
        """
        self._leftChild = node

    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Input: A Node() reference.
        """
        self._rightChild = node

    #comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                     nodes. Now we can do node1 > node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key > other._key
        return returnValue

    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                     nodes. Now we can do node1 < node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key < other._key
        return returnValue

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes. Now we can do node1 == node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key == other._key
        return returnValue

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes. Now we can do node1 != node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key != other._key
        return returnValue

    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                     nodes. Now we can do node1 <= node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key <= other._key
        return returnValue

    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                     nodes. Now we can do node1 >= node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key >= other._key
        return returnValue

    #Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This method returns true if the current node
                     has a left child
        """
        returnValue = False
        cond1 = not self._leftChild.isSentinel()
        cond2 = self._leftChild._parent is self
        if(cond1 and cond2):
                returnValue = True
        return returnValue

    def hasRightChild(self):
        """ This method returns true|false depending on if the current
            node has a right child or not."""
        returnValue = False
        cond1 = not self._rightChild.isSentinel()
        cond2 = self._rightChild._parent is self
        if(cond1 and cond2):
                returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """ Returns True if the current node has only one child."""
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)

    def hasBothChildren(self):
        """ Returns True if the current node has both children"""
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """ Returns true if the current node is a leaf node."""
        returnValue = False
        if(self._rightChild.isSentinel() and self._leftChild.isSentinel()):
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """Returns true if the current node is a left child"""
        cond1 = not self._parent.isSentinel()
        cond2 = self._parent._leftChild is self
        cond3 = self._parent._rightChild is not self
        return cond1 and cond2 and cond3

    def isRightChild(self):
        """Returns true if the current node is a right child"""
        cond1 = not self._parent.isSentinel()
        cond2 = self._parent._rightChild is self
        cond3 = self._parent._leftChild is not self
        return cond1 and cond2 and cond3

    def isRoot(self):
        """ Returns true if the current node is the root"""
        return self._parent.isSentinel()
#===============================================================================

#================================ BST Class ====================================
class BinarySearchTree:
    """
    Description: A Binary Search Tree (BST).
    Note: Algorithms for the BST can be found in ch. 12 of the book.
    """

    def __init__(self):
        """ The constructor for our BST """
        self._root = Sentinel()
        #Add any other instance variables you need.
        self._currentSize = 0

    def _isValid(self, ticket):
        """
        Description: A method for checking if the given ticket is a valid
                     mealticket.
        Inputs: Some object in the variable ticket.
        Outputs: Boolean (True|False) depending on if it is a valid mealticket.
        """
        return type(ticket) == MealTicket

    def _findMinimum(self, node):
        """
        Description: Finds the minimum child of a tree when given a node.
        Inputs: A node from the BST.
        Outputs: The minumum node from the sub-tree (e.g the left-most child).
        """
        returnValue = False
        if not node.isSentinel():
            returnValue = node
            while not returnValue._leftChild.isSentinel():
                returnValue = returnValue._leftChild
        return returnValue

    def _findSuccessor(self, node):
        """
        Description: Given a node, returns the successor of that node,
                     or False if there is no successor.
        """
        successor = False
        # if node has a right child
        if(node.hasRightChild()):
            # then successor is the min of the right subtree
            successor = self._findMinimum(node._rightChild)
        elif(node._parent): # node has no right child, but has a parent
            if(node.isLeftChild()): # node is a left child
                successor = node._leftChild._parent #self._parent # then succ is the parent
            else: # node is right child, and has not right child
                successor = node._parent
                while not successor._parent.isSentinel() and node.isRightChild():
                    node = successor
                    successor = successor._parent
        return successor

    def _transplant(self, uNode, vNode):
        """
        Description: Replaces subtree at uNode with subtree at vNode.
        Note: See pg. 296 for description of the transplant routine.
        """
        if uNode == self._root:
            self._root = vNode
            uNode._leftChild = None
            uNode._rightChild = None
        elif uNode.isLeftChild():
            uNode._parent._leftChild = vNode
        else:
            uNode._parent._rightChild = vNode
        if vNode != None:
            vNode._parent = uNode._parent

    def _transplantR(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getRChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def _transplantL(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getLChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)


    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                     of the tree according to the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "  "
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if(not node.isSentinel()):
            self.inorder(node.getLChild())
            self.output += str(node._key) + ", "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(not node.isSentinel()):
            self.output += str(node._key) + ", "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if(not node.isSentinel()):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            self.output += str(node._key) + ", "

    def insert(self, ticket):
        """
        Description: Inserts given MealTicket into the tree while
                     preserving binary tree property.
                     Returns True if successful, False otherwise
        """
        ret = False
        if self._isValid(ticket): #check for valid ticket
            ret = True #if that passes, set ret to True
            node = Node(ticket) #create a node with the MealTicket
            root = self._root #create a variable for the root

            if root.isSentinel():
                self._root = node

            else:
                while ret: #while True
                    if root._key < node._key:
                        if root.hasRightChild(): #if it has rightChild
                            root = root._rightChild  #set the root to rightChild
                        else:
                            node.setParent(root)
                            root.setRChild(node)
                            break
                    else:
                        if root.hasLeftChild():
                            root = root._leftChild
                        else:
                            node.setParent(root)
                            root.setLChild(node)
                            break
        return ret


    def delete(self, ticketID):
        """
        Description: Deletes node from tree with given ticketID;
                     restructures binary tree. Returns True if successful,
                     False otherwise
        """
        ret = False
        if(type(ticketID) is int and ticketID > 0): #ONLY CONTINUE ON VALID INPUT
            node = self._find(ticketID) #_find returns a node with that ticketID
            if node is False: #node with THAT ticketID does not exist
                return False
            else:
                ret = True

            if node.isLeaf(): #if it has no children, its a leaf
                parent = node._parent #get the parent of current node

                if node is self._root: #if it is at the root
                    self._root = Sentinel() #set root to sentinel
                elif (node is not self._root) and node.isLeftChild():
                    parent.setLChild(Sentinel()) #set parent LC to sentinel
                elif (node is not self._root) and node.isRightChild():
                    parent.setRChild(Sentinel()) #set parent RC to sentinel

            if node.hasOnlyOneChild(): #CASE 2: IF current has only one child
                if node.hasLeftChild(): #if it has left child
                    if node is self._root: #subcase
                        self._root = node._leftChild #set root to current.leftChild
                    else: #if NOT ROOT
                        self._transplantL(node) #transplantL(current node)
                if node.hasRightChild(): #if it has right child
                    if node is self._root: #if the current node if the root
                        self._root = node._rightChild #set root to current.rightChild
                    else: #otherwise
                        self._transplantR(node) #transplatR(current node)

            #SWAP
            if node.hasBothChildren(): #if it has both children
                successor = self._findSuccessor(node) #find the successor
                self.delete(successor._key) #delete the successor with the key (recursive call)
                temporary = node._key #set up two temporary variables
                temporary2 = node._value

                node._key = successor._key #do the swapping
                successor._key = temporary
                node._value = successor._value
                successor._value = temporary2

        return ret


    def find(self, ticketID):
        """
        Description: Finds node in tree with given ticketID,
                     returns corresponding ticket. Returns False if unsuccessful.
        """
        """
        ret = False
        if type(ticketID) is int and ticketID > 0:
            rootPtr = self._root

            if rootPtr.isSentinel():
                pass
            else:
                while True:
                    if (ticketID is not rootPtr._key) and rootPtr.isLeaf():
                        break
                    elif ticketID is rootPtr._key:
                        ret = rootPtr.getValue()
                        break
                    else:
                        ret = False
                        if rootPtr._key < ticketID:
                            if rootPtr.hasRightChild():
                                rootPtr = rootPtr._rightChild
                            else:
                                break
        return ret
        """
        answer = False
        if type(ticketID) is int and ticketID > 0: #is valid ticketID
            current = self._root #grab the root of the tree
            while True: #LOOP
                if current._key == ticketID: #CASE 1
                    answer = current._value #CHANGE ANSWER VARIABLE TO TRUE
                    break
                if current.isSentinel(): #CASE 2
                    break #answer = False remains
                if ticketID < current._key: #if the ticketID is less than the key, we know its the leftChild
                    if current.hasLeftChild():
                        current = current._leftChild #update current variable
                    else:
                        break
                if ticketID > current._key: #if the ticketID is less than the key, we know its the rightChild
                    if current.hasRightChild():
                        current = current._rightChild #update current variable
                    else:
                        break
        return answer



    def _find(self, ticketID):
        """Almost exactly the same as the above function, but returns a
        node instead of corresponding ticket. False otherwise"""
        ret = False
        if type(ticketID) is int and ticketID > 0:
            current = self._root #current equal to root
            while True:
                if current._key == ticketID:
                    ret = current #THIS IS THE ONLY LINE THAT CHANGES
                    break
                if current.isSentinel():
                    break
                if ticketID < current._key:
                    if current.hasLeftChild(): #check for left
                        current = current._leftChild
                    else:
                        break
                if ticketID > current._key:
                    if current.hasRightChild():
                        current = current._rightChild
                    else:
                        break
        return ret

