// var doCreate = function() {
//     const username = $('#username').val()
//     const password = $('#password').val()
//     const data = {
//         "username": username,
//         "password": password
//     }
//     /*
//     p1 = "localhost:5000"
//     p2 = "http://127.0.0.1:5000"
//     endpoint = "/create"
//     url = ""
//     if (op == 1) {
//         url = p1.concat(endpoint)
//     } else {
//         url = p2.concat(endpoint)
//     }
//     */
//     prefix = "http://127.0.0.1:5000"
//     endpoint = "/create"
//     url = prefix.concat(endpoint)
//
//     fetch(url, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify(data)
//     }).then(response => {
//         response.json().then(data => {
//             const name = data["username"]
//             $("#showName").val(name);
//
//         })
//     });
// }
//
//
// $("input#createButton").click(function() {
//     doCreate();
// });
