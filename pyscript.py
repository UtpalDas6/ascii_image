#career roadmap visualizer
exp = dict()
id = 0
arrow = '\n<' + '-'*20+'\\'+'\n'+'/' + '-'*20+'/'+'\n'+'\\' + '-'*20+':\n'
print(arrow)
while True:
    company = input("Enter Company Name: ")
    start_year = int(input("From(year): "))
    end_year = int(input("To(year): "))
    salary = int(input("Enter salary: "))
    exp[id]={'company':company, 'start':start_year, 'end':end_year, 'salary':salary}
    ch = input("Do you want to continue? [Y/n] ")
    if ch.lower()=='n':
        break
    id+=1
op = ''
c=len(exp)-1
for k,v in exp.items():
    op += str(exp[k])+(arrow if c else '')
    c -= 1
print(op)