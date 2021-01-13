  def solution(args):
      next_n=-1000
      start = 0
      even = 0
      next_even = 0
      t = []
      for key in args:
         #print("start", start,"next: ", next_n, "key" ,key)
         if int(next_n) < int(key) :
            if even < int(key):
              if start+1 == even:
                 t.append(str(start))
                 t.append(str(even))
              else:  
                 t.append(str(start)+"-"+str(even))
              start = key  
            else:  
              if start!=0:
                t.append(str(start))
              start = key 
            next_n = key+1  
         if int(next_n) == int(key):
             print("start", start,"igual next: ", next_n, "key" ,key)
             even = key
             next_n = key+1  

         print(start, next_n-1)    

      print(t) 
