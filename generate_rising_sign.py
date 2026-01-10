#!/usr/bin/env python3
"""
Generate Rising Sign (Ascendant) Reading Tool
Deep interpretations on outer personality and life approach for all 12 zodiac signs
"""

# Rising Sign Interpretations (500-800 words each)
RISING_SIGN_INTERPRETATIONS = {
    "Aries": """Your Rising Sign is Aries, {preferredName}, meaning you enter every room, situation, and new experience with boldness, confidence, and pioneering energy. Your first instinct in life is to take action, lead the charge, and meet challenges head-on. People perceive you as dynamic, courageous, and somewhat impatient.

When others first meet you, they notice your energy immediately. You have a direct, assertive presence that commands attention without trying. You don't fade into the background—you announce yourself simply by existing. This isn't arrogance; it's the natural expression of your Aries Ascendant's warrior spirit.

Your approach to life is straightforward: see what you want, go after it, don't overthink. Where others deliberate and plan, you prefer to leap and figure things out mid-air. This makes you an excellent initiator and pioneer but can also lead to impulsive decisions you later regret.

Physically, Aries Rising often manifests as athletic build, strong features, a prominent forehead or distinctive eyebrows, and energetic movement. You walk fast, talk fast, and generally operate at a quicker pace than those around you. Stillness feels foreign to your body.

Your ruling planet is Mars, giving you competitive drive and warrior energy. You're drawn to challenges, competitions, and situations that test your courage. Boredom is your enemy—you need constant stimulation, new frontiers to conquer, and obstacles to overcome.

In relationships, you come on strong. When you're interested in someone, you pursue directly and openly. Subtlety isn't your style—you'd rather risk rejection through bold approach than miss opportunity through hesitation. This refreshing honesty attracts people but can also overwhelm those who prefer slower pacing.

Your challenge with Aries Rising is learning patience and collaboration. Your instinct is to do everything yourself, right now, your way. But life often requires waiting for right timing, coordinating with others, and allowing processes to unfold naturally. Learning to channel your initiative into sustainable effort rather than sporadic bursts serves you well.

You may also struggle with anger and impulsive reactions. When frustrated, you want to fight or flee immediately. Developing a pause between impulse and action prevents you from burning bridges or creating unnecessary conflicts. Your directness is a gift, but it requires wisdom about when to use it.

People often misunderstand your assertiveness as aggression. You're not trying to dominate—you simply know what you want and see no reason to pretend otherwise. Learning to soften your approach when necessary while maintaining your authentic directness is an ongoing balancing act.

Your greatest strength is your courage to begin. Where others fear failure, you embrace the challenge. You show people what's possible when you stop overthinking and start acting. This pioneering spirit is your gift to the world, {preferredName}.""",

    "Taurus": """Your Rising Sign is Taurus, {preferredName}, meaning you approach life with steady, grounded, and sensual energy. You enter situations calmly, assess them thoroughly, and move forward only when you feel secure. People perceive you as reliable, patient, and unshakeable.

When others first meet you, they notice your calming presence. There's something solid and trustworthy about you that makes people feel safe. You don't rush, you don't panic, and you don't create unnecessary drama. This grounded quality draws others to you, especially those seeking stability in chaotic times.

Your approach to life is methodical and practical. You need to understand what you're getting into before committing. Once you decide on a path, however, you're remarkably persistent. You may be slow to start, but you have extraordinary endurance. You're the tortoise who wins the race through consistent effort.

Physically, Taurus Rising often manifests as strong, sturdy build, attractive features (Venus-ruled), a thick neck or shoulders, and graceful, deliberate movement. You may have a love for good food that shows in your body. There's often a natural beauty or pleasant appearance that draws positive attention.

Your ruling planet is Venus, giving you appreciation for beauty, comfort, and sensory pleasure. You're drawn to quality over quantity—fine food, beautiful environments, comfortable fabrics, pleasant scents. You build your life around tangible pleasures and material security.

In relationships, you're loyal and affectionate but slow to commit. You need to know someone is reliable before opening your heart. Once you do commit, however, you're extraordinarily devoted. You show love through providing comfort, physical affection, and creating beautiful shared experiences.

Your challenge with Taurus Rising is overcoming resistance to change. Your need for stability can become stubborn rigidity. When circumstances require adaptation, you may dig in your heels and refuse to budge, even when holding on causes more problems than letting go would.

You may also struggle with possessiveness—of people, things, and situations. Because you value security so highly, you try to control and maintain what you have. Learning that nothing in life is truly permanent, and that trying to possess actually creates the loss you fear, is crucial wisdom.

Laziness or excessive indulgence can also be issues. Your love of comfort can become excuse for avoiding necessary effort. You may choose ease over growth, staying in situations that feel good but don't serve your evolution. Balancing your need for comfort with willingness to stretch yourself is important.

People sometimes misinterpret your slowness as stupidity or your calmness as lack of passion. Neither is true—you simply process thoroughly and express steadily. You're deeply feeling and intelligent; you just don't perform these qualities for others' entertainment.

Your greatest strength is your ability to create lasting value and stability. You build things that endure—relationships, careers, homes, and legacies. You show others what's possible through patient, persistent effort, {preferredName}.""",

    "Gemini": """Your Rising Sign is Gemini, {preferredName}, meaning you approach life with curiosity, versatility, and communication focus. You enter situations eager to learn, quick to adapt, and ready to engage in conversation. People perceive you as witty, intelligent, and socially graceful.

When others first meet you, they notice your mental agility and conversational skill. You can talk to anyone about anything, finding common ground effortlessly. Your quick wit and interesting observations make you entertaining company. You seem to know a little about everything, making you fascinating to be around.

Your approach to life is exploratory and flexible. You want to experience variety, gather information, and keep options open. Commitment to one path feels limiting—you prefer to sample many experiences rather than diving deep into one. This makes you adaptable and well-rounded but can also lead to scattered focus.

Physically, Gemini Rising often manifests as youthful appearance regardless of age, expressive hands, animated facial expressions, and quick, nervous energy. You may gesture a lot when speaking. There's often something playful or mischievous in your expression.

Your ruling planet is Mercury, giving you sharp intellect and communication gifts. You're drawn to learning, teaching, writing, speaking, and any activity that engages your mind. You process life through language and logic, needing to articulate experiences to fully understand them.

In relationships, you need mental stimulation as much as emotional connection. You're attracted to intelligent, articulate people who can keep up with your quick mind. Conversations are how you bond—long talks are more intimate to you than silent togetherness. Partners who bore you intellectually won't hold your interest.

Your challenge with Gemini Rising is developing depth and follow-through. Your desire for variety can prevent you from staying with anything long enough to master it. You start many projects but finish few, learn broad basics but rarely expert-level depth. Choosing some areas for deep commitment serves you well.

You may also struggle with nervous energy and mental overload. Your mind processes constantly, analyzing everything, considering multiple perspectives simultaneously. This can create anxiety, restlessness, and difficulty being present. Learning to quiet your mind through meditation or physical activity is essential.

Inconsistency can also be an issue. You may say one thing today and something different tomorrow, not from dishonesty but because you've genuinely changed your mind. People may perceive you as unreliable or two-faced when really you're just adapting to new information.

People sometimes mistake your social ease for superficiality. Because you can talk to anyone about anything, they assume you don't go deep. But you're capable of profound thought—you simply prefer to keep things light in casual interactions. Your depth reveals itself to those who truly know you.

Your greatest strength is your ability to connect diverse ideas and people. You're an excellent communicator, translator, and networker. You show others that intelligence includes flexibility, that staying curious keeps you young, {preferredName}.""",

    "Cancer": """Your Rising Sign is Cancer, {preferredName}, meaning you approach life with sensitivity, protectiveness, and emotional awareness. You enter situations cautiously, feeling out the emotional atmosphere before fully engaging. People perceive you as nurturing, intuitive, and sometimes shy or reserved.

When others first meet you, they notice your warmth and empathy. You seem to genuinely care about how they're feeling, and you pick up on emotional undercurrents others miss. There's something maternal or protective about you, regardless of your gender—people instinctively feel you'll take care of them.

Your approach to life is emotionally-led and security-focused. You need to feel safe before you open up or take risks. You test waters carefully, retreat when threatened, and only fully emerge when you trust the environment. This protects your tender heart but can also limit your experiences.

Physically, Cancer Rising often manifests as round or soft features, expressive eyes that reveal emotion, a full chest or torso, and nurturing energy in your presence. You may have a baby face or youthful quality. Your body language is often protective—crossed arms, hunched shoulders—when feeling vulnerable.

Your ruling planet is the Moon, making you highly changeable and emotionally responsive to your environment. Your mood shifts with lunar cycles, and you're extremely sensitive to others' emotional states. You absorb feelings from your surroundings like a psychic sponge.

In relationships, you're deeply caring and devoted once you feel safe. You show love through nurturing—cooking, caring for, creating home together. You need emotional security and reassurance in partnership. Without it, you retreat into your shell and shut down. Partners who can hold space for your sensitivity without trying to toughen you up are ideal.

Your challenge with Cancer Rising is overcoming fear-based withdrawal. When you feel threatened emotionally, you retreat completely—ending relationships, avoiding situations, building walls. Learning to stay present with discomfort rather than automatically protecting yourself opens you to deeper connection and growth.

You may also struggle with taking things too personally. You interpret everything through an emotional lens, finding personal meaning in situations that aren't about you. Someone's bad mood becomes evidence they don't like you. Developing objectivity about others' behavior protects your emotional wellbeing.

Clingy or manipulative behavior can emerge when you're insecure. You may use guilt, emotional outbursts, or excessive caretaking to keep people close. Learning to feel secure within yourself rather than requiring constant reassurance from others is crucial maturity.

People sometimes mistake your protective shell for coldness or your emotional nature for weakness. Neither is accurate—you're deeply feeling and caring, you simply protect yourself until you trust. Once you open up, people discover your vast emotional depth and loyalty.

Your greatest strength is your emotional intelligence and nurturing capacity. You create safe harbor for others' feelings. You show people what unconditional care looks like, teaching that vulnerability and sensitivity are strengths, not weaknesses, {preferredName}.""",

    "Leo": """Your Rising Sign is Leo, {preferredName}, meaning you approach life with confidence, warmth, and creative flair. You enter every situation as if you own the place, radiating presence and charisma. People perceive you as magnetic, generous, and naturally authoritative.

When others first meet you, they notice you. You have star quality—something distinctive and memorable that draws attention. Even if you're physically quiet, there's an energy about you that fills space. You command respect without demanding it, and people naturally look to you for leadership.

Your approach to life is bold and heart-centered. You want to create, express, shine, and make an impact. You need to feel special and to do work that matters. You're not interested in blending in or playing small—you came here to leave a mark, and your rising sign ensures you do.

Physically, Leo Rising often manifests as thick, distinctive hair (your mane), proud posture, warm smile, and regal bearing. You may have broad shoulders or a strong back. There's often something cat-like in your movement—graceful yet powerful. You dress to be noticed, favoring bold colors or statement pieces.

Your ruling planet is the Sun, making you naturally central in any group. Just as planets orbit the Sun, people tend to orbit around you. You're generous and warm-hearted, sharing your light freely. But you also expect appreciation and acknowledgment for what you give.

In relationships, you're passionate and loyal. You love big and express affection dramatically. You want to be proud of your partner and have them be proud of you. You need admiration and celebration in partnership—not from vanity but because feeling special to someone you love is how you feel secure.

Your challenge with Leo Rising is managing ego and need for validation. When you don't receive the recognition you crave, you may become demanding, dramatic, or attention-seeking in problematic ways. Learning to validate yourself rather than requiring constant external applause is essential growth.

You may also struggle with taking criticism. Because you identify strongly with your creations and expressions, feedback can feel like personal attack. You may become defensive or dismiss valid input. Developing the ability to hear critique without ego-wound serves you well.

Pride can prevent you from admitting mistakes or showing vulnerability. You want to maintain your regal image, which can isolate you. Learning that true strength includes acknowledging weaknesses and asking for help when needed deepens your leadership.

People sometimes mistake your confidence for arrogance or your need for recognition as narcissism. You're not trying to dominate—you simply know your worth and see no reason to dim your light. Learning to shine while also illuminating others' lights, rather than outshining them, is your evolution.

Your greatest strength is your generous heart and natural leadership. You inspire others to be braver, more creative, more authentic. You show people what's possible when you refuse to play small and fully embrace your magnificence, {preferredName}.""",

    "Virgo": """Your Rising Sign is Virgo, {preferredName}, meaning you approach life with discernment, practicality, and attention to detail. You enter situations analytically, immediately noticing what could be improved. People perceive you as intelligent, helpful, and somewhat reserved or modest.

When others first meet you, they notice your precision and thoughtfulness. You choose words carefully, dress neatly, and present yourself with understated competence. You don't demand attention—you earn respect through demonstrated skill and genuine helpfulness. There's a quiet intelligence about you that people find reassuring.

Your approach to life is methodical and improvement-focused. You analyze situations, identify problems, and develop practical solutions. You're not a dreamer—you're a doer who makes things work better. You need to feel useful and competent, and you measure your worth by how effectively you serve.

Physically, Virgo Rising often manifests as clean, precise features, youthful appearance, slender or wiry build, and meticulous personal grooming. You pay attention to details others overlook—a wrinkle in your clothes, a hair out of place. There's often nervous energy in your body, manifesting as fidgeting or restlessness.

Your ruling planet is Mercury, giving you sharp analytical mind and communication skill focused on practical utility. You're drawn to systems, processes, and techniques that improve efficiency. You process life through categorizing, organizing, and perfecting.

In relationships, you show love through service and practical support. You may not be overly romantic or emotionally demonstrative, but you'll help fix problems, organize chaos, and support your partner's health and growth. You need partners who appreciate your practical care and don't mistake your reserve for lack of feeling.

Your challenge with Virgo Rising is overcoming perfectionism and self-criticism. You notice every flaw—in yourself, others, and situations. This critical eye is valuable for improvement but becomes destructive when it prevents you from appreciating what's already good. Learning to accept "good enough" is difficult but necessary.

You may also struggle with excessive worry and analysis paralysis. You can see every potential problem, which prevents action. You analyze situations to death, seeking the perfect approach, but never finding it. Learning to act despite imperfection serves you better than waiting for certainty that never comes.

Being overly critical of others can damage relationships. Your helpful suggestions feel like harsh judgment to sensitive people. Learning to appreciate what people do right before pointing out what could improve creates better reception for your valuable insights.

People sometimes mistake your analytical nature for coldness or your modesty for lack of confidence. Neither is accurate—you feel deeply and you're quite capable. You simply don't advertise your emotions or abilities. You prefer to demonstrate worth through action rather than declaration.

Your greatest strength is your ability to see how things can be better and actually make them so. You're genuinely helpful, competently skilled, and reliably excellent. You show others that mastery comes through attention to detail and continuous improvement, {preferredName}.""",

    "Libra": """Your Rising Sign is Libra, {preferredName}, meaning you approach life with grace, diplomacy, and relationship focus. You enter situations seeking balance, harmony, and connection. People perceive you as charming, fair-minded, and socially skilled.

When others first meet you, they notice your pleasant demeanor and social grace. You know how to make people comfortable, find common ground, and smooth social situations. There's an elegance about you—in how you speak, move, and interact—that draws people in. You seem approachable and genuinely interested in others.

Your approach to life is partnership-oriented and balance-seeking. You prefer collaboration over solo ventures, harmonious environments over chaotic ones, and fair solutions over one-sided victories. You need beauty, balance, and connection to feel truly alive. Ugliness and discord drain you.

Physically, Libra Rising often manifests as symmetrical, attractive features, graceful movement, pleasant voice, and refined aesthetic sense. Venus-ruled, you're naturally drawn to beauty and typically look put-together. There's often something classically beautiful about your appearance.

Your ruling planet is Venus, giving you natural charm and aesthetic sensibility. You're drawn to art, beauty, relationships, and creating harmony. You see life through the lens of balance and fairness, constantly seeking equilibrium in all situations.

In relationships, you thrive and suffer equally. You need partnership but can lose yourself in it. You're romantic, considerate, and skilled at compromise, making you an excellent partner. However, you may struggle to know what you want independently of others, changing your desires to match your partner's.

Your challenge with Libra Rising is developing independent identity and decision-making. You define yourself through relationships and see yourself in others' mirrors. Who are you when you're alone? What do you want independent of what maintains harmony? These questions are crucial for your growth.

You may also struggle with conflict avoidance and people-pleasing. To maintain peace, you suppress your true feelings, avoid necessary confrontations, and agree when you actually disagree. This creates resentment and prevents authentic intimacy. Learning that healthy conflict can deepen relationships rather than destroy them is essential.

Indecisiveness can paralyze you. You see all perspectives so clearly that choosing one feels like betraying the others. You may wait for others to decide, afraid of making the wrong choice. Developing trust in your own judgment, even knowing it might be imperfect, is important growth.

People sometimes mistake your diplomatic nature for lack of conviction or your conflict avoidance for weakness. You actually have strong values and considerable strength—you simply prefer persuasion over force and harmony over discord. Learning when to fight is as important as knowing how to make peace.

Your greatest strength is your ability to bring people together and find fair solutions. You create beauty, foster connection, and show others how cooperation produces better results than competition. You demonstrate that grace and diplomacy are forms of power, {preferredName}.""",

    "Scorpio": """Your Rising Sign is Scorpio, {preferredName}, meaning you approach life with intensity, depth, and penetrating perception. You enter situations reading hidden dynamics and unspoken truths. People perceive you as mysterious, powerful, and somewhat intimidating.

When others first meet you, they sense your power immediately. You have a presence that demands notice—not through volume but through intensity. Your eyes seem to see through facades into souls. You don't engage in small talk comfortably; you prefer real conversation or comfortable silence. There's something enigmatic about you that draws curiosity.

Your approach to life is all-or-nothing and transformation-focused. You don't do anything halfway. When you commit, you dive to the depths. You're not interested in surface experiences—you want to understand the hidden machinery, the psychological undercurrents, the shadow side that others fear to explore.

Physically, Scorpio Rising often manifests as intense, penetrating eyes (your most distinctive feature), strong or angular features, magnetic presence, and controlled movement. You may have prominent brows or bone structure. There's often something about your appearance that's both attractive and slightly dangerous.

Your ruling planet is Pluto (and traditionally Mars), giving you transformative power and warrior courage. You're drawn to depth psychology, occult knowledge, power dynamics, and situations that require facing what others avoid. You process life through experiencing its extremes.

In relationships, you're intensely loyal and passionate. You want soul-level intimacy—complete honesty, total trust, merged vulnerability. Superficial partnership doesn't interest you. You test people's loyalty, sometimes unconsciously creating situations that reveal their true character. Once you trust, you're fiercely devoted.

Your challenge with Scorpio Rising is managing control and power dynamics. You fear vulnerability and betrayal, so you try to control situations and people. You may manipulate, test, or use intimate knowledge as power. Learning to trust without controlling, to be vulnerable without guarantee of safety, is difficult but necessary growth.

You may also struggle with jealousy and possessiveness. Your intensity extends to ownership—you want complete claim on those you love. You may perceive threats where none exist, driven by fear of loss or betrayal. Developing security within yourself rather than requiring it from others is crucial.

Holding grudges and seeking revenge can poison you more than those you resent. When hurt, you never forget, and you may wait years for opportunity to settle scores. Learning that true power lies in transformation and release, not in maintaining resentment, liberates you.

People sometimes fear your intensity or misinterpret your privacy as having something to hide. You're not deliberately mysterious—you simply don't share your depths casually. You reveal yourself slowly, testing trustworthiness. Once you open up, people discover your profound capacity for loyalty and transformation.

Your greatest strength is your ability to see truth others avoid and to transform through facing darkness. You help people confront their shadows and emerge stronger. You show that real power comes from complete honesty and willingness to die and be reborn, {preferredName}.""",

    "Sagittarius": """Your Rising Sign is Sagittarius, {preferredName}, meaning you approach life with optimism, enthusiasm, and philosophical perspective. You enter situations with curiosity and openness, ready for adventure and growth. People perceive you as upbeat, honest, and freedom-loving.

When others first meet you, they notice your friendly, enthusiastic energy. You smile easily, laugh readily, and seem genuinely interested in learning about people and ideas. You have an openness that puts others at ease—you don't judge; you explore. There's something larger-than-life about you, even if you're physically small.

Your approach to life is exploratory and meaning-seeking. You want to understand the bigger picture, discover truth, and expand your horizons—physically, mentally, and spiritually. You're not interested in details or limitations; you focus on possibilities and principles. You need freedom to roam, whether geographically or intellectually.

Physically, Sagittarius Rising often manifests as athletic or lanky build, long limbs, friendly face, and energetic movement. You may be tall or give the impression of height. There's often something youthful and adventurous in your appearance, regardless of age. You dress for comfort and mobility rather than fashion.

Your ruling planet is Jupiter, giving you optimistic outlook and expansive nature. You're drawn to travel, higher learning, philosophy, and experiences that broaden perspective. You process life by finding the lesson, the silver lining, the bigger meaning in every situation.

In relationships, you need freedom and intellectual connection. You're attracted to adventurous, growth-oriented people who want to explore life with you rather than settle into routine. You're honest to a fault, sometimes painfully so. You'd rather risk hurting someone with truth than comfort them with lies.

Your challenge with Sagittarius Rising is learning depth and commitment. Your desire for freedom and new experiences can prevent you from staying anywhere long enough to go deep. You may abandon relationships, jobs, or interests when they start feeling limiting, missing the depth that develops through sustained commitment.

You may also struggle with tactlessness and over-promising. Your honesty is admirable but can be hurtful when delivered without consideration. You blurt truths that would be better softened or left unsaid. Learning that not every truth needs speaking, and kind delivery doesn't diminish honesty, serves you well.

Restlessness can prevent presence. You're always looking ahead to the next adventure, the next insight, the next experience. This constant forward motion means you rarely enjoy where you are. Learning to be present with current blessings rather than constantly seeking new ones deepens your happiness.

People sometimes mistake your need for freedom as inability to commit or your optimism as naivety. Neither is true—you can commit when it doesn't feel like imprisonment, and your optimism comes from faith in life's benevolence, not ignorance of its difficulties.

Your greatest strength is your ability to see possibilities and inspire hope. You help people expand their perspectives and believe in better futures. You show that life is meant to be an adventure of continuous growth and discovery, {preferredName}.""",

    "Capricorn": """Your Rising Sign is Capricorn, {preferredName}, meaning you approach life with seriousness, ambition, and self-discipline. You enter situations assessing how to achieve goals and establish yourself as competent. People perceive you as mature, responsible, and somewhat reserved.

When others first meet you, they notice your professionalism and composure. You present yourself with dignity and competence, even as a young person. There's something adult about you, as if you were born 40 years old. You command respect through demonstrated capability rather than demanding it through force.

Your approach to life is goal-oriented and achievement-focused. You have plans, ambitions, and the discipline to execute them. You're willing to delay gratification, work harder than others, and climb mountains one methodical step at a time. Success isn't optional for you—it's necessary for self-respect.

Physically, Capricorn Rising often manifests as lean or angular features, strong bone structure, reserved demeanor, and controlled movement. You may have prominent cheekbones or jaw. There's often a serious expression, though you have a wonderful dry wit when comfortable. You may age in reverse—looking old when young, youthful when older.

Your ruling planet is Saturn, giving you discipline, responsibility, and respect for structure and authority. You're drawn to tradition, hierarchy, and proven methods. You process life through achievement, building lasting structures and legacies.

In relationships, you're loyal and committed but emotionally reserved. You show love through providing, protecting, and helping partners achieve their goals. You need respect and shared ambition in partnership. Frivolous people drain you—you want serious partners who have their lives together.

Your challenge with Capricorn Rising is learning emotional expression and playfulness. You're so focused on achievement and responsibility that you forget to simply enjoy life. You may judge yourself harshly for having fun when you could be productive. Learning that rest and pleasure are necessary, not indulgent, is important growth.

You may also struggle with workaholism and excessive seriousness. You take everything—including yourself—very seriously. You have difficulty relaxing or being silly. Your standards are impossibly high, creating constant stress. Learning to lighten up and accept imperfection without feeling like you've failed is crucial.

Fear of failure or judgment can paralyze you. You won't try unless you're certain of success, missing opportunities that require risk. You care deeply about others' opinions, especially authority figures. Developing internal validation rather than constantly seeking external approval liberates you.

People sometimes mistake your reserve for coldness or your ambition for heartlessness. You actually feel deeply—you simply don't display emotions publicly. You care tremendously about people you love; you simply show it through actions rather than words.

Your greatest strength is your ability to build lasting achievement through disciplined effort. You create structures that endure—careers, institutions, legacies. You show others that meaningful success comes through consistent hard work and unwavering commitment, {preferredName}.""",

    "Aquarius": """Your Rising Sign is Aquarius, {preferredName}, meaning you approach life with independence, originality, and humanitarian focus. You enter situations as your authentic self, unconcerned with conforming to others' expectations. People perceive you as unique, intellectual, and slightly detached.

When others first meet you, they notice you're different. There's something distinctive about you—your appearance, ideas, or energy—that sets you apart. You don't try to fit in, and you don't apologize for your unconventionality. You seem comfortable being yourself, which is both refreshing and sometimes perplexing to others.

Your approach to life is intellectual and progressive. You're interested in innovation, social change, and ideas that improve collective existence. You think in terms of systems, patterns, and future possibilities. Individual emotional drama bores you—you care about humanity as a whole more than individual personalities.

Physically, Aquarius Rising often manifests as distinctive or unconventional appearance, angular features, tall or lanky build, and unique personal style. You may have something unusual about your look—unusual hair, striking eyes, eccentric fashion. You dress to express individuality rather than to attract or fit in.

Your ruling planet is Uranus (and traditionally Saturn), giving you revolutionary energy and intellectual brilliance. You're drawn to technology, astrology, social activism, and anything progressive or unconventional. You process life through understanding patterns and envisioning better futures.

In relationships, you need friendship and intellectual connection as much as romance. You're attracted to unique, independent people who respect your freedom. You're loyal in your own way but resist traditional relationship structures. You may prefer open relationships, unconventional arrangements, or significant personal space within partnership.

Your challenge with Aquarius Rising is developing emotional intimacy and personal connection. Your intellectual approach to life can disconnect you from feelings—yours and others'. You may analyze emotions rather than feeling them, creating distance in relationships. Learning to be emotionally present and vulnerable is difficult but deepens your connections.

You may also struggle with being contrary simply for the sake of being different. You automatically resist anything mainstream or traditional, even when it has value. You may reject good advice simply because it's conventional. Discerning between authentic individuality and reactive rebellion serves you well.

Detachment can isolate you. You maintain emotional distance, observing life rather than fully participating. You may intellectualize pain rather than processing it emotionally. This protects you from hurt but also prevents genuine intimacy. Learning to engage emotionally as well as intellectually enriches your experience.

People sometimes mistake your detachment for lack of caring or your unconventionality for attention-seeking. Neither is accurate—you care deeply about humanity and progressive causes. You're simply wired to see the bigger picture rather than get lost in personal dramas.

Your greatest strength is your authentic individuality and visionary thinking. You help humanity evolve by refusing to accept limiting norms. You show people that being different isn't just acceptable—it's necessary for progress, {preferredName}.""",

    "Pisces": """Your Rising Sign is Pisces, {preferredName}, meaning you approach life with sensitivity, imagination, and spiritual openness. You enter situations feeling the emotional atmosphere and absorbing unspoken energies. People perceive you as gentle, compassionate, and somewhat otherworldly.

When others first meet you, they notice your softness and empathy. You seem to genuinely care about their wellbeing, and you pick up on emotional nuances others miss. There's something dreamy or ethereal about you, as if you're not quite fully present in mundane reality. People often feel they can open up to you easily.

Your approach to life is intuitive and boundary-less. You trust feelings over logic, respond to subtle energies, and navigate life more through sensing than thinking. You experience life as fluid and interconnected rather than solid and separate. Harsh reality often feels too much, so you naturally seek gentler realms—through art, spirituality, or imagination.

Physically, Pisces Rising often manifests as soft features, dreamy or sleepy eyes, fluid movement, and gentle presence. You may have a youthful, angelic quality. Your body language is often open and unguarded, lacking the defensive postures others adopt. You may seem to float rather than walk.

Your ruling planet is Neptune (and traditionally Jupiter), giving you spiritual sensitivity and creative imagination. You're drawn to art, music, mysticism, and helping professions. You process life through feeling, imagining, and seeking transcendent meaning beyond material reality.

In relationships, you're romantic, compassionate, and self-sacrificing. You want fairy-tale love, soul-mate connection, and complete emotional merging. You give everything to partners, sometimes losing yourself entirely. You're attracted to people who need saving, which creates complicated dynamics where you're more rescuer than equal partner.

Your challenge with Pisces Rising is developing boundaries and discernment. You absorb everyone's emotions, making it hard to know what's yours versus what you picked up from others. You give endlessly without protecting your own energy, leading to depletion. Learning to distinguish between compassion and martyrdom is crucial.

You may also struggle with escapism and avoiding reality. When life gets hard, you disappear—into fantasy, substances, sleep, or spiritual bypassing. You may choose delusional comfort over painful truth. Developing the courage to face reality directly, even when it hurts, strengthens you.

Victimhood and helplessness can become patterns. You may unconsciously choose situations where you suffer, confusing suffering with loving. You may believe you're powerless when you're actually choosing powerlessness. Recognizing your own agency and responsibility empowers you.

People sometimes take advantage of your giving nature or mistake your gentleness for weakness. You're stronger than you appear—spiritual strength is often invisible. You endure tremendous emotional weight that would crush harder-seeming people. Your gentleness is courage, not cowardice.

Your greatest strength is your boundless compassion and spiritual depth. You help others access their own souls and feel divine love. You show that true strength includes vulnerability, that the highest power is unconditional love, {preferredName}."""
}

