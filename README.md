# **GameMaster**

*Embrace the darkness. Craft your story. Challenge the unknown.*

## Before you Dive In

Welcome to GameMaster, a complex project still very much under construction. Here's the reality: most parts aren't functioning correctly. The databases are solid, and the initial scripts do what they're supposed to. However, the core located in `gamemaster` is, frankly, a mess. I am not talking fun surprises; I am talking "not working" territory.

If you still wish to navigate this tricky terrain:

1. **Craft the Essential Scroll:**:
   In the root directory, conjure up a `config.ini`  file and etch upon it these lines:
   ```ini
   [openai]
   api_key = <your_openai_key>
   ```
   Remember, this scroll holds potent magic. Ensure you add `config.ini` to your `.gitignore` to safeguard its secrets from wandering eyes.

2. With this scroll at hand, you can attempt to summon `generate.py`. A note of caution: its responses might be as wild as the wind, if it even responds at all.
3. The main invocation in this realm is `gamemaster.py`. As of now, however, it remains dormant and does nothing. Awaken it at your own risk!

## Overview

In a realm where darkness blurs into light, where the line between hero and villain is but a thin veil, GameMaster beckons brave souls to step forth and carve their destiny. The world you are about to enter is not for the faint-hearted—it thrives on raw emotions, passion, and peril. Here, your choices don't merely alter paths; they shape universes.

### Every Soul a Weaver
Every being in this vast universe, from the humblest human to the mightiest elf, from the mysterious Thiefling to the fierce Orc, plays a crucial role in this great cosmic tapestry. Their joys, sorrows, hopes, and fears are interwoven threads that, when pulled, can either tighten or unravel the fabric of existence.

As you traverse this land, you won't be just a passive listener. You are a Mythos—a being with the power to influence, change, and even create legends. The stories you've heard since childhood, of Baba Yaga's enchanted hut or the fierce battles of Beowulf, are not just tales in this world; they are living histories that might intertwine with your own journey. With every decision you make, with every beast you confront, and with every ally you befriend, you're not just shaping your story—you're adding to the mythological legacy of Dyssomnia.

### Duality of Existence
In this realm, the line between right and wrong is ever-shifting. Moral compasses are constantly tested, and the path of righteousness is not always illuminated. Heroes might be forged in darkness, and villains might find redemption under the sun. The world does not judge; it merely watches, listens, and remembers.

Every quest undertaken, every monster confronted, every ally made or enemy forged, culminates in a grand tale of epic proportions. But remember: in GameMaster, tales are not just told; they are lived. The question is, how will you live yours?

Embrace the darkness, craft your story and challenge the unknown in GameMaster. Where your story ends, another begins. Welcome to a world of endless possibilities.

***Note to Filip**: I wanted to bring something fresh to the table instead of replicating DnD, you know. So I thought of setting it in a dark world ala witcher. Moral dilemmas, hunting mythological creatures from Slavic-English mythology and others, and grumpy relations between races. But that was just an idea.*

## The Races

*Born of diverse realms, bound by a shared destiny.*

---

### **1. Human:** 
Driven by ambition, their cities rise as monuments to progress, but their wars scar the land.

### **2. Elf:** 
Ancient forests echo with elven songs of beauty, but time has also taught them cold indifference.

- **High Elf** - Masters of arcane, their studies occasionally blind them to worldly affairs.
- **Dark Elf (Drow)** - Thriving in shadows, their society is a web of alliances and betrayals.
- **Wood Elf** - Protectors of the wilds, yet sometimes isolationist in their forested realms.

### **3. Dwarf:** 
Underground fortresses hide vast treasures, but old grudges smolder in the shadowed halls.

- **Hill Dwarf** - Bound to the earth, their grounded nature can lead to stubbornness.
- **Mountain Dwarf** - Valor and craftsmanship define them, though pride can be their downfall.

### **4. Halfling:** 
While most find solace in homely comforts, some are driven to adventure by an insatiable wanderlust.

- **Lightfoot Halfling** - Ever on the move, their curiosity sometimes lands them in peril.
- **Stout Halfling** - Robust and unyielding, their resistance can make them seem aloof.

### **5. Orc:** 
Fierce tribal bonds unify them, but a tumultuous relationship with nature often brings chaos to their steps.

### **6. Aasimar:** 
Touched by celestial grace, they shine brightly, but some are haunted by a darker call.

- **Protector** - Sworn defenders, yet their commitment can sometimes overshadow personal desires.
- **Scourge** - Embodying light's wrath, their intensity can be both a boon and a bane.
- **Fallen** - Trapped between redemption and despair, their path is fraught with inner turmoil.

### **7. Genasi:** 
Elemental fury courses through them, granting both the serenity of still waters and the rage of a storm.

