🌐 [English](Step-3-Get-Internet-Speeds) · [Dansk](Step-3-Get-Internet-Speeds-da) · **Bahasa Malaysia**

# Langkah 3: Dapatkan kelajuan internet

`get_internet_speed()` membuka speedtest.net, memulakan ujian, menunggu keputusan dan membaca kelajuan muat turun dan muat naik.

![Ujian kelajuan yang selesai di speedtest.net](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-3-speedtest-result.png)

Output konsol bagi satu larian dalam kontena Docker:

```text
Speed test started; waiting up to 180 s
Download: 97.32 Mbps, upload: 49.72 Mbps
```

## Apa yang kami lakukan

- Menolak sepanduk kuki (pilihan yang paling mesra privasi) dan mengklik butang **GO**, yang dicari menggunakan XPath.
- Menunggu dengan `WebDriverWait` sehingga halaman memaparkan `Result ID`, dan bukannya `sleep` tetap. Tempoh menunggu paling lama 180 saat, ditetapkan dalam `constants.py`.
- Membaca nombor dengan XPath dan menukarkannya dengan `parse_mbps()`.
- Menjalankan pelayar secara headless (tanpa paparan) dalam kontena Docker (`docker/Dockerfile`), supaya ujian tidak pernah mengambil alih desktop anda.

## Apa yang kami peroleh

- **Penantian eksplisit.** Menunggu sesuatu syarat dipenuhi lebih pantas dan lebih selamat daripada meneka kelewatan.
- **Latihan XPath.** Halaman yang dibina dengan nama kelas yang dijana disasarkan menggunakan teks dan atribut sebaliknya.
- **Pemilih di satu tempat.** Apabila speedtest.net berubah, hanya `constants.py` yang berubah.
- **Larian headless.** Kontena memberikan larian yang boleh diulang dan tangkapan skrin tanpa pelayar yang kelihatan.
