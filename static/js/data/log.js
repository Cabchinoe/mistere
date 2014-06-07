
$(function(){
		
        var logInEnter = $("#logInEnter");
        
        logInEnter.click(function(){
              
            var userID = $("#userNameInput").val();
            var pwd = $("#pwdInput").val();
             
            if (userID === "" || pwd === "")
            {
                alert("填写尚未完整！");
            }
            else
            {
                $.post('/login',{userName : userID, pwd : pwd}, function(json){
                    //直接后台判断角色之后跳转到相关页。
                 
                });
            }
        })
		
		
})