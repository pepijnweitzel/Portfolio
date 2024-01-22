document.addEventListener('DOMContentLoaded', function() {
    // By default, load all the posts
    load_page(1);
});

let ableFollowButton;

function load_page(pageNumber) {

    const currentUrl = window.location.href;
    const urlSplit = currentUrl.split("/");

    // Set fetch url to according path
    let url;
    if (urlSplit[3] === 'following') {
        url = `/followingposts/?page=${pageNumber}`;
    } else if (urlSplit[3] === 'profile') {
        url = `/profileposts/${urlSplit[urlSplit.length - 1]}/?page=${pageNumber}`;
        ableFollowButton = true;
    } else {
        url = `/posts/?page=${pageNumber}`;
    }

    // Make a GET request to backend to fetch the posts
    fetch(url)
    .then(response => response.json())
    .then(data => {

        // Unfold the data
        const posts = data.posts;
        const maxPages = data.max_pages;

        // Get the container where you want to append the posts.
        const postsView = document.querySelector('#posts-view');

        // Clear the container
        postsView.innerHTML = '';

        // Create and append a div for each post.
        posts.forEach(post => {
            const postContainer = createPostContainer(post);
            // Append the post container to the posts view.
            postsView.appendChild(postContainer);
        });

        // Create div for pagination
        const pageButtons = createPaginationButtons(pageNumber, maxPages);
        postsView.appendChild(pageButtons);

    });
    if (ableFollowButton) {
        load_follow_action(); // Load follow button action
    }
}


