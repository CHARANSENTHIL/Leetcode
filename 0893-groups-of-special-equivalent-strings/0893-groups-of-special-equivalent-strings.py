class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
                                                            #  Example: 
        wSet = set()                                        #   words = ["abc","acb","bac","bca","cab","cba"]

        for word in words:                                  #           sorted((enu-   
            word = tuple(sorted((enumerate(word)),          #  word     merate word)         wSet
                           key = lambda x: (x[0]%2,x[1])))  #  –––––    ––––––––––––         ––––––––––––––
                                                            #   abc     ((0,a),(2,c),(1,b))  {(a,c,b)}
            wSet.add(list(zip(*word))[1])                   #   acb     ((0,a),(2,b),(1,c))  {(a,c,b), (a,b,c)}
                                                            #   bac     ((0,b),(2,c),(1,a))  {(a,c,b), (a,b,c), (b,c,a)}
        return len(wSet)                                    #   bca     ((2,a),(0,b),(1,c))  {(a,c,b), (a,b,c), (b,c,a)}
                                                            #   cab     ((2,b),(0,c),(1,a))  {(a,c,b), (a,b,c), (b,c,a)}
                                                            #   cba     ((2,a),(0,c),(1,b))  {(a,c,b), (a,b,c), (b,c,a)}