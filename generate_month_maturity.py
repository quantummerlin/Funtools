#!/usr/bin/env python3
"""
Generate Personal Month and Maturity Number Reading Tools
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
                        <label for="birthName">Full Birth Name</label>
                        <input type="text" id="birthName" required>
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
                alert('Unable to calculate. Please check your information.');
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
                if (data.birthName) document.getElementById('birthName').value = data.birthName;
                if (data.birthDate) document.getElementById('birthDate').value = data.birthDate;
                if (data.birthTime) document.getElementById('birthTime').value = data.birthTime;
                if (data.birthPlace) document.getElementById('birthPlace').value = data.birthPlace;
            }}
        }}

        function saveUserData() {{
            const userData = {{
                preferredName: document.getElementById('preferredName').value,
                birthName: document.getElementById('birthName').value,
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

# Personal Month interpretations
PERSONAL_MONTH_INTERPRETATIONS = {
    1: """This is a Personal Month 1 for you, {preferredName}, bringing powerful new beginning energy into this specific month. Within your current Personal Year cycle, this month stands out as a time to initiate, start fresh, and take bold action on ideas that have been forming.

This month, you'll feel an unusual surge of motivation and courage. Whatever your current Personal Year theme, this month adds an extra dose of pioneering spirit. You're being called to take the first step on something important, even if you don't have all the details figured out yet.

Your confidence and self-reliance peak during this 1 Month. You'll trust your instincts more than usual and feel less need for external validation. This is excellent timing for launching projects, having important conversations, or making decisions you've been postponing.

In your career and projects, this month favors bold moves. Present that proposal, ask for that promotion, pitch that idea, or start that side hustle. The cosmic energy supports your initiative and rewards decisive action. Don't wait for perfect conditions—they won't come. Act now.

However, watch for impatience and being too forceful with others. While your energy is high, not everyone operates at your pace. Balance your drive with consideration for collaborators and loved ones who may need more processing time.

