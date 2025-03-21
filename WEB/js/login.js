const troca_p_criar = document.querySelector("body > main > button.troca.nao-login")
const troca_p_login = document.querySelector("body > main > button.troca.ja-login")

troca_p_criar.addEventListener("click", () => {
    troca_p_criar.style.display = "none"
    troca_p_login.style.display = "flex"
})