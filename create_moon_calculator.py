#!/usr/bin/env python3
"""
Generate Moon Sign CALCULATOR (not just reading)
Uses astronomy calculations to determine Moon sign from birth data
"""

import json

# We'll use the astronomia JavaScript library or a simple API approach
# For now, let's create a tool that uses the Astro-Seek API or similar

CALCULATOR_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moon Sign Calculator | Calculate Your Moon Sign</title>
    <meta name="description" content="Calculate your Moon Sign from your birth date, time, and location. Get accurate astronomical calculations and deep interpretations.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&family=Cinzel:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
    <!-- Swiss Ephemeris JavaScript Library -->
    <script src="https://cdn.jsdelivr.net/npm/swisseph@2.10.3/sweph.min.js"></script>
    <style>
        /* Same styling as other premium tools */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Cormorant Garamond', serif;
            background: #0a0a0f;
            background-image: 
                radial-gradient(circle at 20% 50%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.8;
            color: #e0e0e0;
        }
        .container { max-width: 900px; margin: 0 auto; }
        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 30px;
        }
        .header h1 {
            font-family: 'Cinzel Decorative', serif;
            font-size: 2.8em;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #fbbf24 0%, #06b6d4 50%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 2px;
            font-weight: 700;
        }
        .note-box {
            background: rgba(251, 191, 36, 0.1);
            border: 2px solid rgba(251, 191, 36, 0.3);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 25px;
        }
        .note-box p {
            margin: 0;
            font-size: 1.05em;
            line-height: 1.6;
        }
        .tool-card {
            background: rgba(20, 20, 30, 0.8);
            border: 2px solid rgba(6, 182, 212, 0.3);
            border-radius: 20px;
            padding: 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
        }
        .input-group {
            margin-bottom: 25px;
        }
        label {
            display: block;
            font-family: 'Cinzel', serif;
            font-size: 1.1em;
            margin-bottom: 10px;
            color: #06b6d4;
            font-weight: 600;
        }
        input, select {
            width: 100%;
            padding: 15px;
            border: 2px solid rgba(6, 182, 212, 0.3);
            background: rgba(10, 10, 15, 0.6);
            color: #e0e0e0;
            border-radius: 10px;
            font-size: 1.1em;
            font-family: 'Cormorant Garamond', serif;
            transition: all 0.3s ease;
        }
        input:focus, select:focus {
            outline: none;
            border-color: #06b6d4;
            background: rgba(6, 182, 212, 0.05);
        }
        .helper-text {
            font-size: 0.9em;
            color: rgba(224, 224, 224, 0.7);
            margin-top: 5px;
            font-style: italic;
        }
        button[type="submit"] {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%);
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 1.3em;
            font-family: 'Cinzel', serif;
            font-weight: 700;
            cursor: pointer;
            margin-top: 30px;
            transition: all 0.3s ease;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        button[type="submit"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(139, 92, 246, 0.4);
        }
        .result {
            display: none;
            margin-top: 40px;
            padding: 40px;
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(6, 182, 212, 0.1) 100%);
            border: 2px solid rgba(6, 182, 212, 0.4);
            border-radius: 15px;
        }
        .result.show { display: block; animation: fadeIn 0.5s ease; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .result h2 {
            font-family: 'Cinzel Decorative', serif;
            font-size: 2.2em;
            margin-bottom: 25px;
            background: linear-gradient(135deg, #fbbf24 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .result-content p {
            font-size: 1.15em;
            margin-bottom: 20px;
            line-height: 1.9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌙 Moon Sign Calculator</h1>
            <p>Calculate your Moon Sign from birth data</p>
        </div>

        <div class="tool-card">
            <div class="note-box">
                <p><strong style="color: #fbbf24;">✨ How it works:</strong> Enter your exact birth date, time, and location below. 
                We'll calculate your Moon Sign using astronomical data and provide a deep interpretation of your emotional nature.</p>
            </div>

            <form id="calculator-form" onsubmit="calculateMoonSign(event)">
                <div class="input-group">
                    <label for="preferredName">Your Name</label>
                    <input type="text" id="preferredName" required placeholder="What you like to be called">
                </div>

                <div class="input-group">
                    <label for="birthDate">Birth Date</label>
                    <input type="date" id="birthDate" required>
                </div>

                <div class="input-group">
                    <label for="birthTime">Birth Time *</label>
                    <input type="time" id="birthTime" required>
                    <div class="helper-text">* Exact time is required for accurate Moon Sign calculation</div>
                </div>

                <div class="input-group">
                    <label for="birthPlace">Birth Place</label>
                    <input type="text" id="birthPlace" required placeholder="City, Country (e.g., New York, USA)">
                    <div class="helper-text">We'll look up the coordinates automatically</div>
                </div>

                <button type="submit">🔮 Calculate My Moon Sign</button>
            </form>

            <div id="result" class="result">
                <h2 id="result-title"></h2>
                <div id="result-content" class="result-content"></div>
            </div>
        </div>
    </div>

    <script>
        // For MVP, we'll use a simpler approach: OpenCage Geocoding API (free tier)
        // and a simplified Moon position calculation

        // Placeholder - we need to implement actual astronomical calculations
        // This would require either:
        // 1. Swiss Ephemeris library (complex, large)
        // 2. External API call to astronomy service
        // 3. Simplified calculation (less accurate)

        async function calculateMoonSign(event) {
            event.preventDefault();
            
            const name = document.getElementById('preferredName').value;
            const birthDate = document.getElementById('birthDate').value;
            const birthTime = document.getElementById('birthTime').value;
            const birthPlace = document.getElementById('birthPlace').value;

            // Show loading state
            const submitBtn = event.target.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = '🔮 Calculating...';
            submitBtn.disabled = true;

            try {
                // Step 1: Get coordinates for birth place
                const coords = await geocodeLocation(birthPlace);
                
                // Step 2: Calculate Moon position
                const moonSign = await getMoonPosition(birthDate, birthTime, coords);
                
                // Step 3: Show result
                showResult(name, moonSign);
                
            } catch (error) {
                alert('Error calculating Moon Sign: ' + error.message + '\\n\\nPlease check your birth location and try again.');
            } finally {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }
        }

        async function geocodeLocation(location) {
            // Using OpenStreetMap Nominatim (free, no API key required)
            const url = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(location)}&format=json&limit=1`;
            
            const response = await fetch(url, {
                headers: {
                    'User-Agent': 'QuantumMerlinTools/1.0'
                }
            });
            
            if (!response.ok) throw new Error('Failed to geocode location');
            
            const data = await response.json();
            if (data.length === 0) throw new Error('Location not found. Please try a different format (e.g., "Los Angeles, USA")');
            
            return {
                lat: parseFloat(data[0].lat),
                lon: parseFloat(data[0].lon)
            };
        }

        async function getMoonPosition(date, time, coords) {
            // Combine date and time
            const datetime = new Date(`${date}T${time}`);
            
            // For now, we'll use a simplified calculation
            // TODO: Implement Swiss Ephemeris or use an astronomy API
            
            // Placeholder: Calculate based on date (simplified, not accurate)
            const dayOfYear = getDayOfYear(datetime);
            const moonCycle = (dayOfYear * 12.368) % 360; // Simplified moon progression
            
            // Map to zodiac sign
            const zodiacIndex = Math.floor(moonCycle / 30);
            const signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
                          'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'];
            
            return signs[zodiacIndex];
        }

        function getDayOfYear(date) {
            const start = new Date(date.getFullYear(), 0, 0);
            const diff = date - start;
            const oneDay = 1000 * 60 * 60 * 24;
            return Math.floor(diff / oneDay);
        }

        function showResult(name, moonSign) {
            // TODO: Load actual interpretations from existing moon-sign-reading.html
            const interpretation = `Your Moon is in ${moonSign}, ${name}...`;
            
            document.getElementById('result-title').textContent = `Your Moon Sign: ${moonSign}`;
            document.getElementById('result-content').innerHTML = `<p>${interpretation}</p>`;
            document.getElementById('result').classList.add('show');
            document.getElementById('calculator-form').style.display = 'none';
        }
    </script>
</body>
</html>"""

with open('moon-sign-calculator-draft.html', 'w', encoding='utf-8') as f:
    f.write(CALCULATOR_HTML)

print("✅ Created draft Moon Sign Calculator")
print("⚠️  Note: This draft uses simplified calculations")
print("🔧 Need to implement proper astronomical calculations using:")
print("   - Swiss Ephemeris library, OR")
print("   - Astronomy API service")
print("")
print("The challenge: Swiss Ephemeris is very large (~15MB) and complex")
print("Better approach: Find a lightweight astronomy API or library")
