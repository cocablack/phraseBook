"use strict";

$( document ).ready(function() {
    $("#query").mousedown(function() {
        submit_search_query();
    });
});

function submit_search_query() {
    var value = $("#input_text").val();
    
    console.log("submitting: " + value);
    
//    current_cursor = "progress";
    
    query(value, true);
}

function query(search_term, new_query) {
    $.ajax({
        url: "http://127.0.0.1:8080/query/",
        type: "POST",
        data: "hi",
        dataType: "text",
        success: function(data) {
            console.log("success " + data)
        }
    });
}