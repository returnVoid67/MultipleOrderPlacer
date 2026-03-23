function connectBreeze() {
    const sessionTokenInput = document.getElementById('sessionToken');
    const token = sessionTokenInput.value.trim();
    if (!token) {
        alert('Please enter session token');
        return;
    }

    // Disable button during call
    const button = event.target || event.srcElement;
    button.disabled = true;
    button.textContent = 'Connecting...';

    eel.connectBreeze(token)(function(response) {
        button.disabled = false;
        button.textContent = 'Connect';
        if (response.success) {
            alert('Connected to Breeze: ' + response.message);
        } else {
            alert('Connection failed: ' + response.message);
        }
    });
}
