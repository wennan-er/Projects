var doCreate = function() {
    const email = $('#email').val()
    const password = $('#password').val()
    const data = {
        "email": email,
        "password": password
    }
    prefix = "http://127.0.0.1:5000"
    endpoint = "/create_user"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
                const val = data["value"];
                if(val == "success") {
                        $("#showName").val($('#email').val());
                        alert("You've create a new account!")
                }
                else {
                        alert("failed to create new user")
                }
        })
    });
}


$("input#createButton").click(function() {
        doCreate();
});
