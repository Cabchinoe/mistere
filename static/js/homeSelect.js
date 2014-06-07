
$(function(){
		
		
		var $sum_nav = $("#menu ul li");
        var $home = $("#stuHome");
		//设置起始状态
		$sum_nav.eq(0).removeClass("notSelect").addClass("select");
		$("#indexPage").show();
		$("#notStartPage").hide();
		$("#takingPage").hide();
		$("#hotPage").hide();
        $("#stuHomeIndex").hide();
		
        
         
        
        
        //关于页码的设置；
        $(".pageFooter a").click(function(){
            $(this).removeClass("notSelect").addClass("select");
			$(this).siblings().removeClass("select").addClass("notSelect");
        })
        
		//个人主页的点击；
        $home.click(function(){
            $("#indexPage").hide();
            $("#notStartPage").hide();
            $("#takingPage").hide();
            $("#hotPage").hide();
            $("#stuHomeIndex").show();
        
        })
		
		//设置点击选择
		$sum_nav.click(function(){
			$(this).find("a").removeClass("notSelect").addClass("select");
			$(this).siblings().find("a").removeClass("select").addClass("notSelect");
		
			var sum_index = $sum_nav.index(this);
			
			if(sum_index == 0)
			{	
				$("#indexPage").show();
                $("#notStartPage").hide();
                $("#takingPage").hide();
                $("#hotPage").hide();
                $("#stuHomeIndex").hide();
			}
			if(sum_index == 1)
			{
				$("#indexPage").hide();
                $("#notStartPage").show();
                $("#takingPage").hide();
                $("#hotPage").hide();
                $("#stuHomeIndex").hide();
			}
			if (sum_index == 2)
			{	
				$("#indexPage").hide();
                $("#notStartPage").hide();
                $("#takingPage").show();
                $("#hotPage").hide();
                $("#stuHomeIndex").hide();
			}
			if (sum_index == 3)
			{	
				$("#indexPage").hide();
                $("#notStartPage").hide();
                $("#takingPage").hide();
                $("#hotPage").show();
                $("#stuHomeIndex").hide();
			}
           
		})
        
      
		
		
		
})