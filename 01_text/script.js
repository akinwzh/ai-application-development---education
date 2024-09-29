document.addEventListener("DOMContentLoaded", function () {
  // 汉堡菜单
  const hamburger = document.querySelector(".hamburger-menu");
  const navLinks = document.querySelector(".nav-links");

  hamburger.addEventListener("click", function () {
    navLinks.classList.toggle("active");
  });

  // AI教育解决方案展示
  const solutions = [
    { name: "智能批改作业", description: "AI 技术自动批改作业，提高教师效率" },
    {
      name: "自动推荐学习路径",
      description: "基于学生个人情况，AI 智能推荐最佳学习路径",
    },
    {
      name: "情绪识别辅助教学",
      description: "AI 分析学生情绪，帮助教师调整教学策略",
    },
  ];

  const solutionsSection = document.querySelector("#solutions");
  solutions.forEach((solution) => {
    const solutionElement = document.createElement("div");
    solutionElement.classList.add("solution-card");
    solutionElement.innerHTML = `
      <h3>${solution.name}</h3>
      <p>${solution.description}</p>
    `;
    solutionsSection.appendChild(solutionElement);
  });

  // 检查登录状态
  function checkLoginStatus() {
    const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
    const loginBtn = document.querySelector(".login-btn");
    const registerBtn = document.querySelector(".register-btn");
    const userInfo = document.getElementById("userInfo");
    const usernameSpan = document.getElementById("username");

    if (isLoggedIn) {
      loginBtn.textContent = "退出";
      loginBtn.href = "#";
      loginBtn.addEventListener("click", function (e) {
        e.preventDefault();
        localStorage.removeItem("isLoggedIn");
        localStorage.removeItem("username");
        window.location.reload();
      });
      registerBtn.style.display = "none";
      userInfo.style.display = "inline";
      usernameSpan.textContent = localStorage.getItem("username");
    } else {
      loginBtn.textContent = "登录";
      loginBtn.href = "login.html";
      registerBtn.style.display = "inline-block";
      userInfo.style.display = "none";
    }
  }

  checkLoginStatus();

  // 添加聊天机器人链接的点击事件处理
  const chatbotLink = document.getElementById("chatbotLink");
  chatbotLink.addEventListener("click", function (e) {
    e.preventDefault();
    const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
    if (isLoggedIn) {
      window.open("http://localhost:8501/", "_blank");
    } else {
      alert("请先登录后再访问聊天机器人。");
      window.location.href = "login.html";
    }
  });

  // 初始化轮播图
  const swiper = new Swiper(".swiper-container", {
    loop: true,
    // 删除或注释掉 pagination 选项
    // pagination: {
    //   el: ".swiper-pagination",
    //   clickable: true,
    // },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
  });

  console.log("Swiper initialized:", swiper); // 添加这行来检查 Swiper 是否正确初始化

  // 这里可以添加更多的交互效果，如动态加载成功案例等
});
