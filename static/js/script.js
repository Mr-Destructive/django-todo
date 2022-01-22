
document.getElementById("stat").addEventListener("click", update_status);


function update_status()
{
    let url = "http://127.0.0.1:8000/update/"+"task.id";
    let task_status, task_name;
    if( task_status == "done" )
    {
        task_status="pending";
    }
    else{
        task_status="done";
    }
    const task = { "task": task_name, "status": task_status };
    axios.post(url, task) 
    .then(function (response)
    {

    })
    .catch(function (error) {
        console.log(error);
    })
}
