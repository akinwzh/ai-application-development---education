document.addEventListener("DOMContentLoaded", function () {
  const registerForm = document.getElementById("registerForm");

  registerForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(registerForm);
    const data = Object.fromEntries(formData.entries());

    if (data.password !== data.confirmPassword) {
      alert("密码和确认密码不匹配");
      return;
    }

    fetch("http://127.0.0.1:5000/register", {
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
          window.location.href = "login.html";
        } else {
          alert("注册失败：" + result.message);
        }
      })
      .catch((error) => {
        console.error("Register error:", error);
        alert("注册过程中发生错误，请稍后再试。");
      });
  });
});
