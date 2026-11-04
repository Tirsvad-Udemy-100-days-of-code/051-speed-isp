# Headless browser image for the live runs of the bot (see README, "Live run in Docker").
FROM python:3.13-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER=/usr/bin/chromedriver \
    SPEED_ISP_HEADLESS=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install --upgrade pip && python -m pip install .

CMD ["python", "-m", "speed_isp"]
