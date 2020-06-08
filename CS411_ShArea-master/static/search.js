var doLogin = function() {
    const email = $('#usr').val()
    const data = {
        "email": email
    }
    endpoint = "/contact"
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
            const info = data["contacts"]
            var listItemString = $('#listItem').html();
            for(var i = 0; i < info.length; i++) {
                    var listItem = $('<li>'+listItemString+'</li>');
                    var listItemTitle = $('.title', listItem);
                    var it = $('#usr').val()+": " + info[i]
                    listItemTitle.html(it);
                    $('#dataList').append(listItem);
            }
        })
    });
}


$("input#submitBtn").click(function() {
        $(dataList).empty();
        doLogin();
});
