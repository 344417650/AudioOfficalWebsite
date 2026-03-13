document.addEventListener('DOMContentLoaded', () => {
    // Custom Cursor Logic
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');
    let mouseX = 0;
    let mouseY = 0;
    let outlineX = 0;
    let outlineY = 0;

    // Listen to mouse movement
    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        // Instant dot movement
        cursorDot.style.left = `${mouseX}px`;
        cursorDot.style.top = `${mouseY}px`;
    });

    // Smooth outline movement loop
    function animateCursor() {
        // Easing function for smooth follow
        let distX = mouseX - outlineX;
        let distY = mouseY - outlineY;
        
        outlineX += distX * 0.15;
        outlineY += distY * 0.15;
        
        cursorOutline.style.left = `${outlineX}px`;
        cursorOutline.style.top = `${outlineY}px`;
        
        requestAnimationFrame(animateCursor);
    }
    animateCursor();

    // Add hover state for interactive elements
    const iteractables = document.querySelectorAll('a, button, .accent-text, .gallery-item, .service-card');
    iteractables.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursorOutline.classList.add('hovering');
        });
        el.addEventListener('mouseleave', () => {
            cursorOutline.classList.remove('hovering');
        });
    });

    // Scroll Animations using Intersection Observer
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: stop observing once revealed
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.gallery-item, .service-card, .testimonial h2, .testimonial p, .client-brand');
    
    // Add base classes for new animated elements if not set in CSS
    document.querySelectorAll('.service-card, .testimonial h2, .testimonial p, .client-brand').forEach(el => {
        el.classList.add('fade-in-scroll');
    });

    animatedElements.forEach(item => {
        observer.observe(item);
    });

    // Simple Parallax Effect on Scroll
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        
        // Parallax for gallery items
        const parallaxItems = document.querySelectorAll('.gallery-item[data-speed]');
        parallaxItems.forEach(item => {
            const speed = parseFloat(item.getAttribute('data-speed'));
            // small movement based on scroll
            const yPos = -(scrolled * speed * 0.05);
            // Apply parallax but preserve the base layout transform behavior
            if (item.classList.contains('visible')) {
                item.style.transform = `translateY(${yPos}px)`;
            }
        });

        // Parallax for Geometric Shape
        const shape = document.querySelector('.geometric-shape');
        if (shape) {
            shape.style.transform = `translateY(calc(-50% + ${scrolled * 0.2}px))`;
        }
    });

    // --- Mobile Nav Drawer (checkbox-driven, JS only handles closing) ---
    const navToggle = document.getElementById('nav-toggle');

    function closeDrawer() {
        if (navToggle) navToggle.checked = false;
    }

    // Close when tapping drawer links or sub-tabs
    document.querySelectorAll('.drawer-item, .drawer-sub-item').forEach(el => {
        el.addEventListener('click', closeDrawer);
    });

    console.log("Luminium Studio: Audio Player Initialized.");

    // --- Magnetic Button Effect ---
    const magneticElements = document.querySelectorAll('.explore-btn, .primary-btn, .secondary-btn');
    
    magneticElements.forEach((el) => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            // Move the button slightly towards the mouse
            gsap.to(el, {
                x: x * 0.4,
                y: y * 0.4,
                duration: 0.4,
                ease: 'power2.out'
            });
        });

        el.addEventListener('mouseleave', () => {
            // Reset to original position
            gsap.to(el, {
                x: 0,
                y: 0,
                duration: 0.6,
                ease: 'elastic.out(1, 0.3)'
            });
        });
    });

    // --- WebGL Particle Background (Three.js) ---
    const canvas = document.querySelector('#webgl-canvas');
    if (canvas && window.THREE) {
        const scene = new THREE.Scene();
        // create foggy cinematic atmosphere
        scene.fog = new THREE.FogExp2(0x050505, 0.001);

        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
        
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        // Create particles
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 1500;
        
        const posArray = new Float32Array(particlesCount * 3);
        const colorsArray = new Float32Array(particlesCount * 3);
        
        const colorAccent = new THREE.Color(0xff3c00);
        const colorWhite = new THREE.Color(0xffffff);

        for(let i = 0; i < particlesCount * 3; i+=3) {
            // Spread particles across a wide volume
            posArray[i] = (Math.random() - 0.5) * 20;     // x
            posArray[i+1] = (Math.random() - 0.5) * 20;   // y
            posArray[i+2] = (Math.random() - 0.5) * 15;   // z

            // Mix orange accent and white/grey particles
            const mixColor = Math.random() > 0.8 ? colorAccent : colorWhite;
            const intensity = Math.random() * 0.5 + 0.1; // Dim them out slightly for subtlety
            
            colorsArray[i] = mixColor.r * intensity;
            colorsArray[i+1] = mixColor.g * intensity;
            colorsArray[i+2] = mixColor.b * intensity;
        }

        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colorsArray, 3));

        // Create magical/cinematic particle material
        const particlesMaterial = new THREE.PointsMaterial({
            size: 0.03,
            vertexColors: true,
            blending: THREE.AdditiveBlending,
            transparent: true,
            opacity: 0.8
        });

        const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particlesMesh);

        camera.position.z = 5;

        // Mouse interaction with particles
        let targetX = 0;
        let targetY = 0;
        const windowHalfX = window.innerWidth / 2;
        const windowHalfY = window.innerHeight / 2;

        document.addEventListener('mousemove', (event) => {
            targetX = (event.clientX - windowHalfX) * 0.001;
            targetY = (event.clientY - windowHalfY) * 0.001;
        });

        // Animation Loop
        const clock = new THREE.Clock();

        const tick = () => {
            const elapsedTime = clock.getElapsedTime();

            // Slowly rotate the entire particle cloud
            particlesMesh.rotation.y = elapsedTime * 0.05;
            particlesMesh.rotation.x = elapsedTime * 0.02;

            // Ease camera movement based on mouse position
            camera.position.x += (targetX - camera.position.x) * 0.05;
            camera.position.y += (-targetY - camera.position.y) * 0.05;
            camera.lookAt(scene.position);

            renderer.render(scene, camera);
            window.requestAnimationFrame(tick);
        };

        tick();

        // Handle Resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    }

});
