
var a=[false,false,false,false,false,false,false];
function start(){
    
    var qa=document.getElementById("qa");
    qn=[
        qa.children[1].children[1],
        qa.children[1].children[1],
        qa.children[1].children[1],
        qa.children[1].children[1],
        qa.children[1].children[1],
        qa.children[1].children[1],
        qa.children[1].children[1],
    ];
    for(i=1;i<=7;i++){
        var q2=qa.children[i].children[1];
        qn[i-1]=q2;
        qa.children[i].removeChild(q2);
    }
}
function click1(){
    window.location.href="https://im.qq.com/";
}
function click2(){
    var mail=document.createElement('input');
    var E_mail=document.getElementById("ctchoice");
    mail.setAttribute("type","text");
    mail.value="newthread-geek@outlook.com";
    E_mail.appendChild(mail);
    mail.select();
    document.execCommand("Copy");
    mail.style.display="none"; 
    alert("已复制邮箱newthread-geek@outlook.com");
}
function click3(){
    window.location.href="https://github.com/";
}

function q(i){
    var qa=document.getElementById("qa");
    if(a[i-1]===false){
        qa.children[i].appendChild(qn[i-1]);
        a[i-1]=true;
    }
    else{
        var q2=qa.children[i].children[1];
        qa.children[i].removeChild(q2);
        a[i-1]=false;
    }
}
function biger1(){
    var t=0;
    var k=25;
    var p=document.getElementById("picture1");
    var timer=setInterval(function(){
            p.style.width=k+'vw';
            t++;
            k=k+0.5;
            if(t===10){
                clearInterval(timer);   
            }      
    },15);
}
function smaller1(){
    var t=0;
    var k=29.5;
    var p=document.getElementById("picture1");
    var timer=setInterval(function(){
            p.style.width=k+'vw';
            t++;
            k=k-0.5;
            if(t===10){
                clearInterval(timer);   
            }      
    },15);
}
function biger2(){
    var t=0;
    var k=2.5;
    var p=document.getElementById("map0");
    var timer=setInterval(function(){
            p.style.fontSize=k+'vw';
            t++;
            k=k+0.05;
            if(t===10){
                clearInterval(timer);   
            }      
    },15);
}
function smaller2(){
    document.getElementById("map0").style.fontSize='2.5vw';    
}
function white(p){
    var k1=55;
    var k2=55;
    var k3=55;
    var timer=setInterval(function(){
        p.style.color='rgb('+k1+','+k2+','+k3+')';
        k1=k1+5;
        k2=k2+5;
        k3=k3+5;
        if(k1===255){
            clearInterval(timer);   
        }      
},10);
}
function black(p){
    p.style.color='rgb(54,57,63)';
}
