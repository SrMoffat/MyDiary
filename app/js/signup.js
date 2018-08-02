import { api } from './app';
const signup = document.getElementById("#signupForm")

signup.addEventListener('submit', e =>  {
    e.preventDefault()
    const username = document.querySelector("#username").value
    const email = document.querySelector("#email").value
    const password = document.querySelector("#password").value

    const data = {
        username, 
        email, 
        password 
    }

    api.post('/auth/signup', data)
    .then(res => res)
    .then(data => {
        if(data.message === 'User registered!') {            
            redirect: window.location.replace('./signin.html')
        } else {
            alert("Something went wrong. Signup Again")
        }
    }) 
})