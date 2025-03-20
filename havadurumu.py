import numpy as np
import matplotlib.pyplot as plt

sicakliklar = np.random.uniform(-10, 40, 365)

ortalama_sicaklik = np.mean(sicakliklar)
en_sicak_gun = np.argmax(sicakliklar) + 1
en_soguk_gun = np.argmin(sicakliklar) + 1

print("\n--- Hava Durumu Verileri ---")
print(f"Ortalama sıcaklık: {ortalama_sicaklik:.2f} °C")
print(f"En sıcak gün: {en_sicak_gun}. gün, Sıcaklık: {np.max(sicakliklar):.2f} °C")
print(f"En soğuk gün: {en_soguk_gun}. gün, Sıcaklık: {np.min(sicakliklar):.2f} °C")

# Sıcaklık değişim grafiği
plt.figure(figsize=(10,5))
plt.plot(sicakliklar, color='orange')
plt.title('365 Günlük Sıcaklık Değişimi')
plt.xlabel('Gün')
plt.ylabel('Sıcaklık (°C)')
plt.grid(True)
plt.show()