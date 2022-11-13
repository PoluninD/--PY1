from random import sample
import string
def get_random_password() -> str:
    #n=int(input("Введите длину пароля:"))
    num = string.digits
    Alpha =string.ascii_letters
    base = num + Alpha

    password_elements = sample(base, 8)#Если неизвестная длина прароля: sample(base,n)

    return "".join(password_elements)

print(get_random_password())
