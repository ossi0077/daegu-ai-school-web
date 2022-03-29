//다크모드 낮모드 함수
function dark_mode(){
    document.getElementById('indexstyle').href='index_dark_style.css';
    document.querySelector('body').style.backgroundColor='black';
    document.querySelector('body').style.color='white';
    let hyper = document.querySelectorAll('a');
    for(i=0;i<hyper.length;i++){
        hyper[i].style.color='white'
    }
}

function day_mode(){
    document.getElementById('indexstyle').href='index_style.css';
    document.querySelector('body').style.backgroundColor='inherit';
    document.querySelector('body').style.color='inherit';
    let hyper = document.querySelectorAll('a');
    for(i=0;i<hyper.length;i++){
        hyper[i].style.color='inherit'
    }
}

