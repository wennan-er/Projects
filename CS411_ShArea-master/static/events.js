// Credit for li function: https://codepen.io/anantanandgupta/pen/oLLgyN
var getEvents = function() {
    endpoint = "/get_all_events"
    prefix = "http://127.0.0.1:5000"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "GET",

        headers: {
            "Content-Type": "application/json",
        }
    }).then(response => {
        response.json().then(data => {
                // console.log(res)
                var obj = data["result"]
                var listItemString = $('#listItem').html();
                for(var i = 0; i < obj.length; i++) {
                        var it = obj[i]
                        var listItem = $('<li>' + listItemString + '</li>');
                        var listItemTitle = $('.title', listItem);
                        listItemTitle.html("User_ID: " + it.id);
                        var listItemAmount = $('.tag', listItem);
                        listItemAmount.html("Tags: " + it.tags);
                        var listItemDesc = $('.duration', listItem);
                        listItemDesc.html("Start time: " + it.start_time + " Duration:" + it.duration);
                        $('#dataList').append(listItem);
                }
        })
    });
}

var searchEvent = function() {
    const query = $('#tag_info').val()
    const data = {
        "query": query
    }
    prefix = "http://127.0.0.1:5000"
    endpoint = "/search_event"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
                var obj = data["result"]
                var listItemString = $('#listItem').html();
                for(var i = 0; i < obj.length; i++) {
                        var it = obj[i]
                        var listItem = $('<li>' + listItemString + '</li>');
                        var listItemTitle = $('.title', listItem);
                        listItemTitle.html("User_ID: " + it.id);
                        var listItemAmount = $('.tag', listItem);
                        listItemAmount.html("Tags: " + it.tags);
                        var listItemDesc = $('.duration', listItem);
                        listItemDesc.html("Start time: " + it.start_time + " Duration:" + it.duration);
                        $('#dataList').append(listItem);
                }
        })
    });
}

$("input#searchBtn").click(function() {
        $(dataList).empty();
        searchEvent();
});
