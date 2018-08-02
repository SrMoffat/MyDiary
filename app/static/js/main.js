// main.js
const addPost = () => {
    fetch("http://127.0.0.1:5000/api/v2/auth/signup", {
        method: "POST",
        body:JSON.stringify({
            username: document.getElementById("username").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        })
    })
}