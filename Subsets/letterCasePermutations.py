class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        st=[]
        res=[]

        def backtrack(i):
            if len(s)==len(st):
                res.append("".join(st))
                return
            
            if s[i].isnumeric():
                st.append(s[i])
                backtrack(i+1)
                st.pop()
            elif s[i].isupper():
                st.append(s[i])
                backtrack(i+1)
                st.pop()
                st.append(s[i].lower())
                backtrack(i+1)
                st.pop()
            else:
                st.append(s[i])
                backtrack(i+1)
                st.pop()
                st.append(s[i].upper())
                backtrack(i+1)
                st.pop()
        backtrack(0)
        return res            


        
