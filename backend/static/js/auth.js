document.getElementById("registerForm")?.addEventListener("submit", function(e) {
  e.preventDefault();

  let user = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value
  };

  localStorage.setItem("user", JSON.stringify(user));

  alert("Registered successfully!");
  window.location.href = "/";
});

document.getElementById("loginForm")?.addEventListener("submit", function(e) {
  e.preventDefault();

  let savedUser = JSON.parse(localStorage.getItem("user"));

  let email = document.getElementById("loginEmail").value;
  let password = document.getElementById("loginPassword").value;

  if (savedUser && email === savedUser.email && password === savedUser.password) {
    alert("Login successful!");
    localStorage.setItem("loggedIn", "true");
    window.location.href = "home.html";
  } else {
    alert("Wrong email or password");
  }
});