# TESTING

## Table of Contents

- [Manual testing of user stories](#manual-testing-of-user-stories)
  - [Profile](#profile)
  - [Posts](#posts)
  - [Comments](#comments)
  - [Likes](#likes)
  - [Followers](#followers)
- [Bugs](#bugs)
  - [Code](#code)
  - [CI Python Linter](#ci-python-linter)
  - [Heroku Deployment](#heroku-deployment)
- [Unfixed Bugs](#unfixed-bugs)

## Manual testing of user stories

### Profile
1- As a user, I can view lists of profiles so that I can see all the profiles have been created.<br>
2- As a user, I can get each profile by id so that I can see individual profile data.<br>
3- As a logged-in user, I can get my profile by id so that I can update my profile data when I want.<br>
4- As a logged-in user, I can filter profiles so that I can list the profiles according to my wishes.<br>
| User Story                                | Steps                                       | Expected Result                          | Actual Result          |
|-------------------------------------------|---------------------------------------------|------------------------------------------|------------------------|
| 1- View lists of profiles                 | Navigate to "/profiles" endpoint            | Profile list page opens                  | Work as expected       |
|                                           | Scroll through the profile list             | Profiles of users are displayed          | Work as expected       |
| 2- Get each profile by id                | Navigate to "/profiles/<user_id>" endpoint  | Individual profile data is displayed     | Work as expected       |
| 3- Get logged-in user's profile by id for editing    | Navigate to "/profiles/<user_id>" endpoint | Logged-in user's profile data  with ability of edit is shown  | Work as expected       |
| 4- Filter profiles                       | Navigate to "/profiles amd from filter option, select an option | Profiles are listed based on the filters | Work as expected       |


### Posts
1- As a user, I can view a list of all posts so that I can see all posts have been posted.<br>
2- As a user, I can get each post by id so that I can see individual post content.<br>
3- As a logged-in user , I can create a post so that I can post it to be visible for other users.<br>
4- As a logged-in user, I can get my posts by id so that I can edit or delete them.<br>
5- As a logged-in user, I can filter/search posts so that I can list the posts according to my wishes.<br>
| User Story                                | Steps                                       | Expected Result                          | Actual Result          |
|-------------------------------------------|---------------------------------------------|------------------------------------------|------------------------|
| 1- View list of all posts                | Navigate to "/posts" endpoint               | Post list page opens                     | Work as expected       |
|                                           | Scroll through the post list                | Posts are displayed                      | Work as expected       |
| 2- Get each post by id                   | Navigate to "/posts/<post_id>" endpoint      | Individual post content is displayed     | Work as expected       |
| 3- Create a post                         | Navigate to "/posts" endpoint and fill the post form and send it   | Post is created and visible for users    | Work as expected       |
| 4- Get logged-in user's posts by id for delete or editing     | Navigate to "/posts/<post_id>" endpoint     | Logged-in user's post data with ability of delete or edit is shown      | Work as expected       |
| 5- Filter/search posts                   | Navigate to "/posts amd from filter option, select an option    | Posts are listed based on the filters    | Work as expected       |


### Comments
1- As a user, I can view a list of all comments so that I can see all comments have been created.<br>
2- As a user, I can get each comment by id so that I can see individual comment content.<br>
3- As a logged-in user, I can add comments to the posts so that I can interact with various people regarding a post.<br>
4- As a logged-in user, I can retrieve my comments by their id so that I can edit/delete the comment.<br>
5- As a logged-in user, I can filter/search comments so that I can list the comments according to my wishes.<br>
| User Story                                | Steps                                       | Expected Result                          | Actual Result          |
|-------------------------------------------|---------------------------------------------|------------------------------------------|------------------------|
| 1- View list of all comments             | Navigate to "/comments" endpoint            | Comment list page opens                  | Work as expected       |
|                                           | Scroll through the comment list              | Comments are displayed                   | Work as expected       |
| 2- Get each comment by id                | Navigate to "/comments/<comment_id>"   | Individual comment content is displayed  | Work as expected       |
| 3- Add a comment to a post              | Navigate to "/comments" endpoint and fill the post form and send it| Comment is added to the post             | Work as expected       |
| 4- Retrieve logged-in user's comments by id for delete or editing  | Navigate to "/comments/<comment_id>" endpoint | Logged-in user's comment data with ability of delete or edit is shown | Work as expected       |
| 5- search comments by post              | Navigate to "/comments and from filter option, select a post  | Comments are listed based on selected post | Work as expected       |


### Likes
1- As a user, I can view the list of likes so that I can see all the likes created in the API for the posts.<br>
2- As a user, I can retrieve likes by id so that I can see individual like content.<br>
3- As a logged-in user, I can like a post so that I can express interest in the post.<br>
4- As a logged-in user, I can remove my like from a post, so that I can change my opinion about a post.<br>
| User Story                                | Steps                                       | Expected Result                          | Actual Result          |
|-------------------------------------------|---------------------------------------------|------------------------------------------|------------------------|
| 1- View list of all likes                | Navigate to "/likes" endpoint               | Likes list page opens                    | Work as expected       |
|                                           | Scroll through the likes list               | Likes are displayed                      | Work as expected       |
| 2- Get each like by id                   | Navigate to "/likes/<like_id>"      | Individual like content is displayed     | Work as expected       |
| 3- Like a post as logged in user                          | Navigate to  "/likes" endpoint and select a post    | Post is liked by the user               | Work as expected       |
| 4- Unlike a post as logged in user                        | Navigate to "/likes/<like_id>" | If user created the like, the like is removed from the post     | Work as expected       |

### Followers
1- As a user, I can view a list of followers so that I can see who is following whom.<br>
2- As a user, I can retrieve followers by id so that I can see individual follower content.<br>
3- As a logged-in user, I can make a follow so that I can follow my favorite user.<br>
4- As a logged-in user, I can delete a follow so that I can unfollow a followed user.<br>
| User Story                                | Steps                                                 | Expected Result                          | Actual Result          |
|-------------------------------------------|-------------------------------------------------------|------------------------------------------|------------------------|
| 1- View list of all followers            | Navigate to "/followers" endpoint                     | Followers list page opens                | Work as expected       |
|                                           | Scroll through the followers list                     | Followers are displayed                  | Work as expected       |
| 2- Get each follower by id               | Navigate to "/followers/<follower_id>"         | Individual follower content is displayed| Work as expected       |
| 3- Make a follow as logged in user                        | Navigate to  "/followers" endpoint and select a user          | User starts following another user      | Work as expected       |
| 4- Delete a follow as logged in user                       | Navigate to "/followers/<follower_id>"   | User stops following the other user     | Work as expected       |


### Bugs

#### Code

- No error was found 

#### CI Python Linter

- No bug was found during Python Validation

#### Heroku Deployment

- No error found during deployment

### Unfixed Bugs

- No unfixed bugs from developer side



