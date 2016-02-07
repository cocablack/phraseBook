"use strict";

$( document ).ready(function() {
    
    $("#query").mousedown(function() {
        submit_search_query();
    });
});

function submit_search_query() {
    var value = $("#input_text").val();
    
    console.log("submitting: " + value);
    
    var data = {}
    data["text"] = value;
    
    query(data);
}

function query(json_data) {
    console.log("query")
    $.ajax({
        url: "/query",
        type: "POST",
        data: JSON.stringify(json_data),
        dataType: "text",
        success: function(data) {
            console.log("success");
            var resp = JSON.parse(JSON.parse(data));
            console.log(resp);

            Window.hi = resp;
            Window.ho = data;

            $("#inputBox").css("display", "none");

            var author = resp[3];
            var title = resp[2];
            var url = resp[4];
            var sentiment = resp[5];
            var sentiment_word = resp[6];

            console.log(resp);
            // console.log(author)

            $("#sentiment_text").text( "Sentiment Value: " + sentiment );
            $("#title_text").text("Title: "+ title );
            $("#author_text").text("Author: "+ author );

            // $("#url_text").text( "" );
            $("#url_link").attr("href", url);

            $("#outputBox").css("display", "block");


        },
        error: function(data) {
            console.log("something went wrong");
            console.log(data);
        }
    });
    
    console.log(JSON.stringify(json_data));
}