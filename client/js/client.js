const logElem = document.getElementById("log");
const socket = new WebSocket('ws://localhost:9289');

socket.addEventListener('open', (event) => {
    logMessage('Connected to game server');
});

socket.addEventListener('message', (event) => {
    logMessage(`Received: ${event.data}`);
    
    // Handle chat messages. You can check if the message has a specific prefix or structure, 
    // or if it doesn't match any command pattern, treat it as a chat message.
    if (!event.data.startsWith("CHALLENGE:") && !event.data.startsWith("AUTH:") && !event.data.startsWith("REGISTER:")) {
        // Assume this is a chat message and display it
        let chatBox = document.getElementById('chatBox');
        chatBox.innerHTML += '<div style="text-align: left; color: green;">' + event.data + '</div>';
        return;
    }
    
    // Handle challenge
    if (event.data.startsWith("CHALLENGE:")) {
        const salt = event.data.replace("CHALLENGE:", "");
        // You'd typically hash your password using the salt here. 
        // For simplicity, we're just sending the salt back as a placeholder.
        socket.send(salt);
    }
});

socket.addEventListener('error', (event) => {
    logMessage('Error: ' + event);
});

socket.addEventListener('close', (event) => {
    logMessage('Connection closed');
});

function switchMode(mode) {
    const authButton = document.querySelector('.auth-button');
    const regButton = document.querySelector('.reg-button');
    const authSection = document.querySelector('.auth-section');
    const regSection = document.querySelector('.reg-section');

    if (mode === 'auth') {
        authSection.style.display = 'block';
        regSection.style.display = 'none';
        authButton.style.display = 'none';
        regButton.style.display = 'block';
    } else if (mode === 'register') {
        authSection.style.display = 'none';
        regSection.style.display = 'block';
        authButton.style.display = 'block';
        regButton.style.display = 'none';
    }
}


function authenticate() {
    let username = document.getElementById('authUsername').value;
    let password = document.getElementById('authPassword').value;

    socket.send(`AUTH:${username}`);
}

function register() {    
    let username = document.getElementById('regUsername').value; // Corrected the element id here
    let password = document.getElementById('regPassword').value; // This password is not used yet

    socket.send(`REGISTER:${username}`);
}
function logMessage(message) {
    logElem.value += `${message}\n`;
}
function sendMessageToBot() {
    let message = document.getElementById('chatInput').value;
    
    // You can use a prefix to distinguish chat messages from other commands or send the message directly. 
    // Here we are just sending the chat message as is.
    socket.send(message); 

    // Append the user's message to chatBox
    let chatBox = document.getElementById('chatBox');
    chatBox.innerHTML += '<div style="text-align: right; color: blue;">' + message + '</div>';
    
    // Clear the chat input field
    document.getElementById('chatInput').value = '';
}