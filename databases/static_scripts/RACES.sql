------------------------------------------------------------CREATE TABLES------------------------------------------------------------

CREATE TABLE RACES (
    RaceID INTEGER PRIMARY KEY,
    RaceName TEXT NOT NULL,
    ShortDescription TEXT,
    Appearance TEXT,
    AbilityScoreIncrease TEXT,  -- JSON, e.g., '{"DEX": 2, "INT": 1}'
    Relations TEXT   -- Optional, JSON, e.g., '{"allies": ["Dwarves"], "enemies": ["Orcs"]}'
);

CREATE TABLE TRAITS (
    TraitID INTEGER PRIMARY KEY,
    TraitName TEXT NOT NULL,
    TraitDescription TEXT
);
CREATE TABLE PROFICIENCIES (
    ProficiencyID INTEGER PRIMARY KEY,
    ProficiencyName TEXT NOT NULL,
    ProficiencyType TEXT  -- E.g., 'Weapon', 'Armor', 'Skill'
);

CREATE TABLE RACES_TRAITS (
    RaceID INTEGER,
    TraitID INTEGER,
    PRIMARY KEY (RaceID, TraitID),
    FOREIGN KEY (RaceID) REFERENCES RACES (RaceID),
    FOREIGN KEY (TraitID) REFERENCES TRAITS (TraitID)
);
CREATE TABLE RACES_PROFICIENCIES (
    RaceID INTEGER,
    ProficiencyID INTEGER,
    PRIMARY KEY (RaceID, ProficiencyID),
    FOREIGN KEY (RaceID) REFERENCES RACES (RaceID),
    FOREIGN KEY (ProficiencyID) REFERENCES PROFICIENCIES (ProficiencyID)
);

------------------------------------------------------------INSERT DATA------------------------------------------------------------
------ Inserting races into RACES table
-- Humans
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Human', 
 'Driven by ambition, their cities rise as monuments to progress, but their wars scar the land.', 
 'Average height, varying skin tones, hair colors, and eye colors. Wide diversity in features.',
 '{"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}', 
 '{"allies": ["Dwarf", "Halfling"], "enemies": ["Orc"]}');

-- Elves
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Elf', 
 'Ancient forests echo with elven songs of beauty, but time has also taught them cold indifference.', 
 'Tall and slender, with fair skin, almond-shaped eyes, and long pointed ears.', 
 '{"DEX": 2}', 
 '{"allies": ["Half-Elf", "Aasimar"], "enemies": ["Dwarf"]}');

-- Dwarves
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Dwarf', 
 'Underground fortresses hide vast treasures, but old grudges smolder in the shadowed halls.', 
 'Short and stout, with thick beards, deep-set eyes, and tanned or grayish skin.',
 '{"CON": 2}', 
 '{"allies": ["Human", "Halfling"], "enemies": ["Elf", "Orc"]}');

-- Halflings
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Halfling', 
 'While most find solace in homely comforts, some are driven to adventure by an insatiable wanderlust.', 
 'Short in stature, with curly hair, round faces, and rosy cheeks.',
 '{"DEX": 2}', 
 '{"allies": ["Human", "Dwarf"], "enemies": []}');

-- Orcs
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Orc', 
 'Fierce tribal bonds unify them, but a tumultuous relationship with nature often brings chaos to their steps.', 
 'Tall and muscular, with green or gray skin, large tusks, and a broad nose.',
 '{"STR": 2}', 
 '{"allies": ["Half-Orc", "Tiefling"], "enemies": ["Human", "Dwarf"]}');

-- Aasimar
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Aasimar', 
 'Touched by celestial grace, they shine brightly, but some are haunted by a darker call.', 
 'Radiant skin that may shimmer, eyes that glow, sometimes with ethereal wings.',
 '{"CHA": 2}', 
 '{"allies": ["Elf", "Genasi"], "enemies": ["Tiefling"]}');

-- Genasi
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Genasi', 
 'Elemental fury courses through them, granting both the serenity of still waters and the rage of a storm.', 
 'Skin and hair that reflect their elemental lineage; blue for water, red for fire, gray for air, green/brown for earth.',
 '{"CON": 2}', 
 '{"allies": ["Aasimar", "Half-Elf"], "enemies": []}');

-- Tieflings
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Tiefling', 
 'Born of infernal deals, their arcane talents are as likely to save as to curse.', 
 'Red, purple, or dark blue skin, horns, pointed tail, and sometimes glowing eyes.',
 '{"CHA": 2, "INT": 1}', 
 '{"allies": ["Orc", "Dragonborn"], "enemies": ["Aasimar"]}');

-- Half-Elves
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Half-Elf', 
 'Bridging two worlds, their diverse gifts often come with a sense of unbelonging.', 
 'Mix of human and elf traits; medium height, slightly pointed ears, diverse eye and hair colors.',
 '{"CHA": 2}', 
 '{"allies": ["Elf", "Genasi", "Human"], "enemies": []}');

-- Dragonborn
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Dragonborn', 
 'Their breath tells of dragon lineage, and with it, a legacy of awe and fear.', 
 'Humanoid dragons; tall, scaly, and with a color that represents their draconic ancestry.',
 '{"STR": 2, "CHA": 1}', 
 '{"allies": ["Tiefling"], "enemies": []}');

