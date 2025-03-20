import numpy as np
import matplotlib.pyplot as plt

# Görev 1: 500 kişinin maaşlarını simüle etme
maaslar = np.random.randint(3000, 15001, 500)

# Ortalama, maksimum ve minimum maaşları hesapla
ortalama_maas = np.mean(maaslar)
max_maas = np.max(maaslar)
min_maas = np.min(maaslar)

print("--- Şirket Maaş Analizi ---")
print(f"Ortalama Maaş: {ortalama_maas:.2f} TL")
print(f"Maksimum Maaş: {max_maas} TL")
print(f"Minimum Maaş: {min_maas} TL")

# Maaş dağılımını histogram ile göster
plt.figure(figsize=(8,5))
plt.hist(maaslar, bins=20, color='skyblue', edgecolor='black')
plt.title('Maaş Dağılımı')
plt.xlabel('Maaş (TL)')
plt.ylabel('Çalışan Sayısı')
plt.grid(True)
plt.show()

# Görev 2: 500 çalışanı 3 departmana rastgele ata
departmanlar = np.random.choice([1, 2, 3], size=500)

# Her departmandaki ortalama maaşı hesapla
for departman in [1, 2, 3]:
    ort_maas = np.mean(maaslar[departmanlar == departman])
    departman_adi = "Mühendislik" if departman == 1 else ("Muhasebe" if departman == 2 else "Pazarlama")
    print(f"{departman_adi} departmanı ortalama maaşı: {ort_maas:.2f} TL")