# Same template as Moon Sign but for Rising Sign
TEMPLATE = open("moon-sign-reading.html", "r", encoding="utf-8").read()

# Replace Moon-specific content with Rising-specific
TEMPLATE = TEMPLATE.replace("Moon Sign Reading", "Rising Sign Reading")
TEMPLATE = TEMPLATE.replace("Discover your emotional nature and inner world", "Reveal your outer personality and life approach")
TEMPLATE = TEMPLATE.replace("🌙 Moon Sign Reading", "⬆️ Rising Sign Reading")
TEMPLATE = TEMPLATE.replace("Moon in", "Rising in")
TEMPLATE = TEMPLATE.replace("Select Your Moon Sign", "Select Your Rising Sign (Ascendant)")
TEMPLATE = TEMPLATE.replace('id="moonSign"', 'id="risingSign"')
TEMPLATE = TEMPLATE.replace("Don't know your Moon Sign?", "Don't know your Rising Sign?")
TEMPLATE = TEMPLATE.replace("const moonSign =", "const risingSign =")

# Replace interpretations
import json
interp_str = json.dumps(RISING_SIGN_INTERPRETATIONS)
# Find and replace the entire script section with new interpretations
script_start = TEMPLATE.find('const interpretations = ')
script_end = TEMPLATE.find('};', script_start) + 2
old_interpretations = TEMPLATE[script_start:script_end]
new_interpretations = f'const interpretations = {interp_str};'
TEMPLATE = TEMPLATE.replace(old_interpretations, new_interpretations)

