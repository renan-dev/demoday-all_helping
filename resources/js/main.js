const btnProximo = document.querySelector('#btnNext');
const btnNao = document.querySelector('#btnNo');
const btnSim = document.querySelector('#btnYes');
const inputNumber = document.querySelector('.inputNum');
const msgErr = document.querySelector('.msgError');
const modal = document.querySelector('#modal');
const confirmNum = document.querySelector(".numInformado");
const numeroInformado = document.querySelector(".inputNum");

function validaInput() {
    if (inputNumber.value === "" || inputNumber.value.length < 11) {
        msgErr.style = "display:block";
        inputNumber.focus();
        return false;
    }

    confirmNum.textContent = numeroInformado.value;
    addModal();
    return;
}
btnProximo.addEventListener('click', validaInput);

function addModal() {
    modal.classList.add("d-flex");
    msgErr.style = "display:none";
}

function removeModal() {
    modal.classList.remove("d-flex");
    inputNumber.value = "";
    inputNumber.focus();
}
btnNao.addEventListener('click', removeModal);