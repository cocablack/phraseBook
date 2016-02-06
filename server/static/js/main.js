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
    console.log("query")
    $.ajax({
        url: "/query",
        type: "POST",
        data: "hi",
        dataType: "text",
        success: function(data) {
            console.log("success " + data)
        }
    });
}