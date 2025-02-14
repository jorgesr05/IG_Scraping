document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    
    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            fetch("/api/token/", {  
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ 
                    username: document.getElementById("username").value,
                    password: document.getElementById("password").value 
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log("Respuesta del backend:", data);  // 🔥 Verifica la respuesta en la consola
                // console.log("✅ Token recibido:", data.access);  // 🔥 Verifica si el token llega bien
                if (data.access) {
                    console.log("✅ Intentando guardar el token...");
                    console.log("✅ Token recibido:", data.access);  // 🔥 Verificar en consola
                    localStorage.setItem("token", data.access);  // 🔥 Guardar token en localStorage
                    // document.cookie = `sessionid=${data.access}; path=/`;  // 🔥 Guarda el token en cookies también
                    console.log("Token guardado en localStorage:", localStorage.getItem("token"));  // 🔥 Verificar en consola
                    
                    // const urlParams = new URLSearchParams(window.location.search);
                    // const nextUrl = urlParams.get("next") || "/dashboard/";
                    
                    window.location.href = "/dashboard/";
                    // window.location.href = nextUrl;
                    


                } else {
                    console.error("Error: No se recibió el token.");
                    alert("Usuario o contraseña incorrectos.");
                }
            })
            .catch(error => console.error("Error en la autenticación:", error));
        });
    }
});







