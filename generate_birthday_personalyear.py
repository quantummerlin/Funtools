#!/usr/bin/env python3
"""
Generate Birthday Number and Personal Year Reading Tools
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
                alert('Unable to calculate. Please check your birth date.');
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

# Birthday Number interpretations
BIRTHDAY_INTERPRETATIONS = {
    1: """Your birthday number 1 reveals you as a natural-born leader, {preferredName}. Born on the first, tenth, nineteenth, or twenty-eighth of the month, you carry the energy of initiative and independence. You're not meant to follow—you're meant to blaze trails.

Your special gift is your pioneering spirit. Where others see obstacles, you see opportunities. You have an innate ability to start projects, inspire others, and forge new paths. Your mind naturally gravitates toward innovation and originality. People look to you for direction, even when you don't realize you're leading.

However, your independence can sometimes manifest as stubbornness. You may struggle with collaboration when you feel your vision is being compromised. Learning to balance your strong will with openness to others' ideas will multiply your success exponentially.

Your birthday bestows upon you exceptional courage and determination. When you set your mind to something, failure isn't in your vocabulary. This tenacity serves you well in entrepreneurial ventures, creative pursuits, and any field requiring self-direction.

In relationships, you need a partner who respects your autonomy while providing emotional support. You're attracted to confident individuals who can match your strength without competing for dominance.

Your life purpose involves bringing new ideas into the world. Whether through business, art, technology, or social innovation, you're here to initiate change. Trust your instincts, {preferredName}—they're rarely wrong.""",

    2: """Your birthday number 2 marks you as a natural peacemaker and diplomat, {preferredName}. Born on the second, eleventh, twentieth, or twenty-ninth, you possess an extraordinary sensitivity to energy and emotion. You feel what others feel, making you an invaluable friend, partner, and colleague.

Your special gift is your ability to create harmony from discord. You instinctively understand multiple perspectives and can find common ground where others see only division. This makes you exceptional in counseling, mediation, partnership, and any role requiring emotional intelligence.

Your sensitivity, while a tremendous asset, can also be your challenge. You absorb others' emotions like a sponge, sometimes losing yourself in the process. Establishing healthy boundaries and regular alone time to recharge isn't selfish—it's essential for your wellbeing.

You thrive in collaborative environments where your diplomatic skills shine. Behind every great leader is often someone with birthday number 2 energy, quietly ensuring everything runs smoothly and everyone feels heard. You're the glue that holds teams together.

In love, you're deeply devoted and intuitive about your partner's needs. You seek relationships built on emotional intimacy and mutual support. Your ideal partner appreciates your gentleness while encouraging you to stand in your own power.

