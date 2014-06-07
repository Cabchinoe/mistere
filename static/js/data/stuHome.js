//显示活动的函数，下次就直接调用就okay；
function showAcIndex(ret,idName)
{
    var str = "";
    for(var i=0; i<ret.list.length; ++i)
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
                    <button class=\"JoinEnter\" type=\"submit\" id=\"AcId"+ret.list[i]["AcId"]+"\">马上参加</button>\
                </div>\
                <div class=\"clear\"></div>\
            </div>";
    }
    
    $("#"+idName).html(str);
    
}

//个人中心的显示活动；
function showAcHome(ret,idName)
{
    var str = "",
        AcComState = "",
        AcAuthenState ="";
        
    for (var i=0; i<ret.list.length; ++i)
    {
        //判断完成和认证状态；
        if(ret.list[i]["AcComState"] == 0)
        {
            AcComState = "<div class=\"takingState isTaking\">进行中...</div>";
        }
        else if(ret.list[i]["AcComState"] == 1)
        {
            AcComState = "<div class=\"takingState notTaking\">已完成</div>";
        }
        
        if (ret.list[i]["AcAuthenState"] == 0)
        {
            AcAuthenState = "<a href=\"#\" class=\"notConfirm\">未认证</a>";
        }
        else if (ret.list[i]["AcAuthenState"] == 1)
        {
            AcAuthenState = "<a href=\"#\" class=\"haveConfirm\">已认证</a>";
        }
        str +="<div class=\"stuHomeList\">\
                   <div class=\"homeListLeft\">"+ret.list[i]["dateTime"]+"</div>\
                   <div class=\"homeListRight\">\
                        <img src=\""+ret.list[i]["imgSrc"]+"\"/>\
                        <div class=\"homeListTxt\"> \
                            +AcComState+\
                            <div class=\"homeAcTime\">"+ret.list[i]["dateTime"]+"</div>\
                            <div class=\"homeAcName\">"+ret.list[i]["AcName"]+"</div>\
                            <div class=\"homeAcOrang\">By "+ret.list[i]["AcOrg"]+"</div>\
                            <div class=\"homeAcPlace\">活动地点："+ret.list[i]["AcPlace"]+"</div>\
                            <div class=\"homeAcNum\">上限人数："+ret.list[i]["AcNum"]+"</div>\
                            <div class=\"homeAcHour\">公益时长："+ret.list[i]["AcHour"]+"</div>\
                            <div class=\"confirmState\" id=\"HomeAcId"+ret.list[i]["AcId"]+"\">"+AcAuthenState+"</div>\
                        </div>\
                   </div>\
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


//主函数；
$(function(){
    
    //pageType的含义：’pageType’：0表示首页，1表示未开始，2表示进行中，3表示热门。
    //分别4个变量记录是否需要询问新数据；1代表不用再次询问，0表示要问后台询问数据；
    var pageType = 0,
        indexPage = 1,
        notStartPage = 0,
        takingPage = 0,
        hotPage = 0,
        menu = $("#menu ul li"),
        isHome = 0,
        nowIdName = "";
       
    
    
    //页面一开始点进去的是首页的内容
    //询问后台取数据；
   
    $.post('/stuIndex',{pageType: 0}, function(json){
        var ret = $.parseJSON(json);
        
        $("#stuName").html(ret.stuName);//修改学生名字；
        showAcIndex(ret,"indexPageCont"); //活动显示；
        showPage(ret,"indexPage");  //页码显示；
    });
   
   
    
    
    
    //分别点击4个tab；
        
   
		menu.click(function(){
		
			var menu_index = menu.index(this);
			//首页
			if(menu_index == 0)
			{	
				pageType = 0;
                isHome = 0;
                
                if(indexPage == 1){}
                else
                {
                    //dosomething;
                }
			}
            //未开始
			if(menu_index == 1)
			{
				pageType = 1;
                isHome = 0;
                
                if(notStartPage == 1){}
                else
                {
                    $.post('/stuIndex',{pageType: 1}, function(json){
                        var ret = $.parseJSON(json);
                        showAcIndex(ret,"notStartPageCont"); //活动显示；
                        showPage(ret,"notStartPage");  //页码显示；
                    });
                    notStartPage = 1;
                }
			}
            //进行中
			if (menu_index == 2)
			{	
				pageType = 2;
                isHome = 0;
                
                if(takingPage == 1){}
                else{
                     $.post('/stuIndex',{pageType: 2}, function(json){
                        var ret = $.parseJSON(json);
                        showAcIndex(ret,"takingPageCont"); //活动显示；
                        showPage(ret,"takingPage");  //页码显示；
                    });
                    takingPage = 1;
                }
			}
            //热门
			if (menu_index == 3)
			{	
				pageType = 3;
                isHome = 0;
                
                if(hotPage == 1){}
                else{
                     $.post('/stuIndex',{pageType: 3}, function(json){
                        var ret = $.parseJSON(json);
                        showAcIndex(ret,"hotPageCont"); //活动显示；
                        showPage(ret,"hotPage");  //页码显示；
                    });
                    hotPage = 1;
                }
			}
           
		})
        
        
        
        //个人中心；
        $("#stuHome").click(function(){
            isHome = 1;
            $.post('/stuHome',{}, function(json){
                var ret = $.parseJSON(json);
                showAcHome(ret,"stuHomeIndexCont"); //活动显示；
                showPage(ret,"stuHomeIndex");  //页码显示；
            });
        })
        
        //点击页码；
        $(".pageFooter a").click(function(){
            var pageNum = $(this).html();
            
            if(isHome == 1)
            {
                $.post('/stuHomePage',{page : pageNum}, function(json){
                    var ret = $.parseJSON(json);
                    showAcHome(ret,"stuHomeIndexCont"); //活动显示；
                });
            }
            else{
                switch(pageType)
                {
                    case 0: 
                        nowIdName = "indexPageCont";
                        break;
                    case 1:
                        nowIdName = "notStartPageCont";
                        break;
                    case 2:
                        nowIdName = "takingPageCont";
                        break;
                    case 3:
                        nowIdName = "hotPageCont";
                        break;
                        
                }
                $.post('/stuIndexPage',{pageType: pageType, page : pageNum}, function(json){
                    var ret = $.parseJSON(json);
                    showAcIndex(ret,nowIdName); //活动显示；
                });
            }
        })
        
        
        //参加比赛；
        $(".JoinEnter").click(function(){
            var AcId = $(this).attr("id").substr(4);
            $.post('/stuParticipate',{AcId : AcId}, function(json){
                var ret = $.parseJSON(json);
                if (ret.success == 1) alert("成功参加！");
                else alert("参加失败！");
            });
        })
        
        
        //退出按钮
        $("#exitEnter").click(function(){
            $.post('/logout',{}, function(json){
                var ret = $.parseJSON(json);
                if (ret.success == 1) 
                {
                    alert("成功退出！");
                    location.href = "logIn.html";
                }
                else alert("退出失败！");
            });  
        })
   
    
        
})