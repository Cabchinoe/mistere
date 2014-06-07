
$(function(){
		
		
		var $sum_nav = $("#menu2 ul li");
        
		//设置起始状态
		$sum_nav.eq(0).removeClass("notSelect").addClass("select");
		$("#releasePage").show();
		$("#notConfirm").hide();
		$("#haveConfirm").hide();
		
        
        //关于页码的设置；
        $(".pageFooter a").click(function(){
            $(this).removeClass("notSelect").addClass("select");
			$(this).siblings().removeClass("select").addClass("notSelect");
        })
        
		
		//设置点击选择
		$sum_nav.click(function(){
			$(this).find("a").removeClass("notSelect").addClass("select");
			$(this).siblings().find("a").removeClass("select").addClass("notSelect");
		
			var sum_index = $sum_nav.index(this);
			
			if(sum_index == 0)
			{	
				$("#releasePage").show();
                $("#notConfirm").hide();
                $("#haveConfirm").hide();
			}
			if(sum_index == 1)
			{
				$("#releasePage").hide();
                $("#notConfirm").show();
                $("#haveConfirm").hide();
			}
			if (sum_index == 2)
			{	
				$("#releasePage").hide();
                $("#notConfirm").hide();
                $("#haveConfirm").show();
			}
			
           
		})
        
      
		
		
		
})