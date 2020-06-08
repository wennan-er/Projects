var update = function() {
    const email = $('#usrname').val()
    const oldName = $('#oldName').val()
    const newName = $('#newName').val()
    const edit = $('#editType').val()
    const data = {
        "email": email,
        "oldval": oldName,
        "newval": newName,
        "edit": edit
    }
    endpoint = "/edit_contact"
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
                    alert("You've made changes to your settings")
            }
            else {
                    alert("failed to insert new changes")
            }
        })
    });
}


$("input#submit_btn").click(function() {
        update();
});
