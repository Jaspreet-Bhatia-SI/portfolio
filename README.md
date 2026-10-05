<div align="center">
  <h1>🎮 JBSI 3D Portfolio Experience</h1>
  <p><strong>A fully playable WebGL survival-game portfolio built with Three.js.</strong></p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
</p>

---

## 🚀 Overview

Welcome to my developer portfolio—reimagined as an interactive 3D WebGL game! 

Instead of scrolling through a standard webpage, you are dropped into a virtual town inspired by Erangel. You can drive a Ferrari supercar, explore the village, dynamically toggle between Day, Evening, and Night modes, and walk into buildings to read about my software engineering projects and technical skills.

## ✨ Features

- **🏎️ Dynamic Vehicle Physics:** Drive a 3D supercar with acceleration, friction, and responsive steering mechanics.
- **🏃‍♂️ 3rd Person Character Controller:** Get out of your car and explore the town on foot. Features custom walking/running animations and interactions.
- **🏠 Interactive Buildings:** Enter different houses across the map. Each house represents a specific project or skill (Frontend, Backend, AI, Mobile Dev).
- **📖 In-Game UI Overlays:** Sit on the couch inside a building and read magazines that pull up interactive HTML/CSS overlays containing detailed project specs.
- **🗺️ Live Minimap:** Real-time 2D Canvas minimap that tracks your coordinates, rotation, and surrounding architecture.
- **🌅 Dynamic Day/Night Cycle:** Seamlessly transition between bright daylight, a pinkish evening sunset, and a moonlit starry night.
- **📱 Responsive Mobile Support:** Includes virtual joysticks and touch buttons so the game is fully playable on phones and tablets.

## 🕹️ Controls

| Action | PC (Keyboard & Mouse) | Mobile (Touch) |
| :--- | :--- | :--- |
| **Move / Drive** | `W`, `A`, `S`, `D` | Left Virtual Joystick |
| **Look Around** | `Mouse Move` | Right Screen Drag |
| **Enter/Exit Car or House** | `F` | On-screen "Loot" button |
| **Read Magazine / Sit** | `E` | On-screen "Read" button |

## 🛠️ Architecture

This project is built to run entirely in the browser using a lightweight stack, served natively via Docker.
- **Rendering Engine:** [Three.js](https://threejs.org/)
- **UI Framework:** [Tailwind CSS](https://tailwindcss.com/)
- **Icons:** [Iconify (Solar Icons)](https://iconify.design/)
- **Deployment:** Dockerized Nginx Alpine server deployed on AWS EC2.

## 🐳 Running Locally (Docker)

If you'd like to run the portfolio locally, you can use the provided Docker configuration.

```bash
# Clone the repository
git clone https://github.com/Jaspreet-Bhatia-SI/portfolio.git

# Navigate to the directory
cd portfolio

# Build and run the container in detached mode
docker-compose up -d --build
```
The game will be running on `http://localhost:8086`.

## 🌍 Connect With Me

- **LinkedIn:** [linkedin.com/in/jaspreet-bhatia-si](https://linkedin.com/in/jaspreet-bhatia-si)
- **Email:** [bhatiajaspreet161@gmail.com](mailto:bhatiajaspreet161@gmail.com)
- **GitHub:** [@Jaspreet-Bhatia-SI](https://github.com/Jaspreet-Bhatia-SI)
- **Instagram:** [@jass_bhatia.si](https://instagram.com/jass_bhatia.si)

<br/>

<div align="center">
  <i>© 2026 JBSI Technologies. All rights reserved.</i>
</div>
