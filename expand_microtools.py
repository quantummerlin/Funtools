#!/usr/bin/env python3
"""
Expand micro-tool readings to be more meaningful (3-5 sentences instead of 1 line)
"""

import re

# Enhanced interpretations for micro-tools
MICRO_TOOL_UPDATES = {
    "coin-flip.html": {
        "heads": "The coin has landed on Heads, {name}! This result suggests that the universe is encouraging you to move forward with confidence. Heads often represents the active, assertive choice—the path of taking initiative and stepping into leadership. Trust that this direction aligns with your highest good. Whatever question you asked, this is your sign to proceed with courage and conviction.",
        "tails": "The coin reveals Tails, {name}! This outcome invites you to consider the reflective, receptive path. Tails often signifies patience, waiting for the right timing, or choosing the more introspective option. Sometimes the wisest action is strategic pause or gentle approach rather than forceful advance. Trust that this guidance is protecting you from premature action and steering you toward perfect timing."
    },
    
    "dice-roller.html": {
        # We'll add interpretations for 1-6
        1: "You rolled a 1, {name}! This number carries the energy of new beginnings, independence, and pioneering spirit. In the context of your question, this suggests it's time to take initiative, trust yourself, and start fresh. The universe is telling you to be bold, original, and self-reliant. Whatever you're considering, take the lead and don't wait for others' approval. This is your moment to initiate.",
        2: "The dice reveal a 2, {name}! This number resonates with partnership, patience, and diplomacy. Your answer suggests that cooperation and collaboration will serve you better than solo effort right now. Consider seeking allies, being patient with timing, or finding the middle ground in any conflicts. Balance and harmony are your pathways forward. Trust in divine timing and the power of working together.",
        3: "You've rolled a 3, {name}! This joyful number carries creative, expressive, and optimistic energy. The message for you is to lighten up, express yourself authentically, and approach your situation with creativity and joy. Communication, artistic expression, or social connection may hold your answer. Don't take things too seriously—playfulness and enthusiasm attract positive outcomes. Let your natural charisma shine through.",
        4: "The number 4 appears for you, {name}! This is the energy of structure, stability, and practical action. Your guidance suggests getting organized, creating a solid plan, and doing the necessary groundwork. Success comes through discipline, patience, and systematic effort now. Build your foundation carefully and don't skip steps. Hard work and dedication will pay off, but only if you're willing to do what's required methodically.",
        5: "A 5 rolls for you, {name}! This dynamic number represents change, freedom, and adventure. The universe is signaling that transformation is coming or needed. Be flexible, embrace the unexpected, and welcome variety into your situation. This may be the time to take calculated risks, try something different, or break free from limiting routines. Adaptability is your superpower right now—go with the flow and enjoy the ride.",
        6: "You rolled a 6, {name}! This number vibrates with love, responsibility, and service. Your answer relates to relationships, family, home, or caring for others. Focus on nurturing connections, creating harmony, and taking responsibility for your part in situations. Beauty, compassion, and domestic matters may need your attention. The path forward involves balancing your own needs with service to those you love. Lead with your heart."
    },
    
    "yes-no-oracle.html": {
        "yes": "The Oracle speaks: YES, {name}! The cosmic energies are aligning in your favor regarding this question. This affirmative answer suggests that proceeding with your plans, trusting your instincts, or taking that leap will serve your highest good. The universe is giving you a green light—move forward with confidence and optimism. Sometimes we need external confirmation for what we already know deep down. This is that confirmation. Trust yourself and take action.",
        "no": "The Oracle speaks: NO, {name}. This answer is actually protecting you from a path that wouldn't serve your highest good right now. A 'no' from the universe isn't rejection—it's redirection toward something better. Perhaps the timing isn't right, or there's information you don't yet have, or a better option is waiting to reveal itself. Trust this guidance and either wait for clearer signs or consider alternative approaches. Sometimes what we think we want isn't what we truly need.",
        "maybe": "The Oracle speaks: MAYBE, {name}. This uncertain answer reflects that the situation is still in flux—energies haven't fully formed yet, or your own clarity about what you truly want needs development. The outcome depends on choices you have yet to make or information that hasn't been revealed. Rather than frustration, view this as an invitation to gather more information, reflect on what you really want, and trust that clarity will come when the time is right. The universe is asking you to wait just a bit longer before deciding."
    },
    
    "crystal-ball.html": {
        # Crystal ball probably has random mystical messages - we'll need to check structure
        "pattern": "enhanced_mystical"
    },
    
    "fortune-cookie.html": {
        # Fortune cookie has preset fortunes - we'll check and enhance them
        "pattern": "enhanced_wisdom"
    }
}

print("🔮 Expanding Micro-Tool Readings...")
print("=" * 60)

