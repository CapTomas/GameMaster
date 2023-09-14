const logElem = document.getElementById("log");
const socket = new WebSocket('ws://localhost:9289');
let currentAction = '';

socket.addEventListener('open', (event) => {
    logMessage('Connected to game server');
});

socket.addEventListener('message', async (event) => {
    logMessage(`Received: ${event.data}`);

    if (!event.data.startsWith("CHALLENGE:") && !event.data.startsWith("AUTH:") && !event.data.startsWith("REGISTER:")) {
        appendChatMessage(event.data);  // Using the above function
        return;
    }

    logMessage(`I am here: ${event.data}`);
    if (event.data.startsWith("LOGIN SUCCESS") || event.data.startsWith("REGISTRATION SUCCESS")) {
        const authSection = document.querySelector('.auth-section');
        const regSection = document.querySelector('.reg-section');
        
        logMessage("Handling success message.");  // Debugging line
        
        authSection.style.display = 'none';
        regSection.style.display = 'none';
        return; // Exit early since the message was processed
    }

    // Handle challenge
    if (event.data.startsWith("CHALLENGE:")) {
        const salt = event.data.replace("CHALLENGE:", "");
        let passwordInputId = (currentAction === 'auth') ? 'authPassword' : 'regPassword';
        let password = document.getElementById(passwordInputId).value;
        let hashedPassword = await hashPassword(password, salt);
        socket.send(hashedPassword);
    }
});



socket.addEventListener('error', (event) => {
    logMessage('Error: ' + event);
});

socket.addEventListener('close', (event) => {
    logMessage('Connection closed');
});

async function hashPassword(password, salt) {
    const textEncoder = new TextEncoder();
    const passwordUint8 = textEncoder.encode(password);
    const saltUint8 = textEncoder.encode(salt);
    const combined = new Uint8Array([...passwordUint8, ...saltUint8]);
    const hashBuffer = await crypto.subtle.digest('SHA-256', combined);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');
}

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
    currentAction = 'auth';
    socket.send(`AUTH:${username}`);
}

function register() {    
    let username = document.getElementById('regUsername').value;
    currentAction = 'register';
    socket.send(`REGISTER:${username}`);
}

function logMessage(message) {
    logElem.value += `${message}\n`;
}
function sendMessageToBot() {
    let message = document.getElementById('chatInput').value;
    socket.send(message); 

    // Append the user's message to chatBox
    let chatBox = document.getElementById('chatBox');
    appendChatMessage(message, 'right', 'blue');     
    // Clear the chat input field
    document.getElementById('chatInput').value = '';
}

document.getElementById('chatInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();  // prevents the default Enter key action
        
        sendMessageToBot();

        // Add hover effect
        const sendButton = document.getElementById('sendButton');  // Assuming you've given your Send button the ID "sendButton"
        sendButton.classList.add('pressed-effect');

        // Remove the effect after 1 second
        setTimeout(() => {
            sendButton.classList.remove('pressed-effect');
        }, 250);
    }
});

function appendChatMessage(message, alignment = 'left', color = 'green') {
    let chatBox = document.getElementById('chatBox');
    chatBox.innerHTML += `<div style="text-align: ${alignment}; color: ${color};">${message}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}