🌐 **English** · [Dansk](Run-and-Test-da) · [Bahasa Malaysia](Run-and-Test-ms)

# Run and test

## Create and use a local `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

## Run the bot

```bash
python -m speed_isp
```

Without a display, use the Docker image:

```bash
docker build -t speed-isp -f docker/Dockerfile .
docker run --rm -e SPEED_ISP_SCREENSHOT_DIR=/shots -v "$PWD/docs/images:/shots" speed-isp
```

Add `-e Y_EMAIL=... -e Y_PASSWORD=...` to let the bot post on Y.

## Run the tests

```bash
python -m pytest
```

The unit tests need no browser and no network. Build the API documentation with `doxygen Doxyfile`.

## What we gained

- **A repeatable setup.** Anyone can recreate the environment from `pyproject.toml`.
- **Fast, reliable tests.** Fake drivers replace the browser.
- **One dependency.** Only Selenium is needed to run the bot; `pytest` is only for the tests.
