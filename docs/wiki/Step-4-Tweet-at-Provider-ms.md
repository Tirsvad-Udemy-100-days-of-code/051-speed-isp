🌐 [English](Step-4-Tweet-at-Provider) · [Dansk](Step-4-Tweet-at-Provider-da) · **Bahasa Malaysia**

# Langkah 4: Tweet kepada penyedia perkhidmatan

`tweet_at_provider()` membandingkan kelajuan yang diukur dengan kelajuan yang dijanjikan dan, apabila terlalu rendah, log masuk ke Y (atau X) dan menyiarkan aduan.

Mesej dibina oleh fungsi tulen (pure function), `compose_complaint()`, contohnya:

```text
Hey @YourProvider, why is my internet speed 97.3down/49.7up when I pay for 150down/10up?
```

## Apa yang kami lakukan

- Menulis `compose_complaint()` dalam lapisan `domain`. Ia tidak pernah memendekkan teks secara senyap dan menimbulkan `ValueError` apabila siaran melebihi 280 aksara.
- Menulis satu kelas bagi setiap laman, `YSite` dan `XSite`, di sebalik antara muka kecil `SocialSite`: `login()` dan `post(text)`. Pemilih ialah pemalar.
- Menyemak kelayakan log masuk sebelum membuka pelayar. `Y_EMAIL` atau `Y_PASSWORD` yang tiada menghentikan bot dengan mesej yang jelas dan kod keluar 1:

```text
set the environment variables Y_EMAIL and Y_PASSWORD
```

- Tidak cuba memintas CAPTCHA atau pengesahan e-mel di X; jika log masuk tidak selesai, bot berhenti.

## Tangkapan skrin tweet yang disiarkan

![Aduan sebagai siaran teratas di Y](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-4-tweet-posted.png)

Tangkapan skrin, `docs/images/step-4-tweet-posted.png`, datang daripada larian langsung dalam bekas Docker dengan akaun Y milik pemilik repositori (bot menulisnya apabila `SPEED_ISP_SCREENSHOT_DIR` ditetapkan). Siaran itu berbunyi: "Hey, why is my internet speed 93.5down/52.4up when I pay for 150down/10up?"

## Apa yang kami peroleh

- **Pisahkan peraturan daripada pelayar.** Teks diuji tanpa Selenium.
- **Terbuka untuk dilanjutkan.** Laman baharu ialah kelas baharu di sebalik antara muka yang sama; tiada apa-apa lagi yang berubah.
- **Berhati-hati dengan rahsia.** Kelayakan log masuk datang daripada persekitaran dan tidak pernah muncul dalam log atau mesej ralat.
- **Had yang jujur.** X mungkin meminta CAPTCHA; bot melaporkannya dan berhenti, dan perkhidmatan tiruan Y digunakan untuk demonstrasi.
