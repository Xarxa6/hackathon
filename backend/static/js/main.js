(function () {

    //First time loads content under index
    $('#content').load('/index',function(){
        // console.log("YAY")
    });

    //Events
    $('#menu-search').click(function(){
        $('#content').html('<div>Hello</div>')
        $('#content').load('/index',function(){
            // console.log("stuff")
        })
    });

    $('#menu-console').click(function(){
        $('#content').load('/admin',function(){
            // console.log("stuff2")
        });
    });

})()


