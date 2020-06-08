// var test = "http://localhost:5000/login"
// var url = "http://127.0.0.1:5000/login"

var doLogin = function() {
    const email = $('#email').val()
    const password = $('#password').val()
    const data = {
        "email": email,
        "password": password
    }
    endpoint = "/login"
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
            const val = data["value"]
            if (val == "success") {
                    window.location.href = 'events.html';
            }
            else {
                alert("Invalid Username/Password")
            }
        })
    });
}


$("input#login_btn").click(function() {
        doLogin();
});