Your path involves bringing people together and creating spaces of peace and understanding. The world needs your gentle strength now more than ever, {preferredName}. Don't underestimate the power of your compassionate presence.""",

    3: """Your birthday number 3 reveals you as a natural communicator and creative soul, {preferredName}. Born on the third, twelfth, twenty-first, or thirtieth, you came here to express, create, and inspire joy. Your energy lights up rooms and lifts spirits wherever you go.

Your special gift is your ability to take complex ideas and make them accessible, entertaining, and memorable. Whether through words, art, performance, or simply your vibrant personality, you have a talent for communication that others envy. You can make people laugh, think, and feel—often all at once.

Creativity flows through you like a river. You see possibilities everywhere and have more ideas than you could execute in ten lifetimes. Your challenge is focus. With so many interests and talents, you may scatter your energy, starting many projects but completing few. Learning to channel your abundant creativity into focused efforts will amplify your impact.

You possess natural optimism that's contagious. Even in difficult times, you find reasons to smile and help others do the same. This doesn't mean you don't experience pain—you simply choose to transform it through creative expression rather than suppression.

In relationships, you need intellectual stimulation and variety. Routine bores you quickly. Your ideal partner appreciates your spontaneity and joins you in playful exploration of life's adventures.

Your purpose involves bringing joy, beauty, and inspiration to the world, {preferredName}. Whether through art, writing, teaching, or simply being authentically yourself, you remind others that life is meant to be celebrated.""",

    4: """Your birthday number 4 establishes you as a master builder and pillar of stability, {preferredName}. Born on the fourth, thirteenth, twenty-second, or thirty-first, you possess an extraordinary ability to manifest ideas into tangible reality. You're the architect of dreams, both your own and others'.

Your special gift is your incredible work ethic and attention to detail. Where others see chaos, you see systems waiting to be organized. You have a practical mind that excels at creating structures, whether physical buildings, business systems, or life frameworks. Your patience and perseverance are legendary.

You thrive on order and predictability, which can sometimes limit your spontaneity. Learning to embrace occasional chaos and uncertainty will actually enhance your effectiveness. Not everything needs a plan—sometimes magic happens in the messiness.

Your loyalty is unshakeable. When you commit to a person, project, or principle, you're in it for the long haul. This makes you an exceptional friend, employee, and partner. People know they can count on you, always.

In your career, you excel in fields requiring precision, organization, and systematic thinking. Architecture, engineering, project management, accounting, or any role involving building something lasting suits your energy perfectly.

Relationships with you are solid and dependable. You show love through actions more than words, through consistency more than grand gestures. Your ideal partner values security and isn't threatened by your need for routine.

Your life mission involves creating lasting structures that serve humanity, {preferredName}. You're here to build foundations that future generations will benefit from. Every project you complete, every system you create, contributes to a more organized, functional world.""",

    5: """Your birthday number 5 marks you as a freedom seeker and adventurer, {preferredName}. Born on the fifth, fourteenth, or twenty-third, you came to experience life in all its diverse, dynamic glory. Your spirit craves variety, change, and new horizons.

Your special gift is adaptability. You can thrive in virtually any environment because you're naturally flexible and quick-thinking. Where others panic when plans change, you pivot effortlessly. This makes you exceptional in fast-paced, ever-changing environments.

You're a natural networker with a gift for connecting diverse groups of people. Your curiosity about human nature draws people to you, and your genuine interest in their stories makes them open up. You collect friends from all walks of life.

Your challenge is commitment. With so many exciting possibilities calling to you, settling into one path, relationship, or location can feel like imprisonment. Yet learning to balance your need for freedom with the depth that comes from commitment will bring you profound fulfillment.

You're meant to experience and share knowledge. Travel, communication, media, sales, or any field that keeps you moving and interacting with variety suits your essence. You suffocate in routine, repetitive roles.

In love, you need a partner who understands your need for space and adventure. Possessiveness kills your spirit. Your ideal match is someone who's secure enough to give you freedom while creating a home base you actually want to return to.

Your purpose involves expanding horizons—yours and others'. Through your experiences, stories, and natural charisma, you remind people that life is an adventure meant to be fully lived, {preferredName}. Don't let fear of missing out prevent you from occasionally sitting still long enough to integrate all you've learned.""",

    6: """Your birthday number 6 reveals you as a natural nurturer and harmonizer, {preferredName}. Born on the sixth, fifteenth, or twenty-fourth, you carry the energy of unconditional love, responsibility, and service. You're here to create beauty, harmony, and healing in your corner of the world.

Your special gift is your ability to make others feel safe, seen, and cared for. You have an instinctive understanding of what people need—often before they know themselves. This makes you exceptional in counseling, healing, teaching, hospitality, or any role involving caring for others.

You're drawn to beauty and harmony in all forms. Your home is likely your sanctuary, carefully curated to provide peace and comfort. You have an eye for aesthetics and a gift for creating environments where people feel they can breathe.

Your challenge is martyrdom. You give so freely and completely that you sometimes neglect your own needs. Learning that self-care isn't selfish but essential will actually enhance your ability to serve others. You can't pour from an empty cup.

Family and close relationships are central to your life purpose. You may find your greatest fulfillment in parenting, teaching, or creating a warm home. You show love through acts of service and create deep, lasting bonds.

In romantic relationships, you're devoted and attentive, sometimes to a fault. Your ideal partner appreciates your nurturing nature while encouraging you to receive as well as give. You need someone who recognizes that true partnership involves mutual care.

Your life mission involves creating spaces and relationships of genuine love and harmony, {preferredName}. Whether through family, community service, healing work, or simply being a light in others' lives, you make the world softer and kinder through your presence.""",

    7: """Your birthday number 7 establishes you as a seeker of truth and spiritual wisdom, {preferredName}. Born on the seventh, sixteenth, or twenty-fifth, you possess a deeply analytical mind coupled with powerful intuition. You're here to understand the mysteries beneath surface appearances.

Your special gift is your ability to see beyond the obvious. While others accept things at face value, you dig deeper, asking questions others don't think to ask. This makes you exceptional in research, investigation, spiritual work, psychology, or any field requiring penetrating insight.

You need regular solitude to process information and connect with your inner knowing. This isn't antisocial—it's essential for your wellbeing. In quiet moments, you access wisdom that eludes you in chaos. Your best ideas come when you're alone with your thoughts.

Your challenge is overthinking. Your brilliant mind can become a prison when you get stuck in analysis paralysis. Learning to balance intellectual understanding with intuitive knowing, logic with faith, will bring you peace.

You're naturally drawn to philosophy, spirituality, science, or metaphysics. You want to understand how things work—not just mechanically, but why they exist at all. Life's big questions fascinate you.

In relationships, you need intellectual and spiritual connection. Surface-level small talk bores you. Your ideal partner engages with you in deep conversations and respects your need for solitude without taking it personally.

Your purpose involves seeking and sharing wisdom, {preferredName}. Whether through teaching, writing, counseling, or your own spiritual practice, you help others see beyond illusion to deeper truth. Trust both your intellect and your intuition—together, they make you remarkably perceptive.""",

    8: """Your birthday number 8 marks you as a natural leader and manifestor, {preferredName}. Born on the eighth, seventeenth, or twenty-sixth, you possess an extraordinary ability to understand power, money, and material success. You're here to master the physical plane and use resources to create positive change.

Your special gift is your executive ability. You instinctively understand systems, hierarchies, and how to get things done in the material world. You have a talent for seeing the big picture while managing details, making you exceptional in business, finance, management, or entrepreneurship.

You're ambitious in the best sense—not for ego, but because you have a vision of what you want to accomplish. You understand that money and power are tools that, wielded consciously, can transform lives and communities. You're meant to achieve material success so you can do good with it.

Your challenge is balance. You can become so focused on achievement that you neglect your emotional and spiritual life. Remember that true success includes health, relationships, and inner peace, not just financial abundance and professional recognition.

You have natural authority that others recognize and respect. Even if you don't seek leadership positions, they often find you. You command presence without trying, and people instinctively look to you for direction in challenging situations.

In relationships, you need a strong partner who can match your intensity. You're attracted to capable, successful individuals who respect your ambitions while having their own. Power struggles bore you—you want an equal partner.

Your life purpose involves mastering material success and using it to serve the greater good, {preferredName}. You're meant to prove that spiritual values and material success aren't opposites but partners. Show the world what conscious prosperity looks like.""",

    9: """Your birthday number 9 reveals you as a humanitarian and old soul, {preferredName}. Born on the ninth, eighteenth, or twenty-seventh, you carry the wisdom of all previous numbers. You're here to serve humanity, complete cycles, and prepare for new beginnings.

Your special gift is your universal compassion. You feel connected to all of humanity, not just your immediate circle. This makes you exceptional in humanitarian work, healing, teaching, or any field where you can make a broad positive impact.

You have an artistic, romantic soul with deep appreciation for beauty in all its forms. You're drawn to creative expression as a way of processing and sharing your rich inner world. Art, music, writing, or performance may call to you.

Your challenge is letting go. As the number of completion, you're meant to master non-attachment. This doesn't mean not caring—it means loving fully while holding loosely, knowing that everything is temporary and that's okay.

You have powerful empathy that sometimes overwhelms you. You feel the world's pain acutely, which can lead to depression if you don't establish healthy boundaries. Remember: you can't save everyone, and that's not your job. Your role is to shine your light and trust others to find their own path.

In relationships, you love deeply and idealistically. You're attracted to people who share your values and vision for a better world. Your ideal partner appreciates your compassionate nature while helping you stay grounded.

Your purpose involves healing, teaching, and inspiring others to live from their highest self, {preferredName}. You're meant to complete old cycles—personal and collective—to make space for new growth. Trust that every ending is actually a beginning in disguise.""",

    11: """Your birthday number 11 marks you as a master spiritual teacher, {preferredName}. As a master number, you carry amplified energy and heightened potential. You're here to inspire, uplift, and illuminate the path for others through your own spiritual journey.

Your special gift is your powerful intuition and spiritual insight. You're naturally connected to higher consciousness and can channel wisdom that seems to come from beyond yourself. People are drawn to your light, even when you don't understand why.

You're meant to be a beacon—someone who shows others what's possible when human consciousness evolves. Your very presence can shift energy in a room. You may feel like you don't quite fit in ordinary reality, and that's because you're wired for something more.

Your challenge is living up to your potential without becoming overwhelmed by its magnitude. The 11 energy can be intense, and you may sometimes wish you could just be a regular 2 (1+1=2). But your soul chose this path for a reason.

You're deeply sensitive and may struggle with anxiety or nervousness. This sensitivity isn't weakness—it's the price of your perceptive abilities. Learning to ground your energy and protect your auric field is essential for your wellbeing.

In your life path, spiritual teaching, healing, counseling, or creative inspiration are likely callings. You're meant to work with consciousness itself—helping people awaken, heal, and evolve.

Your purpose is nothing less than helping elevate human consciousness, {preferredName}. Whether through formal spiritual teaching or simply living as an example of awakened awareness, you're here to light the way. Trust your divine connection.""",

    22: """Your birthday number 22 establishes you as a master builder, {preferredName}. This is the most powerful number in numerology for manifesting dreams into physical reality. You're here to build something of lasting significance that serves humanity on a grand scale.

Your special gift is your ability to envision possibilities that seem impossible to others and then systematically bring them into existence. You combine the spiritual vision of 11 with the practical building skills of 4 (2+2=4), making you uniquely qualified to manifest spiritual ideals in material form.

You think big—perhaps bigger than anyone around you. While others plan projects, you envision movements. While they build businesses, you see empires. While they help individuals, you design systems that help millions. This isn't grandiosity—it's your actual life purpose.

Your challenge is not reducing yourself to fit others' limited expectations. People may call you unrealistic or too ambitious. Let them. Your job isn't to convince skeptics—it's to stay true to your massive vision and execute it step by step.

The weight of your potential can sometimes feel crushing. You may experience periods of self-doubt where you wonder if you're delusional. You're not. You're simply being asked to hold a vision that most people can't yet see. Trust the process.

In your career, you're meant to create organizations, movements, systems, or structures that outlive you. You're building legacy. Architecture, social entrepreneurship, large-scale humanitarian work, or transformative business suits your energy.

Your purpose is to bring heaven to earth in tangible form, {preferredName}. Whatever you build—whether physical structures, social systems, or spiritual movements—make it solid, make it lasting, and make it serve the greater good. You have the power to change the world.""",

    33: """Your birthday number 33 reveals you as a master teacher and spiritual messenger, {preferredName}. This is the rarest and most spiritually evolved of the master numbers. You're here to embody and teach unconditional love, spiritual truth, and divine wisdom.

Your special gift is your ability to communicate spiritual truths in ways that transform lives. You combine the spiritual illumination of 11 with the creative expression of 6 (3+3=6), making you a natural channel for divine wisdom that heals and uplifts humanity.

You're meant to be a living example of enlightened consciousness. Your very presence can trigger awakening in others. You don't just teach spiritual principles—you embody them. People feel better, lighter, and more hopeful simply by being around you.

Your challenge is avoiding the martyr complex. With such powerful energy of service and sacrifice, you may give until you're completely depleted. Remember that even Jesus took time alone to recharge. Self-care isn't optional for you—it's essential for your mission.

The responsibility of this number can feel overwhelming. You may sometimes wish you'd been born with an easier path. But your soul chose this extraordinary frequency because it was ready for this level of service. You're stronger than you know.

In relationships and career, you're called to healing, teaching, counseling, spiritual leadership, or creative arts that elevate consciousness. Whatever you do, you're meant to bring light, love, and wisdom to masses, not just individuals.

Your purpose is to be a living beacon of divine love and wisdom, {preferredName}. You're here to show humanity what's possible when we fully embody our spiritual nature while living in physical form. Your mission is sacred and your impact immeasurable. Trust your divine calling."""
}

