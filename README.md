# Python Signal Graphs - Kurulum ve Çalıştırma Talimatları

Bu projede iki adet Python dosyası bulunmaktadır:
- `task1.py`: Temel sinyal üretimi ve grafiği
- `task2.py`: DTMF tuş takımı ve sinyal üretimi (modern arayüz)

## Gereksinimler

Aşağıdaki Python paketlerinin yüklü olması gerekmektedir:
- numpy
- matplotlib
- sounddevice (sadece `task2.py` için)
- pillow (sadece `task2.py` için, logo desteği için)

## Kurulum

1. **Python 3.8+** yüklü olmalıdır. [Python İndir](https://www.python.org/downloads/)
2. Proje klasöründe terminal/powershell açın.
3. Gerekli paketleri yüklemek için aşağıdaki komutu çalıştırın:

```
pip install numpy matplotlib sounddevice pillow
```

## Kullanım

### 1. Sinyal Grafikleri (`task1.py`)

```
python task1.py
```

- 3 farklı sinyalin ve toplamlarının grafiğini gösterir.

### 2. DTMF Keypad Uygulaması (`task2.py`)

```
python task2.py
```

- Modern arayüzlü DTMF tuş takımı açılır.
- Tuşlara tıklayarak ilgili DTMF sinyalini dinleyebilir ve grafiğini görebilirsiniz.
- Uygulama başlığında ve pencerede `istun_logo_red.png` dosyası kullanılmaktadır. Bu dosyanın proje klasöründe olması gerekir.

## Notlar
- `sounddevice` bazı sistemlerde ek driver gerektirebilir. Sorun yaşarsanız [sound device docs](https://python-sounddevice.readthedocs.io/) adresine bakınız.
- Eğer arayüzde logo görünmüyorsa, Pillow kütüphanesinin yüklü olduğundan ve logo dosyasının adının doğru olduğundan emin olun.