# Fix the variable reference
TEMPLATE = TEMPLATE.replace("document.getElementById('moonSign')", "document.getElementById('risingSign')")
TEMPLATE = TEMPLATE.replace('const moonSign = dropdown.value', 'const risingSign = dropdown.value')
TEMPLATE = TEMPLATE.replace('if (!moonSign)', 'if (!risingSign)')
TEMPLATE = TEMPLATE.replace('const interpretation = interpretations[moonSign]', 'const interpretation = interpretations[risingSign]')
TEMPLATE = TEMPLATE.replace('`Moon in ${moonSign}:', '`Rising in ${risingSign}:')

# Update title and meta
TEMPLATE = TEMPLATE.replace('<title>Moon Sign Reading', '<title>Rising Sign Reading')
TEMPLATE = TEMPLATE.replace('Discover your Moon Sign - your emotional nature', 'Discover your Rising Sign (Ascendant) - your outer personality')

print("⬆️ Generating Rising Sign Reading Tool...")
print("=" * 60)

with open("rising-sign-reading.html", "w", encoding="utf-8") as f:
    f.write(TEMPLATE)

print("✅ Generated: rising-sign-reading.html")
print("=" * 60)
print("✨ Rising Sign Reading tool created!")
print("📝 Features:")
print("   • 12 zodiac sign interpretations (500-800 words each)")
print("   • Outer personality & life approach insights")
print("   • Profile management system")
print("   • localStorage auto-fill")
print("   • Quantum Merlin branding")
