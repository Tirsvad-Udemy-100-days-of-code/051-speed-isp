🌐 **English** · [Dansk](Step-3-Get-Internet-Speeds-da) · [Bahasa Malaysia](Step-3-Get-Internet-Speeds-ms)

# Step 3: Get internet speeds

`get_internet_speed()` opens speedtest.net, starts the test, waits for the result and reads the download and upload speed.

![The finished speed test on speedtest.net](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-3-speedtest-result.png)

Console output of a run in a Docker container:

```text
Speed test started; waiting up to 180 s
Download: 97.32 Mbps, upload: 49.72 Mbps
```

## What we did

- Declined the cookie banner (the most privacy-friendly choice) and clicked the **GO** button, found with XPath.
- Waited with `WebDriverWait` until the page shows `Result ID`, instead of a fixed `sleep`. The wait is at most 180 seconds, set in `constants.py`.
- Read the numbers with XPath and converted them with `parse_mbps()`.
- Ran the browser headless in a Docker container (`docker/Dockerfile`), so the test never takes over your desktop.

## What we gained

- **Explicit waits.** Waiting for a condition is faster and safer than guessing a delay.
- **XPath practice.** Pages built with generated class names are targeted by text and attributes instead.
- **Selectors in one place.** When speedtest.net changes, only `constants.py` changes.
- **Headless runs.** A container gives repeatable runs and screenshots without a visible browser.
