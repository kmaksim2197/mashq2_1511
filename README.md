# Universitet Tizimi – Polimorfizm Misoli (Python)

## Tavsif
Ushbu loyiha universitet tizimidagi uchta rolni modellashtiradi:

- **Talaba**
- **Oqituvchi**
- **Xodim**

Har biri umumiy `Universitet` bazaviy sinfidan meros oladi va quyidagi metodlarga ega:

- `ish_kuni_boshlash()` – kunni boshlash jarayoni
- `maosh_hisoblash(soat)` – oylik ish soatlariga ko‘ra maosh hisoblash
- `dars_otish(fan)` – faqat Oqituvchi sinfida ishlaydi, boshqalar hech narsa qilmaydi

Polimorfizm orqali barcha obyektlar bitta ro‘yxat orqali boshqariladi.

---

## Funksionallik

- Talaba, Oqituvchi, Xodim obyektlari yaratiladi.
- Har birining oylik ish soati beriladi.
- Polimorfizm yordamida umumiy ro‘yxatda aylantirilib:
  - umumiy oylik maosh hisoblanadi.
- Oqituvchi sinfi `dars_otish()` metodiga ega.

---

## Ishga tushirish

```bash
python main.py
