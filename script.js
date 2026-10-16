// Función para crear el gráfico de rendimiento en el hero
function createPerformanceChart() {
    const canvas = document.getElementById('performanceChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.offsetWidth;
    const height = canvas.height = canvas.offsetHeight;
    
    // Configuración del gráfico
    const padding = 40;
    const graphWidth = width - padding * 2;
    const graphHeight = height - padding * 2;
    
    // Datos de ejemplo para el gráfico (escala y rendimiento)
    const dataPoints = [
        { x: 25, y: 50 },
        { x: 50, y: 80 },
        { x: 100, y: 120 },
        { x: 200, y: 180 },
        { x: 300, y: 250 },
        { x: 400, y: 320 },
        { x: 500, y: 390 },
        { x: 600, y: 460 },
        { x: 700, y: 530 },
        { x: 800, y: 600 },
        { x: 900, y: 670 },
        { x: 1000, y: 740 },
        { x: 1100, y: 810 },
        { x: 1200, y: 880 },
        { x: 1300, y: 950 },
        { x: 1400, y: 1020 }
    ];
    
    // Limpiar canvas
    ctx.clearRect(0, 0, width, height);
    
    // Estilo del gráfico
    ctx.strokeStyle = '#0080FF';
    ctx.lineWidth = 3;
    ctx.fillStyle = 'rgba(0, 128, 255, 0.1)';
    
    // Dibujar línea del gráfico
    ctx.beginPath();
    dataPoints.forEach((point, index) => {
        const x = padding + (point.x / 1400) * graphWidth;
        const y = height - padding - (point.y / 1100) * graphHeight;
        
        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    });
    ctx.stroke();
    
    // Rellenar área bajo la curva
    ctx.lineTo(padding + graphWidth, height - padding);
    ctx.lineTo(padding, height - padding);
    ctx.closePath();
    ctx.fill();
    
    // Dibujar ejes
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
    ctx.lineWidth = 1;
    
    // Eje X
    ctx.beginPath();
    ctx.moveTo(padding, height - padding);
    ctx.lineTo(width - padding, height - padding);
    ctx.stroke();
    
    // Eje Y
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height - padding);
    ctx.stroke();
    
    // Etiquetas
    ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
    ctx.font = '12px -apple-system, BlinkMacSystemFont, sans-serif';
    ctx.textAlign = 'center';
    
    // Etiquetas eje X (Scale)
    const xLabels = [0, 250, 500, 750, 1000, 1250];
    xLabels.forEach(label => {
        const x = padding + (label / 1400) * graphWidth;
        ctx.fillText(label.toString(), x, height - padding + 20);
    });
    
    // Título eje X
    ctx.fillText('Scale', width / 2, height - 5);
    
    // Etiquetas eje Y
    ctx.textAlign = 'right';
    const yLabels = [0, 200, 400, 600, 800, 1000];
    yLabels.forEach(label => {
        const y = height - padding - (label / 1100) * graphHeight;
        ctx.fillText(label.toString(), padding - 10, y + 4);
    });
    
    // Título eje Y
    ctx.save();
    ctx.translate(15, height / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = 'center';
    ctx.fillText('Performance', 0, 0);
    ctx.restore();
}

// Animación de scroll suave para los enlaces
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Efecto de aparición al hacer scroll
function revealOnScroll() {
    const reveals = document.querySelectorAll('.stat-card, .feature-card, .resource-card');
    
    reveals.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
}

// Inicializar estilos para animación
document.querySelectorAll('.stat-card, .feature-card, .resource-card').forEach(element => {
    element.style.opacity = '0';
    element.style.transform = 'translateY(20px)';
    element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
});

// Event listeners
window.addEventListener('load', () => {
    createPerformanceChart();
    revealOnScroll();
});

window.addEventListener('scroll', revealOnScroll);

window.addEventListener('resize', () => {
    createPerformanceChart();
});

// Animación de números contadores para las estadísticas
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const text = counter.textContent;
        const hasPercent = text.includes('%');
        const hasX = text.includes('x');
        
        let target = parseFloat(text);
        if (isNaN(target)) return;
        
        let current = 0;
        const increment = target / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            
            let displayValue = Math.floor(current);
            if (hasPercent) {
                counter.textContent = displayValue + '%';
            } else if (hasX) {
                counter.textContent = displayValue + 'x';
            } else {
                counter.textContent = displayValue;
            }
        }, 20);
    });
}

// Observador para animar los contadores cuando entran en viewport
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
            entry.target.dataset.animated = 'true';
            setTimeout(animateCounters, 200);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.stats-grid').forEach(grid => {
    counterObserver.observe(grid);
});

// Navbar scroll effect
let lastScroll = 0;
const navbar = document.querySelector('.main-header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > lastScroll && currentScroll > 100) {
        navbar.style.transform = 'translateY(-100%)';
    } else {
        navbar.style.transform = 'translateY(0)';
    }
    
    lastScroll = currentScroll;
});

// Transición suave del navbar
if (navbar) {
    navbar.style.transition = 'transform 0.3s ease';
}
