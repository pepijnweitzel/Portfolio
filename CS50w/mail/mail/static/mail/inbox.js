document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email(null));

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(email) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';


  if (email) {
    // User got here through reply button
    document.querySelector('#compose-recipients').value = email['sender'];
    document.querySelector('#compose-subject').value = `Re: ${email['subject']}`;
    document.querySelector('#compose-body').value = `On ${email['timestamp']} ${email['sender']} wrote: ${email['body']}`;
  } else{
    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }

  // Get acces to form of the compose email on submit
  document.querySelector('#compose-form').addEventListener("submit", (event) => {
    // Prevent reloading DOM
    event.preventDefault();

    // Get values of all forms
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;

    // Post the email
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipients,
          subject: subject,
          body: body
      })
    })
    .then(response => response.json())
    .then(result => {

        // Check for errors
        if (result['error']) {

          // Check which error it is
          if (result['error'] === 'At least one recipient required.') {

            // Handle One Recipient Error
            console.log("One recipient Error")
          } else {

            // Handle Email Nonexistent Error
            console.log("email does not exist error");
          }
        } else {

          // Everything went right
          // Load user's sent inbox
          load_mailbox('sent');
        }
    });
  });
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Make get request to '/emails/<mailbox>' to request the emails for a particular mailbox.
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {

      // Create div for every email
      emails.forEach(email => {

        // Create the div
        const element = document.createElement('div');
        // Add its content
        element.innerHTML = `${email['sender']} - ${email['subject']} - ${email['timestamp']}`;
        // Add its style
        if (email['read'] === false) {
          element.style.backgroundColor = 'gray';
        } else {
          element.style.backgroundColor = 'white';
        }
        element.style.border = "thin solid #000000";
        // Add event listener for accessing the email
        element.addEventListener('click', function() {

            // Mark email as read
            fetch(`/emails/${email['id']}`, {
              method: 'PUT',
              body: JSON.stringify({
                  read: true
              })
            })

            // Load email
            load_email(email, mailbox);
        });
        // Add element to the view
        document.querySelector('#emails-view').append(element);
      })
  });
}

function load_email(email, mailbox) {
  // Show the email and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Remove previous email-page
  document.querySelector('#email-view').innerHTML = '';

  // Add info of email
  const info = document.createElement('div');
  info.innerHTML = `<h3>From: ${email['sender']}</h3><br><h3>To: ${email['recipients']}</h3><br><h3>Subject: ${email['subject']}</h3><br><h3>Timestamp: ${email['timestamp']}</h3>`
  document.querySelector('#email-view').append(info);

  // Show body of email
  document.querySelector('#email-view').innerHTML += `<hr><p>${email['body']}</p>`;

  // Add reply button
  // Create button
  const reply = document.createElement('button');
  reply.innerHTML = 'Reply';
  reply.addEventListener('click', function() {
    // Load Compose
    compose_email(email)
  });
  // Add button
  document.querySelector('#email-view').append(reply);

  if (mailbox !== 'sent') {
    // Create button
    const element = document.createElement('button');
    if (email['archived'] === false) {
      element.innerHTML = 'Archive';
    } else {
      element.innerHTML = 'Unarchive';
    }
    element.addEventListener('click', function() {
      if (email['archived'] === false) {
        // Archive email
        fetch(`/emails/${email['id']}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: true
          })
        })
      } else {
        // Unarchive email
        fetch(`/emails/${email['id']}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: false
          })
        })
      }
      // Load inbox
      load_mailbox('inbox')
    });
  // Add button
  document.querySelector('#email-view').append(element);
  }
}