- **Air** - As unpredictable as the wind, their free nature can be both refreshing and stormy.
- **Earth** - Pillars of strength, yet sometimes inflexible to change.
- **Fire** - Ignited by passion, they burn brightly but risk consuming themselves.
- **Water** - Reflecting depth and mystery, their emotions run as deep as the oceans.

### **8. Tiefling:** 
Born of infernal deals, their arcane talents are as likely to save as to curse.

- **Asmodeus** - Bearing the strongest infernal legacy, they move with a sense of supremacy.
- **Dispater** - Stealthy and silver-tongued, they often find their way out of trouble.
- **Mephistopheles** - Embracing the arcane, their pursuit of power sometimes knows no bounds.

### **9. Half-Elf:** 
Bridging two worlds, their diverse gifts often come with a sense of unbelonging.

### **10. Dragonborn:** 
Their breath tells of dragon lineage, and with it, a legacy of awe and fear.

### **11. Half-Orc:** 
In their veins, human cunning meets orcish fury, forging warriors of unmatched vigor, often misunderstood by both sides.

## Classes Overview

*Carve your path, for in choice lies true power.*

---

### **1. Barbarian:** 
Harnessing primal rage for fierce combat.
- **Path of the Berserker:** A fury-driven warrior. **Type:** Melee DPS/Tank
- **Path of the Totem Warrior:** Bonded with nature's spirits. **Type:** Melee DPS/Tank
- **Path of the Storm Herald:** Channeling elemental fury. **Type:** Melee DPS/Control

### **2. Bard:** 
Versatile spellcasters with a song or story for every situation.
- **College of Lore:** Masters of knowledge and arcane secrets. **Type:** Support/Magical DPS
- **College of Valor:** Inspiring allies in the thick of battle. **Type:** Support/Melee DPS
- **College of Swords:** Blending weapon arts with bardic flair. **Type:** Melee DPS

### **3. Cleric:** 
Channeling the divine to support and defend.
- **Life Domain:** Focused on healing and preserving life. **Type:** Support
- **War Domain:** Bringing divine wrath to the battlefield. **Type:** Melee DPS/Support
- **Light Domain:** Channeling radiant energy and fire. **Type:** Magical DPS

### **4. Druid:** 
Nature's guardians, wielding its power.
- **Circle of the Moon:** Transforming into powerful beasts. **Type:** Melee DPS/Tank
- **Circle of the Land:** Masters of environmental spells. **Type:** Magical DPS/Support

### **5. Fighter:** 
Skilled in all manners of combat.
- **Champion:** The peak of martial training. **Type:** Melee DPS
- **Battle Master:** Tactical and cunning fighters. **Type:** Melee DPS/Tank
- **Eldritch Knight:** Merging martial prowess with arcane spells. **Type:** Melee DPS/Magical DPS

### **6. Monk:** 
Harnessing ki to perform martial feats.
- **Way of the Open Hand:** Hand-to-hand combat specialists. **Type:** Melee DPS
- **Way of the Shadow:** Stealthy and deceptive. **Type:** Melee DPS/Stealth
- **Way of the Four Elements:** Manipulating elemental forces. **Type:** Melee DPS/Control

### **7. Paladin:** 
Holy oath-bound warriors.
- **Oath of Devotion:** Paragons of virtue and justice. **Type:** Melee DPS/Tank
- **Oath of Vengeance:** Relentless pursuers of justice. **Type:** Melee DPS
- **Oath of the Ancients:** Defenders of the light and natural order. **Type:** Melee DPS/Tank

### **8. Ranger:** 
Masters of terrain and tracking.
- **Hunter:** Specialists against certain foes. **Type:** Ranged/Melee DPS
- **Beast Master:** Fighting alongside animal companions. **Type:** Ranged/Melee DPS

### **9. Rogue:** 
Experts in subterfuge and precision.
- **Assassin:** Masters of disguise and sudden strikes. **Type:** Melee/Ranged DPS
- **Thief:** Skilled at stealth, burglary, and evasion. **Type:** Melee/Ranged DPS
- **Arcane Trickster:** Blending roguish skills with magic. **Type:** Melee/Ranged DPS/Magical Control

### **10. Sorcerer:** 
Magic flows innately within them.
- **Draconic Bloodline:** Tied to dragon ancestry. **Type:** Magical DPS
- **Wild Magic:** Unpredictable arcane surges. **Type:** Magical DPS/Support

### **11. Warlock:** 
Drawing power from ancient beings.
- **Pact of the Chain:** Communing with otherworldly familiars. **Type:** Magical DPS
- **Pact of the Fiend:** Drawing power from infernal beings. **Type:** Magical DPS
- **Pact of the Tome:** Expanding arcane knowledge with a book of secrets. **Type:** Magical DPS

