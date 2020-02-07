# Wordsearch

## Question
Given a 2D board and a word, find if the word exists in the grid.
 
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are thosehorizontally or vertically neighboring. The same letter cell may not be usedmore than once.
 
For example,
Given board =
 
[
 ['A','B','C','E'],
 ['S','F','C','S'],
 ['A','D','E','E']
]
word = "ABCCED", -> returnstrue,
word = "SEE", -> returns true,
word = "ABCB", -> returnsfalse.

## Procedures
 1. Find the first character in the grid, we call it searching node(the node which searches from).
 
 2. Search the up,down,right,left side of this searching node to match next word
 
 3. If there is a match, set the current searching node as unaccessible and set the matched node as the new searching node, then jump to step 2.
    If there is not a match, return false
    
 ## Some notes
 1. You can set the matched node as irrelevant symbol or word to make it unaccessible like "$"
 
 2. You can add a round of '0' outside the grid like this, then you can ignore the problem of "index out of range". or you can set the limitation of each direction.


                       
    
  
