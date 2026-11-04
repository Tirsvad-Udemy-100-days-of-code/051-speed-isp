🌐 [English](Run-and-Test) · [Dansk](Run-and-Test-da) · **Bahasa Malaysia**

# Jalankan dan uji

## Cipta dan gunakan `.venv` setempat

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

## Jalankan bot

```bash
python -m speed_isp
```

Tanpa paparan, gunakan imej Docker:

```bash
docker build -t speed-isp -f docker/Dockerfile .
docker run --rm -e SPEED_ISP_SCREENSHOT_DIR=/shots -v "$PWD/docs/images:/shots" speed-isp
```

Tambah `-e Y_EMAIL=... -e Y_PASSWORD=...` untuk membenarkan bot menyiarkan di Y.

## Jalankan ujian

```bash
python -m pytest
```

Ujian unit tidak memerlukan pelayar atau rangkaian. Bina dokumentasi API dengan `doxygen Doxyfile`.

## Apa yang kami peroleh

- **Persediaan yang boleh diulang.** Sesiapa sahaja boleh mencipta semula persekitaran (virtual environment) daripada `pyproject.toml`.
- **Ujian yang pantas dan boleh dipercayai.** Pemacu palsu menggantikan pelayar.
- **Satu kebergantungan.** Hanya Selenium diperlukan untuk menjalankan bot; `pytest` hanya untuk ujian.
