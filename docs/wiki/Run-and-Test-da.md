🌐 [English](Run-and-Test) · **Dansk** · [Bahasa Malaysia](Run-and-Test-ms)

# Kør og test

## Opret og brug en lokal `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

## Kør botten

```bash
python -m speed_isp
```

Uden skærm bruges Docker-imaget:

```bash
docker build -t speed-isp -f docker/Dockerfile .
docker run --rm -e SPEED_ISP_SCREENSHOT_DIR=/shots -v "$PWD/docs/images:/shots" speed-isp
```

Tilføj `-e Y_EMAIL=... -e Y_PASSWORD=...` for at lade botten skrive på Y.

## Kør testene

```bash
python -m pytest
```

Enhedstestene kræver hverken browser eller netværk. Byg API-dokumentationen med `doxygen Doxyfile`.

## Hvad vi fik ud af det

- **En gentagelig opsætning.** Alle kan genskabe miljøet ud fra `pyproject.toml`.
- **Hurtige, pålidelige tests.** Falske drivere erstatter browseren.
- **Én afhængighed.** Kun Selenium skal bruges for at køre botten; `pytest` er kun til testene.
