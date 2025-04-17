const form = document.querySelector(".send-form")
const input = document.querySelector("#message-input")
const url = "http://localhost:3000"
const login = localStorage.getItem("login")
const chat  = document.querySelector(".messages")

form.addEventListener("submit", (e) => {
    e.preventDefault();
    fetch(`${url}/mensagens`, {
        method: "POST",
        body: JSON.stringify({ login, mensagem: input.value }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => {
        if (res.status == 201) {
            form.reset()
        } else {
            alert("Erro ao enviar a mensagem!")
        }
    })
})

setInterval(async () => {
    if(chat.scrollHeight - chat.scrollTop <= chat.clientHeight + 1){
        await fetch(`${url}/mensagens`)
            .then(res => res.json())
            .then(data => {
                chat.innerHTML = ""
                data.forEach(msg => {
                    const div = document.createElement("div")
                    div.classList.add("message")
                    div.classList.add(msg.login == login ? "mine" : "other")
                    div.innerHTML = `
                        <strong>${msg.login}</strong>
                        <p>${msg.mensagem}</p>
                        <span>${new Date(msg.dataHora).toLocaleString()}</span>
                    `
                    chat.appendChild(div)
            })
        })
        chat.scrollTop = chat.scrollHeight;
    }
}, 1000)