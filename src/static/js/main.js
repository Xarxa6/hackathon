var main = (function () {

    function undisplayError(){
        $('#noti-bar').css('background','#FFFFFF')
        $('#placeholder_center').html("")
        $('#placeholder_right').html("<a id=\"placeholder_right\" class=\"navmenu-brand\" href=\"#\">Unnamed project</a>")
    }

    function displayError(xhr){

        function display(c,s,m){
            $('#noti-bar').css('background','#F2DEDE')
            $('#placeholder_center').html(c+" <b>"+s+"  </b>"+m)
            $('#placeholder_right').html("<a class=\"navmenu-brand close\">x</a>")
            $('#placeholder_right .close').click(function(){
                undisplayError()})
        }

        function tryParseJson(jsonMaybe){
            if(jsonMaybe[0] == '{'){
                var parsed = JSON.parse(jsonMaybe)
                return parsed['error']
            } else {
                return jsonMaybe
            }
        }

        var statuscode = xhr.status
        var statusMessage = xhr.statusText

        if(xhr.responseJSON != undefined){
            var message = xhr.responseJSON['error']
            display(statuscode,statusMessage,message)
        } else {
            var message = tryParseJson(xhr.responseText)
            display(statuscode,statusMessage,message)
        }

    }

    function init(){
        //First time loads content under index
        $('#content').load('/index',function(){
            // console.log("YAY")
        });

        //Events
        $('#menu-search').click(function(){
            $('#content').load('/index',function( response, status, xhr){
                if ( status == "error" ) {
                    displayError(xhr)
                } else {
                    undisplayError()
                }
            })
        });

        $('#menu-saved').click(function(){
            $('#content').load('/saved',function( response, status, xhr){
                if ( status == "error" ) {
                    displayError(xhr)
                } else {
                    undisplayError()
                }
            })
        });

        $('#menu-account').click(function(){
            $('#content').load('/account',function( response, status, xhr){
                if ( status == "error" ) {
                    displayError(xhr)
                } else {
                    undisplayError()
                }
            })
        });

        $('#menu-console').click(function(){
            $('#content').load('/console',function(response, status, xhr){
                if ( status == "error" ) {
                    displayError(xhr)
                } else {
                    undisplayError()
                }
            });
        });

        $('#menu-config').click(function(){
            $('#content').load('/config',function( response, status, xhr){
                if ( status == "error" ) {
                    console.log(xhr)
                    displayError(xhr)
                } else {
                    undisplayError()
                }
            });
        });
    }

    return {
        "init" : init,
        "displayError" : displayError,
        "undisplayError" : undisplayError
    }

})()


