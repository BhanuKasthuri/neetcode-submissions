class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:


        
        for i in range(len(arr)):

            if i == (len(arr) - 1):
                arr[i]=-1
            else:
                max_num = arr[i+1]
            for j in range(i+1,len(arr)):
              
                if arr[j] > max_num:
                    max_num = arr[j]
              
                


            
            if i == (len(arr) - 1):
                arr[i]=-1
            else:
                arr[i] = max_num
            

        return arr
                    

                
        