function createPostContainer(post) {
    const postContainer = document.createElement('div');
    postContainer.classList.add('post-container');

    // Create user info section.
    const userInfo = document.createElement('div');
    userInfo.classList.add('post-user-info');

    const userAvatar = document.createElement('img');
    userAvatar.src = post['avatarLocation'];
    userAvatar.alt = 'User Avatar';

    userAvatar.style.height = '48px'; 
    userAvatar.style.width = 'auto'; // Maintain aspect ratio

    const username = document.createElement('span');
    username.classList.add('username');
    username.textContent = `@${post['author']}`;
    // Add eventlistener to get to profile page 
    username.addEventListener('click', function() {
    document.location.href = `/profile/${post['author']}`;
    });

    // Add title of post
    const title = document.createElement('span');
    title.textContent = `${post['title']}`;

    // Create timestamp of post creation.
    const timeStamp = document.createElement('div');
    timeStamp.classList.add('time-stamp');
    timeStamp.textContent = `${post['timestamp']}`;

    userInfo.appendChild(userAvatar);
    userInfo.appendChild(username);
    userInfo.appendChild(title);
    userInfo.appendChild(timeStamp);

    // Create post content section.
    const postContent = document.createElement('div');
    postContent.classList.add('post-content');
    postContent.textContent = post['content'];

    // Create post actions section.
    const postActions = document.createElement('div');
    postActions.classList.add('post-actions');

    const likeButton = document.createElement('img');
    likeButton.id = 'likebutton';
    likeButton.alt = 'Like';

    // Create event listener for liking if user is logged in
    if (typeof currentUsername !== 'undefined') {
        if (post['likers'].includes(currentUsername)) {
            // Current user has liked the post
            likeButton.src = '/static/network/avatars/liked.png';
        } else {
            likeButton.src = '/static/network/avatars/unliked.png';
        }
        likeButton.addEventListener('click', function () {
            // Fetch to manage_likes endpoint
            fetch(`/manage_likes/${post['id']}`, {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Toggle the likeButton source based on the response
                    likeButton.src = data.message.includes('unliked') ?
                        '/static/network/avatars/unliked.png' :
                        '/static/network/avatars/liked.png';
                    
                    // Reload page to load count of likes
                    load_page(pageNumber);
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
        });
    } else {
        // User is not logged in
        likeButton.src = '/static/network/avatars/unliked.png';
    }

    // Create delete trashcan if user is author of post
    if (typeof currentUsername !== 'undefined') {
        if (currentUsername === post['author']) {
            var deleteCan = document.createElement('img');
            deleteCan.src = '/static/network/avatars/trashCanIcon.png';
            deleteCan.alt = 'Delete';
            deleteCan.classList.add('trash-can-icon');
            deleteCan.id = 'delete-can';
            
            // Add event listener to make fetch and delete the post
            deleteCan.addEventListener('click', function() {
                fetch(`/delete_post/${post['id']}`, {
                    method: 'POST',
                    credentials: 'same-origin', // Ensure that cookies are sent only for same-origin requests (so no automatically sent cookies)
                    headers: {
                    'Content-Type': 'application/json', // To indicate request body is in JSON format
                    'X-CSRFToken': getCSRFToken(), // CSRF Token because of POST request
                    }
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    load_page(pageNumber);
                    return response.json();
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
            });
        }
    }

    const likes = document.createElement('div');
    likes.id = 'likescount';
    likes.textContent = post['likesCount'];
    
    postActions.appendChild(likes);
    postActions.appendChild(likeButton);

    // Edit button if current user is author of post
    if (typeof currentUsername !== 'undefined') {
        if (currentUsername === post['author']) {
            // Create edit button
            const editButton = document.createElement('button');
            editButton.classList.add('edit-button');
            editButton.textContent = 'Edit';

            // Add eventListener for editing
            editButton.addEventListener('click', function() {
                const textarea = document.createElement("textarea"); // Create a textarea element
                textarea.value = postContent.innerText; // Set the initial value of the textarea to the content of the div
                textarea.style.width = "100%"; // Set the width of the textarea to 100%
                postContent.parentNode.replaceChild(textarea, postContent); // Replace the div with the textarea

                // Add save button
                const saveButton = document.createElement('button');
                saveButton.classList.add('save-button');
                saveButton.textContent = 'Save';

                // Add eventListener for saving the edit
                saveButton.addEventListener('click', function() {
                    fetch(`/edit/${post['id']}`, {
                        method: 'POST',
                        credentials: 'same-origin', // Ensure that cookies are sent only for same-origin requests (so no automatically sent cookies)
                        headers: {
                        'Content-Type': 'application/json', // To indicate request body is in JSON format
                        'X-CSRFToken': getCSRFToken(), // CSRF Token because of POST request
                        },
                        body: JSON.stringify({'content': textarea.value}),
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        load_page(pageNumber);
                        return response.json();
                    })
                    .catch(error => {
                        console.error('There was a problem with the fetch operation:', error);
                    });
                });

                // Add button to div
                postActions.appendChild(saveButton);
            });
            // Append to postActions div
            postActions.appendChild(editButton);
        }
    }
    if (typeof currentUsername !== 'undefined') {
        if (currentUsername === post['author']) {
            // Add delete trashcan
            postActions.appendChild(deleteCan);
        }
    }

    // Append all sections to the post container.
    postContainer.appendChild(userInfo);
    postContainer.appendChild(postContent);
    postContainer.appendChild(postActions);
    // Return container
    return postContainer;
}


function createPaginationButtons(pageNumber, maxPages) {
    const pageButtons = document.createElement('div');
    pageButtons.classList.add('page-buttons')
    
    // Create buttons for pagination
    const nextButton = document.createElement('button');
    nextButton.classList.add('page-button');
    nextButton.textContent = 'Next';
    const backButton = document.createElement('button');
    backButton.classList.add('page-button');
    backButton.textContent = 'Back';

    // Add eventListeners for pagination
    nextButton.addEventListener('click', function() {
        load_page(pageNumber + 1);
        postsView.scrollTop = 0; // Scroll to the top of the container
    });
    backButton.addEventListener('click', function() {
        load_page(pageNumber - 1);
        postsView.scrollTop = 0; // Scroll to the top of the container
    });
    
    // Append to div and posts view bottom
    if (pageNumber !== 1) {
        pageButtons.appendChild(backButton);
    }
    if (pageNumber !== maxPages) {
        pageButtons.appendChild(nextButton);
    }
    // Return buttons
    return pageButtons;
}


function load_follow_action() {
    const followButton = document.querySelector('#follow-button');
    followButton.addEventListener('click', function() {
  
        // Get variables
        const currentUrl = window.location.href;
        const myArray = currentUrl.split("/");
        const targetUser = myArray[myArray.length - 1];
        const action = followButton.innerHTML;
    
        // Make fetch request
        fetch(`/manage_follower/${targetUser}/${action}`, {
            method: 'POST',
            credentials: 'same-origin', // Ensure that cookies are sent only for same-origin requests (so no automatically sent cookies)
            headers: {
            'Content-Type': 'application/json', // To indicate request body is in JSON format
            'X-CSRFToken': getCSRFToken(), // CSRF Token because of POST request
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Change button to other action
            if (action === 'Follow') {
            followButton.innerHTML = 'Unfollow';
            const followersDiv = document.querySelector('#follower-count');
            followersDiv.innerHTML = data.newCount;
            } else {
            followButton.innerHTML = 'Follow';
            const followersDiv = document.querySelector('#follower-count');
            followersDiv.innerHTML = data.newCount;
            }
        })
    });
}


// For fetch request with POST
function getCSRFToken() {
const cookieValue = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    .split('=')[1];

return cookieValue;
}
