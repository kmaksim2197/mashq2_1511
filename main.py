class Universitet:
    def ish_kuni_boshlash(self):
        raise NotImplementedError

    def maosh_hisoblash(self, soat):
        raise NotImplementedError

    def dars_otish(self, fan):
        pass


class Talaba(Universitet):
    def __init__(self, ism, soatlik):
        self.ism = ism
        self.soatlik = soatlik

    def ish_kuni_boshlash(self):
        return f"{self.ism} universitetga keldi."

    def maosh_hisoblash(self, soat):
        return self.soatlik * soat


class Oqituvchi(Universitet):
    def __init__(self, ism, soatlik):
        self.ism = ism
        self.soatlik = soatlik

    def ish_kuni_boshlash(self):
        return f"{self.ism} darsga tayyorlanmoqda."

    def maosh_hisoblash(self, soat):
        return self.soatlik * soat

    def dars_otish(self, fan):
        return f"{self.ism} {fan} fanidan dars o'tmoqda."


class Xodim(Universitet):
    def __init__(self, ism, soatlik):
        self.ism = ism
        self.soatlik = soatlik

    def ish_kuni_boshlash(self):
        return f"{self.ism} ishni boshladi."

    def maosh_hisoblash(self, soat):
        return self.soatlik * soat


xodimlar = [
    Talaba("Akmal", 20000),
    Oqituvchi("Dilshod", 50000),
    Xodim("Kamola", 30000)
]

soatlar = [80, 120, 100]

umumiy_maosh = 0

for i in range(len(xodimlar)):
    umumiy_maosh += xodimlar[i].maosh_hisoblash(soatlar[i])

print(umumiy_maosh)
print(xodimlar[1].dars_otish("Matematika"))
print(xodimlar[0].dars_otish("Tarix"))
