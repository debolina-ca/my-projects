// create references to page elements
var addButton = document.getElementById("add");
var taskInput = document.getElementById("task");
var taskList = document.getElementById("taskList");
var clearButton = document.getElementById("clear");

// add new item to task list
addButton.addEventListener("click", function(){
    var task = taskInput.value;
    // Don't add an empty string
    if(task.trim()){
        // add new task list item
        var newItem = document.createElement("li");
        var taskText = document.createTextNode(task);
        newItem.appendChild(taskText);
        // clear text input box
        taskInput.value = "";
        // add remove option for new item
        var removeButton = document.createElement("button");
        removeButton.innerHTML = "Done";
        removeButton.className = "remove";
        removeButton.addEventListener("click", removeTask);
        newItem.appendChild(removeButton);
        taskList.appendChild(newItem);
    }
    else{
        alert("Task cannot be empty");
    }
});

// clear entire list
clearButton.addEventListener("click", function(){
    taskList.innerHTML = "";
});

// When a Done button is clicked, remove the list item the button is associated with to clear the task 
// (using event.target, the parentElement property, and removeChild)
function removeTask(e) {
    // get the parent list item to remove
    var taskItem = e.target.parentElement;
    taskList.removeChild(taskItem);
}