/**
 * Cosmic Loader - "Consulting the Cosmic Patterns" animation
 * Shows a mystical loading animation before revealing reading results
 * Version: 1.0
 */

const CosmicLoader = {
    initialized: false,
    
    // Initialize the loader (inject styles and overlay HTML)
    init: function() {
        if (this.initialized) return;
        
        // Inject CSS
        const style = document.createElement('style');
        style.textContent = `
            .cosmic-loader-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: #0a0a0f;
                z-index: 10000;
                display: flex;
                align-items: center;
                justify-content: center;
                opacity: 0;
                visibility: hidden;
                transition: opacity 0.3s ease;
            }
            
            .cosmic-loader-overlay.active {
                opacity: 1;
                visibility: visible;
            }
            
            .cosmic-loader-overlay::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: 
                    radial-gradient(ellipse at 30% 20%, rgba(191, 90, 242, 0.2) 0%, transparent 50%),
                    radial-gradient(ellipse at 70% 80%, rgba(0, 245, 255, 0.15) 0%, transparent 50%),
                    radial-gradient(ellipse at 50% 50%, rgba(255, 217, 61, 0.1) 0%, transparent 60%);
                animation: cosmicBgPulse 4s ease-in-out infinite alternate;
            }
            
            @keyframes cosmicBgPulse {
                0% { opacity: 0.7; transform: scale(1); }
                100% { opacity: 1; transform: scale(1.1); }
            }
            
            .cosmic-loader-container {
                text-align: center;
                padding: 40px;
                max-width: 600px;
                position: relative;
                z-index: 1;
            }
            
            .cosmic-orb-container {
                position: relative;
                width: 200px;
                height: 200px;
                margin: 0 auto 40px;
            }
            
            .cosmic-orb {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                background: radial-gradient(circle at 30% 30%, rgba(191, 90, 242, 0.8), rgba(0, 245, 255, 0.4) 50%, rgba(10, 10, 20, 0.9));
                box-shadow: 
                    0 0 60px rgba(191, 90, 242, 0.5),
                    0 0 100px rgba(0, 245, 255, 0.3),
                    inset 0 0 40px rgba(255, 255, 255, 0.1);
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                animation: cosmicOrbPulse 2s ease-in-out infinite;
            }
            
            @keyframes cosmicOrbPulse {
                0%, 100% { 
                    box-shadow: 
                        0 0 60px rgba(191, 90, 242, 0.5),
                        0 0 100px rgba(0, 245, 255, 0.3),
                        inset 0 0 40px rgba(255, 255, 255, 0.1);
                }
                50% { 
                    box-shadow: 
                        0 0 80px rgba(191, 90, 242, 0.7),
                        0 0 120px rgba(0, 245, 255, 0.5),
                        inset 0 0 60px rgba(255, 255, 255, 0.2);
                }
            }
            
            .cosmic-ring {
                position: absolute;
                top: 50%;
                left: 50%;
                border: 2px solid transparent;
                border-radius: 50%;
                border-top-color: #00f5ff;
                border-bottom-color: #bf5af2;
            }
            
            .cosmic-ring-1 {
                width: 180px;
                height: 180px;
                margin: -90px 0 0 -90px;
                animation: cosmicSpin 3s linear infinite;
            }
            
            .cosmic-ring-2 {
                width: 200px;
                height: 200px;
                margin: -100px 0 0 -100px;
                animation: cosmicSpin 4s linear infinite reverse;
                border-top-color: #ffd93d;
                border-bottom-color: #ff6b6b;
            }
            
            @keyframes cosmicSpin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .cosmic-particles {
                position: absolute;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
            }
            
            .cosmic-particle {
                position: absolute;
                width: 4px;
                height: 4px;
                border-radius: 50%;
                animation: cosmicFloat 3s ease-in-out infinite;
            }
            
            .cosmic-particle:nth-child(1) { left: 10%; top: 20%; background: #00f5ff; animation-delay: 0s; }
            .cosmic-particle:nth-child(2) { left: 80%; top: 30%; background: #bf5af2; animation-delay: 0.5s; }
            .cosmic-particle:nth-child(3) { left: 20%; top: 70%; background: #ffd93d; animation-delay: 1s; }
            .cosmic-particle:nth-child(4) { left: 70%; top: 80%; background: #ff6b6b; animation-delay: 1.5s; }
            .cosmic-particle:nth-child(5) { left: 50%; top: 10%; background: #00f5ff; animation-delay: 2s; }
            .cosmic-particle:nth-child(6) { left: 90%; top: 60%; background: #bf5af2; animation-delay: 2.5s; }
            
            @keyframes cosmicFloat {
                0%, 100% { transform: translateY(0) scale(1); opacity: 0.7; }
                50% { transform: translateY(-20px) scale(1.2); opacity: 1; }
            }
            
            .cosmic-title {
                font-family: 'Cinzel Decorative', serif;
                font-size: clamp(1.5rem, 5vw, 2.2rem);
                background: linear-gradient(135deg, #ffd93d 0%, #00f5ff 50%, #bf5af2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 20px;
                animation: cosmicTextGlow 2s ease-in-out infinite alternate;
            }
            
            @keyframes cosmicTextGlow {
                0% { filter: drop-shadow(0 0 10px rgba(255, 217, 61, 0.3)); }
                100% { filter: drop-shadow(0 0 20px rgba(0, 245, 255, 0.5)); }
            }
            
            .cosmic-loading-text {
                font-family: 'Cormorant Garamond', serif;
                font-size: 1.3rem;
                color: #C4B998;
                font-style: italic;
                margin-bottom: 30px;
                min-height: 30px;
                transition: opacity 0.2s ease;
            }
            
            .cosmic-progress-bar {
                width: 100%;
                max-width: 300px;
                height: 4px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 2px;
                margin: 0 auto;
                overflow: hidden;
            }
            
            .cosmic-progress-fill {
                height: 100%;
                background: linear-gradient(90deg, #bf5af2, #00f5ff, #ffd93d);
                border-radius: 2px;
                width: 0%;
                transition: width 0.1s linear;
            }
            
            .cosmic-loader-overlay.active .cosmic-progress-fill {
                animation: cosmicProgress 3s ease-in-out forwards;
            }
            
            @keyframes cosmicProgress {
                0% { width: 0%; }
                100% { width: 100%; }
            }
        `;
        document.head.appendChild(style);
        
        // Inject overlay HTML
        const overlay = document.createElement('div');
        overlay.className = 'cosmic-loader-overlay';
        overlay.id = 'cosmicLoaderOverlay';
        overlay.innerHTML = `
            <div class="cosmic-loader-container">
                <div class="cosmic-orb-container">
                    <div class="cosmic-particles">
                        <div class="cosmic-particle"></div>
                        <div class="cosmic-particle"></div>
                        <div class="cosmic-particle"></div>
                        <div class="cosmic-particle"></div>
                        <div class="cosmic-particle"></div>
                        <div class="cosmic-particle"></div>
                    </div>
                    <div class="cosmic-ring cosmic-ring-1"></div>
                    <div class="cosmic-ring cosmic-ring-2"></div>
                    <div class="cosmic-orb"></div>
                </div>
                
                <h1 class="cosmic-title">Consulting the Cosmic Patterns</h1>
                <p class="cosmic-loading-text" id="cosmicLoadingText">Aligning celestial energies...</p>
                
                <div class="cosmic-progress-bar">
                    <div class="cosmic-progress-fill" id="cosmicProgressFill"></div>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);
        
        this.initialized = true;
    },
    
    // Loading messages
    messages: [
        "Aligning celestial energies...",
        "Reading the ancient patterns...",
        "Channeling cosmic wisdom...",
        "Decoding your unique vibration...",
        "The universe is speaking...",
        "Unveiling your destiny..."
    ],
    
    // Show the loader, execute callback after animation
    show: function(callback, duration = 3000) {
        this.init();
        
        const overlay = document.getElementById('cosmicLoaderOverlay');
        const loadingText = document.getElementById('cosmicLoadingText');
        const progressFill = document.getElementById('cosmicProgressFill');
        
        // Reset progress bar
        progressFill.style.animation = 'none';
        progressFill.offsetHeight; // Trigger reflow
        progressFill.style.animation = '';
        
        // Show overlay
        overlay.classList.add('active');
        
        // Cycle through messages
        let messageIndex = 0;
        const messageInterval = setInterval(() => {
            messageIndex = (messageIndex + 1) % this.messages.length;
            loadingText.style.opacity = '0';
            setTimeout(() => {
                loadingText.textContent = this.messages[messageIndex];
                loadingText.style.opacity = '1';
            }, 200);
        }, 800);
        
        // Hide after duration and execute callback
        setTimeout(() => {
            clearInterval(messageInterval);
            overlay.classList.remove('active');
            
            // Small delay for fade out
            setTimeout(() => {
                if (typeof callback === 'function') {
                    callback();
                }
            }, 300);
        }, duration);
    },
    
    // Helper: Show result element with animation
    showResult: function(resultElement, formElement) {
        this.show(() => {
            if (resultElement) {
                if (typeof resultElement === 'string') {
                    resultElement = document.getElementById(resultElement);
                }
                resultElement.style.display = 'block';
            }
            if (formElement) {
                if (typeof formElement === 'string') {
                    formElement = document.getElementById(formElement);
                }
                formElement.style.display = 'none';
            }
            
            // Scroll to result
            if (resultElement) {
                resultElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    }
};

// Make it globally available
window.CosmicLoader = CosmicLoader;
