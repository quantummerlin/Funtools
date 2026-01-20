/**
 * Quantum Merlin Share Utilities
 * Enhanced sharing functionality with multiple platforms and native share API support
 */

const QMShare = {
    // Site base URL
    baseUrl: 'https://funtools.quantummerlin.com/',
    
    // Default share configuration
    defaults: {
        hashtags: 'quantummerlin,numerology',
        via: ''  // Twitter handle without @
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
        const title = document.querySelector('title')?.textContent || 'Check this out!';
        return encodeURIComponent(title);
    },
    
    /**
     * Share on Twitter/X
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
     * Share on WhatsApp
     */
    whatsapp(customText, customUrl) {
        const text = customText || document.querySelector('title')?.textContent || '';
        const url = customUrl || window.location.href;
        const message = encodeURIComponent(`${text}\n${url}`);
        // Use api.whatsapp.com for better cross-platform support
        window.open(`https://api.whatsapp.com/send?text=${message}`, '_blank');
    },
    
    /**
     * Share via Email
     */
    email(subject, body, customUrl) {
        const title = subject || document.querySelector('title')?.textContent || 'Check this out!';
        const url = customUrl || window.location.href;
        const emailBody = body ? `${body}\n\n${url}` : `I thought you might enjoy this:\n\n${url}`;
        const mailtoUrl = `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(emailBody)}`;
        window.location.href = mailtoUrl;
    },
    
    /**
     * Share via SMS/Text Message
     */
    sms(customText, customUrl) {
        const text = customText || document.querySelector('title')?.textContent || '';
        const url = customUrl || window.location.href;
        const message = encodeURIComponent(`${text} ${url}`);
        // Use sms: protocol - works on mobile
        window.location.href = `sms:?body=${message}`;
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
                    style="background: #1da1f2; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; font-size: 24px; transition: transform 0.2s, filter 0.2s;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    𝕏
                </button>
                <button onclick="QMShare.facebook(); QMShare.closeModal();" 
                    style="background: #4267B2; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; font-size: 24px; transition: transform 0.2s;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    📘
                </button>
                <button onclick="QMShare.whatsapp('${encodeURIComponent(shareData.text || '')}'); QMShare.closeModal();" 
                    style="background: #25D366; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; font-size: 24px; transition: transform 0.2s;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    💬
                </button>
                <button onclick="QMShare.email('${encodeURIComponent(shareData.title || '')}', '${encodeURIComponent(shareData.text || '')}'); QMShare.closeModal();" 
                    style="background: #EA4335; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; font-size: 24px; transition: transform 0.2s;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    ✉️
                </button>
                <button onclick="QMShare.sms('${encodeURIComponent(shareData.text || '')}'); QMShare.closeModal();" 
                    style="background: #5856D6; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; font-size: 24px; transition: transform 0.2s;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    📱
                </button>
                <button onclick="QMShare.copyLink(); QMShare.closeModal();" 
                    style="background: #667eea; border: none; border-radius: 12px; padding: 15px; cursor: pointer; color: white; font-size: 24px; transition: transform 0.2s;"
                    onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    📋
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
