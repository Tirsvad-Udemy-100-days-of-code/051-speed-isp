# Headless browser image for the live runs of the bot (see README, "Live run in Docker").
# python:3.13-slim, pinned to a digest for reproducible builds; update it on purpose.
FROM python:3.13-slim@sha256:ae14d4ce8771606477a81446e7ef429edd6762305fc50c84507c1041fa8285d1

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver fonts-liberation \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER=/usr/bin/chromedriver \
    SPEED_ISP_HEADLESS=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install --upgrade pip && python -m pip install .

# Run as an unprivileged user, not as root.
RUN useradd --create-home --uid 1000 bot
USER bot

CMD ["python", "-m", "speed_isp"]
