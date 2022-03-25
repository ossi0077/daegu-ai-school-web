//다크모드 낮모드 함수
function dark_mode(){
    document.getElementById('indexstyle').href='index_dark_style.css';
    let hyper = document.querySelectorAll('a');
    for(i=0;i<hyper.length;i++){
        hyper[i].style.color='white'
    }
}

function day_mode(){
    document.getElementById('indexstyle').href='index_style.css';
    let hyper = document.querySelectorAll('a');
    for(i=0;i<hyper.length;i++){
        hyper[i].style.color='inherit'
    }
}

