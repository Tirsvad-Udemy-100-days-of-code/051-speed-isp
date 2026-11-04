🌐 [English](Step-1-Account-and-Constants) · [Dansk](Step-1-Account-and-Constants-da) · **Bahasa Malaysia**

# Langkah 1: Akaun dan pemalar

Bot memerlukan dua perkara sebelum ia boleh membuat aduan: akaun di X (atau di perkhidmatan latihan Y) dan kelajuan yang dijanjikan oleh penyedia perkhidmatan anda.

![Halaman log masuk perkhidmatan latihan Y](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-1-y-login.png)

## Apa yang kami lakukan

- Menggunakan perkhidmatan latihan Y (`https://app.100daysofpython.dev/`), supaya tiada akaun media sosial sebenar yang terjejas. X juga disokong.
- Meletakkan kelajuan yang dijanjikan dan URL dalam `src/speed_isp/constants.py`:

```python
PROMISED_DOWN: int = 150
PROMISED_UP: int = 10
Y_LOGIN_URL: str = "https://app.100daysofpython.dev/services/y/login"
```

- Membaca kelayakan log masuk daripada pemboleh ubah persekitaran (environment variables), tidak pernah daripada kod:

```bash
export Y_EMAIL="you@example.com"
export Y_PASSWORD="your-password"
```

## Apa yang kami peroleh

- **Satu tempat untuk tetapan.** Pemalar berada dalam `constants.py`, jadi pemilih atau kelajuan yang berubah hanya perlu disunting sekali.
- **Rahsia kekal di luar repositori.** Kata laluan datang daripada persekitaran, dan `.env` berada dalam `.gitignore`.
- **Tempat bermain yang selamat.** Perkhidmatan tiruan membolehkan anda berlatih log masuk dan menyiarkan tanpa menyentuh akaun peribadi.
