# CarShare
#### Video Demo:  <URL HERE>
#### Description:
CarShare is a web-based application using JavaScript, Python and Sqlite3. I walk you slowly through it by starting off with the html pages.

### Frontend:
starting of with layout.html you'll find the layout I used for all my html pages. There is a distinction between the login and register page and the other pages since you're not meant to acces some things from the login and register page. It shows how I used Bootstrap's navbar with some edits and changes made to it. The login page shows 2 input containers and a submit button, below that it is joined by a carousel of 3 pictures, swiping automatically through Bootstrap's help. The register page is quiet similar to the login page but contains a couple more input containers, also it contains some JavaScript to show and hide text explaining the joining/creating group process. The index page is the page with the most going on. By using bootstrap grid, it is divided into halves showing the calendar and calendar-update-forms on the left side and the following things on the right-side. Through a select option you're able to choose any of existing cars within your group and change its kilometercount, also you can add or remove already existing cars from your group. Through JavaScript I created all the info except for the reservations info for into the calendar. Getting the correct month for the correct corresponding days and the correct weekday's, then adding that info into the table headers and giving them the appropiate tag so i can locate the right location for the reservations later on. At last you'll find the last bit of JavaScript code recieving a list of dictionaries from my backend code and then placing the reservations into the calendar accordingly. The profile page is a simply page with three input containers and a submit button, through this form you can change your username or password. The history page shows a table which also uses a list of dictionaries from my backend code. It accesses this data through Jinja syntax and inputs it into the table to show recent changes made to the kilometercount. Last but not least is the apology page, this page is called upon when wrong input has been given by the user, it shows a picture with text edited ontop of it from memegen.

#### CSS:
In the static folder you'll find

### Backend:
