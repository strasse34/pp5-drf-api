# RideReview

## Project Structure
### Project Apps
- profile app: This app contains model, views, serializers, and urls for profile
- posts app: This app contains model, views, serializers, and urls for posts
- comments app: This app contains model, views, serializers, and urls for comments
- like app: This app contains model, views, serializers, and urls for like
- rating app: This app contains model, views, serializers, and urls for rating
- followers app: This app contains model, views, serializers, tests and urls for followers

### Django Apps
- settings.py: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- Procfile: This file is used to specify the commands that should be executed when your Django app is deployed on a hosting platform.
- requirements.txt: This file lists the dependencies required for the Django project to run.
- env.py: This file is used to store environment variables for a Django project or application, such as database connection details or API keys.

## User Stories

### Profiles
- As a user, I can view lists of profiles so that I can see all the profiles have been created.  
- As a user, I can get each profile by id so that I can see individual profile data. 
- As a logged-in user, I can get my profile by id so that I can update my profile data when I want.
- As a logged-in user, I can filter profiles so that I can list the profiles according to my wishes. 

### Posts
- As a user, I can view a list of all posts so that I can see all posts have been posted.
- As a user, I can get each post by id so that I can see individual post content.
- As a logged-in user , I can create a post so that I can post it to be visible for other users.
- As a logged-in user, I can get my posts by id so that I can edit or delete them.
- As a logged-in user, I can filter/search posts so that I can list the posts according to my wishes.

### Comments
- As a user, I can view a list of all comments so that I can see all comments have been created.
- As a user, I can get each comment by id so that I can see individual comment content.
- As a logged-in user, I can add comments to the posts so that I can interact with various people regarding a post.
- As a logged-in user, I can retrieve my comments by their id so that I can edit/delete the comment.
- As a logged-in user, I can filter/search comments so that I can list the comments according to my wishes.

### Likes
- As a user, I can view the list of likes so that I can see all the likes created in the API for the posts.
- As a user, I can retrieve likes by id so that I can see individual like content.
- As a logged-in user, I can like a post so that I can express interest in the post.
- As a logged-in user, I can remove my like from a post, so that I can change my opinion about a post.

### Ratings
- As a user, I can view the list of ratings so that I can see all the ratings created in the API for the posts.
- As a user, I can retrieve ratings by id so that I can see individual rating content.
- As a logged-in user, I can rate a post so that I can express my opinion in the post.
- As a logged-in user, I can remove my rating from a post, so that I can change my opinion about a post.

### Followers
- As a user, I can view a list of followers so that I can see who is following whom.
- As a user, I can retrieve followers by id so that I can see individual follower content.
- As a logged-in user, I can make a follow so that I can follow my favorite user.
- As a logged-in user, I can delete a follow so that I can unfollow a followed user.



defaul car image source: https://clipart-library.com/clipart/6ir5kXA5T.htm















































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome strasse34,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software users, it will be great practice to see how these shell scripts work.

---

Happy coding!
