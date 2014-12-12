/**
 * Created by eric on 12/10/14.
 */

var landingPage = (function () {


    function drawTable (collection){

        var textVal = '<table class="table"><tr><th>Analysis ID</th><th>Tags</th></th><th>Payload</th><th>Status</th></tr>';
        var i;

        for (i=0; i<collection["content"].length; i++) {
            textVal += "<tr>";
            textVal += "<td>" + collection["content"][i]["analysis_id"] + "</td>";
            textVal += "<td>" + JSON.stringify(collection["content"][i]["tags"]) + "</td>";
            textVal += "<td>" + JSON.stringify(collection["content"][i]["payload"]) + "</td>";
            textVal += "<td>" + collection["content"][i]["status"]+ "</td>";
            textVal += "</tr>";
        }

        textVal += "</table>";
        textVal += '<button id="displeased" onclick="landingPage.submitDispleasure()" class="btn btn-mini">';
        textVal += "Not What I'm looking for";
        textVal += "</button>";


        $("#queryresults").html(textVal);

    }

    var submitQuery = function () {
        var queryString = $("#searchQuery").val();

        var ajaxSettings = {
            async       :  true,
            contentType : "json",
            data        :  {"request": queryString },
            type        :  "GET"};

        $.ajax("/api/v1.0/analysis", ajaxSettings)
            .done(function (collection) {
                drawTable(collection);
             });
     };


    var submitDispleasure = function (){
        var queryString = $("#searchQuery").val();
        console.log(queryString);

        var ajaxSettings = {
            async       :  true,
            contentType : "application/json",
            data        :  {"request": queryString },
            type        :  "POST"};

        $.ajax("/api/v1.0/analysis", ajaxSettings)
            .done(function (collection) {
                var settings = collection;
                drawTable(collection);
            });
    };

    return { "submitQuery"       : submitQuery,
             "submitDispleasure" : submitDispleasure};

})();
