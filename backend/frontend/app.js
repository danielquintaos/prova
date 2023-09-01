console.log('app.js');
let currentUser = null;
const buttonLogin = document.getElementById("login");
buttonLogin.addEventListener('onclick', login());

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === "teste" && password === "teste123") {
        // Mocking successful login
        currentUser = {
            id: 1,
            username: "teste"
        };
        document.getElementById('loginPage').style.display = 'none';
        document.getElementById('mainPage').style.display = 'block';
        getTasks();
    }
}

async function addTask() {
    const taskInput = document.getElementById('newTask');
    const task = taskInput.value;
    taskInput.value = '';

    // POST request to add a new task
    const response = await fetch("http://localhost:5000/tasks", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task: task, userId: currentUser.id }) // replace these keys with whatever your backend expects
    });

    if (response.ok) {
        getTasks();  // Refresh the task list
    }
}

async function getTasks() {
    const taskListElement = document.getElementById('taskList');
    taskListElement.innerHTML = '';

    // Fetch tasks from the backend
    const response = await fetch(`http://localhost:5000/tasks?userId=${currentUser.id}`);
    const tasks = await response.json();

    tasks.forEach(task => {
        const taskElement = document.createElement('li');
        taskElement.innerHTML = `${task.task} <button onclick="deleteTask(${task.id})">Delete</button>`;
        taskListElement.appendChild(taskElement);
    });
}

async function deleteTask(id) {
    // DELETE request to remove a task
    const response = await fetch(`http://localhost:5000/tasks/${id}`, {
        method: "DELETE"
    });

    if (response.ok) {
        getTasks();  // Refresh the task list
    }
}

// Show login page on initial load
document.getElementById('loginPage').style.display = 'block';