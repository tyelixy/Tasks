
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