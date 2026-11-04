🌐 **English** · [Dansk](Step-2-Create-a-Class-da) · [Bahasa Malaysia](Step-2-Create-a-Class-ms)

# Step 2: Create a class

A bot with several steps is easier to keep tidy as a class. `InternetSpeedTwitterBot` holds the browser and the measured speeds.

![The bot has opened speedtest.net and is ready to start the test](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/051-speed-isp/raw/branch/main/docs/images/step-2-speedtest-ready.png)

## What we did

- Created `InternetSpeedTwitterBot` in `src/speed_isp/infrastructure/bot.py`. Its `__init__` creates the Selenium driver and the two properties `down` and `up`.
- Added the two methods of the assignment, `get_internet_speed()` and `tweet_at_provider()`.
- Outside the class the entry point creates the object and calls the two methods in order:

```python
bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()
bot.tweet_at_provider()
```

## What we gained

- **A bot with state.** The driver and the speeds travel together, so the second method can use what the first one measured.
- **Readable steps.** The code reads like the lecture: first get the speed, then tweet.
- **Testable code.** The driver is passed in, so unit tests use a fake driver and need no browser and no network.
- **Layers.** Rules (`domain`), the order of steps (`application`), Selenium (`infrastructure`) and the command line (`presentation`) are separate folders; imports point inward.
