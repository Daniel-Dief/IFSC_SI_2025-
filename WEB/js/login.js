const troca_p_criar = document.querySelector("body > main > button.troca.nao-login")
const troca_p_login = document.querySelector("body > main > button.troca.ja-login")
const form_login = document.querySelector("body > main > form.entrar")
const form_criar = document.querySelector("body > main > form.criar-login")

const url = "http://localhost:3000"

troca_p_criar.addEventListener("click", () => {
    troca_p_criar.style.display = "none"
    troca_p_login.style.display = "flex"
    form_criar.style.display = "flex"
    form_login.style.display = "none"
})

troca_p_login.addEventListener("click", () => {
    troca_p_criar.style.display = "flex"
    troca_p_login.style.display = "none"
    form_criar.style.display = "none"
    form_login.style.display = "flex"
})

form_criar.addEventListener("submit", (e) => {
    e.preventDefault()
    const data = new FormData(form_criar)
    const login = data.get("login")
    const senha = data.get("senha")
    const confirmar_senha = data.get("confirmar-senha")
    console.log(JSON.stringify({
        login,
        senha,
        confirmar_senha
    }))
    fetch(`${url}/criar-login`, {
        method: "POST",
        body: JSON.stringify({ login, senha, confirmar_senha }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => {
        if (res.status == 201) {
            alert("Usuário criado com sucesso!")
            form_criar.reset()
            troca_p_criar.click()
        } else {
            alert("erro ao criar usuário")
        }
    })
})

form_login.addEventListener("submit", (e) => {
    e.preventDefault()
    const data = new FormData(form_login)
    const login = data.get("login")
    const senha = data.get("senha")
    console.log(JSON.stringify({ login, senha }))
    fetch(`${url}/login`, {
        method: "POST",
        body: JSON.stringify({ login, senha }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => {
        if (res.status == 200) {
            alert("Login efetuado com sucesso!")
        } else {
            alert("Erro ao fazer login")
        }
    })
})