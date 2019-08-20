const btnProximo = document.querySelector('#btnNext');
const btnNao = document.querySelector('#btnNo');
const btnSim = document.querySelector('#btnYes');
const inputNumber = document.querySelector('.inputNum');
const msgErr = document.querySelector('.msgError');
const num = document.querySelector('#num');
const inputNumberBd = document.querySelector('#inputNumberBd');

function validaInput(){
    if (inputNumber.value === "" || inputNumber.value.length < 11) {
        msgErr.style = "display:block";
        inputNumber.focus();
        return false;
    } 
    msgErr.style = "display:none";
    abrirModal();
}
btnProximo.addEventListener('click', validaInput);

function abrirModal(){
    let modal = document.querySelector('#modal');
    modal.classList.add('d-flex');
    num.innerHTML = inputNumber.value;
    inputNumberBd.value = inputNumber.value;
}

function fechaModal(){
    let modal = document.querySelector('#modal');
    modal.classList.remove('d-flex');
    inputNumber.value = "";
    inputNumber.focus();
}
btnNao.addEventListener('click', fechaModal);

function mostrarModal(){
    let modal = document.querySelector('#modal');
    modal.classList.add('d-flex');
}

document.getElementById("ajudar").addEventListener("click", function(event){
    event.preventDefault();
    btnAjudar = document.querySelector('#ajudar');
    inputPapel = document.querySelector('#papel');
    inputPapel.value = btnAjudar.value;
});

function fMasc(objeto,mascara) {
    obj=objeto
    masc=mascara
    setTimeout("fMascEx()",1)
}

function mTel(tel) {
    tel=tel.replace(/\D/g,"")
    tel=tel.replace(/^(\d)/,"($1")
    tel=tel.replace(/(.{3})(\d)/,"$1)$2")
    if(tel.length == 9) {
        tel=tel.replace(/(.{1})$/,"-$1")
    } else if (tel.length == 10) {
        tel=tel.replace(/(.{2})$/,"-$1")
    } else if (tel.length == 11) {
        tel=tel.replace(/(.{3})$/,"-$1")
    } else if (tel.length == 12) {
        tel=tel.replace(/(.{4})$/,"-$1")
    } else if (tel.length > 12) {
        tel=tel.replace(/(.{4})$/,"-$1")
    }
    return tel;
}

function fMascEx() {
    obj.value=masc(obj.value)
}