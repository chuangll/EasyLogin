from EasyLogin import EasyLogin
a = EasyLogin()
page = a.get("http://ip.cn/")
myIP, mylocation = a.f("code", attrs={})
print(myIP)
print(mylocation)
print(a.img())
print(a.css())
print(a.js())
print(";".join(a.text()))