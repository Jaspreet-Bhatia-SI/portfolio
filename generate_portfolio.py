import os

html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Jaspreet Bhatia — Full-Stack AI Engineer</title>
  
  <!-- CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            mono: ['JetBrains Mono', 'monospace'],
            sans: ['Inter', 'sans-serif'],
          },
          colors: {
            bg: { base: '#050914', surface: '#0a0f1c', card: '#0f1627', elevated: '#161f36' },
            cyan: { 400: '#22d3ee', glow: 'rgba(34,211,238,0.2)' },
            purple: { 500: '#a855f7', glow: 'rgba(168,85,247,0.2)' },
            slate: { border: 'rgba(255,255,255,0.05)' }
          },
          animation: {
            'blob': 'blob 7s infinite',
            'float': 'float 6s ease-in-out infinite',
          },
          keyframes: {
            blob: {
              '0%': { transform: 'translate(0px, 0px) scale(1)' },
              '33%': { transform: 'translate(30px, -50px) scale(1.1)' },
              '66%': { transform: 'translate(-20px, 20px) scale(0.9)' },
              '100%': { transform: 'translate(0px, 0px) scale(1)' }
            },
            float: {
              '0%, 100%': { transform: 'translateY(0)' },
              '50%': { transform: 'translateY(-20px)' },
            }
          }
        }
      }
    }
  </script>

  <style>
    body { background-color: #050914; color: #f8fafc; overflow-x: hidden; }
    .glass-card {
      background: rgba(15, 22, 39, 0.4);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.05);
      transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
      transform: translateY(-5px);
      border-color: rgba(34, 211, 238, 0.3);
      box-shadow: 0 10px 30px rgba(34, 211, 238, 0.1);
    }
    .text-gradient {
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-image: linear-gradient(90deg, #22d3ee, #a855f7);
    }
    .vfx-border {
      position: relative;
    }
    .vfx-border::before {
      content: "";
      position: absolute;
      inset: -2px;
      border-radius: inherit;
      background: linear-gradient(45deg, #22d3ee, #a855f7, #3b82f6);
      z-index: -1;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .vfx-border:hover::before { opacity: 1; filter: blur(10px); }
    #vanta-canvas { position: absolute; z-index: 0; top: 0; left: 0; width: 100%; height: 100%; }
  </style>
</head>
<body class="antialiased selection:bg-cyan-500/30 selection:text-cyan-200">

  <!-- Navbar -->
  <nav class="fixed w-full z-50 top-0 border-b border-white/5 bg-bg-base/70 backdrop-blur-md transition-all duration-300" id="navbar">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
      <a href="#" class="font-bold text-xl tracking-tighter flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-cyan-400 to-purple-500 flex items-center justify-center text-white text-sm">JB</div>
        Jaspreet Bhatia
      </a>
      <div class="hidden md:flex gap-8 text-sm font-medium text-slate-400">
        <a href="#about" class="hover:text-cyan-400 transition-colors">About</a>
        <a href="#skills" class="hover:text-cyan-400 transition-colors">Skills</a>
        <a href="#projects" class="hover:text-cyan-400 transition-colors">Projects</a>
        <a href="#contact" class="hover:text-cyan-400 transition-colors">Contact</a>
      </div>
      <a href="#contact" class="hidden md:flex items-center justify-center px-5 py-2.5 rounded-full bg-white/5 border border-white/10 hover:bg-white/10 text-sm font-medium transition-colors">
        Let's Talk
      </a>
    </div>
  </nav>

  <!-- Hero Section with Vanta.js 3D Background -->
  <section class="relative min-h-screen flex items-center justify-center pt-20 overflow-hidden">
    <div id="vanta-canvas"></div>
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-bg-base/80 to-bg-base z-10 pointer-events-none"></div>
    
    <div class="relative z-20 max-w-5xl mx-auto px-6 text-center" data-aos="fade-up" data-aos-duration="1000">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-400/10 border border-cyan-400/20 text-cyan-400 text-xs font-mono mb-8">
        <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span> Available for new opportunities
      </div>
      <h1 class="text-5xl md:text-7xl font-bold tracking-tight mb-6 leading-tight">
        Architecting the future with <br class="hidden md:block"/>
        <span class="text-gradient">Artificial Intelligence</span>
      </h1>
      <p class="text-lg md:text-xl text-slate-400 max-w-2xl mx-auto mb-10 leading-relaxed">
        I am a Full-Stack AI Engineer & Cloud Architect. I build autonomous agents, scalable SaaS platforms, and enterprise AI solutions under my studio brand, JBSI.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="#projects" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white text-bg-base font-semibold hover:bg-slate-200 transition-colors flex items-center justify-center gap-2">
          View My Work <i class="fa-solid fa-arrow-down"></i>
        </a>
        <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white/5 border border-white/10 text-white font-medium hover:bg-white/10 transition-colors flex items-center justify-center gap-2">
          <i class="fa-brands fa-github text-lg"></i> GitHub
        </a>
      </div>
    </div>
  </section>

  <!-- Skills Matrix -->
  <section id="skills" class="py-24 relative z-20 bg-bg-base">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16" data-aos="fade-up">
        <h2 class="text-3xl md:text-4xl font-bold mb-4">Technical <span class="text-cyan-400">Arsenal</span></h2>
        <p class="text-slate-400 max-w-2xl mx-auto">The tools, languages, and frameworks I use to bring ideas to life.</p>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <!-- AI/ML -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="100">
          <i class="fa-solid fa-brain text-purple-400 text-3xl mb-4"></i>
          <h3 class="font-bold mb-2">AI & Machine Learning</h3>
          <p class="text-sm text-slate-400">TensorFlow, PyTorch, LangChain, RAG Systems, OpenAI & Groq APIs.</p>
        </div>
        <!-- Backend -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="200">
          <i class="fa-solid fa-server text-cyan-400 text-3xl mb-4"></i>
          <h3 class="font-bold mb-2">Backend Architecture</h3>
          <p class="text-sm text-slate-400">Python, FastAPI, Node.js, Express, Microservices, REST & GraphQL.</p>
        </div>
        <!-- Frontend -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="300">
          <i class="fa-brands fa-react text-blue-400 text-3xl mb-4"></i>
          <h3 class="font-bold mb-2">Frontend Engineering</h3>
          <p class="text-sm text-slate-400">React, Next.js, Tailwind CSS, Framer Motion, Flutter.</p>
        </div>
        <!-- Cloud -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="400">
          <i class="fa-brands fa-aws text-orange-400 text-3xl mb-4"></i>
          <h3 class="font-bold mb-2">Cloud & DevOps</h3>
          <p class="text-sm text-slate-400">AWS (EC2, S3), Docker, Nginx, CI/CD pipelines, Linux Admin.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Featured Projects -->
  <section id="projects" class="py-24 relative z-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6" data-aos="fade-up">
        <div>
          <h2 class="text-3xl md:text-5xl font-bold mb-4">Featured <span class="text-purple-400">Projects</span></h2>
          <p class="text-slate-400 max-w-xl">A curated selection of my production-grade applications, AI agents, and visualizers.</p>
        </div>
        <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="text-cyan-400 hover:text-cyan-300 font-medium flex items-center gap-2 group">
          View all on GitHub <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Curator AI -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="100">
          <div class="bg-bg-card rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-cyan-400/10 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-cyan-400 to-purple-500 flex items-center justify-center text-white shadow-lg">
                <i class="fa-solid fa-robot text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/CuratorAI" target="_blank" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold mb-3">Curator AI</h3>
            <p class="text-slate-400 text-sm mb-6 flex-1">An autonomous AI media curator using Groq LLMs & DuckDuckGo RAG to generate educational roadmaps and bypass anti-bot systems for media extraction.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-cyan-300">FastAPI</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-purple-300">React</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-blue-300">Docker</span>
            </div>
          </div>
        </div>

        <!-- Foodzie -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="200">
          <div class="bg-bg-card rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-orange-400/10 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-orange-500/20 text-orange-400 border border-orange-500/20 flex items-center justify-center shadow-lg">
                <i class="fa-solid fa-burger text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/foodzie" target="_blank" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold mb-3">Foodzie Platform</h3>
            <p class="text-slate-400 text-sm mb-6 flex-1">A massive full-stack E-Commerce ecosystem. Includes a Flutter mobile app, Python backend, PostgreSQL database, and integrated Razorpay payments.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-cyan-300">Flutter</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-purple-300">Python</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-orange-300">PostgreSQL</span>
            </div>
          </div>
        </div>

        <!-- Stark AI -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="300">
          <div class="bg-bg-card rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-blue-400/10 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-blue-500/20 text-blue-400 border border-blue-500/20 flex items-center justify-center shadow-lg">
                <i class="fa-solid fa-microchip text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/stark-ai" target="_blank" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold mb-3">Stark AI Assistant</h3>
            <p class="text-slate-400 text-sm mb-6 flex-1">An intelligent desktop voice assistant capable of automating system tasks, fetching live intelligence, and executing natural language commands.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-cyan-300">NLP</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-purple-300">Python</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-green-300">Speech-to-Text</span>
            </div>
          </div>
        </div>

        <!-- ML Tree -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="400">
          <div class="bg-bg-card rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-green-400/10 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-green-500/20 text-green-400 border border-green-500/20 flex items-center justify-center shadow-lg">
                <i class="fa-solid fa-network-wired text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/ml-tree" target="_blank" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold mb-3">ML Tree Visualizer</h3>
            <p class="text-slate-400 text-sm mb-6 flex-1">An interactive node-based architecture mapping 150+ machine learning algorithms, bridging the gap between theoretical data science and practical application.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-cyan-300">D3.js</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-purple-300">Data Science</span>
            </div>
          </div>
        </div>

        <!-- Secure Password Generator -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="500">
          <div class="bg-bg-card rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-red-400/10 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-red-500/20 text-red-400 border border-red-500/20 flex items-center justify-center shadow-lg">
                <i class="fa-solid fa-shield-halved text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/secure-password-generator" target="_blank" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold mb-3">CryptoAuth Generator</h3>
            <p class="text-slate-400 text-sm mb-6 flex-1">A highly secure cryptographic tool for generating unbreakable passwords using entropy algorithms and strict policy enforcements.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-cyan-300">Cryptography</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-purple-300">Security</span>
            </div>
          </div>
        </div>

        <!-- ResQ AI -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="600">
          <div class="bg-bg-card rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-yellow-400/10 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-yellow-500/20 text-yellow-400 border border-yellow-500/20 flex items-center justify-center shadow-lg">
                <i class="fa-solid fa-truck-medical text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/ResQ-AI" target="_blank" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold mb-3">ResQ AI</h3>
            <p class="text-slate-400 text-sm mb-6 flex-1">A machine learning driven emergency response orchestration platform. Optimizes routing and resource allocation for critical situations in real-time.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-cyan-300">AI Routing</span>
              <span class="px-3 py-1 rounded-full bg-white/5 text-xs font-mono text-purple-300">Python</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="py-24 relative z-20">
    <div class="max-w-4xl mx-auto px-6 text-center" data-aos="fade-up">
      <div class="w-20 h-20 rounded-full bg-gradient-to-br from-cyan-400 to-purple-500 mx-auto mb-8 p-1">
        <div class="w-full h-full bg-bg-base rounded-full flex items-center justify-center">
          <i class="fa-solid fa-envelope text-2xl text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-500"></i>
        </div>
      </div>
      <h2 class="text-4xl md:text-5xl font-bold mb-6">Ready to <span class="text-gradient">Collaborate?</span></h2>
      <p class="text-xl text-slate-400 mb-10 max-w-2xl mx-auto">Whether you have a massive AI infrastructure project or need an intelligent web application, my inbox is always open.</p>
      
      <div class="flex flex-wrap justify-center gap-4">
        <a href="mailto:bhatiajaspreet161@gmail.com" class="px-8 py-4 rounded-full bg-white text-bg-base font-bold hover:bg-slate-200 transition-colors flex items-center gap-2">
          Say Hello <i class="fa-solid fa-paper-plane"></i>
        </a>
      </div>
      
      <div class="flex justify-center gap-6 mt-16 border-t border-white/5 pt-10">
        <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="w-12 h-12 rounded-full bg-white/5 hover:bg-white/10 flex items-center justify-center text-slate-400 hover:text-white transition-all hover:-translate-y-1">
          <i class="fa-brands fa-github text-xl"></i>
        </a>
        <a href="https://linkedin.com/in/jaspreet-bhatia-si" target="_blank" class="w-12 h-12 rounded-full bg-white/5 hover:bg-white/10 flex items-center justify-center text-slate-400 hover:text-blue-400 transition-all hover:-translate-y-1">
          <i class="fa-brands fa-linkedin text-xl"></i>
        </a>
        <a href="https://instagram.com/jass_bhatia.si" target="_blank" class="w-12 h-12 rounded-full bg-white/5 hover:bg-white/10 flex items-center justify-center text-slate-400 hover:text-pink-500 transition-all hover:-translate-y-1">
          <i class="fa-brands fa-instagram text-xl"></i>
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="py-8 text-center text-slate-500 text-sm border-t border-white/5 relative z-20 bg-bg-base">
    <p>&copy; 2026 Jaspreet Bhatia (JBSI). Engineered with precision.</p>
  </footer>

  <!-- Scripts -->
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.net.min.js"></script>
  
  <script>
    // Initialize Scroll Animations
    AOS.init({
      once: true,
      offset: 50,
      duration: 800,
      easing: 'ease-out-cubic',
    });

    // Initialize Vanta 3D Background
    VANTA.NET({
      el: "#vanta-canvas",
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.00,
      minWidth: 200.00,
      scale: 1.00,
      scaleMobile: 1.00,
      color: 0x22d3ee,
      backgroundColor: 0x050914,
      points: 12.00,
      maxDistance: 22.00,
      spacing: 18.00,
      showDots: true
    });

    // Navbar Scroll Effect
    window.addEventListener('scroll', () => {
      const nav = document.getElementById('navbar');
      if (window.scrollY > 50) {
        nav.classList.add('shadow-lg', 'shadow-cyan-500/5', 'bg-bg-base/90');
      } else {
        nav.classList.remove('shadow-lg', 'shadow-cyan-500/5', 'bg-bg-base/90');
      }
    });
  </script>
</body>
</html>
"""

with open('portfolio.html', 'w') as f:
    f.write(html_content)

