
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
 
        l=[x for x in s]
        n=len(l)
        c=[]
        f=[]
        d=[]
        if len(l)==1:
          return(1)
        elif len(l)==0:
          return(0)
        else: 
          for i in range(n):
            for j in range(i,n):
              if l[j] in d:
                c.append(''.join(d))
                d=[]
              elif j==(n-1):
                d.append(l[j])
                c.append(''.join(d))
                d=[]
              else:
                d.append(l[j])
            f.append(max(c, key=len))
          return(len(max(f,key=len)))
          
          
          
##alternative

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
 
        l=[x for x in s]
        n=len(l)
        c=[]
        d=[]
        if len(l)==1:
          return(1)
        elif len(l)==0:
          return(0)
        else: 
          while j<n:
             if l[j] in d:
               c.append(''.join(d))
               p=d.index(l[j])
               j=j+1-(len(d)-p)
               d=[]
             elif j==(n-1):
               d.append(l[j])
               c.append(''.join(d))
               d=[]
             else:
               d.append(l[j])
             j=j+1
           return(len(max(c,key=len)))