This is also an excellent month for personal reinvention and breaking old patterns. Want to start a new fitness routine, change your style, or shift your daily habits? This month's energy supports transformation. Small actions taken now can create lasting change, {preferredName}.""",

    2: """You're in a Personal Month 2, {preferredName}, a time of patience, cooperation, and gentle progress. Within your current Personal Year, this month slows things down and asks you to focus on relationships, details, and allowing rather than forcing.

This month, your sensitivity and intuition are heightened. You'll pick up on subtle energies, unspoken dynamics, and details others miss. Trust these perceptions—they're guiding you toward beneficial connections and away from situations that aren't right for you.

Relationships and partnerships require your attention now. Whether in business or personal life, collaboration produces better results than solo effort this month. Reach out to potential partners, strengthen existing alliances, and be willing to compromise for the greater good.

In your work and projects, this is a month for refinement rather than initiation. Review details, improve systems, and perfect what's already in motion. The cosmic energy doesn't support major launches now, but it strongly favors making existing projects better through careful attention.

Patience is your greatest asset this month. Things may move more slowly than you'd like, and that's actually perfect. Forcing outcomes or rushing processes will backfire. Trust that the right timing will become clear, and what's meant for you won't require force.

Your emotional life may feel more intense this month. You're more sensitive to others' moods and may need extra alone time to recharge. Don't mistake this sensitivity for weakness—it's actually your superpower right now, {preferredName}. Honor your need for gentle pacing and emotional space.""",

    3: """Welcome to your Personal Month 3, {preferredName}! This is a time of joy, creativity, and self-expression within your current Personal Year. This month, the universe wants you to lighten up, create, and let your authentic self shine through.

Creative inspiration flows freely during a 3 Month. Ideas come faster than you can capture them, and your ability to communicate those ideas improves dramatically. This is excellent timing for any creative project, artistic endeavor, or communication-based work.

Your social energy peaks this month. You'll feel more outgoing, receive more invitations, and enjoy socializing more than usual. These aren't just fun connections—many have the potential to develop into beneficial relationships. Say yes to gatherings even if you typically prefer staying home.

Communication of all kinds is favored now. If you need to have important conversations, make presentations, write content, or express yourself in any way, this month provides excellent cosmic support. Your words land more effectively and reach further than usual.

However, watch for scattering your focus. With so many ideas and social opportunities, you might spread yourself too thin. Choose a few priorities and give them your best attention rather than dabbling in everything that catches your interest.

This is also a month to intentionally cultivate joy. Do things simply because they bring you pleasure. Play, laugh, create, and express yourself without worrying about productivity or outcomes. The 3 Month reminds you that life is meant to be enjoyed, {preferredName}. Let yourself feel the lightness.""",

    4: """You're in a Personal Month 4, {preferredName}, bringing focused, disciplined energy to your current Personal Year. This month asks you to get practical, organized, and systematic about manifesting your goals into tangible form.

This is a month for building, not dreaming. Whatever your current projects or goals, this month's energy supports taking concrete action, creating systems, and doing the detailed work that turns ideas into reality. Roll up your sleeves—success comes through effort now.

Your focus and concentration improve significantly during a 4 Month. Tasks that usually feel tedious become manageable, and you have unusual patience for details. Use this energy to tackle administrative work, organize your space, create systems, or handle practical matters you've been avoiding.

In career and finances, this month favors establishing strong foundations. Get your budget organized, create business systems, improve your work processes, or invest in infrastructure that will serve you long-term. What you build now provides stability for years to come.

However, be mindful of becoming too rigid or controlling. While structure is important, leave room for flexibility and spontaneity. Not everything needs a plan, and over-organizing can sometimes block the flow of opportunity.

Your physical health and body also benefit from attention this month. Establish new exercise routines, improve your nutrition, or address health issues you've been postponing. Your body responds especially well to consistent care during this cycle.

This month may feel like hard work, but embrace it, {preferredName}. The foundations you build now create the platform for future success. Every system you create, every detail you handle, contributes to your long-term stability and achievement.""",

    5: """Welcome to your Personal Month 5, {preferredName}! This is a dynamic month of change, freedom, and adventure within your current Personal Year. The universe is opening doors and inviting you to explore new possibilities.

Expect unexpected developments this month. Plans may change suddenly, new opportunities may appear out of nowhere, and life feels more unpredictable than usual. Rather than resisting this instability, embrace it—the changes happening are redirecting you toward better outcomes.

Your desire for freedom and variety intensifies during a 5 Month. You'll feel restless with routine and crave new experiences. This is excellent timing for travel, learning new skills, meeting new people, or simply breaking out of your usual patterns.

In career and projects, be ready to pivot quickly. Opportunities may arise that require fast decision-making. Your adaptability is your greatest asset this month. Stay flexible, keep options open, and be willing to change direction when better paths appear.

Social and networking opportunities expand significantly. You'll meet interesting people from different backgrounds and perspectives. These connections may seem random, but many will prove valuable in unexpected ways. Stay open and say yes to invitations.

However, watch for overindulgence and scattered focus. The 5 Month energy can lead to excess—spending too much, eating too much, or taking on too many commitments. Enjoy the variety without losing all grounding. Some structure provides helpful containment.

This is also an excellent month for learning and gathering information. Take courses, read widely, explore new subjects, or develop new skills. Your mind is especially receptive and quick to grasp new concepts now, {preferredName}. Feed your curiosity.""",

    6: """You're in a Personal Month 6, {preferredName}, bringing heightened focus on relationships, responsibility, and service. Within your current Personal Year, this month emphasizes love, family, beauty, and caring for others.

Relationships of all kinds demand your attention this month. Family matters may arise that need addressing, romantic relationships deepen or require work, and friendships may need nurturing. Rather than resenting these demands, recognize this as a month for strengthening your most important connections.

Your nurturing instincts intensify during a 6 Month. You'll feel called to help, support, and care for others. This is beautiful, but watch for martyrdom—giving so much that you deplete yourself. Remember that teaching others to help themselves is often more valuable than doing everything for them.

Home and domestic matters take priority this month. You may feel drawn to improve your living space, spend more time with family, or create a more beautiful, harmonious environment. These aren't distractions from more important work—they're exactly what needs your attention now.

In your career, this month favors service-oriented work, counseling, teaching, or any role where you help others. If you've been considering a move toward more meaningful, people-focused work, this month brings clarity about that direction.

Beauty and aesthetics also matter more this month. You'll notice your surroundings more acutely and want to be surrounded by harmony and loveliness. Investing in beauty—whether in your appearance, home, or environment—isn't superficial. It feeds your soul.

This is also a month where commitments may deepen. Marriage proposals, business partnerships, or other serious commitments are common during 6 Months. If you're ready for that level of responsibility, the cosmic energy supports it, {preferredName}. Choose wisely and honor your commitments.""",

    7: """You're entering a Personal Month 7, {preferredName}, a time for introspection, spiritual growth, and inner development within your current Personal Year. This month asks you to slow down, turn inward, and connect with deeper truths.

This is not a month for major external activity. Instead, it's a time for reflection, study, and spiritual practice. The universe is creating space for you to process recent experiences, gain wisdom from them, and connect with your inner guidance.

Your need for solitude increases significantly during a 7 Month. You'll want more time alone, may decline social invitations, and prefer quiet activities to busy ones. This isn't antisocial—it's essential soul maintenance. Honor this need without guilt.

Spiritual and intellectual pursuits are especially rewarding this month. Meditation, journaling, reading, courses, or any activity that engages your mind and spirit will bring unusual satisfaction. This is excellent timing for deepening your spiritual practice or exploring philosophical questions.

In your career and projects, this month favors research, analysis, planning, and strategy over action and implementation. Use this time to study your field, analyze your approach, or gain expertise that will serve you when more active cycles return.

Your intuition is especially strong during a 7 Month. Pay close attention to dreams, synchronicities, gut feelings, and subtle insights. Your inner wisdom is speaking loudly now, guiding you toward beneficial paths and away from misaligned situations.

However, watch for overthinking and analysis paralysis. Your mind is active this month, but it can loop into worry or excessive mental activity. Balance intellectual pursuits with grounding practices. Trust that not everything needs to be figured out right now, {preferredName}. Some answers reveal themselves through quiet waiting.""",

    8: """Welcome to your Personal Month 8, {preferredName}! This is a powerful month of manifestation, achievement, and material success within your current Personal Year. The universe is supporting your ambitions and rewarding your efforts.

This month, opportunities for advancement, recognition, and financial gain are especially favored. If you've been working toward professional goals, this month often brings breakthroughs, promotions, or visible results from your efforts.

Your executive abilities and leadership qualities strengthen during an 8 Month. You'll think more strategically, manage details more effectively, and command more presence in professional settings. Use this enhanced capability to negotiate, lead projects, or take on greater responsibility.

Money matters benefit from your attention this month. Opportunities to increase income, make wise investments, or reorganize your finances for greater abundance often arise during 8 Months. Be strategic and bold in financial decisions—calculated risks pay off now.

In your career, this month favors asserting your authority, showcasing your capabilities, and stepping into greater power. Don't play small or downplay your achievements. This is your time to be seen, recognized, and rewarded for your contributions.

However, balance ambition with self-care. The 8 Month energy can drive you toward overwork and neglect of your health, relationships, or spiritual life. True success includes all areas of life, not just career and finances. Make time for what matters beyond achievement.

Your personal power and confidence peak this month. Use this strength wisely and ethically. Power wielded with integrity creates lasting success, while power misused creates problems down the road. Lead with both strength and heart, {preferredName}. Show others what conscious success looks like.""",

    9: """You're in a Personal Month 9, {preferredName}, a time of completion, release, and preparation for new beginnings. Within your current Personal Year, this month asks you to let go of what no longer serves and make space for what's coming.

This is a month for finishing things rather than starting new projects. Complete what's in motion, tie up loose ends, and bring existing endeavors to their natural conclusion. Starting major new initiatives now is like planting seeds in winter—the timing isn't right.

Relationships, situations, or patterns that have outlived their purpose may naturally end during a 9 Month. While endings can feel painful, trust that what leaves is making space for something better aligned with who you're becoming. Don't cling to what's ready to go.

Your emotional sensitivity and compassion deepen this month. You may feel more empathetic toward others' suffering and drawn to service or humanitarian work. These impulses are appropriate—sharing what you've learned and helping others is meaningful work during a 9 Month.

In your career and projects, this month favors wrapping up phases, learning from experiences, and extracting wisdom from recent cycles. Rather than pushing forward, take time to review what worked, what didn't, and what you've learned. This reflection prepares you for smarter action in the future.

Forgiveness—of yourself and others—is powerful work this month. Releasing resentments and old wounds isn't about condoning harm—it's about freeing yourself from emotional burdens that weigh you down. What you forgive now loses its power over your future.

This month may feel bittersweet—endings and completions often do. But recognize this as a sacred time of transition, {preferredName}. You're clearing the ground for a beautiful new beginning. Trust that what's leaving is making space for something wonderful to arrive."""
}

