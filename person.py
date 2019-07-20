def person(name, age, **kw):
    if 'city' in kw:
 # 有 city 参数
        print(kw["city"])
        pass
    if 'job' in kw:
 # 有 job 参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
kw={"city":121,"job":131}
person('ly',7,)