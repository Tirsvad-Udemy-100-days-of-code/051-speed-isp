🌐 [English](Step-2-Create-a-Class) · [Dansk](Step-2-Create-a-Class-da) · **Bahasa Malaysia**

# Langkah 2: Cipta sebuah kelas

Bot yang mempunyai beberapa langkah lebih mudah dikemas jika dijadikan kelas. `InternetSpeedTwitterBot` menyimpan pelayar dan kelajuan yang diukur.

![Bot telah membuka speedtest.net dan sedia memulakan ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-2-speedtest-ready.png)

## Apa yang kami lakukan

- Mencipta `InternetSpeedTwitterBot` dalam `src/speed_isp/infrastructure/bot.py`. `__init__`nya mencipta pemacu (driver) Selenium dan dua sifat `down` dan `up`.
- Menambah dua kaedah daripada tugasan, `get_internet_speed()` dan `tweet_at_provider()`.
- Di luar kelas, titik masuk mencipta objek dan memanggil kedua-dua kaedah mengikut urutan:

```python
bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()
bot.tweet_at_provider()
```

## Apa yang kami peroleh

- **Bot yang mempunyai keadaan (state).** Pemacu dan kelajuan dibawa bersama, jadi kaedah kedua boleh menggunakan apa yang diukur oleh kaedah pertama.
- **Langkah yang mudah dibaca.** Kod dibaca seperti kuliah: dapatkan kelajuan dahulu, kemudian tweet.
- **Kod yang boleh diuji.** Pemacu diserahkan dari luar, jadi ujian unit menggunakan pemacu palsu dan tidak memerlukan pelayar atau rangkaian.
- **Lapisan.** Peraturan (`domain`), urutan langkah (`application`), Selenium (`infrastructure`) dan baris perintah (`presentation`) berada dalam folder berasingan; import menuju ke dalam.
