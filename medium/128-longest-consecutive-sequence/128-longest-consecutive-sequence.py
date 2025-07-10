                length=1
                while current+1 in num_set:
                    current+=1
                    length+=1
                longest=max(longest,length)
                current= i
        return longest
        
        