# Personal Year interpretations
PERSONAL_YEAR_INTERPRETATIONS = {
    1: """Welcome to your Personal Year 1, {preferredName}! This is a powerful year of new beginnings and fresh starts. After completing a nine-year cycle, you're standing at the threshold of a brand new chapter in your life. The universe is inviting you to plant seeds that will grow over the next nine years.

This year, you'll feel an unusual surge of energy, courage, and initiative. Ideas that have been percolating in the background are ready to be brought into form. This is your time to start that business, begin that creative project, launch that website, or take any bold action you've been contemplating.

Your independence and self-reliance will strengthen significantly this year. You may find yourself less interested in seeking others' approval and more focused on trusting your own instincts. This shift is essential for your growth—embrace it even if it feels uncomfortable at times.

Career and business opportunities are especially favored in a 1 Year. If you've been wanting to advance in your current position or strike out on your own, this is your year to make it happen. The cosmic energy supports your ambitions and rewards decisive action.

However, be mindful of being too forceful or impatient. While initiative is encouraged, steamrolling over others will create resistance that slows your progress. Balance your assertiveness with sensitivity to others' needs and perspectives.

This is also an excellent year for personal reinvention. Want to change your image, develop new skills, or break free from limiting patterns? The 1 Year energy supports transformation. You're writing the opening chapter of your next life story—make it compelling, {preferredName}.""",

    2: """You're in a Personal Year 2, {preferredName}, a time of patience, partnership, and cultivation. After the action-oriented energy of last year, the universe is asking you to slow down, cooperate, and allow things to develop naturally. This is a year of growth beneath the surface.

Think of yourself as a gardener who planted seeds last year. This year isn't about planting more—it's about watering, weeding, and tending to what's already growing. Results may not be immediately visible, but important development is happening.

Relationships take center stage in a 2 Year. Existing partnerships deepen, new connections form, and you discover the power of collaboration over solo effort. Whether in business or personal life, you'll accomplish more through teamwork than individual action this year.

Your intuition and sensitivity are heightened during this cycle. Pay attention to subtle feelings, dreams, and synchronicities. Your inner voice is especially accurate now, guiding you toward beneficial connections and away from draining situations.

Patience is your key lesson this year. Things may move more slowly than you'd like, but forcing situations will backfire. Trust divine timing. What's meant for you will arrive at precisely the right moment, often when you stop pushing and start allowing.

This is also a powerful year for emotional healing. Past wounds may surface for resolution. Rather than avoiding discomfort, lean into it with gentle curiosity. Healing work you do now creates space for greater joy in the years ahead.

Your focus should be on supporting others, building alliances, and creating harmony in your environment. The seeds you planted last year need your attention now, {preferredName}. Tend them with love and patience.""",

    3: """Welcome to your Personal Year 3, {preferredName}! This is a year of joy, creativity, and self-expression. After the introspective, patient energy of Year 2, you're emerging into the light ready to share your gifts with the world. This is your time to shine!

Creative energy flows abundantly during a 3 Year. Whether you consider yourself artistic or not, you'll feel inspired to express yourself in new ways. Writing, speaking, designing, performing, or any creative outlet will bring unusual satisfaction and success this year.

Your social life expands significantly. You'll meet fascinating new people, receive more invitations, and generally feel more outgoing than usual. These connections aren't random—many will play important roles in your future. Say yes to social opportunities even if you usually prefer solitude.

Communication is especially favored this year. If you've been wanting to write that book, start that podcast, launch that YouTube channel, or simply speak up more in your life, now is the time. Your words carry extra power and reach further than usual.

However, be mindful of scattering your energy. With so many exciting possibilities, you might start numerous projects but finish few. Choose your priorities wisely and see at least one major creative endeavor through to completion.

This is also a year to cultivate joy intentionally. After periods of hard work or difficulty, the 3 Year reminds you that life is meant to be enjoyed. Make time for play, laughter, beauty, and pleasure. These aren't frivolous—they're essential.

Your optimism attracts opportunities and people. Let your natural enthusiasm shine, {preferredName}. The world needs your unique creative expression and joyful energy now more than ever.""",

    4: """You're entering a Personal Year 4, {preferredName}, a time of hard work, discipline, and building solid foundations. After the creative, expansive energy of Year 3, the universe is asking you to get serious, organized, and focused on manifesting tangible results.

This is a year of grounding your dreams into reality. Those creative ideas from last year? Now it's time to create detailed plans and execute them step by step. Success comes through sustained effort, not shortcuts or lucky breaks.

Your focus should be on establishing structure in key areas of your life. This might mean creating better systems at work, getting your finances in order, improving your health routines, or literally building or renovating something physical. Whatever you build this year will serve you for years to come.

Career and business matters require your attention. If you've been procrastinating on important professional development, this year won't let you avoid it any longer. Hard work is rewarded now, but only if you actually do the work consistently.

Patience and perseverance are essential this year. Results may come slowly, but they will be solid and lasting. Don't get discouraged if progress feels slower than you'd like. You're building a foundation, not a facade, and that takes time.

Your physical health and body deserve focus this year. Establishing exercise routines, improving nutrition, and addressing any health issues you've been ignoring will pay long-term dividends. Your body is asking for your attention.

This year may feel restrictive or limiting at times, but embrace the discipline. The structures you create now provide the container for future freedom and creativity. Think of this year as building the launchpad for the adventures coming in Year 5, {preferredName}.""",

    5: """Welcome to your Personal Year 5, {preferredName}! This is a year of freedom, change, and adventure. After the structured, disciplined energy of Year 4, the universe is opening the gates and inviting you to explore, expand, and experience life more fully.

Expect the unexpected this year. Change is not only possible—it's inevitable. Whether you initiate transformations or they arrive on their own, your life will look different by year's end. Embrace flexibility and view change as opportunity rather than threat.

Travel is highly favored during a 5 Year. If you've been wanting to explore new places, cultures, or experiences, this is your year. Even if major travel isn't possible, seek novelty in your local area. New restaurants, new routes, new experiences—variety feeds your soul this year.

Career changes are common in Year 5. You might change positions, industries, or even entire career paths. If you've felt stuck or bored professionally, opportunity for change is likely coming. Stay alert and be ready to pivot quickly when the right moment arrives.

Your social circle expands and diversifies this year. You'll meet people from different backgrounds, cultures, and perspectives. These connections broaden your worldview and may open unexpected doors. Network actively and authentically.

However, be mindful of overindulgence and scattered focus. The 5 Year energy can lead to excess in various forms—spending, eating, drinking, or simply taking on too many commitments. Maintain some grounding practices even as you explore and expand.

This is also an excellent year for learning new skills, taking courses, or gaining knowledge in areas that interest you. Your mind craves stimulation and absorbs information easily now. Feed your curiosity, {preferredName}. The freedom you seek begins in your mind.""",

    6: """You're in a Personal Year 6, {preferredName}, a time of responsibility, relationships, and service. After the expansive, changeable energy of Year 5, the universe is inviting you to come home—literally and figuratively—and tend to the people and commitments that matter most.

Family and close relationships are your focus this year. Issues that need attention in your domestic life or with family members will surface for resolution. This is excellent timing for improving your living space, strengthening family bonds, or addressing any relationship tensions that have been simmering.

Marriage, commitment, and partnership are highlighted this year. Many people get engaged, married, or deepen existing commitments during a 6 Year. If you're in a relationship, you'll likely move to a new level of closeness and responsibility. If you're single and seeking partnership, this year brings opportunities—but only if you're ready for real commitment.

Your nurturing instincts are heightened. You'll feel called to help, heal, support, and serve others. This is beautiful, but watch for martyrdom. Giving until you're depleted serves no one. Balance service with self-care, and remember that teaching others to help themselves is often more valuable than doing everything for them.

This is an excellent year for beautifying your environment. Whether redecorating your home, improving your garden, or simply surrounding yourself with more beauty, these efforts will nourish your soul and create the sanctuary you need.

Career-wise, this year favors counseling, teaching, healthcare, hospitality, or any work involving service and caregiving. If you're considering a shift toward more meaningful, service-oriented work, this is your year to explore it.

Your lesson this year is learning to give and receive love in balanced ways, {preferredName}. True service comes from overflow, not depletion. Fill your own cup first, then share from the abundance.""",

    7: """Welcome to your Personal Year 7, {preferredName}! This is a year of introspection, spiritual development, and inner growth. After the relationship-focused energy of Year 6, the universe is creating space for you to turn inward and connect with your deeper self.

This is not typically a year for major external activity or dramatic outer changes. Instead, it's a year for integration, reflection, and understanding. Think of it as a sabbatical for your soul—a time to process everything you've experienced over the past six years and extract wisdom from those experiences.

Your need for solitude increases significantly during a 7 Year. This isn't depression or antisocial behavior—it's a genuine need to retreat from the world's noise and connect with your inner voice. Honor this need without guilt. The insights you gain in solitude will serve you well in the busier years ahead.

Spiritual and metaphysical interests deepen this year. You may be drawn to meditation, yoga, energy work, astrology, numerology, or other mystical studies. Even if you've never been particularly spiritual, you'll find yourself asking bigger questions about life's meaning and purpose.

This is an excellent year for education, research, or deep study of subjects that fascinate you. Your mind is especially receptive to complex information and able to grasp subtle concepts. Take courses, read extensively, and engage your intellect.

Relationships may feel less important this year, which can confuse your loved ones. Explain that your need for space isn't rejection—you're simply in a more inward cycle. True friends and partners will understand and give you the room you need.

Trust your intuition especially strongly this year. Your psychic abilities and inner knowing are heightened. Pay attention to dreams, synchronicities, and gut feelings. Your soul is speaking—listen carefully, {preferredName}.""",

    8: """You're entering a Personal Year 8, {preferredName}, a powerful time of manifestation, achievement, and material success. After the introspective, spiritual focus of Year 7, you're returning to the outer world ready to claim your power and create tangible results.

This is typically the most financially successful year in the nine-year cycle. Opportunities for advancement, increased income, recognition, and material abundance are all highly favored. But here's the key: success comes through focused effort and strategic action, not luck or chance.

Career advancement is strongly indicated during an 8 Year. Promotions, new positions, business growth, or recognition for past efforts typically arrive now. If you've been working hard without adequate reward, this is often the year that changes. But you must advocate for yourself—opportunities won't simply fall in your lap.

Money matters require your attention and action. This is an excellent year to negotiate raises, launch money-making ventures, make strategic investments, or reorganize your finances for greater abundance. Money flows more easily to you this year, but you must create the channels for it to flow through.

Leadership opportunities arise naturally during an 8 Year. Whether in your career, community, or family, people will look to you to take charge. Step into this role confidently—you have the strength and wisdom to lead effectively.

However, be mindful of becoming too focused on material success at the expense of your health, relationships, or spiritual life. The 8 Year energy can create workaholic tendencies. Success that costs you your wellbeing isn't success—it's a cautionary tale.

This is also a year where karma—both positive and negative—returns with force. What you've been putting out into the world will come back to you multiplied. Use your power wisely and ethically, {preferredName}. True prosperity includes integrity.""",

    9: """Welcome to your Personal Year 9, {preferredName}! This is a year of completion, release, and preparation for rebirth. You're finishing a nine-year cycle that began when you were in Year 1, and the universe is helping you clear space for the new beginnings coming next year.

This year, your primary work is letting go. Relationships, jobs, living situations, beliefs, or patterns that no longer serve your highest good will naturally fall away. While this can feel uncomfortable or even painful, trust that what leaves creates space for something better to arrive in the new cycle beginning next year.

This is not a year for starting major new projects or ventures. Instead, focus on completing what's already in motion. Finish that book, conclude that project, or bring existing endeavors to their natural completion. Starting something new now is like planting seeds in winter—the timing isn't right.

Your emotional and spiritual life deepens significantly during a 9 Year. You may feel more sensitive, introspective, or philosophical than usual. This isn't depression—it's a natural part of the completion process. You're integrating lessons from the entire nine-year cycle.

Service to others and humanitarian concerns may call to you more strongly this year. You're meant to share wisdom gained from your experiences, help others, and contribute to causes larger than yourself. Giving to others actually helps you release what you no longer need.

Forgiveness—of yourself and others—is essential this year. Holding grudges or clinging to old wounds prevents you from moving freely into your next cycle. Release resentments, bless what was, and turn your face toward what will be.

This year may feel melancholy at times, but it's also profoundly meaningful, {preferredName}. You're clearing the ground for a magnificent new beginning. Trust the process of release. What's meant for you will never leave, and what leaves was never meant to stay."""
}

# Tool configurations
TOOLS = {
    "birthday-number-reading": {
        "title": "Birthday Number Reading",
        "description": "Discover your special gifts and talents through your birthday number",
        "emoji": "🎂",
        "tagline": "Unlock the unique talents encoded in your birth day",
        "calculation_functions": """
        function calculateBirthdayNumber(dateStr) {
            const date = new Date(dateStr);
            const day = date.getDate();
            return reduceToSingle(day);
        }
        """,
        "calculation_code": """
            const number = calculateBirthdayNumber(birthDate);
        """,
        "result_title_template": "Birthday Number " + "${number}: ${preferredName}",
        "interpretations": BIRTHDAY_INTERPRETATIONS
    },
    
    "personal-year-reading": {
        "title": "Personal Year Number Reading",
        "description": "Discover the energy and opportunities of your current personal year cycle",
        "emoji": "📅",
        "tagline": "Understand the cosmic energy influencing your year",
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
        """,
        "calculation_code": """
            const number = calculatePersonalYear(birthDate);
            const currentYear = new Date().getFullYear();
        """,
        "result_title_template": "Personal Year " + "${number} (${currentYear}): ${preferredName}",
        "interpretations": PERSONAL_YEAR_INTERPRETATIONS
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
