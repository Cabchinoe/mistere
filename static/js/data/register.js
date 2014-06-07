
$(function(){
		
        var registerEnter = $("#registerEnter");
        
        registerEnter.click(function(){
              
            var userID = $("#userNameInput").val();
            var pwd = $("#pwdInput").val();
            var departmentInput = $("#departmentInput").val();
            var nameInput = $("#nameInput").val();
             
            //something debug;
            //console.log(userID, pwd, departmentInput, nameInput);
             
            if (userID === "" || pwd === "" || departmentInput ==="" || nameInput ==="")
            {
                alert("填写尚未完整！");
            }
            else
            {
                $.post('/register',{stuID : userID, pwd : pwd, department : departmentInput, trueName : nameInput}, function(json){
                    //直接后台判断角色之后跳转到相关页。
                    //要跳转到登陆后的状态；
                });
            }
        })
		
		
})