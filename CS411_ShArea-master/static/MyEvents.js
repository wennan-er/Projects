// Credit for li function: https://codepen.io/anantanandgupta/pen/oLLgyN
var update = function () {
        const id = $('#id').val()
    const start_time = $('#start_time').val()
    const duration = $('#duration').val()
    const tags = $('#tags').val()
    const arr = tags.split(", ")
    const data = {
        "id": id,
        "start_time": start_time,
        "duration": duration,
        "tags": arr
    }
    endpoint = "/create_event"
    prefix = "http://127.0.0.1:5000"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
            const val  = data["value"]
            if(val == "success") {
                    alert("You've created an event")
            }
            else {
                    alert("failed to create an event")
            }
        })
    });
}

var deleteEvent = function() {
    const id = $('#usrname').val()
    const data = {
        "id":id
    }
    endpoint = "/delete_event"
    prefix = "http://127.0.0.1:5000"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
            const val  = data["value"]
            if(val == "success") {
                    alert("You've deleted an event")
            }
            else {
                    alert("failed to delete an event")
            }
        })
    });
}
$("input#createEvent").click(function() {
        update();
});
$("input#deleteEvent").click(function() {
        deleteEvent();
});
