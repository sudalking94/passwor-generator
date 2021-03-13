const button = document.querySelector("button");

function handleCheckBox(e) {
    const checked= document.querySelectorAll("input[type='checkbox']:checked.js-required");    
    if (checked.length == 0) {
        alert("적어도 한개를 체크해야 합니다.");
        e.preventDefault();
    }
}

function init() {
    button.addEventListener("click", handleCheckBox);
}

init()