import express from 'express';
import cors from 'cors';

const app = express();
const port = 3000;
app.use(express.json());
app.use(cors());

interface Login {
    login: string;
    senha: string;
}

const loginDeUsuarios : Login[] = [
    {
        login: 'admin',
        senha: 'admin'
    }
]

app.post('/login', (req, res) => {
    const { login, senha } = req.body;

    const user = loginDeUsuarios.find(user => {
        if(user.login == login && user.senha == senha) {
            console.log(user.login, user.senha)
            return user;
        }
    });

    if(user) {
        res.status(200).json({
            message: 'Usuário logado com sucesso'
        });
    } else {
        res.status(401).json({
            message: 'Usuário ou senha inválidos'
        });
    }
});

app.post('/criar-login', (req, res) => {
    const { login, senha, confirmar_senha } = req.body;

    if(senha !== confirmar_senha) {
        res.status(400).json({
            message: 'As senhas não são iguais'
        });
    }

    loginDeUsuarios.push({
        login,
        senha
    });

    res.status(201).json({
        message: 'Usuário criado com sucesso'
    })
});

app.listen(port, () => {
    console.log(`Url: http://localhost:${port}`);
});