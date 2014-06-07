//显示活动的函数，下次就直接调用就okay；
function showAcIndex2(ret, idName)
{
    var str = "";
    for (var i=0; i<ret.list.length; ++i)
    {
        str += "<div class=\"homeLiCont\">\
                <img src=\""+ret.list[i]["imgSrc"]+"\"/>\
                <div class=\"homeLiTxt\">\
                    <div class=\"AcTime\">"+ret.list[i]["dateTime"]+"</div>\
                    <div class=\"AcName\">"+ret.list[i]["AcName"]+"</div>\
                    <div class=\"AcOrang\">By "+ret.list[i]["AcOrg"]+"</div>\
                    <div class=\"AcPlace\">活动地点："+ret.list[i]["AcPlace"]+"</div>\
                    <div class=\"AcNum\">上限人数："+ret.list[i]["AcNum"]+"（剩余<span class=\"greenColor\">"+ret.list[i]["AcNumRest"]+"</span>个空位）</div>\
                    <div class=\"AcHour\">公益时长："+ret.list[i]["AcHour"]+"</div>\
                    <div class=\"AcBtn\" id=\"AcId"+ret.list[i]["AcId"]+"\">\
                        <button class=\"confirmEnter\" type=\"submit\">认证</button>\
                        <button class=\"checkEnter\" type=\"submit\">查看</button>\
                        <button class=\"changeEnter\" type=\"submit\">修改</button>\
                        <button class=\"delEnter\" type=\"submit\">删除</button>\
                    </div>\
                </div>\
                <div class=\"clear\"></div>\
            </div>";
    }
    
    $("#"+idName).html(str);
}

function showPage(ret, idName)
{
    var str = "<div class=\"pageFooter\">";
    for (var i=1;i<=ret.pageCnt;++i)
    {
       str += "<a href=\"#\">"+i+"</a>";
    }
    str+="</div>";
    $("#"+idName).append(str);
    $("#"+idName).find(".pageFooter a:first-child").removeClass("notSelect").addClass("select");  
}

$(function(){
		
    //pageType的含义：’pageType’：0表示已发布，1表示未认证，2表示已认证。
    //分别4个变量记录是否需要询问新数据；1代表不用再次询问，0表示要问后台询问数据；
    var pageType = 0,
        releasePage = 1,
        notConfirm = 0,
        haveConfirm = 0,
        menu = $("#menu2 ul li"),
        nowIdName = "";
        
        
        
	//页面一开始点进去的是已发布的内容
    //询问后台取数据；	
    
    $.post('/adminIndex',{pageType: 0}, function(json){
        var ret = $.parseJSON(json);
        
        showAcIndex2(ret,"releasePageCont"); //活动显示；
        showPage(ret,"releasePage");  //页码显示；
    });
    
    
    
    //分别点击三个tab
        menu.click(function(){
		
			var menu_index = menu.index(this);
			//已发布
			if(menu_index == 0)
			{	
				pageType = 0;
                
                if(releasePage == 1){}
                else
                {
                    //dosomething;
                }
			}
            //未认证
			if(menu_index == 1)
			{
				pageType = 1;
                
                if(notConfirm == 1){}
                else
                {
                    $.post('/adminIndex',{pageType: pageType}, function(json){
                        var ret = $.parseJSON(json);
                        showAcIndex2(ret,"notConfirmCont"); //活动显示；
                        showPage(ret,"notConfirm");  //页码显示；
                    });
                   notConfirm = 1;
                }
			}
            //已认证
			if (menu_index == 2)
			{	
				pageType = 2;
               
                if(haveConfirm == 1){}
                else{
                   $.post('/adminIndex',{pageType: pageType}, function(json){
                        var ret = $.parseJSON(json);
                        showAcIndex2(ret,"haveConfirmCont"); //活动显示；
                        showPage(ret,"haveConfirm");  //页码显示；
                    });
                   haveConfirm = 1;
                }
			}
            
           
		})
        
        
    //点击某个页码
    $(".pageFooter a").click(function(){
    
                var pageNum = $(this).html();
          
                switch(pageType)
                {
                    case 0: 
                        nowIdName = "releasePageCont";
                        break;
                    case 1:
                        nowIdName = "notConfirmCont";
                        break;
                    case 2:
                        nowIdName = "haveConfirmCont";
                        break;
                    
                }
                $.post('/adminIndexPage',{pageType: pageType, page : pageNum}, function(json){
                    var ret = $.parseJSON(json);
                    showAcIndex2(ret,nowIdName); //活动显示；
                });
    })
    
    
    //认证按钮；
    $(".confirmEnter").click(function(){
        var AcId = $(this).parent().attr("id").substr(4);
        location.href="confirmAc.html"+"?"+"id="+AcId;
    })
    
    //查看按钮;
    $(".checkEnter").click(function(){
        var AcId = $(this).parent().attr("id").substr(4);
        location.href="checkAc.html"+"?"+"id="+AcId;
    })
    
    //修改按钮;
    $(".changeEnter").click(function(){
        var AcId = $(this).parent().attr("id").substr(4);
        location.href="changeAc.html"+"?"+"id="+AcId;
    })
    
    //删除按钮；
    $(".delEnter").click(function(){
        var AcId = $(this).parent().attr("id").substr(4);
        $.post('/deleteAc',{AcId: AcId}, function(json){
            var ret = $.parseJSON(json);
            if (ret.success == 1) 
            {
                alert("成功删除！");   
            }else {
                alert("删除失败！");
            }
        });
    })
    
})