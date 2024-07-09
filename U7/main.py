'''U7:

Mashina nomli class yarating. Ushbu classning elementlari nomi, turi (yengil, yuk avtomobili), narxi, ishlab_chiqarilgan_yili. Mashinaning malumot nomli methodi bor unda mashina xaqida malumot chiqib keladi. 10 ta mashina xaqida malumot berilgan mashinalarni ishlab chiqarilgan yili bo’yicha saralab ekranga chop eting. Mashinani narxi kiritilmaganda default 4.000$ qiymatni berib keting.'''
class Mashina:
    def __init__(self, nomi, turi, ishlab_chiqarilgan_yili, narxi=4000):
        self.nomi = nomi
        self.turi = turi
        self.ishlab_chiqarilgan_yili = ishlab_chiqarilgan_yili
        self.narxi = narxi

    def malumot(self):
        return f"Nomi: {self.nomi}, Turi: {self.turi}, Narxi: ${self.narxi}, Ishlab chiqarilgan yili: {self.ishlab_chiqarilgan_yili}"

mashinalar = [
    Mashina("Toyota Corolla", "yengil", 2023, 20000),
    Mashina("Honda Accord", "yengil", 2022, 25000),
    Mashina("Ford Mustang", "yengil", 2021, 30000),
    Mashina("Chevrolet Silverado", "yuk avtomobili", 2020, 35000),
    Mashina("BMW 3 Series", "yengil", 2019, 45000),
    Mashina("Audi A4", "yengil", 2018, 40000),
    Mashina("Mercedes-Benz C-Class", "yengil", 2017, 38000),
    Mashina("Nissan Altima", "yengil", 2016, 22000),
    Mashina("Volkswagen Golf", "yengil", 2015, 18000),
    Mashina("Subaru Outback", "yuk avtomobili", 2014, 23000)
]

saralangan_mashinalar = sorted(mashinalar, key=lambda x: x.ishlab_chiqarilgan_yili)

for mashina in saralangan_mashinalar:
    print(mashina.malumot())





