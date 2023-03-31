### True Shuffle For Spotify

# What is it?

Spotify fake randomness algorithm is making some people crazy, so I made script that will make it completely random each time. Finally. 

# How to make it work? 
To make script work you have to get your own client id and client secret from spotify, it's ultra simple. To get that please go to https://developer.spotify.com/dashboard/applications

`pip install -r requirements.txt`
^ use this command in cmd opened in folder where you cloned repository

Then proceed with instructions:

1. Clone the repository to a new folder. You will get an main.py file and .env file
2. Go to: https://developer.spotify.com/dashboard/applications | Create an app using "Create an App" green button on the top right.
3. Enter anything you want. It doesn't matter at all.
4. Click "Edit settings" and set at least one redirect URI https://i.imgur.com/UacYsjB.png ⚠️⚠️⚠️ it has to be `https://localhost`
5. Copy client ID and client secret. https://i.imgur.com/2sDk4CG.png <- it looks like on this screenshot
6. Paste both of those tokens into .env file REMEMBER TO SET THE REDIRECT URI TOO!
7. Run the script by command line `python main.py`. Keep the window in the background. If you want to stop the script close window.