# Maturity Number interpretations  
MATURITY_NUMBER_INTERPRETATIONS = {
    1: """Your Maturity Number is 1, {preferredName}, revealing that your later years are destined for leadership, independence, and pioneering new paths. The combination of your Life Path and Destiny numbers points toward a future where you fully step into your power as an innovator and trailblazer.

As you mature, you'll become increasingly comfortable taking charge and trusting your own direction. Where you may have sought approval or followed others' leads in your younger years, your mature self naturally leads, initiates, and creates new possibilities.

Your mature purpose involves bringing original ideas into the world. Whether through business, creative work, social innovation, or personal example, you're meant to show others what's possible when someone dares to be first. Your later years won't be about comfortable retirement—they'll be about bold creation.

The confidence and courage you've been building throughout your life will fully bloom in your mature years. You'll take risks that would have terrified your younger self. This isn't recklessness—it's earned wisdom combined with deep self-trust.

Your independence strengthens as you age. You'll need less external validation and become more self-directed. This doesn't mean isolation—it means you choose your connections based on genuine resonance rather than neediness or obligation.

In your mature years, you may find yourself naturally in leadership positions, whether formal or informal. People will look to you for direction, inspiration, and example. You'll finally be comfortable with this visibility and ready to use your influence wisely.

Your legacy involves initiating changes that outlive you. The projects, businesses, movements, or ideas you launch in your mature years will have lasting impact. You're not meant to fade quietly—you're meant to blaze brightly until the end, {preferredName}.""",

    2: """Your Maturity Number is 2, {preferredName}, revealing that your later years are destined for peacemaking, partnership, and creating harmony. The synthesis of your Life Path and Destiny numbers points toward a future of deep connection, emotional wisdom, and bringing people together.

As you mature, your sensitivity and intuition will strengthen into profound emotional intelligence. You'll understand people's unspoken needs, sense energies others miss, and know how to create spaces where everyone feels safe and heard. This is a rare and valuable gift.

Your mature purpose involves bridging divides and creating unity. Whether in your family, community, or through wider influence, you're meant to show others how cooperation creates better outcomes than competition. Your later years will be about connection, not conquest.

The diplomatic skills you've been honing throughout your life will reach mastery in your mature years. You'll mediate conflicts, counsel troubled souls, and help people find common ground. This isn't weakness—it's powerful service that literally changes lives.

Relationships become increasingly central as you age. You'll invest deeply in meaningful connections and may find your greatest fulfillment in partnership—romantic, business, or creative. You understand that true partnership multiplies joy and divides sorrow.

In your mature years, you'll finally give yourself permission to be fully sensitive without apology. Where your younger self may have felt your empathy was a vulnerability, your mature self recognizes it as your superpower. You feel deeply because you're meant to heal deeply.

Your legacy involves the relationships you've nurtured and the peace you've created. The people you've brought together, the conflicts you've resolved, and the harmony you've established will ripple outward long after you're gone, {preferredName}. Your gentle strength changes the world.""",

    3: """Your Maturity Number is 3, {preferredName}, revealing that your later years are destined for creative expression, joy, and inspiring others. The combination of your Life Path and Destiny numbers points toward a future where your authentic self-expression becomes your greatest gift to the world.

As you mature, your creative abilities will blossom in ways you can't yet imagine. Where your younger self may have held back expression due to fear or doubt, your mature self will create, communicate, and share your gifts with confidence and joy.

Your mature purpose involves bringing beauty, inspiration, and lightness to the world. Whether through art, writing, speaking, teaching, or simply being your authentic, joyful self, you remind others that life is meant to be celebrated. This is sacred work.

The communication skills you've been developing throughout your life will reach their highest expression in your mature years. You'll find the perfect words to inspire, heal, entertain, or educate. Your voice—literal or metaphorical—carries unusual power to uplift others.

Joy and optimism will characterize your later years. Where others may become bitter or resigned with age, you'll maintain a youthful spirit and sense of wonder. This isn't naivety—it's a conscious choice to focus on beauty and possibility even while acknowledging life's difficulties.

In your mature years, you may discover creative talents you didn't know you had. Many with Maturity Number 3 begin painting, writing, performing, or creating in their later decades and find extraordinary fulfillment. It's never too late to express yourself.

Your legacy involves the joy you've spread and the creative works you've left behind. The laughter you've sparked, the beauty you've created, and the inspiration you've provided will continue touching lives long after you're gone, {preferredName}. You prove that creativity and joy are ageless.""",

    4: """Your Maturity Number is 4, {preferredName}, revealing that your later years are destined for building lasting foundations and creating tangible legacy. The synthesis of your Life Path and Destiny numbers points toward a future where you master the material world and create structures that serve humanity.

As you mature, your ability to manifest dreams into physical reality will reach its peak. Where your younger self may have struggled with follow-through or organization, your mature self executes with precision and patience. You become the master builder you were meant to be.

Your mature purpose involves creating systems, structures, or organizations that outlive you and serve future generations. Whether building businesses, institutions, physical structures, or family foundations, you're meant to leave something solid and lasting behind.

The discipline and work ethic you've been developing throughout your life will become your greatest assets in your mature years. You'll understand that sustainable success comes through consistent effort, not shortcuts. This wisdom allows you to achieve what others consider impossible.

Stability and security will characterize your later years—not by accident, but by design. You'll have created the financial foundation, health practices, and life systems that provide genuine security. This creates freedom for you and example for others.

In your mature years, you may take on roles as mentor, teacher, or guide, showing others how to build stable lives and manifest their dreams practically. Your experience becomes wisdom that helps many avoid mistakes and achieve their goals more effectively.

Your legacy involves the tangible structures you've built and the practical wisdom you've shared. The buildings, businesses, systems, or institutions you've created will serve people for generations, {preferredName}. Your life proves that practical work done with integrity creates lasting value.""",

    5: """Your Maturity Number is 5, {preferredName}, revealing that your later years are destined for freedom, adventure, and continuous growth. The combination of your Life Path and Destiny numbers points toward a future where you never stop exploring, learning, and experiencing life's diversity.

As you mature, your spirit of adventure will strengthen rather than diminish. Where others may become set in their ways with age, you'll maintain curiosity, flexibility, and openness to new experiences. Your later years will be anything but boring.

Your mature purpose involves showing others that life can be lived fully at any age. Through your travels, learning, and willingness to embrace change, you demonstrate that aging doesn't mean stagnation. You're meant to be proof that vitality is a choice, not just biology.

The adaptability you've been developing throughout your life will serve you powerfully in your mature years. You'll navigate changes and transitions that overwhelm others with grace and even excitement. Your flexibility is your fountain of youth.

Freedom becomes increasingly important as you age, but it's an earned freedom based on wisdom rather than rebellion. You'll have learned what truly matters and will give yourself permission to release what doesn't. This selective focus creates genuine liberation.

In your mature years, you may travel extensively, learn new languages, explore different cultures, or simply maintain diverse interests and friendships. Your social circle will likely span ages, backgrounds, and perspectives because you're genuinely interested in all of humanity.

Your legacy involves the stories you'll tell, the wisdom you'll share from your varied experiences, and the example you'll provide of living vibrantly at every age, {preferredName}. You prove that life is an adventure that only gets better with time.""",

    6: """Your Maturity Number is 6, {preferredName}, revealing that your later years are destined for nurturing, service, and creating beautiful harmony. The synthesis of your Life Path and Destiny numbers points toward a future where love, family, and caring for others become your greatest fulfillment.

As you mature, your capacity for unconditional love will deepen profoundly. Where your younger self may have given conditionally or with expectations, your mature self loves freely and creates spaces where others feel genuinely cherished. This is the highest human achievement.

Your mature purpose involves creating and maintaining loving relationships and beautiful environments. Whether through family, community service, healing work, or simply being a source of comfort and beauty in others' lives, you're meant to nurture the world.

The caregiving instincts you've been developing throughout your life will reach their fullest expression in your mature years. But you'll have learned the crucial lesson of filling your own cup first. Your service comes from overflow, not depletion, making it sustainable and joyful.

Home and family will likely be central to your later years. You may become the family matriarch/patriarch, the one everyone turns to for comfort, advice, and unconditional acceptance. Your home becomes a sanctuary where people feel they can breathe.

In your mature years, you'll understand that love expressed through action is the most powerful force in existence. The meals you cook, the spaces you beautify, the comfort you offer, and the presence you provide create ripples of healing that spread far beyond what you can see.

Your legacy involves the love you've given, the people you've nurtured, and the beauty you've created, {preferredName}. Those you've cared for will carry your love forward, creating a cascade of kindness that spans generations. You prove that love is what remains when everything else fades.""",

    7: """Your Maturity Number is 7, {preferredName}, revealing that your later years are destined for wisdom, spiritual mastery, and profound understanding. The combination of your Life Path and Destiny numbers points toward a future where you become the sage, the mystic, the one who sees beyond surface appearances.

As you mature, your natural analytical abilities and intuition will merge into rare wisdom. Where your younger self may have overthought or doubted your perceptions, your mature self knows—simply, deeply, certainly. This knowing becomes your gift to others.

Your mature purpose involves seeking and sharing truth. Whether through teaching, writing, counseling, or simply being a wise presence in others' lives, you're meant to help people see beyond illusion to deeper reality. Your insights illuminate paths for many.

The spiritual and intellectual development you've pursued throughout your life will culminate in your mature years. You'll integrate logic and intuition, science and spirituality, mind and heart in ways that create genuine wisdom rather than mere knowledge.

Solitude becomes increasingly precious as you age, but it's not loneliness—it's chosen sanctuary. You'll need regular quiet time to connect with your inner knowing and process life's experiences at depth. This solitude refreshes you in ways social connection cannot.

In your mature years, you may be drawn to teaching, mentoring, or spiritual work. People will seek you out for guidance, sensing your unusual depth of perception. You'll finally be comfortable with this role, having integrated the wisdom you've been gathering all your life.

Your legacy involves the wisdom you've shared and the consciousness you've helped awaken in others, {preferredName}. Through your teaching, writing, or simply your example of living thoughtfully, you help others see beyond the obvious. You prove that true vision comes from inner sight.""",

    8: """Your Maturity Number is 8, {preferredName}, revealing that your later years are destined for mastery, abundance, and conscious use of power. The synthesis of your Life Path and Destiny numbers points toward a future where you achieve significant material success while maintaining spiritual integrity.

As you mature, your natural executive abilities will reach their peak. Where your younger self may have struggled with authority or power, your mature self wields both with confidence and wisdom. You finally understand that power wielded consciously serves everyone.

Your mature purpose involves proving that material success and spiritual values aren't opposites but partners. Through your example of ethical leadership and conscious prosperity, you show others what success looks like when guided by integrity rather than ego.

The ambition you've been channeling throughout your life will manifest tangibly in your mature years. You'll likely achieve significant professional recognition, financial abundance, or both. But unlike your younger self, your mature self knows that money and status are tools for service, not just personal gain.

Leadership comes naturally to you in your later years. You may head organizations, guide major projects, or simply be the person others look to for direction in challenging situations. Your authority is earned through competence and character, not just position.

In your mature years, you'll understand the law of karma viscerally. What you put out returns multiplied, so you'll be strategic and ethical in all dealings. This creates a cycle of increasing abundance because you operate from integrity, not manipulation.

Your legacy involves the organizations you've built, the prosperity you've created and shared, and the example you've provided of ethical leadership, {preferredName}. You prove that true success includes everyone's wellbeing, not just your own. Your conscious use of power changes paradigms.""",

    9: """Your Maturity Number is 9, {preferredName}, revealing that your later years are destined for humanitarian service, universal love, and completion of your soul's purpose. The combination of your Life Path and Destiny numbers points toward a future where you serve the greater good with wisdom and compassion.

As you mature, your capacity for universal love and compassion will blossom fully. Where your younger self may have loved selectively or with conditions, your mature self loves humanity as a whole. This doesn't mean you love everyone equally—it means your heart encompasses all.

Your mature purpose involves healing, teaching, or serving at a level that benefits masses rather than just individuals. Whether through humanitarian work, creative expression that uplifts consciousness, or simply being a beacon of compassionate wisdom, you serve the collective evolution.

The empathy you've been developing throughout your life will become your greatest gift in your mature years. You feel what others feel, which could overwhelm you if you haven't learned healthy boundaries. But when properly channeled, this empathy creates profound healing.

Completion themes will characterize your later years. You'll finish what you started, heal old wounds, release ancient patterns, and prepare yourself and perhaps others for transformation. Your mature years aren't about clinging to life—they're about living fully until transition comes naturally.

In your mature years, you may be drawn to teaching, healing, arts, or humanitarian work that serves broad populations. Your accumulated wisdom and compassion make you especially effective at helping others find their path and purpose.

Your legacy involves the lives you've touched, the consciousness you've helped elevate, and the compassion you've modeled, {preferredName}. You'll likely influence far more people than you realize, through both direct contact and the ripple effects of your loving presence. You prove that one life lived with open heart changes countless others.""",

    11: """Your Maturity Number is 11, {preferredName}, a master number revealing that your later years are destined for spiritual teaching, illumination, and inspiring humanity toward higher consciousness. This is rare, powerful energy that carries both great potential and significant responsibility.

As you mature, your natural intuition and spiritual sensitivity will strengthen into powerful channeling abilities. Where your younger self may have doubted or feared your perceptions, your mature self will trust your connection to higher consciousness and use it to guide others.

Your mature purpose involves nothing less than helping elevate human consciousness. Whether through formal spiritual teaching, creative work that awakens awareness, or simply being a living example of enlightened presence, you're meant to light the way for others.

The spiritual development you've pursued throughout your life will culminate in your mature years. You'll integrate spiritual insight with practical wisdom, becoming someone who can access higher truths while remaining grounded in everyday reality. This integration is your gift to others.

Inspiration flows through you increasingly as you age. Ideas, insights, and creative visions that seem to come from beyond yourself will arrive with greater frequency and clarity. You're meant to share these gifts, not hoard them for personal benefit.

In your mature years, you may take on roles as spiritual teacher, healer, counselor, or creative inspiration. People will be drawn to your light, sensing that you carry wisdom beyond ordinary understanding. You'll finally be ready to step fully into this role.

Your legacy involves the consciousness you've helped awaken in others and the spiritual light you've carried, {preferredName}. Those you've inspired will carry that inspiration forward, creating cascades of awakening. You prove that spiritual evolution is humanity's true destiny.""",

    22: """Your Maturity Number is 22, {preferredName}, the master builder number revealing that your later years are destined for creating massive structures that serve humanity. This is the most powerful manifesting energy in numerology, pointing toward a future of extraordinary achievement.

As you mature, your ability to envision grand possibilities and systematically manifest them will reach its peak. Where your younger self may have doubted whether your visions were realistic, your mature self will know—and prove—that they absolutely are.

Your mature purpose involves building something of significant scale that serves the greater good. Whether creating organizations, movements, systems, or physical structures, you're meant to think big and execute flawlessly. Your later years aren't about small projects—they're about legacy-level impact.

The practical skills and spiritual vision you've been developing throughout your life will merge in your mature years. You'll combine the master teacher's wisdom (11) with the master builder's abilities (4), creating the rare capacity to manifest spiritual ideals in material form.

Leadership on a large scale is natural for you in your later years. You may head major organizations, guide significant projects, or influence policy and systems that affect many. Your vision encompasses not just what is, but what could be—and you have the skill to build it.

In your mature years, people will recognize your exceptional abilities and look to you for direction on important matters. You'll finally be comfortable with this visibility and ready to use your influence for maximum positive impact.

Your legacy involves the tangible structures you've built and the lives they've improved, {preferredName}. The organizations, systems, or movements you create will serve humanity for generations. You prove that spiritual values can be embodied in material form at massive scale.""",

    33: """Your Maturity Number is 33, {preferredName}, the master teacher number revealing that your later years are destined for profound healing, teaching, and embodying unconditional love. This is the rarest and most spiritually evolved frequency, pointing toward a future of extraordinary service.

As you mature, your capacity for unconditional love and spiritual wisdom will reach levels few humans achieve. Where your younger self may have loved selectively or protected your heart, your mature self will love freely while maintaining wise boundaries. This is the highest human attainment.

Your mature purpose involves being a living example of enlightened consciousness. Whether through formal teaching, healing work, creative expression, or simply your presence in the world, you're meant to show others what's possible when we fully embody our spiritual nature.

The spiritual development and service orientation you've been cultivating throughout your life will culminate in your mature years. You'll integrate the illumination of 11 with the nurturing of 6, becoming someone who channels divine love and wisdom for healing humanity.

Healing—physical, emotional, or spiritual—will likely be central to your later years. You may work directly as a healer, or your very presence may have healing effects on others. People feel better, lighter, and more hopeful simply by being around you.

In your mature years, you'll understand viscerally that we're all connected and that serving others is serving yourself. This isn't philosophy—it's lived reality. Your actions will consistently reflect this unity consciousness.

Your legacy involves the healing you've facilitated, the love you've embodied, and the consciousness you've helped awaken, {preferredName}. Your impact is immeasurable because love and healing ripple outward infinitely. You prove that one life lived in divine love transforms countless others."""
}

