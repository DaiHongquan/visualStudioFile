function getSum(){
    var sum = 0;
    for(var i = 0; i < arguments.length; i++){
        try{
            if(isNaN(arguments[i])){
                throw "不是一个数字";
            }
            sum += arguments[i];
        }
        catch(err){
            alert(err);
            break;
        }
    }
    return sum;
}

function checkEmail(email){
    var index1 = email.indexOf("@");
    var index2 = email.lastIndexOf(".");
    if(index1 <= -1 || index1 + 2 >= index2 || index1 + 2 > email.length){
        alert("邮箱地址不合法");
    }
}

//获取字符串年月日
function getYearMonthDay(){
    var sysDate = new Date();
    var year = sysDate.getFullYear();
    var month = sysDate.getMonth() + 1;
    if(month < 10){
        month = "0" + month;
    }
    var day = sysDate.getDate();
    if(day < 10){
        day = "0" + day;
    }
    var yearMonthDay = year + "-" + month + "-" + day;
    return yearMonthDay;
}

//正则表达式
function checkRegEx(str,myRegEx){
    if(str.match(myRegEx)){
        alert("匹配成功");
    }else{
        alert("匹配失败");
    }
}



function onAlert(a){
    alert(a);
}

function writeA(eId,a,b){
    var c = getSum(a,b);
    document.getElementById(eId).innerHTML=c;
}

