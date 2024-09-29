document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("loginForm");

  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(loginForm);
    const data = Object.fromEntries(formData.entries());

    fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        if (result.success) {
          alert(result.message);
          localStorage.setItem("isLoggedIn", "true");
          localStorage.setItem("username", result.username);
          window.location.href = "index.html";
        } else {
          alert("登录失败：" + result.message);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("登录过程中发生错误，请稍后再试。");
      });
  });
});
