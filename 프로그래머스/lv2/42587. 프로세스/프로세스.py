def solution(priorities, location):
    answer = 0
    while priorities:
        if location==0:
            for i in range(1,len(priorities)): 
                if priorities[0]<priorities[i]:
                    priorities.append(priorities[0])
                    priorities.pop(0)
                    location=len(priorities)-1
                    break
            else:
                answer+=1
                return answer
        else:
            for i in range(1,len(priorities)):
                if priorities[0]<priorities[i]:
                    priorities.append(priorities[0])
                    priorities.pop(0)
                    break
            else:
                priorities.pop(0)
                answer+=1
            location-=1

######################################

def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)] #Use 'enumearte' instead of moving location manually(=location-=1, location=len(priorities)-1)
    while True:
        cur=queue.pop(0)
        if any(cur[1]<q[1] for q in queue): #Use 'any' instead of 'for' loop.
            queue.append(cur)
        else:
            answer+=1
            if cur[0]==location:
                return answer
            
                    