-- Half-Orcs
INSERT INTO RACES (RaceName, ShortDescription, Appearance, AbilityScoreIncrease, Relations) VALUES
('Half-Orc', 
 'In their veins, human cunning meets orcish fury, forging warriors of unmatched vigor, often misunderstood by both sides.', 
 'Mix of human and orc traits; tall, muscular, with a slightly green tint to their skin and pronounced tusks.',
 '{"STR": 2, "CON": 1}', 
 '{"allies": ["Orc", "Human"], "enemies": []}');


------ Inserting traits into TRAITS table

INSERT INTO TRAITS (TraitName, TraitDescription) VALUES
('Darkvision', 'Can see in dim light.'),
('Keen Senses', 'Proficient in Perception.'),
('Dwarven Resilience', 'Resistant to poison damage.'),
('Dwarven Combat Training', 'Proficient with certain weapons.'),
('Brave', 'Advantage against being frightened.'),
('Halfling Nimbleness', 'Can move through larger creature spaces.'),
('Relentless Endurance', 'Drop to 1 hit point instead of 0 once.'),
('Celestial Resistance', 'Resistant to necrotic and radiant damage.'),
('Elemental Legacy', 'Access to elemental spells.'),
('Infernal Legacy', 'Access to certain spells.'),
('Fey Ancestry', 'Advantage against being charmed.'),
('Draconic Ancestry', 'Breath weapon and damage resistance.'),
('Savage Attacks', 'Extra damage dice on critical melee hit.');


------ Mapping traits to races in RACES_TRAITS table

-- Elf
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (2, 1), (2, 2), (2, 11);

-- Dwarf
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (3, 1), (3, 3), (3, 4);

-- Halfling
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (4, 5), (4, 6);

-- Orc
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (5, 7), (5, 13);

-- Aasimar
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (6, 8);

-- Genasi
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (7, 9);

-- Tiefling
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (8, 1), (8, 10);

-- Half-Elf
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (9, 1), (9, 2), (9, 11);

-- Dragonborn
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (10, 12);

-- Half-Orc
INSERT INTO RACES_TRAITS (RaceID, TraitID) VALUES (11, 7), (11, 13);


-------- Inserting proficiencies into PROFICIENCIES table

-- Weapon Proficiencies
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Dagger', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Shortsword', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Longsword', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Handaxe', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Greataxe', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Battleaxe', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Javelin', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Shortbow', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Longbow', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Mace', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Quarterstaff', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Rapier', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Scimitar', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Shortbow', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Sling', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Warhammer', 'Weapon');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Crossbow', 'Weapon');


-- Armor Proficiencies
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Shield', 'Armor');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Unarmored', 'Armor');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Light armor', 'Armor');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Medium armor', 'Armor');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Heavy armor', 'Armor');

-- Tool Proficiencies
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Thieves’ tools', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Smith’s tools', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Brewer’s supplies', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Mason’s tools', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Potter’s tools', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Tinker’s tools', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Herbalism kit', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Navigator’s tools', 'Tool');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Disguise kit', 'Tool');

-- Skill Proficiencies
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Acrobatics', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Animal Handling', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Arcana', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Athletics', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Deception', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('History', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Insight', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Intimidation', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Investigation', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Medicine', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Nature', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Perception', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Performance', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Persuasion', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Religion', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Sleight of Hand', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Stealth', 'Skill');
INSERT INTO PROFICIENCIES (ProficiencyName, ProficiencyType) VALUES ('Survival', 'Skill');


------ Mapping proficiencies to races in RACES_PROFICIENCIES table

-- Humans (variant humans might get to pick a skill, but in general humans don't have racial proficiencies)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (1, NULL); 

-- Elf (proficient with longswords, shortswords, shortbows, and longbows, perception)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (2, 2), (2, 3), (2, 8), (2, 9), (2, 43);

-- Dwarf (proficient with battleaxes, handaxes, throwing hammers, warhammers, light and medium armor, history relating to stonework)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (3, 6), (3, 5), (3, 16), (3, 20), (3, 21), (3, 37);

-- Halfling (Stealthy)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (4, 48); 

-- Orc (typically proficient with greataxes, javelins, and Intimidation in certain settings)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (5, 5), (5, 7), (5, 39);

-- Aasimar (typically have some celestial resistances, no standard weapon proficiencies but sometimes insight and persuasion)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (6, 38), (6, 45);

-- Genasi (proficiencies vary depending on elemental subrace, but we'll skip for the core race)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (7, NULL);

-- Tiefling (depending on lore, they might have resistances, no typical weapon proficiencies but some versions might have deception)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (8, 36);

-- Half-Elf (get to choose two skills of their choice)
-- This is tricky because the proficiencies aren't fixed.
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (9, NULL); 

-- Dragonborn (no typical proficiencies)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (10, NULL); 

-- Half-Orc (proficient with greataxes, javelins, and Intimidation)
INSERT INTO RACES_PROFICIENCIES (RaceID, ProficiencyID) VALUES (11, 5), (11, 7), (11, 39);
