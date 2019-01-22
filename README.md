# YoutubeVideoRepeater
This python program requires Selenium to be installed. If you don't have it, simply do pip install selenium to install it.
There are 2 arguments that are required in order for the program to work. The first is the os path to the chrome driver. If you 
don't have the selenium chrome driver installed, you can download it [here](http://chromedriver.chromium.org/downloads)
The second argument that is required is the youtube video url that you would like to have repeated. 
Optional arguments that can be provided after these first two are os paths to zipped chrome extension folders. For example,
you could zip the chrome adblock folder, and add it as an argument so that selenium will open chrome with adblock installed.

Running the script
------------------
To run this script, simply run this command in the terminal
```
python repeatYoutubeVideo.py <path_to_chromedriver> <url> <optional_extensions>
```
