import numpy as np
import matplotlib.pyplot as plt

# =====================
# PARAMETRELER
# =====================

f0 = 152
f1 = f0
f2 = f0 / 2
f3 = 10 * f0   # 1520 Hz

fs = 8000

# En düşük frekansa göre 3 periyot
t_end = 3 * (1 / f2)
t = np.arange(0, t_end, 1/fs)

# =====================
# SİNYALLER
# =====================

x1 = np.sin(2*np.pi*f1*t)
x2 = np.sin(2*np.pi*f2*t)
x3 = np.sin(2*np.pi*f3*t)

x_sum = x1 + x2 + x3

# =====================
# 3 ALT ALTA GRAFİK
# =====================

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

plt.figure(figsize=(10,4))
plt.plot(t, x_sum)
plt.title("Sum of Three Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()