name = input('请输入要备份的文件名:')
f = open(name,'r')
content = f.read()
f.close()
print(name.split('.'))
name_list = name.split('.')
new_name = name_list[0] + '-copy.'+ name_list[1]
f = open(new_name,'w')
content = f.flush()