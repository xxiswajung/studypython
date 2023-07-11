def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        skill_list=list(skill) 
        #이름을 다르게 해서 리스트를 새로 만드는 이유
        #만약 이름을 안 바꾸고 그대로 하면, 아래의 pop() 실행이 될때 원래 매개변수로 주어졌던 skill이 비어버려 더이상 문자 비교를 할 수 없기 때문에
        #주어진 매개변수 skill은 유지하고, 새로 똑같은 내용의 리스트를 만드는 것.
        
        for y in skills:
            if y in skill_list:
                if y!=skill_list.pop(0):
                    break
        else:
            answer+=1   
    return answer
