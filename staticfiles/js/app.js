const toggleBtn = document.querySelector('.toggle');
toggleBtn.addEventListener('click',toggleHandle);
const slider = document.querySelector('.list');

function toggleHandle(e){
    if(slider.classList.contains('change')){
        slider.classList.remove('change');
        e.target.classList.remove('fa-times');
        e.target.classList.add('fa-bars');
    }else{
        slider.classList.add('change');
        e.target.classList.add('fa-times');
        e.target.classList.remove('fa-bars');
    }
}

  