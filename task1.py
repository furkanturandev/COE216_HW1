# Gerekli kütüphaneler import ediliyor
import numpy as np
import matplotlib.pyplot as plt

# =====================
# PARAMETRELER
# =====================

# Temel frekans ve diğer frekanslar tanımlanıyor
f0 = 152
f1 = f0           # Birinci sinyalin frekansı
f2 = f0 / 2       # İkinci sinyalin frekansı
f3 = 10 * f0      # Üçüncü sinyalin frekansı (1520 Hz)

fs = 8000         # Örnekleme frekansı (Hz)

# En düşük frekansa göre 3 periyotluk zaman dizisi oluşturuluyor
# t_end: 3 periyotluk toplam süre
# t: 0'dan t_end'e kadar, fs örnekleme ile zaman dizisi

t_end = 3 * (1 / f2)
t = np.arange(0, t_end, 1/fs)

# =====================
# SİNYALLER
# =====================

# Üç farklı frekansta sinüs sinyalleri üretiliyor
x1 = np.sin(2*np.pi*f1*t)   # f1 frekanslı sinyal
x2 = np.sin(2*np.pi*f2*t)   # f2 frekanslı sinyal
x3 = np.sin(2*np.pi*f3*t)   # f3 frekanslı sinyal

# Üç sinyalin toplamı hesaplanıyor
x_sum = x1 + x2 + x3

# =====================
# 3 ALT ALTA GRAFİK
# =====================

# Her bir sinyal ayrı alt grafiklerde çiziliyor
plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(t, x1)
plt.title("Signal x1(t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3,1,2)
plt.plot(t, x2)
plt.title("Signal x2(t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3,1,3)
plt.plot(t, x3)
plt.title("Signal x3(t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# =====================
# TOPLAM SİNYAL
# =====================

# Üç sinyalin toplamı tek bir grafikte çiziliyor
plt.figure(figsize=(10,4))
plt.plot(t, x_sum)
plt.title("Sum of Three Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()