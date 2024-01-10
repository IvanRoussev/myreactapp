import React, { useState } from 'react';

const TaskList = () => {
    const [inputTask, setInputTask] = useState("");
    const [taskCounter, setTaskCounter] = useState(1); 
    const [list, setList] = useState([]);
    const [errorMessage, setErrorMessage] = useState("");

    const handleInputChange = (event) => {
        setInputTask(event.target.value);
    };

    const handleAddTask = () => {
        if (inputTask.trim() === "") {
            setErrorMessage("Please enter a task.");
            return;
        }

        const newTask = {
            id: taskCounter,
            task: inputTask,
            isCompleted: false,
        };

        setList([...list, newTask]);
        setInputTask('');
        setErrorMessage("");
        setTaskCounter(taskCounter + 1); 
    };

    const handleDeleteTask = (id) => {
        const newList = list.filter((task) => task.id !== id);
        setList(newList);
    
        newList.forEach((task, index) => {
            task.id = index + 1;
        });
    };

    const handleToggleStatus = (id) => {
        const updatedList = list.map((task) => {
            if (task.id === id) {
                return {
                    ...task,
                    isCompleted: !task.isCompleted,
                };
            }
            return task;
        });
        setList(updatedList);
    };

    return (
        <div className="todo-app">
            <h1>Task Tracker App - Denshi</h1>
            {errorMessage && <p className="error-message">{errorMessage}</p>}
            <div className="input-wrapper">
                <input
                    className="input"
                    type="text"
                    value={inputTask}
                    onChange={handleInputChange}
                    placeholder="Enter a task"
                />
                <button onClick={handleAddTask}>Add Task</button>
            </div>

            <ul>
                {list.map((task) => (
                    <li className='task' key={task.id}>
                        <div className={`task-name ${task.isCompleted ? 'completed' : ''}`}>{task.id}. {task.task} </div>
                        <div className={`status ${task.isCompleted ? 'completed-status' : ''}`}> {task.isCompleted ? ' Completed ' : ' Uncompleted'} </div>
                        <button className='delete' onClick={() => handleDeleteTask(task.id)}>Delete</button>
                        <button className={task.isCompleted ? 'uncompleted-button' : 'completed-button'} onClick={() => handleToggleStatus(task.id)}>
                            {task.isCompleted ? 'Uncompleted' : 'Completed '}
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TaskList;