### **12. Wizard:** 
Studious mages with vast spellbooks.
- **School of Evocation:** Focused on offensive magic. **Type:** Magical DPS
- **School of Abjuration:** Experts in protective spells. **Type:** Support/Magical DPS
- **School of Transmutation:** Masters of changing matter and form. **Type:** Magical Control/Support

## Lore

Born from light, shaped in shadow.*

---
In the vast nothingness that was the universe, the Aether pulsated in silent serenity. There wasn’t a distinction between night and day or a horizon where land met the sky—it was an endless void. However, from this vast nothingness emerged two potent entities: Luminara, a beacon of radiant light, and Tenebros, an embodiment of overwhelming darkness. Their existence fractured the Aether, leading to the birth of Dyssomnia, a realm where light and dark converged, danced, and often clashed. This wasn't a tranquil birth; the violent merging of Luminara's brilliance with Tenebros's gloom was a cataclysmic event. Their tumultuous interactions sculpted mountains, carved out seas, and sowed the seeds of life, creating a world where duality became the very essence of existence.

As the energies of Luminara and Tenebros interplayed, they stirred anomalies throughout Dyssomnia. The powerful emotions, tales, and beliefs they projected gave life to creatures of legend. The forests whispered of the Leshen, protectors of ancient woods; the seas roared with tales of the Nuckelavee, spirits that held grudges against mortals; nights were punctuated with the haunting wails of Banshees and the Wendigos, embodiments of hunger and desolation, haunted the icy terrains. Each creature was a manifestation of shared beliefs, embodying fears and myths passed through generations, serving as a reminder of tales' profound power.

But the world of Dyssomnia was not only to be inhabited by these creatures. As the dust of its creation settled, the races as we know them began to form, each a reflection of the world's complexity and the balance of Luminara and Tenebros. Humans, in all their diversity and contradiction, spread across the land. Their varieties—Nordlings, Southerners, and Midlanders—showed the spectrum of environments that Dyssomnia boasted. Elves, ancient and attuned to the magic pulsing through Dyssomnia, also emerged, their sub-races of Sunborn, Shadowborn, and Woodborn, each echoing an aspect of the world's enchantment. Dwarves, with their unyielding spirit, were born from the heartbeats of the mountains, their subtypes mirroring the elements they were closest to. The Veilwalkers, existing between the tangible and arcane, were a testament to Dyssomnia's mysterious depths, their very essence binding the secrets of the universe. Finally, the Krugs, monumental and wild, epitomized the raw spirit of nature, standing as stalwarts of Dyssomnia's untamed essence.

As the races settled and built societies, they began interpreting their existence, each crediting their emergence to either Luminara's light or Tenebros's shadow. The Elves believed they were birthed from Luminara's pure radiance, while the Tieflings, with their ethereal nature, felt a closer kinship to Tenebros. Humans, being diverse, claimed allegiance to both, embodying the true spirit of Dyssomnia—a world of duality. Over time, this interpretation created divides, with each race and sub-race believing in their superiority or unique role in Dyssomnia's grand tapestry.

Yet, as civilizations burgeoned, so did disparities. In its heart, each race held a distinct interpretation of Dyssomnia's creation, leading to clashing worldviews. With their innate connection to magic, Elves deemed themselves superior, the realm's rightful custodians. This innate arrogance often found them at odds with humans, whom they viewed as lesser, ephemeral entities. Humans, however, with their indomitable spirit, refused to be belittled. Their vast kingdoms and diverse cultures often stood as bulwarks against elvish condescension.

Dwarves, skeptical of surface-dwellers, especially the high-minded elves, entrenched themselves deeper in their mountain fortresses, hoarding secrets and forging alliances only when necessary. Thieflings, with their uncanny abilities, often found themselves isolated, their ethereal nature making them subjects of awe, envy, and, at times, distrust. Their existence between realms made them mediators but also spies in the eyes of many. Orcs, on the other hand, preferred isolation; their monumental stature and raw power were often misunderstood as mere brute force. Their occasional skirmishes with humans or elves over territorial disputes further fueled racial misconceptions.

Rumors and prophecies added to the mix, speaking of a "Mythos", a being from among the races with the potential to either unify Dyssomnia or push it to chaos. This prophecy deepened racial rifts, as each believed the Mythos would be born amongst them, furthering their supremacy. It was a world on the edge, where every encounter, alliance, or dispute could reshape the landscape of Dyssomnia.

This complex interplay of creation, mythology, and belief is the foundation of Dyssomnia. It's a realm where every legend and every being, from the mightiest creature to the humblest individual, is deeply intertwined with its genesis, continuing the dance of light and shadow begun by Luminara and Tenebros. The choices made, the allegiances formed, and the battles fought are all a testament to Dyssomnia's dual essence, reminding every dweller that in this world, every action, no matter how insignificant, has the potential to tip the balance.