# Update coin-flip.html
print("Updating coin-flip.html...")
with open("coin-flip.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find and replace the coin flip results
old_heads = """const result = isHeads ? 'Heads' : 'Tails';
                const emoji = isHeads ? '👑' : '🦅';
                
                document.getElementById('result-title').textContent = `${emoji} ${result}!`;
                document.getElementById('result-text').textContent = `The coin landed on ${result}. Trust your decision!`;"""

new_heads = """const result = isHeads ? 'Heads' : 'Tails';
                const emoji = isHeads ? '👑' : '🦅';
                const preferredName = document.getElementById('preferredName')?.value || 'friend';
                
                const interpretations = {
                    'Heads': '""" + MICRO_TOOL_UPDATES["coin-flip.html"]["heads"].replace("{name}", "${preferredName}") + """',
                    'Tails': '""" + MICRO_TOOL_UPDATES["coin-flip.html"]["tails"].replace("{name}", "${preferredName}") + """'
                };
                
                document.getElementById('result-title').textContent = `${emoji} ${result}!`;
                document.getElementById('result-text').textContent = interpretations[result];"""

content = content.replace(old_heads, new_heads)

with open("coin-flip.html", "w", encoding="utf-8") as f:
    f.write(content)
print("✅ coin-flip.html updated")

# Update dice-roller.html
print("Updating dice-roller.html...")
with open("dice-roller.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the dice roller result section
# Looking for pattern like: result.textContent = `You rolled a ${number}`;
old_dice_pattern = re.search(r"document\.getElementById\('result-text'\)\.textContent = `You rolled a \$\{number\}`;", content)
if old_dice_pattern:
    dice_interpretations = "{\n"
    for num, interp in MICRO_TOOL_UPDATES["dice-roller.html"].items():
        dice_interpretations += f"                    {num}: '{interp}',\n"
    dice_interpretations += "                }"
    
    new_dice = """const preferredName = document.getElementById('preferredName')?.value || 'friend';
                
                const interpretations = """ + dice_interpretations.replace("{name}", "${preferredName}") + """;
                
                document.getElementById('result-text').textContent = interpretations[number] || `You rolled a ${number}!`;"""
    
    # Find the section to replace
    old_section = re.search(
        r"(document\.getElementById\('result-text'\)\.textContent = `You rolled a \$\{number\}`;)",
        content
    )
    
    if old_section:
        content = content.replace(old_section.group(1), new_dice)
        
        with open("dice-roller.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ dice-roller.html updated")
else:
    print("⚠️  dice-roller.html pattern not found, checking structure...")

# Update yes-no-oracle.html
print("Updating yes-no-oracle.html...")
with open("yes-no-oracle.html", "r", encoding="utf-8") as f:
    content = f.read()

# The oracle likely has yes/no/maybe logic - find and enhance it
# Common pattern: const answer = answers[Math.floor(Math.random() * answers.length)];
yes_no_pattern = re.search(r"const answers = \[(.*?)\];", content, re.DOTALL)
if yes_no_pattern:
    # Replace with enhanced interpretations
    oracle_interps = """const preferredName = document.getElementById('preferredName')?.value || 'friend';
            
            const interpretations = {
                'Yes': '""" + MICRO_TOOL_UPDATES["yes-no-oracle.html"]["yes"].replace("{name}", "${preferredName}") + """',
                'No': '""" + MICRO_TOOL_UPDATES["yes-no-oracle.html"]["no"].replace("{name}", "${preferredName}") + """',
                'Maybe': '""" + MICRO_TOOL_UPDATES["yes-no-oracle.html"]["maybe"].replace("{name}", "${preferredName}") + """',
                'Ask Again Later': "The Oracle cannot see clearly at this moment, ${preferredName}. The energies surrounding your question are too turbulent or unfixed for a definitive answer. This isn't a denial—it's wisdom. Wait until you feel more centered about this question, or until circumstances shift. When the time is right, ask again and you'll receive clear guidance. Sometimes 'not now' is the wisest answer of all."
            };
            
            const answers = ['Yes', 'No', 'Maybe', 'Ask Again Later'];"""
    
    # Find where answers are used and add interpretation display
    content = re.sub(
        r"const answers = \[(.*?)\];",
        oracle_interps,
        content,
        flags=re.DOTALL
    )
    
    # Also update the result display to use interpretations
    content = re.sub(
        r"document\.getElementById\('result-text'\)\.textContent = answer;",
        "document.getElementById('result-text').textContent = interpretations[answer] || answer;",
        content
    )
    
    with open("yes-no-oracle.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ yes-no-oracle.html updated")
else:
    print("⚠️  yes-no-oracle.html pattern not found")

print("=" * 60)
print("✨ Micro-tool readings expanded!")
print("📝 Each tool now provides 3-5 sentence interpretations")
print("🎯 Tools updated: coin-flip, dice-roller, yes-no-oracle")
