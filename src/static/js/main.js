var main = (function () {

    function undisplayError(){
        $('#noti-bar').css('background','#FFFFFF')
        $('#placeholder_center').html("")
        $('#placeholder_right').html("<a id=\"placeholder_right\" class=\"navmenu-brand\" href=\"#\">Unnamed project</a>")
    }

    function displayError(textStatus,errorThrown,xr){
        var statuscode = xr.status
        var message = xr.responseJSON['error']
        $('#noti-bar').css('background','#F2DEDE')
        $('#placeholder_center').html(statuscode+" <b>"+errorThrown+"  </b>"+message)
        $('#placeholder_right').html("<a class=\"navmenu-brand close\">x</a>")
        $('#placeholder_right .close').click(function(){
            undisplayError()})
    }

    function init(){
        //First time loads content under index
        $('#content').load('/index',function(){
            // console.log("YAY")
        });

        //Events
        $('#menu-search').click(function(){
            $('#content').html('<div>Hello</div>')
            $('#content').load('/index',function(){
                undisplayError()
            })
        });

        $('#menu-console').click(function(){
            $('#content').load('/admin',function(){
                undisplayError()
            });
        });
    }

    return {
        "init" : init,
        "displayError" : displayError,
        "undisplayError" : undisplayError
    }

})()