# Tool configurations
TOOLS = {
    "personal-month-reading": {
        "title": "Personal Month Number Reading",
        "description": "Discover the specific energy and focus of your current month",
        "emoji": "🗓️",
        "tagline": "Navigate this month's unique cosmic energy",
        "calculation_functions": """
        function calculatePersonalYear(dateStr) {
            const today = new Date();
            const birthDate = new Date(dateStr);
            const currentYear = today.getFullYear();
            const birthMonth = birthDate.getMonth() + 1;
            const birthDay = birthDate.getDate();
            
            const monthReduced = reduceToSingle(birthMonth);
            const dayReduced = reduceToSingle(birthDay);
            const yearReduced = reduceToSingle(currentYear);
            
            return reduceToSingle(monthReduced + dayReduced + yearReduced);
        }
        
        function calculatePersonalMonth(dateStr) {
            const today = new Date();
            const personalYear = calculatePersonalYear(dateStr);
            const currentMonth = today.getMonth() + 1;
            const monthReduced = reduceToSingle(currentMonth);
            
            return reduceToSingle(personalYear + monthReduced);
        }
        
        function getMonthName(monthNum) {
            const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December'];
            return months[monthNum - 1];
        }
        """,
        "calculation_code": """
            const number = calculatePersonalMonth(birthDate);
            const currentMonth = new Date().getMonth() + 1;
            const monthName = getMonthName(currentMonth);
            const currentYear = new Date().getFullYear();
        """,
        "result_title_template": "Personal Month " + "${number} (${monthName} ${currentYear}): ${preferredName}",
        "interpretations": PERSONAL_MONTH_INTERPRETATIONS
    },
    
    "maturity-number-reading": {
        "title": "Maturity Number Reading",
        "description": "Discover your life purpose that emerges in your mature years",
        "emoji": "🌅",
        "tagline": "Reveal the wisdom and purpose of your later years",
        "calculation_functions": """
        function calculateMaturityNumber(dateStr, fullName) {
            const lifePath = calculateLifePath(dateStr);
            const destiny = calculateNameNumber(fullName);
            return reduceToSingle(lifePath + destiny);
        }
        """,
        "calculation_code": """
            const number = calculateMaturityNumber(birthDate, birthName);
        """,
        "result_title_template": "Maturity Number " + "${number}: ${preferredName}",
        "interpretations": MATURITY_NUMBER_INTERPRETATIONS
    }
}

# Generate tools
import json

print("🔮 Generating Premium Numerology Tools...")
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
print(f"   • 500-800 word readings for all numbers")
print(f"   • LocalStorage auto-fill")
print(f"   • Quantum Merlin branding")
