scores = [ ("Emma", 89 , 90 , 59),
      ("Edith", 99 , 49 , 59),
      ("Sophia", 99 , 60 , 20),
      ("May", 40 , 94 , 59),
      ("Ashley", 89 , 90 , 59),
      ("Arny", 89 , 90, 69),
      ("Lucy", 79 , 90 , 59 ),
      ("Gloria", 85 , 90 , 59),
      ("Abby", 89 , 91 , 90)]
def handle_filter(a):
    s = sorted(a[1: ]) #对三科成绩进行排序
    #有 2 科成绩在 80 分以上，并且有 1 科在 60 分以下的
    if s[-2] > 80 and s[0] < 60 :
        return True
    #有 1 科成绩在 90 分以上，另外 2 科成绩都在 60 分以下
    if s[-1] > 90 and s[1] < 60 :
        return True
    if s[-2] > 80 and sum(s)/len(s) < 60:
        #有 1 科成绩在 90 分以上， 且 3 科的平均分在 70 分以下
        return True
    return False
newIter = list(filter(handle_filter, scores))
print(newIter)