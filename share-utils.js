/**
 * Quantum Merlin Share Utilities
 * Enhanced sharing functionality with viral personalized content
 */

window.QMShare = {
    // Site base URL
    baseUrl: 'https://funtools.quantummerlin.com/',
    
    // Current reading result (set dynamically)
    currentResult: null,
    
    // Viral share templates by tool type
    viralTemplates: {
        'life-path': (num, name) => `✨ I'm a Life Path ${num}! What's YOUR cosmic number? 🔮`,
        'destiny': (num, name) => `🌟 My Destiny Number is ${num}! Discover your life purpose →`,
        'soul-urge': (num, name) => `💫 My Soul Urge is ${num} - finally makes sense! What's yours?`,
        'personality': (num, name) => `🎭 Personality Number ${num} - this is SO me! Try it yourself →`,
        'rising': (sign, name) => `⬆️ I'm a ${sign} Rising! This explains everything 🔮`,
        'moon': (sign, name) => `🌙 My Moon is in ${sign}! Find your emotional blueprint →`,
        'zodiac': (sign, name) => `♈ I'm a ${sign}! Classic. What's your sign? 🌟`,
        'chinese': (animal, name) => `🐉 I'm a ${animal} in Chinese Zodiac! What animal are you?`,
        'aura': (color, name) => `✨ My aura is ${color}! What color is YOUR energy?`,
        'age': (days, name) => `🎂 I'm ${days.toLocaleString()} days old! How many days have YOU lived?`,
        'personal-year': (num, name) => `📅 I'm in a Personal Year ${num}! What's your year bringing?`,
        'fortune': (fortune) => `🥠 My fortune: "${fortune.substring(0, 80)}..." Get yours →`,
        'lucky-numbers': (nums) => `🍀 My lucky numbers: ${nums}! Find your cosmic numbers →`,
        'compatibility': (score) => `💕 Our compatibility: ${score}%! Check YOUR love match →`,
        'forecast': (type) => `🔮 Just read my ${type} cosmic forecast! See what the stars say for YOU →`,
        'default': () => `✨ Just discovered something amazing about myself! Try it →`
    },
    
    /**
     * Set the current reading result for personalized sharing
     */
    setResult(resultData) {
        this.currentResult = resultData;
    },
    
    /**
     * Generate viral share text from current result
     */
    getViralText() {
        if (!this.currentResult) {
            return this.viralTemplates.default();
        }
        
        const { type, value, name } = this.currentResult;
        const template = this.viralTemplates[type] || this.viralTemplates.default;
        return template(value, name);
    },
    
    /**
     * Get the current page URL
     */
    getPageUrl() {
        return encodeURIComponent(window.location.href);
    },
    
    /**
     * Get page title or custom text
     */
    getShareText(customText) {
        if (customText) return encodeURIComponent(customText);
        // Use viral text if available
        if (this.currentResult) return encodeURIComponent(this.getViralText());
        const title = document.querySelector('title')?.textContent || 'Check this out!';
        return encodeURIComponent(title);
    },
    
    /**
     * Share on Twitter/X with viral text
     */
    twitter(customText, customUrl) {
        const text = customText ? encodeURIComponent(customText) : this.getShareText();
        const url = customUrl ? encodeURIComponent(customUrl) : this.getPageUrl();
        const tweetUrl = `https://twitter.com/intent/tweet?text=${text}&url=${url}`;
        window.open(tweetUrl, '_blank', 'width=550,height=420');
    },
    
    /**
     * Share on Facebook
     */
    facebook(customUrl) {
        const url = customUrl ? encodeURIComponent(customUrl) : this.getPageUrl();
        const shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
        window.open(shareUrl, '_blank', 'width=580,height=400');
    },
    
    /**
     * Share on WhatsApp with viral text
     */
    whatsapp(customText, customUrl) {
        const text = customText || this.getViralText();
        const url = customUrl || window.location.href;
        const message = encodeURIComponent(`${text}\n\n${url}`);
        window.open(`https://api.whatsapp.com/send?text=${message}`, '_blank');
    },
    
    /**
     * Share via Email with compelling subject
     */
    email(subject, body, customUrl) {
        const title = subject || `You need to try this! ${this.getViralText()}`;
        const url = customUrl || window.location.href;
        const emailBody = body || `Hey!\n\n${this.getViralText()}\n\nTry it yourself:\n${url}\n\n✨ It's eerily accurate!`;
        const mailtoUrl = `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(emailBody)}`;
        window.location.href = mailtoUrl;
    },
    
    /**
     * Share via SMS/Text Message
     */
    sms(customText, customUrl) {
        const text = customText || this.getViralText();
        const url = customUrl || window.location.href;
        const message = encodeURIComponent(`${text}\n${url}`);
        window.location.href = `sms:?body=${message}`;
    },
    
    /**
     * Share on Pinterest
     */
    pinterest(imageUrl, description) {
        const url = encodeURIComponent(window.location.href);
        const desc = encodeURIComponent(description || this.getViralText());
        const img = encodeURIComponent(imageUrl || 'https://funtools.quantummerlin.com/RetroMerlin.jpg');
        window.open(`https://pinterest.com/pin/create/button/?url=${url}&media=${img}&description=${desc}`, '_blank', 'width=750,height=550');
    },
    
    /**
     * Share on Reddit
     */
    reddit(customTitle) {
        const url = encodeURIComponent(window.location.href);
        const title = encodeURIComponent(customTitle || this.getViralText());
        window.open(`https://reddit.com/submit?url=${url}&title=${title}`, '_blank', 'width=750,height=550');
    },
    
    /**
     * Share on Threads
     */
    threads(customText) {
        const text = encodeURIComponent((customText || this.getViralText()) + '\n' + window.location.href);
        window.open(`https://threads.net/intent/post?text=${text}`, '_blank', 'width=550,height=420');
    },
    
    /**
     * Share on Telegram
     */
    telegram(customText, customUrl) {
        const text = encodeURIComponent(customText || this.getViralText());
        const url = encodeURIComponent(customUrl || window.location.href);
        window.open(`https://t.me/share/url?url=${url}&text=${text}`, '_blank', 'width=550,height=420');
    },
    
    /**
     * Copy link to clipboard
     */
    async copyLink(customUrl, showFeedback = true) {
        const url = customUrl || window.location.href;
        try {
            await navigator.clipboard.writeText(url);
            if (showFeedback) {
                this.showCopyFeedback('✓ Link copied!');
            }
            return true;
        } catch (err) {
            // Fallback for older browsers
            const textarea = document.createElement('textarea');
            textarea.value = url;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            try {
                document.execCommand('copy');
                if (showFeedback) {
                    this.showCopyFeedback('✓ Link copied!');
                }
                return true;
            } catch (e) {
                if (showFeedback) {
                    this.showCopyFeedback('Failed to copy');
                }
                return false;
            } finally {
                document.body.removeChild(textarea);
            }
        }
    },
    
    /**
     * Copy viral result text to clipboard (for easy sharing anywhere)
     */
    async copyViralText() {
        const viralText = `${this.getViralText()}\n\n${window.location.href}`;
        try {
            await navigator.clipboard.writeText(viralText);
            this.showCopyFeedback('✨ Ready to paste & share!');
            return true;
        } catch (err) {
            const textarea = document.createElement('textarea');
            textarea.value = viralText;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            try {
                document.execCommand('copy');
                this.showCopyFeedback('✨ Ready to paste & share!');
                return true;
            } catch (e) {
                this.showCopyFeedback('Failed to copy');
                return false;
            } finally {
                document.body.removeChild(textarea);
            }
        }
    },
    
    /**
     * Copy custom result text to clipboard
     */
    async copyResult(resultText) {
        try {
            await navigator.clipboard.writeText(resultText);
            this.showCopyFeedback('✓ Result copied!');
            return true;
        } catch (err) {
            const textarea = document.createElement('textarea');
            textarea.value = resultText;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            try {
                document.execCommand('copy');
                this.showCopyFeedback('✓ Result copied!');
                return true;
            } catch (e) {
                this.showCopyFeedback('Failed to copy');
                return false;
            } finally {
                document.body.removeChild(textarea);
            }
        }
    },
    
    /**
     * Show copy feedback notification
     */
    showCopyFeedback(message) {
        // Remove existing feedback
        const existing = document.querySelector('.qm-copy-feedback');
        if (existing) existing.remove();
        
        const feedback = document.createElement('div');
        feedback.className = 'qm-copy-feedback';
        feedback.textContent = message;
        feedback.style.cssText = `
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 24px;
            border-radius: 25px;
            font-size: 14px;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            z-index: 10000;
            animation: qmFadeInUp 0.3s ease-out;
        `;
        
        document.body.appendChild(feedback);
        
        setTimeout(() => {
            feedback.style.animation = 'qmFadeOutDown 0.3s ease-out forwards';
            setTimeout(() => feedback.remove(), 300);
        }, 2000);
    },
    
    /**
     * Native Share API (mobile-friendly)
     */
    async native(shareData) {
        const data = {
            title: shareData?.title || document.querySelector('title')?.textContent || 'Quantum Merlin',
            text: shareData?.text || document.querySelector('meta[name="description"]')?.content || '',
            url: shareData?.url || window.location.href
        };
        
        if (navigator.share) {
            try {
                await navigator.share(data);
                return true;
            } catch (err) {
                if (err.name !== 'AbortError') {
                    console.log('Native share failed, falling back');
                    this.showShareModal(data);
                }
                return false;
            }
        } else {
            // Fallback to modal on desktop
            this.showShareModal(data);
            return false;
        }
    },
    
    /**
     * Check if native share is supported
     */
    hasNativeShare() {
        return !!navigator.share;
    },
    
    /**
     * Show share modal (fallback for desktop)
     */
    showShareModal(shareData) {
        // Remove existing modal
        const existing = document.querySelector('.qm-share-modal-overlay');
        if (existing) existing.remove();
        
        const overlay = document.createElement('div');
        overlay.className = 'qm-share-modal-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10001;
            animation: qmFadeIn 0.2s ease-out;
        `;
        
        const modal = document.createElement('div');
        modal.className = 'qm-share-modal';
        modal.style.cssText = `
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            max-width: 400px;
            width: 90%;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
        `;
        
        modal.innerHTML = `
            <h3 style="color: #fff; margin: 0 0 20px; text-align: center; font-size: 1.4em;">
                ✨ Share This Reading
            </h3>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 20px;">
                <button onclick="QMShare.twitter('${encodeURIComponent(shareData.text || '')}'); QMShare.closeModal();" 
                    style="background: #000; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; transition: transform 0.2s, filter 0.2s; display: flex; align-items: center; justify-content: center;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </button>
                <button onclick="QMShare.facebook(); QMShare.closeModal();" 
                    style="background: #4267B2; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; transition: transform 0.2s; display: flex; align-items: center; justify-content: center;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                </button>
                <button onclick="QMShare.whatsapp('${encodeURIComponent(shareData.text || '')}'); QMShare.closeModal();" 
                    style="background: #25D366; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; transition: transform 0.2s; display: flex; align-items: center; justify-content: center;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                </button>
                <button onclick="QMShare.email('${encodeURIComponent(shareData.title || '')}', '${encodeURIComponent(shareData.text || '')}'); QMShare.closeModal();" 
                    style="background: #EA4335; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; transition: transform 0.2s; display: flex; align-items: center; justify-content: center;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                </button>
                <button onclick="QMShare.sms('${encodeURIComponent(shareData.text || '')}'); QMShare.closeModal();" 
                    style="background: #5856D6; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; transition: transform 0.2s; display: flex; align-items: center; justify-content: center;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.17L4 17.17V4h16v12z"/></svg>
                </button>
                <button onclick="QMShare.copyLink(); QMShare.closeModal();" 
                    style="background: #667eea; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; transition: transform 0.2s; display: flex; align-items: center; justify-content: center;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
                </button>
            </div>
            <button onclick="QMShare.closeModal();" 
                style="width: 100%; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 10px; padding: 12px; cursor: pointer; color: rgba(255,255,255,0.7); font-size: 14px; transition: all 0.2s;"
                onmouseover="this.style.background='rgba(255,255,255,0.15)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">
                Cancel
            </button>
        `;
        
        overlay.appendChild(modal);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) this.closeModal();
        });
        
        document.body.appendChild(overlay);
    },
    
    /**
     * Close share modal
     */
    closeModal() {
        const modal = document.querySelector('.qm-share-modal-overlay');
        if (modal) {
            modal.style.animation = 'qmFadeOut 0.2s ease-out forwards';
            setTimeout(() => modal.remove(), 200);
        }
    },
    
    /**
     * Share reading as image (requires html2canvas CDN to be loaded)
     * @param {string} elementSelector - CSS selector for the element to capture
     * @param {string} filename - Optional filename for download
     */
    async shareAsImage(elementSelector = '.result, #result, .reading-result', filename = 'quantum-merlin-reading.png') {
        const element = document.querySelector(elementSelector);
        
        if (!element) {
            this.showCopyFeedback('❌ No reading to share');
            return;
        }
        
        // Load html2canvas if not already loaded
        if (typeof html2canvas === 'undefined') {
            await this.loadHtml2Canvas();
        }
        
        try {
            this.showCopyFeedback('📸 Creating image...');
            
            // Create canvas from element
            const canvas = await html2canvas(element, {
                backgroundColor: '#0a0a0f',
                scale: 2, // Higher quality
                logging: false,
                useCORS: true,
                allowTaint: true
            });
            
            // Add watermark
            const ctx = canvas.getContext('2d');
            ctx.font = '16px Cinzel, serif';
            ctx.fillStyle = 'rgba(251, 191, 36, 0.6)';
            ctx.textAlign = 'right';
            ctx.fillText('quantummerlin.com', canvas.width - 20, canvas.height - 15);
            
            // Convert to blob
            canvas.toBlob(async (blob) => {
                // Try native share if available (mobile)
                if (navigator.canShare && navigator.canShare({ files: [new File([blob], filename, { type: 'image/png' })] })) {
                    try {
                        await navigator.share({
                            files: [new File([blob], filename, { type: 'image/png' })],
                            title: 'My Quantum Merlin Reading',
                            text: 'Check out my reading from Quantum Merlin!'
                        });
                        return;
                    } catch (e) {
                        // Fall through to download
                    }
                }
                
                // Fallback: download image
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                
                this.showCopyFeedback('✓ Image downloaded!');
            }, 'image/png');
            
        } catch (error) {
            console.error('Error creating image:', error);
            this.showCopyFeedback('❌ Could not create image');
        }
    },
    
    /**
     * Load html2canvas library dynamically
     */
    loadHtml2Canvas() {
        return new Promise((resolve, reject) => {
            if (typeof html2canvas !== 'undefined') {
                resolve();
                return;
            }
            
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js';
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        });
    },
    
    /**
     * Initialize share buttons on page
     */
    init() {
        // Add CSS animations
        if (!document.querySelector('#qm-share-styles')) {
            const style = document.createElement('style');
            style.id = 'qm-share-styles';
            style.textContent = `
                @keyframes qmFadeIn { from { opacity: 0; } to { opacity: 1; } }
                @keyframes qmFadeOut { from { opacity: 1; } to { opacity: 0; } }
                @keyframes qmFadeInUp { 
                    from { opacity: 0; transform: translate(-50%, 20px); } 
                    to { opacity: 1; transform: translate(-50%, 0); } 
                }
                @keyframes qmFadeOutDown { 
                    from { opacity: 1; transform: translate(-50%, 0); } 
                    to { opacity: 0; transform: translate(-50%, 20px); } 
                }
            `;
            document.head.appendChild(style);
        }
    }
};

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => QMShare.init());
} else {
    QMShare.init();
}

/**
 * Create and inject a viral share card after reading results
 * @param {Object} options - Configuration for the share card
 */
QMShare.injectViralCard = function(options = {}) {
    const {
        container = '.reading-card, .result, #result',
        position = 'afterend',
        resultType = 'default',
        resultValue = '',
        resultLabel = 'Your Result'
    } = options;
    
    // Set current result for viral sharing
    this.setResult({
        type: resultType,
        value: resultValue,
        name: ''
    });
    
    const targetEl = document.querySelector(container);
    if (!targetEl) return;
    
    // Check if card already exists
    if (document.querySelector('.viral-share-card')) return;
    
    const viralText = this.getViralText();
    
    const cardHTML = `
    <div class="viral-share-card">
        <div class="viral-share-header">
            <span class="viral-emoji">🔮</span>
            <span class="viral-title">Share Your Discovery!</span>
        </div>
        <div class="viral-preview">
            <div class="viral-quote">"${viralText}"</div>
        </div>
        <div class="viral-cta">Challenge your friends to discover theirs!</div>
        <div class="viral-buttons">
            <button class="viral-btn viral-btn-primary" onclick="QMShare.copyViralText()" title="Copy to share anywhere">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
                Copy & Share
            </button>
            <button class="viral-btn" onclick="QMShare.twitter()" title="Share on X">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </button>
            <button class="viral-btn" onclick="QMShare.whatsapp()" title="Share on WhatsApp">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            </button>
            <button class="viral-btn" onclick="QMShare.threads()" title="Share on Threads">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.186 24h-.007c-3.581-.024-6.334-1.205-8.184-3.509C2.35 18.44 1.5 15.586 1.472 12.01v-.017c.03-3.579.879-6.43 2.525-8.482C5.845 1.205 8.6.024 12.18 0h.014c2.746.02 5.043.725 6.826 2.098 1.677 1.29 2.858 3.13 3.509 5.467l-2.04.569c-1.104-3.96-3.898-5.984-8.304-6.015-2.91.022-5.11.936-6.54 2.717C4.307 6.504 3.616 8.914 3.589 12c.027 3.086.718 5.496 2.057 7.164 1.43 1.783 3.631 2.698 6.54 2.717 2.623-.02 4.358-.631 5.8-2.045 1.647-1.613 1.618-3.593 1.09-4.798-.31-.71-.873-1.3-1.634-1.75-.192 1.352-.622 2.446-1.284 3.272-.886 1.102-2.14 1.704-3.73 1.79-1.202.065-2.361-.218-3.259-.801-1.063-.689-1.685-1.74-1.752-2.96-.065-1.182.408-2.256 1.332-3.023.88-.73 2.088-1.146 3.396-1.272l.059-.004c.924-.065 1.78.024 2.553.265.193-.658.29-1.404.275-2.2-.043-2.355-1.32-3.652-3.59-3.652-1.453 0-2.548.49-3.255 1.458-.584.8-.905 1.893-.958 3.255l-2.073-.086c.072-1.753.518-3.2 1.327-4.305 1.036-1.418 2.64-2.167 4.77-2.228h.1c3.327 0 5.483 2.098 5.536 5.39.028 1.203-.168 2.318-.574 3.32 1.072.589 1.9 1.405 2.418 2.4.734 1.408.927 3.17.543 4.962-.493 2.304-1.857 4.03-3.946 4.996-1.59.734-3.482 1.1-5.632 1.092zm1.083-7.409c-1.456.132-2.912.696-2.866 1.89.023.602.357 1.063.968 1.334.532.236 1.222.316 1.94.225 1.04-.131 2.468-.725 2.812-3.418-.627-.177-1.282-.245-1.932-.2h-.022l-.9.07z"/></svg>
            </button>
            <button class="viral-btn" onclick="QMShare.facebook()" title="Share on Facebook">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </button>
        </div>
        <button class="viral-more-btn" onclick="this.parentElement.classList.toggle('show-more')">
            More ways to share ▾
        </button>
        <div class="viral-extra-buttons">
            <button class="viral-btn-small" onclick="QMShare.telegram()" title="Telegram">📨 Telegram</button>
            <button class="viral-btn-small" onclick="QMShare.reddit()" title="Reddit">🤖 Reddit</button>
            <button class="viral-btn-small" onclick="QMShare.pinterest()" title="Pinterest">📌 Pinterest</button>
            <button class="viral-btn-small" onclick="QMShare.email()" title="Email">✉️ Email</button>
            <button class="viral-btn-small" onclick="QMShare.sms()" title="SMS">💬 Text</button>
        </div>
    </div>
    `;
    
    // Add styles if not already present
    if (!document.querySelector('#viral-share-styles')) {
        const style = document.createElement('style');
        style.id = 'viral-share-styles';
        style.textContent = `
            .viral-share-card {
                background: linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
                border: 2px solid rgba(251, 191, 36, 0.4);
                border-radius: 20px;
                padding: 25px;
                margin: 30px 0;
                text-align: center;
                animation: viralPulse 3s ease-in-out infinite;
            }
            @keyframes viralPulse {
                0%, 100% { box-shadow: 0 0 20px rgba(251, 191, 36, 0.2); }
                50% { box-shadow: 0 0 30px rgba(251, 191, 36, 0.4); }
            }
            .viral-share-header {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                margin-bottom: 15px;
            }
            .viral-emoji { font-size: 1.8em; }
            .viral-title {
                font-family: 'Cinzel Decorative', serif;
                font-size: 1.4em;
                background: linear-gradient(135deg, #fbbf24 0%, #ec4899 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .viral-preview {
                background: rgba(0, 0, 0, 0.3);
                border-radius: 12px;
                padding: 15px 20px;
                margin: 15px 0;
            }
            .viral-quote {
                font-family: 'Cormorant Garamond', serif;
                font-size: 1.15em;
                font-style: italic;
                color: #fbbf24;
                line-height: 1.5;
            }
            .viral-cta {
                color: #9ca3af;
                font-size: 0.95em;
                margin-bottom: 20px;
            }
            .viral-buttons {
                display: flex;
                gap: 10px;
                justify-content: center;
                flex-wrap: wrap;
            }
            .viral-btn {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: white;
                padding: 12px 16px;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s ease;
                display: flex;
                align-items: center;
                gap: 8px;
                font-size: 0.9em;
            }
            .viral-btn:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
            }
            .viral-btn-primary {
                background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
                border: none;
                color: #000;
                font-weight: 600;
                padding: 14px 24px;
            }
            .viral-btn-primary:hover {
                background: linear-gradient(135deg, #fcd34d 0%, #fbbf24 100%);
                box-shadow: 0 5px 20px rgba(251, 191, 36, 0.4);
            }
            .viral-more-btn {
                background: none;
                border: none;
                color: #6b7280;
                font-size: 0.85em;
                cursor: pointer;
                margin-top: 15px;
                padding: 8px 16px;
                transition: color 0.3s;
            }
            .viral-more-btn:hover { color: #9ca3af; }
            .viral-extra-buttons {
                display: none;
                flex-wrap: wrap;
                gap: 8px;
                justify-content: center;
                margin-top: 15px;
                padding-top: 15px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }
            .viral-share-card.show-more .viral-extra-buttons { display: flex; }
            .viral-share-card.show-more .viral-more-btn { display: none; }
            .viral-btn-small {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.15);
                color: #9ca3af;
                padding: 8px 14px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 0.85em;
                transition: all 0.2s;
            }
            .viral-btn-small:hover {
                background: rgba(255, 255, 255, 0.1);
                color: white;
            }
        `;
        document.head.appendChild(style);
    }
    
    targetEl.insertAdjacentHTML(position, cardHTML);
};

// Legacy function aliases for backward compatibility
function shareOnTwitter(text, url) {
    QMShare.twitter(text, url);
}

function shareOnFacebook(url) {
    QMShare.facebook(url);
}

function copyLink(url) {
    QMShare.copyLink(url);
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = QMShare;
}
