/**
 * Created by eric on 12/10/14.
 */

var user = (function () {

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

        $.ajax("/api/v1.0/analysis", {
            async       :  true,
            data        :  { request: queryString },
            type        :  "GET",
            success : function (collection) {
                main.undisplayError()
                drawTable(collection);
             },
             error : function(jqxhr,status,error){
                main.displayError(jqxhr)
            }
        })
     };


    var submitDispleasure = function (){
        var queryString = $("#searchQuery").val();
        console.log(queryString);

        $.ajax("/api/v1.0/analysis", {
            async       :  true,
            contentType : "application/json",
            dataType : "json",
            data        :  JSON.stringify({request: queryString }),
            type        :  "POST",
            success : function(responseText){
                    main.undisplayError()
                    //Search again and display queued analysis
                    submitQuery()
                },
            error : function(jqxhr,status,error){
                main.displayError(jqxhr)
            }
            });
    };

    return { "submitQuery"       : submitQuery,
             "submitDispleasure" : submitDispleasure};

})();
