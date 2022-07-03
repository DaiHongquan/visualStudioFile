//定义一个包含多个对象的json字符串
var laJsonStr = '{ "languages":[{"language1":"html"},{"language2":"js"},{"language3":"css"}]}';
//将json字符串解析为json对象，此函数存在脚本执行风险，一般不使用此方法，而是使用json解析器解析
var laJson = eval("(" + laJsonStr + ")");
//通过json解析器反序列化（将json字符串转换为json对象）
var laJson2 = JSON.parse(laJsonStr);
//通过json对象.key或者json对象[key]获取value
var stra2 = "<h1 st>"+laJson2.languages[0].language1 + '/' + laJson2.languages[1].language2 + '/' + laJson2.languages[2].language3 +"</h1>";
//通过json解析器序列化（将json对象转换为json字符串）
var laJsonStr3 = JSON.stringify(laJson2);
         
document.write(stra2);
//获取yyyy-mm-dd
function getYearMonthDate(){
    var nowFullDate = new Date();
    var year = nowFullDate.getFullYear();
    var month = nowFullDate.getMonth + 1;
    var nowDate = nowFullDate.getDate();
    if(month < 10){
        month = '0' + month; 
    }
    if(nowDate < 10){
        nowDate = '0' + month; 
    }
    var yearMonthDate = year + '-' + month + nowDate;
    return yearMonthDate;
}
//求和
function getSum(){
    var retunSum = 0;
    var err = new Error();
    alert(typeof(1.1));
    try{
        for(var i = 0; i < arguments.length; i++){
            if(typeof(arguments[i] != "number")){
                err = "不是一个数字";
                throw err;
            }
            retunSum += arguments[i];
        }
    }catch(e){
            alert(e);
    }finally{
        return retunSum;
    }

}
//正则表达式
function myRegEx(str,regEx){
    // if(str.match(regEx)){
    //     return true;
    // }else{
    //     return false;
    // }
    //alert(str.match(regEx));
}

myRegEx("https://www.baidu.com/",/^[^\/]*[\w.]+$/gi);


// var xmlDoc = new ActiveXObject("Microsoft.XMLDOM")
// xmlDoc.async="false"
// xmlDoc.validateOnParse="true"
// xmlDoc.load("xml/note.xml")

// document.write("<br>Error Code: ")
// document.write(xmlDoc.parseError.errorCode)
// document.write("<br>Error Reason: ")
// document.write(xmlDoc.parseError.reason)
// document.write("<br>Error Line: ")
// document.write(xmlDoc.parseError.line)

//jquery 文档dom加载完毕执行。$表示jquery，括号内的内容获取和css选择器基本一致
$(function() {
    $("#box").html("Hello World!");//html()获取元素内容包含字标签 text()获取元素文本，不包含标签，val()获取input的值
    //$(".submit").val(); html()、text()、val()如果输入参数表示设置值
    //$("#jQuery").attr("id");获取属性的值 如果是2个参数,则表示设置属性值
    //$("#jQuery").removerAttract("id");移除一个或多个属性，多个属性用空格隔开
    //$("#jQuery").appern("David");append() 在被选元素结尾插入内容,prepend()在被选元素开头插入内容,after()在被选元素之后插入内容，before()在被选元素之前插入内容
    //$("#jQuery").addClass("box");addClass()从被选元素添加一个或多个类，多个类用空格隔开。removeClass()从被选元素删除一个或多个类，多个类用空格隔开。
                              //toggleClass()添加/删除类的切换操作。
    //$("#jQuery").css({"property":"value","property":"value"});//css()设置或返回样式属性，可以使用json格式设置多个css属性
    //$("#jQuery").width();width()设置或返回元素宽度，height()高度，innerWidth()包含内边距的宽度，innerHeight()包含内边距的高度，outerWidth(),outerHeight()包含外边距和边框
    //dom遍历
    //$("#jQuery").parent();parent()直接父元素，parents()所有祖先元素，children()所有直接子元素，find()后代元素的dom树水平遍历
                        //siblings()返回所有同胞元素，next()下一个同胞元素，nextAll()后面所有同胞元素，prev()上一个同胞元素，prevAll()前面所有同胞元素
    //$("#jQuery").remove();remove()删除被选元素及其子元素，可以接受一个参数，对被删元素进行过滤，empty()从被选元素中删除子元素（清空该元素）        
    //$("#jQuery").eq(1);表示符合条件的第二个元素 ，eq从0开始           
    $(".submit").click(function(event){
        $("#jQuery").html(Date);
        //event.preventDefault()
        //$("#jQuery").animate({width:"250px"},1000，function(){alert("1");});
    }

    );//事件 click单击，dblclick双击,mouseenter鼠标指针进入所选元素,mouseleave鼠标指针离开所选元素,mouseover鼠标指针悬停在所选元素
      //keydown按下键盘触发，keyup键盘按键被释放触发，keypress一次按下抬起按键触发
      //submit提交表单触发，change表单元素的值发生改变触发，focus表单元素获得焦点触发，blur表单元素失去焦点触发
      //ready当Dom加载完成以后触发，resize当浏览器窗口大小改变时触发，scroll当在指定元素拖动滚动条触发

      //事件对象
      //event.type 事件类型，event.pageX,event.pageY获取鼠标当前相对于页面坐标，event.preventDefault()阻止默认行为，event.stopPropagation()阻止事件冒泡
      //event.which 鼠标哪个键，event.data数据绑定事件时传入的任何数据，event.currentTarget在事件冒泡过程中的当前DOM元素，event.result包含有被指定事件触发的事件处理器返回的最后一个值
      
      //$("#jQuery").show();show()显示，hide()隐藏，toggle()切换显示/隐藏,可以有2个参数，速度和回调函数
                          //fadeIn()fadeOut()fateToggle()淡入淡出，可以有2个参数，速度和回调函数，fadeTo()速度和不透明度
                          //slideUp()slideDown()slideToggle(),向上滑，向下滑，可以有2个参数，速度和回调函数

      //.animate({params},speed,callback) 动画，属性值，速度，回调函数，如果存在多个动画，会创建动画队列，逐个运行                   

});