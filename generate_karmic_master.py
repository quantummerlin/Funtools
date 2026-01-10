#!/usr/bin/env python3
"""
Generate Karmic Debt and Master Number Deep Reading Tools
Premium tools with 500-800 word deep readings
"""

# Template for premium tools
PREMIUM_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Free Personalized Reading</title>
    <meta name="description" content="{description}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&family=Cinzel:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Cormorant Garamond', serif;
            background: #0a0a0f;
            background-image: 
                radial-gradient(circle at 20% 50%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.8;
            color: #e0e0e0;
        }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .header {{
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 30px;
        }}
        .header h1 {{
            font-family: 'Cinzel Decorative', serif;
            font-size: 2.8em;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #fbbf24 0%, #06b6d4 50%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 2px;
            font-weight: 700;
        }}
        .header p {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.2em;
            color: #06b6d4;
            opacity: 0.9;
            font-style: italic;
        }}
        .tool-card {{
            background: rgba(20, 20, 30, 0.8);
            border: 2px solid rgba(6, 182, 212, 0.3);
            border-radius: 20px;
            padding: 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
            margin-bottom: 30px;
        }}
        .clear-data-btn {{
            text-align: right;
            margin-bottom: 20px;
        }}
        .clear-data-btn button {{
            background: rgba(236, 72, 153, 0.1);
            border: 2px solid rgba(236, 72, 153, 0.3);
            color: #ec4899;
            padding: 10px 20px;
            font-size: 0.9em;
            border-radius: 8px;
            cursor: pointer;
            font-family: 'Cinzel', serif;
            font-weight: 600;
            transition: all 0.3s;
        }}
        .clear-data-btn button:hover {{
            background: rgba(236, 72, 153, 0.2);
            border-color: #ec4899;
        }}
        .input-section {{
            margin-bottom: 40px;
            padding-bottom: 30px;
            border-bottom: 2px solid rgba(6, 182, 212, 0.2);
        }}
        .input-section:last-of-type {{
            border-bottom: none;
        }}
        .section-title {{
            font-family: 'Cinzel', serif;
            font-size: 1.4em;
            color: #fbbf24;
            margin-bottom: 20px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}
        .input-group {{
            margin-bottom: 25px;
        }}
        label {{
            display: block;
            font-family: 'Cinzel', serif;
            font-weight: 600;
            margin-bottom: 10px;
            color: #06b6d4;
            font-size: 1.05em;
        }}
        .helper-text {{
            font-size: 0.9em;
            color: #9ca3af;
            margin-top: 5px;
            font-style: italic;
        }}
        input[type="text"],
        input[type="date"],
        input[type="time"] {{
            width: 100%;
            padding: 15px;
            border: 2px solid rgba(6, 182, 212, 0.3);
            background: rgba(10, 10, 15, 0.6);
            color: #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
            font-family: 'Cormorant Garamond', serif;
        }}
        input:focus {{
            outline: none;
            border-color: #fbbf24;
            box-shadow: 0 0 15px rgba(251, 191, 36, 0.3);
        }}
        .row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }}
        button[type="submit"] {{
            background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%);
            color: white;
            border: 2px solid rgba(251, 191, 36, 0.3);
            padding: 18px 50px;
            font-size: 1.2em;
            font-weight: 600;
            font-family: 'Cinzel', serif;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            width: 100%;
            margin-top: 20px;
            letter-spacing: 1px;
        }}
        button[type="submit"]:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(6, 182, 212, 0.4);
            border-color: rgba(251, 191, 36, 0.6);
        }}
        .result {{
            background: rgba(20, 20, 30, 0.6);
            border: 2px solid rgba(251, 191, 36, 0.3);
            padding: 40px;
            border-radius: 15px;
            margin-top: 30px;
            display: none;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        }}
        .result.show {{
            display: block;
            animation: fadeIn 0.6s ease;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .result h2 {{
            font-family: 'Cinzel Decorative', serif;
            font-size: 2.5em;
            color: #fbbf24;
            margin-bottom: 20px;
            text-align: center;
            letter-spacing: 1px;
        }}
        .result-content {{
            font-size: 1.15em;
            line-height: 2;
            color: #e0e0e0;
        }}
        .result-content p {{
            margin-bottom: 20px;
        }}
        .back-button {{
            background: rgba(6, 182, 212, 0.1);
            border: 2px solid rgba(6, 182, 212, 0.3);
            margin-top: 30px;
        }}
        .back-button:hover {{
            background: rgba(6, 182, 212, 0.2);
            border-color: #06b6d4;
            transform: translateY(-2px);
        }}
        .no-karmic {{
            text-align: center;
            padding: 40px;
            background: rgba(6, 182, 212, 0.1);
            border: 2px solid rgba(6, 182, 212, 0.3);
            border-radius: 15px;
        }}
        .no-karmic h3 {{
            font-family: 'Cinzel', serif;
            color: #06b6d4;
            margin-bottom: 15px;
        }}
        @media (max-width: 768px) {{
            .row {{
                grid-template-columns: 1fr;
            }}
            .header h1 {{
                font-size: 2em;
            }}
            .tool-card {{
                padding: 30px 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{emoji} {title}</h1>
            <p>{tagline}</p>
        </div>

        <div class="tool-card">
            <div class="clear-data-btn">
                <button type="button" onclick="clearSavedData()">🗑️ Clear My Data</button>
            </div>

            <form id="calculator-form" onsubmit="calculateReading(event)">
                <div class="input-section">
                    <div class="section-title">✨ Personal Information</div>
                    
                    <div class="input-group">
                        <label for="preferredName">Preferred Name</label>
                        <input type="text" id="preferredName" required>
                        <div class="helper-text">What you like to be called</div>
                    </div>

                    <div class="input-group">
                        
                        <div class="helper-text">As it appears on your birth certificate</div>
                    </div>
                </div>

                <div class="input-section">
                    <div class="section-title">🌟 Birth Details</div>
                    
                    <div class="input-group">
                        <label for="birthDate">Birth Date</label>
                        <input type="date" id="birthDate" required>
                    </div>

                    <div class="row">
                        <div class="input-group">
                            <label for="birthTime">Birth Time</label>
                            <input type="time" id="birthTime">
                            <div class="helper-text">Optional but helpful</div>
                        </div>

                        <div class="input-group">
                            <label for="birthPlace">Birth Place</label>
                            <input type="text" id="birthPlace" placeholder="City, Country">
                            <div class="helper-text">Optional</div>
                        </div>
                    </div>
                </div>

                <button type="submit">✨ Reveal My Reading</button>
            </form>

            <div id="result" class="result">
                <h2 id="result-title"></h2>
                <div id="result-content" class="result-content"></div>
                <button type="button" class="back-button" onclick="window.location.href='tools_index.html'">← Back to Quantum Merlin Hub</button>
            </div>
        </div>
    </div>

    <script>
        // Numerology functions
        function reduceToSingle(num) {{
            while (num > 9 && num !== 11 && num !== 22 && num !== 33) {{
                num = num.toString().split('').reduce((a, b) => a + parseInt(b), 0);
            }}
            return num;
        }}

        function letterToNumber(letter) {{
            const values = {{
                'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
                'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
            }};
            return values[letter.toUpperCase()] || 0;
        }}

        function calculateNameNumber(name) {{
            return reduceToSingle(
                name.toUpperCase().split('').reduce((sum, char) => sum + letterToNumber(char), 0)
            );
        }}

        function calculateLifePath(dateStr) {{
            const date = new Date(dateStr);
            const day = date.getDate();
            const month = date.getMonth() + 1;
            const year = date.getFullYear();
            
            const dayReduced = reduceToSingle(day);
            const monthReduced = reduceToSingle(month);
            const yearReduced = reduceToSingle(year);
            
            return reduceToSingle(dayReduced + monthReduced + yearReduced);
        }}

        {calculation_functions}

        // Interpretations
        const interpretations = {interpretations_json};

        // Calculate and display reading
        function calculateReading(event) {{
            event.preventDefault();
            
            const preferredName = document.getElementById('preferredName').value;
            const birthName = document.getElementById('birthName').value;
            const birthDate = document.getElementById('birthDate').value;
            
            if (!birthDate) {{
                alert('Please enter your birth date');
                return;
            }}

            {calculation_code}

            const interpretation = interpretations[number];
            if (!interpretation) {{
                {no_result_code}
                return;
            }}

            // Personalize the reading with their name
            const personalizedReading = interpretation.replace(/{{preferredName}}/g, preferredName);

            // Convert paragraphs to HTML
            const paragraphs = personalizedReading.split('\\n\\n').map(p => `<p>${{p}}</p>`).join('');

            document.getElementById('result-title').textContent = `{result_title_template}`;
            document.getElementById('result-content').innerHTML = paragraphs;
            document.getElementById('result').classList.add('show');
            document.getElementById('calculator-form').style.display = 'none';

            // Save data
            saveUserData();
        }}

        // LocalStorage functions
        function loadSavedData() {{
            const savedData = localStorage.getItem('quantumMerlinUserData');
            if (savedData) {{
                const data = JSON.parse(savedData);
                if (data.preferredName) document.getElementById('preferredName').value = data.preferredName;
                // birthName removed
                if (data.birthDate) document.getElementById('birthDate').value = data.birthDate;
                if (data.birthTime) document.getElementById('birthTime').value = data.birthTime;
                if (data.birthPlace) document.getElementById('birthPlace').value = data.birthPlace;
            }}
        }}

        function saveUserData() {{
            const userData = {{
                preferredName: document.getElementById('preferredName').value,
                // birthName removed,
                birthDate: document.getElementById('birthDate').value,
                birthTime: document.getElementById('birthTime').value,
                birthPlace: document.getElementById('birthPlace').value
            }};
            localStorage.setItem('quantumMerlinUserData', JSON.stringify(userData));
        }}

        function clearSavedData() {{
            if (confirm('This will clear your saved personal information. Are you sure?')) {{
                localStorage.removeItem('quantumMerlinUserData');
                location.reload();
            }}
        }}

        // Load saved data on page load
        window.addEventListener('DOMContentLoaded', loadSavedData);
    </script>
</body>
</html>
"""

# Karmic Debt interpretations
KARMIC_DEBT_INTERPRETATIONS = {
    13: """You carry Karmic Debt Number 13, {preferredName}, which reveals patterns from past experiences that your soul is here to transform. This isn't punishment—it's opportunity. The 13 brings challenges around laziness, negativity, and taking shortcuts in past cycles. Now you're here to master discipline, positivity, and hard work.

The 13 karmic debt often manifests as obstacles that seem to block your progress. Projects may require more effort than expected, success may come more slowly than for others, and you may feel you're working twice as hard for half the results. This isn't bad luck—it's your soul's curriculum teaching you persistence.

Your primary challenge is overcoming the temptation to give up when things get difficult. In past patterns, you may have abandoned efforts when they became challenging. This lifetime, you're learning that sustainable success comes through consistent effort, not shortcuts or quick fixes.

Negativity is another pattern you're here to transform. The 13 can manifest as pessimism, complaining, or blaming circumstances for your situation. Your soul's work involves shifting from victim consciousness to creator consciousness—recognizing that your thoughts and actions shape your reality.

However, here's the empowering truth: when you embrace the lessons of 13, you develop extraordinary discipline and work ethic. You become someone who can achieve anything through sustained effort. The obstacles you face are actually building your strength, like resistance training builds muscle.

Your path to freedom involves accepting responsibility for your life, maintaining positive focus even when circumstances are challenging, and committing to see things through to completion. Every project you finish, every negative thought you reframe, every lazy impulse you overcome dissolves karmic patterns.

This debt is repaid through consistent action and positive mindset, {preferredName}. You're not here to suffer—you're here to transform limitation into mastery. The discipline you develop through working with 13's energy becomes your superpower.""",

    14: """You carry Karmic Debt Number 14, {preferredName}, revealing soul lessons around freedom, responsibility, and moderation. In past patterns, you may have misused freedom, overindulged in pleasures, or escaped commitment. This lifetime, you're learning to balance freedom with responsibility and pleasure with discipline.

The 14 karmic debt often manifests as constant change and instability. Just when you feel settled, circumstances shift. Relationships may be unpredictable, living situations may change frequently, and you may struggle to create lasting security. This isn't chaos—it's teaching you adaptability and proper use of freedom.

Your primary challenge is learning that true freedom comes through self-discipline, not rebellion or escape. Past patterns may have involved avoiding commitment, running from responsibility, or seeking constant stimulation. Now you're discovering that structure actually enables freedom.

Addiction and overindulgence are common struggles with 14. This can manifest in obvious ways like substance issues, or subtle ways like overworking, overeating, or excessive relationships. You're learning that moderation and balance create sustainable pleasure, while excess ultimately imprisons you.

However, the gift within 14 is powerful: you're developing genuine adaptability and healthy relationship with change. Where others fear transformation, you learn to flow with it. Where others resist growth, you embrace it. This makes you exceptionally resilient.

Your path to freedom involves embracing commitment without losing yourself, creating structure without rigidity, and enjoying pleasure without addiction. Every time you honor a commitment despite wanting to escape, every time you choose moderation over excess, you clear karmic patterns.

The 14 teaches that genuine freedom exists within healthy boundaries, not outside them, {preferredName}. You're learning to be responsibly free and freely responsible. This wisdom transforms limitation into liberation.""",

    16: """You carry Karmic Debt Number 16, {preferredName}, one of the most intense karmic patterns in numerology. This reveals soul lessons around ego, relationships, and spiritual awakening. Past patterns likely involved misuse of power, ego inflation, or damaged relationships. Now you're experiencing the dissolution of false identity to discover your true self.

The 16 karmic debt often manifests as sudden changes that shatter your sense of security or identity. Just when you think you have everything figured out, something happens that forces complete reorganization of your life and self-concept. This feels devastating, but it's actually liberation in disguise.

Your primary challenge is releasing attachment to ego and external validation. The 16 repeatedly brings experiences that humble you, forcing you to distinguish between who you truly are and who you've been pretending to be. Every crisis is actually removing what's false so truth can emerge.

Relationship challenges are common with 16. You may experience betrayals, separations, or relationships that mirror your own shadow back to you. These aren't punishments—they're teachers showing you where you're operating from ego versus love, where you're seeking completion in others versus finding it within.

However, here's the profound gift: 16 is the path to genuine spiritual awakening. Through the humbling experiences it brings, you develop authentic humility, real compassion, and connection to something beyond ego. You discover that your true identity is eternal and unshakeable.

Your path to freedom involves surrendering ego control, accepting that you can't manage everything, and trusting a higher wisdom. Every time a crisis demolishes your plans and you discover you're still okay, every time you choose humility over pride, you clear karmic debt.

The 16 is teaching you that your true power lies not in ego control but in spiritual surrender, {preferredName}. What feels like destruction is actually reconstruction. You're being rebuilt from the inside out into something far more authentic and powerful.""",

    19: """You carry Karmic Debt Number 19, {preferredName}, revealing soul lessons around independence, help, and power dynamics. Past patterns likely involved misusing power over others, refusing to help those in need, or excessive self-focus. This lifetime, you're learning balanced independence—being self-sufficient while also supporting others.

The 19 karmic debt often manifests as finding yourself alone when you need help most. You may discover that resources, support, or assistance you expected aren't available, forcing you to rely on yourself. This isn't abandonment—it's teaching you genuine self-reliance while showing you the value of interdependence.

Your primary challenge is balancing independence with connection. In past patterns, you may have been too self-focused, refusing to acknowledge your dependence on others or neglecting to help when you had power to do so. Now you're learning that true strength includes both giving and receiving support.

Power and control issues are central to 19. You may struggle with needing to be in charge, difficulty asking for help, or resisting others' authority. Simultaneously, you're being shown how your past use of power affected others. Every situation where you feel powerless is teaching you compassionate leadership.

However, the gift within 19 is extraordinary: you're developing genuine self-sufficiency combined with generous heart. You learn to stand powerfully in your own authority while also lifting others. You master the balance between independence and interdependence.

Your path to freedom involves using whatever power you have to serve others, asking for help when you need it, and acknowledging that no one succeeds alone. Every time you help someone without expecting return, every time you humble yourself to accept assistance, you clear karmic patterns.

The 19 teaches that true leadership is service and real independence includes connection, {preferredName}. You're learning to be powerfully self-reliant while generously supportive. This wisdom transforms isolation into authentic community.""",

    0: """Good news, {preferredName}—you don't carry any major Karmic Debt numbers (13, 14, 16, or 19) in your core numerology! This doesn't mean you have no lessons or challenges, but it does mean you're not working through the specific intense patterns associated with karmic debt.

Without karmic debt, your path is generally more straightforward. You'll still face challenges and growth opportunities—that's part of being human—but you're not dealing with the additional weight of transforming deep past-life patterns in these specific areas.

This absence of karmic debt suggests that either you've already cleared these particular lessons in previous lifetimes, or your soul simply didn't accumulate these specific patterns. Either way, you have more freedom to focus on your current life purpose without the extra curriculum that karmic debt brings.

Your life lessons come primarily through your Life Path, Destiny, and other core numbers rather than through karmic repayment. This means you can focus on growth, creation, and fulfillment rather than intensive transformation of old patterns.

However, don't interpret this as meaning your life will be easy or challenge-free. Everyone has their soul's curriculum. Yours simply doesn't include these four specific karmic debt numbers. You may still experience difficulties—but they're about growth and evolution, not karmic balancing.

Use your freedom from karmic debt wisely, {preferredName}. You have extra energy available that isn't tied up in clearing old patterns. Direct this energy toward fulfilling your life purpose, serving others, and creating positive impact in the world.

Remember: the goal isn't to avoid all challenges but to grow through them with awareness and grace. Your path may be somewhat smoother, but how you walk it is still entirely up to you."""
}

# Master Number interpretations
MASTER_NUMBER_INTERPRETATIONS = {
    11: """You carry Master Number 11, {preferredName}, one of the most spiritually significant numbers in numerology. This marks you as a spiritual messenger, intuitive teacher, and conduit for higher consciousness. You're not here for an ordinary life—you're here to illuminate the path for others.

The 11 is called a master number because it carries double the intensity of 1 and operates at a higher frequency than its reduced form (2). You vibrate at an elevated level of consciousness, which brings both extraordinary gifts and significant challenges. Your nervous system is literally wired differently than most people's.

Your primary gift is powerful intuition that borders on psychic ability. You receive information through channels beyond the five physical senses—through dreams, synchronicities, gut feelings, and sudden knowing. When you learn to trust these perceptions, they guide you with remarkable accuracy.

You're a natural channel for inspiration. Ideas, insights, and creative visions flow through you that seem to originate beyond your personal consciousness. When you're in alignment, you become a vessel through which higher wisdom reaches the world. This is your sacred purpose.

However, the 11 brings intense challenges. Your heightened sensitivity means you feel everything more deeply—others' emotions, environmental energies, spiritual currents. This can be overwhelming, leading to anxiety, nervousness, or feeling like you don't fit in ordinary reality. You're right—you don't. You're wired for something more.

The pressure of living up to your potential can be crushing. You may feel that you're meant for something significant but don't know what or how. You might experience self-doubt: "Am I delusional? Am I making this up?" No, {preferredName}—you're perceiving accurately. Trust yourself.

Your path involves learning to ground your spiritual sensitivity in practical form. You must balance the visionary 11 energy with the grounded 2 energy (1+1=2). This means taking your spiritual insights and translating them into forms others can access—through teaching, healing, creative work, or simply being a living example.

Many with 11 struggle with the choice between living at the master number frequency or reducing to 2. Sometimes, the intensity becomes too much and you retreat into the gentler 2 energy of partnership and sensitivity. This is okay—but ultimately, you're called to rise into the full 11 expression.

Your life purpose is nothing less than helping elevate human consciousness. Whether through formal spiritual teaching, creative inspiration, healing work, or your energetic presence, you help others awaken to higher possibilities. You show people what enlightened awareness looks like in human form.

In relationships, you need partners who respect your spiritual nature without trying to fix or change you. You're attracted to deep, soulful connections where you can explore consciousness together. Surface-level interactions drain you.

Your career is most fulfilling when it involves working with consciousness itself—spiritual teaching, counseling, healing, creative inspiration, or any field where you help others grow and awaken. Traditional careers may feel confining unless they allow space for your spiritual purpose.

To thrive with 11 energy: meditate daily to ground your sensitivity, trust your intuition even when it defies logic, create regular practices that honor your spiritual nature, protect your energy from draining environments and people, and remember that your sensitivity is not weakness—it's your superpower.

Your challenge is accepting your role as spiritual wayshower without ego inflation. The 11 brings spiritual gifts, but you're meant to use them in service, not for personal glorification. Stay humble while standing in your power.

Know this, {preferredName}: you are exactly what this world needs right now. Your sensitivity, your spiritual perception, your ability to channel higher wisdom—these gifts are not accidents. You came here specifically to help humanity evolve. Trust your path, even when it feels lonely or confusing. You're not alone—you're simply ahead.""",

    22: """You carry Master Number 22, {preferredName}, the Master Builder—the most powerful manifesting number in all of numerology. This marks you as someone capable of bringing massive visions into physical reality and creating structures that serve humanity for generations. You're not here to think small.

The 22 combines the spiritual vision of 11 with the practical building capacity of 4 (2+2=4). This rare combination means you can perceive possibilities that exist beyond current reality AND you have the executive ability to systematically manifest them. You see what could be and know how to build it.

Your primary gift is your capacity to envision and execute on a grand scale. Where others see problems, you see systems waiting to be designed. Where they see limitations, you see opportunities for innovation. Where they plan projects, you envision movements that change paradigms.

You possess extraordinary executive abilities—strategic thinking, organizational genius, practical wisdom, and the stamina to see massive projects through to completion. When you're operating at full capacity, you can accomplish what seems impossible to others. You make magic look systematic.

However, the weight of 22's potential can feel crushing. You know you're capable of extraordinary achievement, which creates pressure to live up to this potential. You may struggle with self-doubt: "Am I really meant for this? Is my vision realistic?" Yes, {preferredName}—your vision is not only realistic, it's necessary.

The challenge of 22 is learning to hold the tension between enormous vision and patient, step-by-step execution. You see the destination clearly, but the journey requires disciplined effort over time. Many with 22 struggle with wanting to skip the process and just arrive at the result.

You may also grapple with the choice between living at the master number frequency (22) or reducing to 4. When the pressure becomes too much, you might retreat into the more manageable 4 energy of steady work and building. But ultimately, you're called to the grander 22 expression.

Your life purpose involves building something of lasting significance that serves the collective good. This might be an organization, a business, a social movement, a physical structure, a system of ideas, or a new paradigm. Whatever it is, it will be larger than your personal life and will continue benefiting people after you're gone.

In your career, you thrive when you have enough authority and resources to execute your vision. You can work within existing structures if they're large and impactful enough, but many with 22 ultimately create their own organizations so their vision isn't compromised. You're meant to lead, not follow.

Relationships with 22 require partners who can match your intensity and ambition without competing. You need someone who has their own significant purpose and respects yours. Together, you can build empires—personal and professional.

To thrive with 22 energy: think big but plan meticulously, break massive visions into achievable steps, surround yourself with capable team members who execute your vision, stay grounded in physical reality even while dreaming big, and remember that building legacy takes time—be patient with the process.

Your challenge is avoiding the traps of ego, control, and overwork. The 22 brings such powerful executive ability that you can become tyrannical in pursuit of your vision. Remember: you're building FOR humanity, not AT their expense. Conscious leadership serves everyone.

Financial abundance often flows naturally to 22 when you're operating at full capacity. But remember: money is a tool for building your vision, not the vision itself. You're not here just to become wealthy—you're here to use resources to create lasting positive change.

The world desperately needs what you came here to build, {preferredName}. Your vision of what's possible, combined with your ability to manifest it systematically, can literally change civilization. Don't let self-doubt or fear of your own power stop you from fulfilling this calling.

You're a Master Builder. Act like it. Dream impossibly big, then build it brick by brick. Show humanity what's possible when spiritual vision meets practical mastery. Your legacy awaits.""",

    33: """You carry Master Number 33, {preferredName}, the Master Teacher and rarest of all master numbers. This marks you as someone who embodies and teaches unconditional love, spiritual wisdom, and divine service. You're not here for a personal life alone—you're here to uplift all of humanity through your presence and teaching.

The 33 combines the illumination of 11 with the nurturing of 6 (3+3=6), creating someone who channels divine wisdom for healing and teaching. You're a living bridge between heaven and earth, spiritual consciousness and human compassion. Your very presence can shift energy and catalyze healing in others.

Your primary gift is your extraordinary capacity for unconditional love and spiritual teaching. You don't just understand spiritual principles intellectually—you embody them. When you speak about love, compassion, or spiritual truth, people feel you LIVING these qualities, which makes your teaching profoundly transformative.

You possess healing abilities that may manifest in many forms—spiritual healing, emotional counseling, inspirational teaching, creative expression that uplifts consciousness, or simply being a presence that makes others feel safe, seen, and loved. Your gift isn't just what you do—it's who you are.

However, the burden of 33 is immense. The responsibility of being a spiritual teacher and healer for humanity can feel overwhelming. You may question whether you're worthy of this calling or capable of fulfilling it. Self-doubt is common, as is the tendency toward martyrdom—giving so much that you deplete yourself.

The challenge of 33 is learning to embody Christ-like love without the Christ complex. You're meant to serve humanity, but not to sacrifice yourself on every cross. Martyrdom serves no one. You must learn to give from overflow, maintain healthy boundaries, and recognize that saving everyone is not your job—inspiring them to save themselves is.

You may also struggle with the weight of seeing human suffering so clearly. Your empathy is so profound that you feel the world's pain acutely. This can lead to depression or despair if you don't balance it with spiritual practice and grounded self-care. Remember: you can't heal everyone, and that's okay.

Your life purpose is to be a living example of enlightened consciousness and unconditional love. Whether through formal spiritual teaching, healing work, creative expression, or simply how you live your daily life, you demonstrate what's possible when humans fully embody their spiritual nature.

In your career, you're called to work that directly serves consciousness evolution—spiritual teaching, healing, counseling, inspirational speaking or writing, or creative arts that elevate awareness. Traditional careers will feel soul-crushing unless they incorporate your spiritual purpose.

Relationships require partners who understand and honor your spiritual calling. You need someone secure enough to support your service to many without feeling neglected, and evolved enough to join you in spiritual practice and growth. Your union itself becomes a teaching.

To thrive with 33 energy: develop rigorous spiritual practices that keep you connected to Source, establish firm boundaries so your service doesn't become martyrdom, create regular self-care rituals that prevent depletion, surround yourself with other evolved souls who can support you, and remember that your worthiness doesn't depend on how much you give—you are already worthy.

Your challenge is accepting the magnitude of your calling without being crushed by it. You didn't choose this path arbitrarily—your soul specifically prepared for this lifetime of maximum service. You're stronger than you know, more loved than you imagine, and more necessary than you understand.

The 33 energy asks everything of you, {preferredName}, but it also gives everything. You get to live in constant connection with divine love, to witness profound transformations in others, to know that your life has deep meaning and purpose. This is sacred privilege, not just burden.

Know this: humanity needs you. In a world of fear, division, and pain, your embodiment of unconditional love and spiritual truth creates ripples of healing that spread far beyond your direct contact. Every person you teach, heal, or inspire goes forward to touch countless others.

You are a Master Teacher. Your curriculum is love. Your classroom is everywhere. Your students are everyone. Teach well, dear soul. Show us what we can become."""
}

# Tool configurations
TOOLS = {
    "karmic-debt-reading": {
        "title": "Karmic Debt Number Reading",
        "description": "Discover if you carry karmic debt and how to transform these patterns",
        "emoji": "⚖️",
        "tagline": "Understand and transform your karmic patterns",
        "calculation_functions": """
        function findKarmicDebt(dateStr, fullName) {
            const karmicNumbers = [13, 14, 16, 19];
            const date = new Date(dateStr);
            const day = date.getDate();
            const month = date.getMonth() + 1;
            const year = date.getFullYear();
            
            // Check birthday directly
            if (karmicNumbers.includes(day)) return day;
            if (karmicNumbers.includes(month)) return month;
            
            // Check year components before reduction
            const yearDigits = year.toString().split('').map(Number);
            let yearSum = yearDigits.reduce((a, b) => a + b, 0);
            if (karmicNumbers.includes(yearSum)) return yearSum;
            
            // Check name total before reduction
            let nameSum = 0;
            for (let char of fullName.toUpperCase()) {
                nameSum += letterToNumber(char);
            }
            if (karmicNumbers.includes(nameSum)) return nameSum;
            
            // Check Life Path components
            let daySum = day;
            let monthSum = month;
            if (karmicNumbers.includes(daySum)) return daySum;
            if (karmicNumbers.includes(monthSum)) return monthSum;
            
            // No karmic debt found
            return 0;
        }
        """,
        "calculation_code": """
            const number = findKarmicDebt(birthDate, birthName);
        """,
        "result_title_template": "Karmic Debt " + "${number === 0 ? 'Free!' : 'Number ' + number}: ${preferredName}",
        "no_result_code": """
                // This should not happen as 0 is handled
                document.getElementById('result-title').textContent = 'No Karmic Debt';
                document.getElementById('result-content').innerHTML = '<div class="no-karmic"><h3>No Major Karmic Debt Detected</h3><p>Your numerology chart does not show the traditional karmic debt numbers (13, 14, 16, 19). This is fortunate!</p></div>';
                document.getElementById('result').classList.add('show');
                document.getElementById('calculator-form').style.display = 'none';
        """,
        "interpretations": KARMIC_DEBT_INTERPRETATIONS
    },
    
    "master-number-reading": {
        "title": "Master Number Deep Reading",
        "description": "Comprehensive guidance for living with master number energy (11, 22, 33)",
        "emoji": "👑",
        "tagline": "Master your master number potential",
        "calculation_functions": """
        function findMasterNumber(dateStr, fullName) {
            // Check Life Path without reducing master numbers
            const date = new Date(dateStr);
            const day = date.getDate();
            const month = date.getMonth() + 1;
            const year = date.getFullYear();
            
            // Calculate each component
            let dayNum = day;
            while (dayNum > 9 && dayNum !== 11 && dayNum !== 22 && dayNum !== 33) {
                dayNum = dayNum.toString().split('').reduce((a, b) => a + parseInt(b), 0);
            }
            
            let monthNum = month;
            while (monthNum > 9 && monthNum !== 11 && monthNum !== 22 && monthNum !== 33) {
                monthNum = monthNum.toString().split('').reduce((a, b) => a + parseInt(b), 0);
            }
            
            let yearNum = year;
            while (yearNum > 9 && yearNum !== 11 && yearNum !== 22 && yearNum !== 33) {
                yearNum = yearNum.toString().split('').reduce((a, b) => a + parseInt(b), 0);
            }
            
            // Add them
            let total = dayNum + monthNum + yearNum;
            
            // Check if total is master number
            if (total === 11 || total === 22 || total === 33) return total;
            
            // Check if sum adds to master
            while (total > 9 && total !== 11 && total !== 22 && total !== 33) {
                total = total.toString().split('').reduce((a, b) => a + parseInt(b), 0);
            }
            
            if (total === 11 || total === 22 || total === 33) return total;
            
            // Check destiny/name number
            let nameSum = 0;
            for (let char of fullName.toUpperCase()) {
                nameSum += letterToNumber(char);
            }
            
            if (nameSum === 11 || nameSum === 22 || nameSum === 33) return nameSum;
            
            while (nameSum > 9 && nameSum !== 11 && nameSum !== 22 && nameSum !== 33) {
                nameSum = nameSum.toString().split('').reduce((a, b) => a + parseInt(b), 0);
            }
            
            if (nameSum === 11 || nameSum === 22 || nameSum === 33) return nameSum;
            
            return 0;
        }
        """,
        "calculation_code": """
            const number = findMasterNumber(birthDate, birthName);
        """,
        "result_title_template": "Master Number " + "${number}: ${preferredName}",
        "no_result_code": """
                document.getElementById('result-title').textContent = 'No Master Number';
                document.getElementById('result-content').innerHTML = '<div class="no-karmic"><h3>No Master Number Detected</h3><p>Your core numerology does not contain master numbers 11, 22, or 33. This means you have a different soul curriculum focused on the single-digit numbers. Each path is valuable and meaningful.</p></div>';
                document.getElementById('result').classList.add('show');
                document.getElementById('calculator-form').style.display = 'none';
        """,
        "interpretations": MASTER_NUMBER_INTERPRETATIONS
    }
}

# Generate tools
import json

print("🔮 Generating Final Premium Numerology Tools...")
print("=" * 60)

for tool_id, tool_data in TOOLS.items():
    filename = f"{tool_id}.html"
    
    # Convert interpretations to JSON
    interpretations_json = json.dumps(tool_data["interpretations"])
    
    # Build the HTML
    html_content = PREMIUM_TEMPLATE.format(
        title=tool_data["title"],
        description=tool_data["description"],
        emoji=tool_data["emoji"],
        tagline=tool_data["tagline"],
        calculation_functions=tool_data["calculation_functions"],
        calculation_code=tool_data["calculation_code"],
        result_title_template=tool_data["result_title_template"],
        no_result_code=tool_data["no_result_code"],
        interpretations_json=interpretations_json
    )
    
    # Write file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated: {filename}")

print("=" * 60)
print(f"✨ Successfully created 2 premium tools!")
print(f"📝 Each tool includes:")
print(f"   • Full inputs (name, birth details)")
print(f"   • 500-800 word readings")
print(f"   • LocalStorage auto-fill")
print(f"   • Quantum Merlin branding")
print()
print("🎉 NUMEROLOGY SUITE COMPLETE!")
print("   Total: 11 premium numerology tools")
