document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Validate the username and password (for simplicity, no actual authentication here)
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    window.location.href = 'data_entry.html'; // Redirect to another page after successful loginelse {
    
  });