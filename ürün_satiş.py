import numpy as np
import matplotlib.pyplot as plt

urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
satis_verileri = {}

for urun in urunler:
    satis_verileri[urun] = np.random.randint(10, 101, 30)

print("\n--- Ürün Satış Analizi ---")
toplam_satislar = []
ortalama_satislar = []

for urun in urunler:
    toplam = np.sum(satis_verileri[urun])
    ortalama = np.mean(satis_verileri[urun])
    toplam_satislar.append(toplam)
    ortalama_satislar.append(ortalama)
    print(f"{urun} - Toplam Satış: {toplam}, Ortalama Günlük Satış: {ortalama:.2f}")

# Ürün bazında çubuk grafiği
plt.figure(figsize=(8,5))
plt.bar(urunler, toplam_satislar, color='purple')
plt.title('Ürün Bazında Toplam Satışlar')
plt.xlabel('Ürünler')
plt.ylabel('Toplam Satış Miktarı')
plt.grid(True, axis='y')
plt.show()
