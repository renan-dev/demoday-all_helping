const btnProximo = document.querySelector('#btnNext');
const btnNao = document.querySelector('#btnNo');
const btnSim = document.querySelector('#btnYes');

const inputNumber = document.querySelector('.inputNum');

const msgErr = document.querySelector('.msgError');

const num = document.querySelector('#num');

const inputNumberBd = document.querySelector('#inputNumberBd');

btnProximo.onclick = () => {
    if (inputNumber.value === "" || inputNumber.value.length < 11) {
        msgErr.style = "display:block";
        inputNumber.focus();
        return false;
    }
    else{
        msgErr.style = "display:none";
        let modal = document.querySelector('#modal');
        modal.classList.add('d-flex');
    }
    num.innerHTML = inputNumber.value;
    inputNumberBd.value = inputNumber.value;
}

btnNao.onclick = () => {
    let modal = document.querySelector('#modal');
    modal.classList.remove('d-flex');
    inputNumber.value = "";
    inputNumber.focus();
}