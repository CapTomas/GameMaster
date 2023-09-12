const socket = new WebSocket('ws://localhost:9289');

socket.addEventListener('open', (event) => {
    console.log('Connected to game server');

    // Example: Request classes and races from the server.
    // Modify as per your WebSocket server's API
    socket.send("GET_CLASSES_AND_RACES");
});

socket.addEventListener('message', (event) => {
    // Assuming the server sends back a JSON string with classes and races
    const data = JSON.parse(event.data);
    populateDropdown('race', data.races);
    populateDropdown('class', data.classes);
});

function populateDropdown(dropdownId, items) {
    const dropdown = document.getElementById(dropdownId);
    items.forEach(item => {
        const option = document.createElement('option');
        option.value = option.textContent = item;
        dropdown.appendChild(option);
    });
}

function submitCharacter() {
    const character = {
        name: document.getElementById('name').value,
        race: document.getElementById('race').value,
        class: document.getElementById('class').value,
        points: document.getElementById('points').value
    };
    
    // Send the character to the server to save in dynamic.db
    // Modify as per your WebSocket server's API
    socket.send(`CREATE_CHARACTER:${JSON.stringify(character)}`);
}
