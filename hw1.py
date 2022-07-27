#Напишите программу, удаляющую из текста все слова, содержащие 'абв'.
str_list = 'С другой абвстороны дальнейшее развабвитие различных форм деятеабвльности играет важную роль'

def strs(str):
    for item in str_list:
        if 'абв' in item:
            str_list.remove(item)
    print(str_list)

res = list(filter(lambda item:'абв' not in item, str_list.split()))
print(res)