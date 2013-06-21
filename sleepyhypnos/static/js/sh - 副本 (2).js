$(document).ready(function(){
// nav
$("#navBtn").click(function(){
  $("#navUl").slideToggle(300);
});
// 主页输入框
  $(".homeInputInput").focus(function(){
  	$(this).css("color","#999").removeAttr("placeholder")
		.parent().css("background-image","url(static/images/homeinput2.png)").end();
  }).blur(function(){
  	$(this).attr("placeholder","在这边可以写写今天的小结和明天的计划。")
		.parent().css("background-image","url(static/images/homeinput1.png)").end();
  });
// 去除注册登录页面点击登录框的说明文字
	$(".login input:not(.btnLogin)").focus(function(){
  	$(this).removeAttr("placeholder");
	})
// 登录框
	$("#inputAccount").blur(function(){
  	$(this).attr("placeholder","帐号");
	});
  	$("#inputPassword").blur(function(){
  	$(this).attr("placeholder","密码");
	});
// 注册页面
  $("#registerAccount").blur(function(){
  	$(this).attr("placeholder","填写用户名");
	});
  $("#registerPassword").blur(function(){
  	$(this).attr("placeholder","请创建一个密码");
	});
  $("#registerRePassword").blur(function(){
  	$(this).attr("placeholder","重新输入密码");
	});
  $("#registerMail").blur(function(){
  	$(this).attr("placeholder","填写您的常用邮箱");
	});
  $("#registerVerificationCode").blur(function(){
  	$(this).attr("placeholder","填写验证码");
});
// 打开时间手风琴
$("#openTimeAccordion").click(function(){
  $("#timeAccordion").slideToggle(300);
});
// 打开日记
var a = Math.ceil($("#p1").text().length+2);
var b = a/31*24+164;
var c = b/2;
var d = c.toString();
var e = $(window).height()*0.84;
var f = $(window).height()*0.42;
var g = e.toString();
var h = f.toString();
if (a<660)
  {
  document.getElementById('diary1').style.cssText = "margin-top:-" + c + "px;";
  }
else
  {
	  
  document.getElementById('diary1').style.cssText = "height:" + g + "px; margin-top:-" + h +"px;";
  document.getElementById('p1').style.cssText = "overflow-y:scroll;";
  }
$("#diaryPreview1").click(function(){
  $(".diaryContainer").fadeIn(300);
  $(".diary").fadeIn(300);
});
$(".diaryContainer:not(.diary)").click(function(){
  $(".diaryContainer").fadeOut(300);
  $(".diary").fadeOut(300);
});
// 时间手风琴
$("#timeAccordion > li").click(function(){
	if(false == $(this).next().is(':visible')) {
		$('#timeAccordion > ul').slideUp(300);
	}
	$(this).next().slideToggle(300);
});
$('#timeAccordion > ul:eq(0)').show();
// -------------------------
});