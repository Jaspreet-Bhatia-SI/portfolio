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
            bg: { base: '#f8fafc', surface: '#ffffff', card: '#ffffff', elevated: '#f1f5f9' },
            accent: { 400: '#3b82f6', glow: 'rgba(59,130,246,0.2)' },
            purple: { 500: '#8b5cf6', glow: 'rgba(139,92,246,0.2)' },
            slate: { border: 'rgba(0,0,0,0.05)' }
          }
        }
      }
    }
  </script>

  <style>
    body { background-color: #f8fafc; color: #0f172a; overflow-x: hidden; }
    .glass-card {
      background: rgba(255, 255, 255, 0.7);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(0, 0, 0, 0.05);
      transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
      transform: translateY(-5px);
      border-color: rgba(59, 130, 246, 0.3);
      box-shadow: 0 10px 30px rgba(59, 130, 246, 0.1);
    }
    .text-gradient {
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-image: linear-gradient(90deg, #3b82f6, #8b5cf6);
    }
    .vfx-border {
      position: relative;
    }
    .vfx-border::before {
      content: "";
      position: absolute;
      inset: -2px;
      border-radius: inherit;
      background: linear-gradient(45deg, #3b82f6, #8b5cf6, #ec4899);
      z-index: -1;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .vfx-border:hover::before { opacity: 1; filter: blur(12px); }
    #vanta-canvas { position: absolute; z-index: 0; top: 0; left: 0; width: 100%; height: 100%; }
  </style>
</head>
<body class="antialiased selection:bg-blue-500/20 selection:text-blue-900">

  <!-- Navbar -->
  <nav class="fixed w-full z-50 top-0 border-b border-black/5 bg-white/70 backdrop-blur-md transition-all duration-300" id="navbar">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
      <a href="#" class="font-bold text-xl tracking-tighter flex items-center gap-2 text-slate-900">
        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-purple-500 flex items-center justify-center text-white text-sm">JB</div>
        Jaspreet Bhatia
      </a>
      <div class="hidden md:flex gap-8 text-sm font-medium text-slate-500">
        <a href="#about" class="hover:text-blue-600 transition-colors">About</a>
        <a href="#skills" class="hover:text-blue-600 transition-colors">Skills</a>
        <a href="#projects" class="hover:text-blue-600 transition-colors">Projects</a>
        <a href="#contact" class="hover:text-blue-600 transition-colors">Contact</a>
      </div>
      <a href="#contact" class="hidden md:flex items-center justify-center px-5 py-2.5 rounded-full bg-slate-100 border border-slate-200 hover:bg-slate-200 text-slate-900 text-sm font-medium transition-colors">
        Let's Talk
      </a>
    </div>
  </nav>

  <!-- Hero Section with Vanta.js 3D Background -->
  <section class="relative min-h-screen flex items-center justify-center pt-20 overflow-hidden">
    <div id="vanta-canvas"></div>
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-bg-base/80 to-bg-base z-10 pointer-events-none"></div>
    
    <div class="relative z-20 max-w-5xl mx-auto px-6 text-center" data-aos="fade-up" data-aos-duration="1000">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-600 text-xs font-mono mb-8">
        <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span> Available for new opportunities
      </div>
      <h1 class="text-5xl md:text-7xl font-bold tracking-tight mb-6 leading-tight text-slate-900">
        Architecting the future with <br class="hidden md:block"/>
        <span class="text-gradient">Artificial Intelligence</span>
      </h1>
      <p class="text-lg md:text-xl text-slate-600 max-w-2xl mx-auto mb-10 leading-relaxed">
        I am a Full-Stack AI Engineer & Cloud Architect. I build autonomous agents, scalable SaaS platforms, and enterprise AI solutions under my studio brand, JBSI.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="#projects" class="w-full sm:w-auto px-8 py-4 rounded-full bg-slate-900 text-white font-semibold hover:bg-slate-800 transition-colors flex items-center justify-center gap-2 shadow-lg shadow-slate-900/20">
          View My Work <i class="fa-solid fa-arrow-down"></i>
        </a>
        <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white border border-slate-200 text-slate-700 font-medium hover:bg-slate-50 transition-colors flex items-center justify-center gap-2 shadow-sm">
          <i class="fa-brands fa-github text-lg"></i> GitHub
        </a>
      </div>
    </div>
  </section>

  <!-- Skills Matrix -->
  <section id="skills" class="py-24 relative z-20 bg-bg-base">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16" data-aos="fade-up">
        <h2 class="text-3xl md:text-4xl font-bold mb-4 text-slate-900">Technical <span class="text-blue-500">Arsenal</span></h2>
        <p class="text-slate-500 max-w-2xl mx-auto">The tools, languages, and frameworks I use to bring ideas to life.</p>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <!-- AI/ML -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="100">
          <i class="fa-solid fa-brain text-purple-500 text-3xl mb-4"></i>
          <h3 class="font-bold text-slate-800 mb-2">AI & Machine Learning</h3>
          <p class="text-sm text-slate-500">TensorFlow, PyTorch, LangChain, RAG Systems, OpenAI & Groq APIs.</p>
        </div>
        <!-- Backend -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="200">
          <i class="fa-solid fa-server text-blue-500 text-3xl mb-4"></i>
          <h3 class="font-bold text-slate-800 mb-2">Backend Architecture</h3>
          <p class="text-sm text-slate-500">Python, FastAPI, Node.js, Express, Microservices, REST & GraphQL.</p>
        </div>
        <!-- Frontend -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="300">
          <i class="fa-brands fa-react text-sky-500 text-3xl mb-4"></i>
          <h3 class="font-bold text-slate-800 mb-2">Frontend Engineering</h3>
          <p class="text-sm text-slate-500">React, Next.js, Tailwind CSS, Framer Motion, Flutter.</p>
        </div>
        <!-- Cloud -->
        <div class="glass-card p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="400">
          <i class="fa-brands fa-aws text-orange-500 text-3xl mb-4"></i>
          <h3 class="font-bold text-slate-800 mb-2">Cloud & DevOps</h3>
          <p class="text-sm text-slate-500">AWS (EC2, S3), Docker, Nginx, CI/CD pipelines, Linux Admin.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Featured Projects -->
  <section id="projects" class="py-24 relative z-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6" data-aos="fade-up">
        <div>
          <h2 class="text-3xl md:text-5xl font-bold mb-4 text-slate-900">Featured <span class="text-purple-500">Projects</span></h2>
          <p class="text-slate-500 max-w-xl">A curated selection of my production-grade applications, AI agents, and visualizers.</p>
        </div>
        <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="text-blue-600 hover:text-blue-700 font-medium flex items-center gap-2 group">
          View all on GitHub <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Curator AI -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="100">
          <div class="bg-white rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-blue-100 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-purple-500 flex items-center justify-center text-white shadow-md">
                <i class="fa-solid fa-robot text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/CuratorAI" target="_blank" class="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-slate-100 transition-colors text-slate-600">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">Curator AI</h3>
            <p class="text-slate-500 text-sm mb-6 flex-1">An autonomous AI media curator using Groq LLMs & DuckDuckGo RAG to generate educational roadmaps and bypass anti-bot systems for media extraction.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-blue-50 text-xs font-mono text-blue-600 border border-blue-100">FastAPI</span>
              <span class="px-3 py-1 rounded-full bg-purple-50 text-xs font-mono text-purple-600 border border-purple-100">React</span>
              <span class="px-3 py-1 rounded-full bg-sky-50 text-xs font-mono text-sky-600 border border-sky-100">Docker</span>
            </div>
          </div>
        </div>

        <!-- Foodzie -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="200">
          <div class="bg-white rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-orange-100 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-500 border border-orange-200 flex items-center justify-center shadow-sm">
                <i class="fa-solid fa-burger text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/foodzie" target="_blank" class="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-slate-100 transition-colors text-slate-600">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">Foodzie Platform</h3>
            <p class="text-slate-500 text-sm mb-6 flex-1">A massive full-stack E-Commerce ecosystem. Includes a Flutter mobile app, Python backend, PostgreSQL database, and integrated Razorpay payments.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-sky-50 text-xs font-mono text-sky-600 border border-sky-100">Flutter</span>
              <span class="px-3 py-1 rounded-full bg-blue-50 text-xs font-mono text-blue-600 border border-blue-100">Python</span>
              <span class="px-3 py-1 rounded-full bg-orange-50 text-xs font-mono text-orange-600 border border-orange-100">PostgreSQL</span>
            </div>
          </div>
        </div>

        <!-- Stark AI -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="300">
          <div class="bg-white rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-blue-100 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-blue-100 text-blue-600 border border-blue-200 flex items-center justify-center shadow-sm">
                <i class="fa-solid fa-microchip text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/stark-ai" target="_blank" class="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-slate-100 transition-colors text-slate-600">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">Stark AI Assistant</h3>
            <p class="text-slate-500 text-sm mb-6 flex-1">An intelligent desktop voice assistant capable of automating system tasks, fetching live intelligence, and executing natural language commands.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-purple-50 text-xs font-mono text-purple-600 border border-purple-100">NLP</span>
              <span class="px-3 py-1 rounded-full bg-blue-50 text-xs font-mono text-blue-600 border border-blue-100">Python</span>
              <span class="px-3 py-1 rounded-full bg-emerald-50 text-xs font-mono text-emerald-600 border border-emerald-100">Speech-to-Text</span>
            </div>
          </div>
        </div>

        <!-- ML Tree -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="400">
          <div class="bg-white rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-emerald-100 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-emerald-100 text-emerald-600 border border-emerald-200 flex items-center justify-center shadow-sm">
                <i class="fa-solid fa-network-wired text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/ml-tree" target="_blank" class="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-slate-100 transition-colors text-slate-600">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">ML Tree Visualizer</h3>
            <p class="text-slate-500 text-sm mb-6 flex-1">An interactive node-based architecture mapping 150+ machine learning algorithms, bridging the gap between theoretical data science and practical application.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-orange-50 text-xs font-mono text-orange-600 border border-orange-100">D3.js</span>
              <span class="px-3 py-1 rounded-full bg-purple-50 text-xs font-mono text-purple-600 border border-purple-100">Data Science</span>
            </div>
          </div>
        </div>

        <!-- Secure Password Generator -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="500">
          <div class="bg-white rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-rose-100 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-rose-100 text-rose-500 border border-rose-200 flex items-center justify-center shadow-sm">
                <i class="fa-solid fa-shield-halved text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/secure-password-generator" target="_blank" class="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-slate-100 transition-colors text-slate-600">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">CryptoAuth Generator</h3>
            <p class="text-slate-500 text-sm mb-6 flex-1">A highly secure cryptographic tool for generating unbreakable passwords using entropy algorithms and strict policy enforcements.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-slate-100 text-xs font-mono text-slate-700 border border-slate-200">Cryptography</span>
              <span class="px-3 py-1 rounded-full bg-red-50 text-xs font-mono text-red-600 border border-red-100">Security</span>
            </div>
          </div>
        </div>

        <!-- ResQ AI -->
        <div class="glass-card vfx-border rounded-3xl p-1 flex flex-col group cursor-pointer" data-aos="fade-up" data-aos-delay="600">
          <div class="bg-white rounded-[22px] p-6 h-full flex flex-col relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-yellow-100 blur-3xl rounded-full"></div>
            <div class="flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-xl bg-yellow-100 text-yellow-600 border border-yellow-200 flex items-center justify-center shadow-sm">
                <i class="fa-solid fa-truck-medical text-xl"></i>
              </div>
              <a href="https://github.com/Jaspreet-Bhatia-SI/ResQ-AI" target="_blank" class="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-slate-100 transition-colors text-slate-600">
                <i class="fa-brands fa-github"></i>
              </a>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">ResQ AI</h3>
            <p class="text-slate-500 text-sm mb-6 flex-1">A machine learning driven emergency response orchestration platform. Optimizes routing and resource allocation for critical situations in real-time.</p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="px-3 py-1 rounded-full bg-blue-50 text-xs font-mono text-blue-600 border border-blue-100">AI Routing</span>
              <span class="px-3 py-1 rounded-full bg-indigo-50 text-xs font-mono text-indigo-600 border border-indigo-100">Python</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="py-24 relative z-20">
    <div class="max-w-4xl mx-auto px-6 text-center" data-aos="fade-up">
      <div class="w-20 h-20 rounded-full bg-gradient-to-br from-blue-500 to-purple-500 mx-auto mb-8 p-1 shadow-lg shadow-purple-500/20">
        <div class="w-full h-full bg-white rounded-full flex items-center justify-center">
          <i class="fa-solid fa-envelope text-2xl text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-purple-500"></i>
        </div>
      </div>
      <h2 class="text-4xl md:text-5xl font-bold mb-6 text-slate-900">Ready to <span class="text-gradient">Collaborate?</span></h2>
      <p class="text-xl text-slate-500 mb-10 max-w-2xl mx-auto">Whether you have a massive AI infrastructure project or need an intelligent web application, my inbox is always open.</p>
      
      <div class="flex flex-wrap justify-center gap-4">
        <a href="mailto:bhatiajaspreet161@gmail.com" class="px-8 py-4 rounded-full bg-slate-900 text-white font-bold hover:bg-slate-800 transition-colors flex items-center gap-2 shadow-lg shadow-slate-900/20">
          Say Hello <i class="fa-solid fa-paper-plane"></i>
        </a>
      </div>
      
      <div class="flex justify-center gap-6 mt-16 border-t border-black/5 pt-10">
        <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="w-12 h-12 rounded-full bg-slate-100 border border-slate-200 hover:bg-slate-200 flex items-center justify-center text-slate-600 hover:text-slate-900 transition-all hover:-translate-y-1">
          <i class="fa-brands fa-github text-xl"></i>
        </a>
        <a href="https://linkedin.com/in/jaspreet-bhatia-si" target="_blank" class="w-12 h-12 rounded-full bg-slate-100 border border-slate-200 hover:bg-slate-200 flex items-center justify-center text-slate-600 hover:text-blue-600 transition-all hover:-translate-y-1">
          <i class="fa-brands fa-linkedin text-xl"></i>
        </a>
        <a href="https://instagram.com/jass_bhatia.si" target="_blank" class="w-12 h-12 rounded-full bg-slate-100 border border-slate-200 hover:bg-slate-200 flex items-center justify-center text-slate-600 hover:text-pink-600 transition-all hover:-translate-y-1">
          <i class="fa-brands fa-instagram text-xl"></i>
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="py-8 text-center text-slate-400 text-sm border-t border-black/5 relative z-20 bg-white">
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

    // Initialize Vanta 3D Background - LIGHT MODE
    VANTA.NET({
      el: "#vanta-canvas",
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.00,
      minWidth: 200.00,
      scale: 1.00,
      scaleMobile: 1.00,
      color: 0x3b82f6,
      backgroundColor: 0xf8fafc,
      points: 12.00,
      maxDistance: 22.00,
      spacing: 18.00,
      showDots: true
    });

    // Navbar Scroll Effect
    window.addEventListener('scroll', () => {
      const nav = document.getElementById('navbar');
      if (window.scrollY > 50) {
        nav.classList.add('shadow-md', 'shadow-slate-200/50', 'bg-white/90');
      } else {
        nav.classList.remove('shadow-md', 'shadow-slate-200/50', 'bg-white/90');
      }
    });
  </script>
</body>
</html>
"""

with open('portfolio.html', 'w') as f:
    f.write(html_content)

