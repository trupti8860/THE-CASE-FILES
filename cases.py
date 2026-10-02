"""
THE CASE FILES - Case Database
Contains 16 complete, deeply plotted mysteries across Indian cities,
international centers, and modern digital forensics.
Each case features:
- Detailed crime scene reconstruction
- 4-5 distinct suspects with unique motives, alibis, and interrogation branches
- 6-10 examine-able clues with hidden layers
- Chronological timeline events
- Progressive multi-tier hints that reveal contradictions logically
- Verified murderer and final deduction debrief
"""

CASES = [
    {
        "id": "CASE-001",
        "title": "The 2:17 AM Call",
        "location": "Hauz Khas, New Delhi",
        "time": "02:17 AM",
        "category": "Indian Mystery",
        "difficulty": "Moderate",
        "victim": "Karan Malhotra (34, Fintech Executive)",
        "cause_of_death": "Blunt force trauma to the occipital bone",
        "synopsis": (
            "Karan Malhotra was discovered dead across his glass desk inside his 5th-floor penthouse. "
            "His mobile phone recorded an answered call lasting 42 seconds at 2:17 AM. The landline cord was cut, "
            "and his vintage mechanical desk clock stopped at 2:18 AM upon impact."
        ),
        "scene_details": [
            "Heavy rain outside; French balcony doors unlocked and slightly ajar.",
            "Broken crystal decanter with traces of 25-year Scotch on the Persian rug.",
            "Victim's desktop monitor running an unsent encrypted wire transfer of ₹1.4 Crores.",
            "A wet mud footprint (size 9 UK) pointing towards the internal hallway.",
            "The victim's wrist watch shattered at precisely 2:18 AM."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Victim's Smartphone",
                "desc": "Screen cracked. Logs confirm an incoming call from an unlisted burner SIM at 2:17 AM, answered for 42 seconds.",
                "details": "Tower triangulation points the caller's signal to within 200 meters of the Hauz Khas apartment complex itself."
            },
            {
                "id": "E-02",
                "name": "Broken Heavy Crystal Decanter",
                "desc": "Covered in blood and hair follicles corresponding to Karan's occipital wound.",
                "details": "Forensics detected smeared latex powder on the handle, showing the killer wore surgical gloves."
            },
            {
                "id": "E-03",
                "name": "Basement Parking CCTV Log",
                "desc": "Camera 3 records a dark sedan leaving at 2:26 AM without headlights turned on.",
                "details": "Security logbook lists Rohit Verma's registered vehicle parking stall directly under Camera 3."
            },
            {
                "id": "E-04",
                "name": "Encrypted Wire Transfer Draft",
                "desc": "A pending transaction of ₹1.4 Crores addressed to 'Vanguard Offshore Holdings'.",
                "details": "Company registry reveals Kabir Sethi is the sole beneficial owner of Vanguard Offshore Holdings."
            },
            {
                "id": "E-05",
                "name": "Damp Muddy Towel in Hallway Hamper",
                "desc": "A white guest towel damp with rainwater and terracotta garden mud.",
                "details": "Terracotta potting soil matches the decorative plants kept exclusively along Maya Roy's adjacent terrace."
            },
            {
                "id": "E-06",
                "name": "Pill Bottle: Zolpidem (Ambien)",
                "desc": "Found inside Karan's jacket. Prescribed to his wife Tara Malhotra two days prior.",
                "details": "Toxicology confirmed low traces of Zolpidem in Karan's Scotch glass, slowing his reflexes before the strike."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Tara Malhotra",
                "role": "Victim's Wife",
                "alibi": "Claims she took sleeping pills and was asleep in the master bedroom with earplugs.",
                "motive": "Facing a contested divorce and standing to inherit the penthouse estate.",
                "dialogue": [
                    ("Where were you at 2:17 AM?", "I took my Zolpidem at midnight. I heard absolutely nothing until the police sirens arrived."),
                    ("Why was your sedative in Karan's drink?", "Karan couldn't sleep because of his audit! He must have taken one from my nightstand."),
                    ("Did you hear the balcony door open?", "The storm was howling. If someone came across the balcony, I wouldn't have heard it.")
                ]
            },
            {
                "id": "S2",
                "name": "Kabir Sethi",
                "role": "Business Co-Founder",
                "alibi": "Claims he was at an all-night diner in Aerocity finishing quarterly pitch slides.",
                "motive": "Karan uncovered Kabir's illicit offshore siphoning and scheduled an audit for 9 AM.",
                "dialogue": [
                    ("Did you know about the ₹1.4 Crore transfer?", "Karan was handling international payouts. It had nothing to do with personal accounts."),
                    ("Can anyone verify you were at Aerocity at 2:15 AM?", "I paid with my card at the diner... well, my assistant grabbed coffee with my card."),
                    ("Why call him at 2:17 AM?", "I didn't call him! My phone battery died around 1:30 AM.")
                ]
            },
            {
                "id": "S3",
                "name": "Rohit Verma",
                "role": "Financial Auditor",
                "alibi": "Claims he was home in Saket reviewing company spreadsheets all evening.",
                "motive": "Karan was blackmailing Rohit to sign off on fabricated balance sheets.",
                "dialogue": [
                    ("Your sedan was logged leaving Karan's basement at 2:26 AM.", "That's impossible! I lent my car to my brother three days ago!"),
                    ("Did you visit the penthouse tonight?", "No. I spoke to Karan on WhatsApp at 9 PM and shut my laptop."),
                    ("What about the size 9 mud prints?", "Half the men in Delhi wear size 9 shoes! You need real evidence.")
                ]
            },
            {
                "id": "S4",
                "name": "Maya Roy",
                "role": "Terrace Neighbor & Architect",
                "alibi": "States she was drafting blueprints in her studio overlooking the courtyard.",
                "motive": "Severe property dispute involving terrace expansion and municipal complaints.",
                "dialogue": [
                    ("The mud on the hallway towel matches your terrace planters.", "We had torrential rains; rainwater overflows across both our balconies."),
                    ("Did you see anyone on Karan's balcony?", "Around 2:10 AM, I noticed someone tall in a dark trench coat slipping past his French doors."),
                    ("Did you place any calls at 2:17 AM?", "No, my phone was charging in my bedroom.")
                ]
            }
        ],
        "timeline": [
            ("01:15 AM", "Karan pours a glass of 25-year Scotch laced with Zolpidem."),
            ("01:45 AM", "A figure enters via the basement fire stairs, avoiding main lobby security."),
            ("02:10 AM", "Terrace observer notices movement near the French doors."),
            ("02:17 AM", "A burner call rings Karan's phone to distract him while he stands up."),
            ("02:18 AM", "Karan is struck from behind with the crystal decanter; clock shatters."),
            ("02:26 AM", "A dark sedan slips out of the basement garage with headlights off.")
        ],
        "murderer_id": "S2",
        "murderer_name": "Kabir Sethi",
        "hints": [
            "HINT 1: Examine the 2:17 AM phone call. It was placed within 200 meters, proving the caller was already on-site to stage a distraction.",
            "HINT 2: Kabir claimed his phone battery died at 1:30 AM, yet his secret offshore account was keyed directly into Karan's desk monitor minutes before the attack.",
            "HINT 3: Kabir's 'Aerocity diner' alibi collapsed—he admitted sending an assistant with his credit card while he took Rohit's borrowed sedan to Hauz Khas."
        ],
        "solution_summary": (
            "Kabir Sethi had embezzled company funds into Vanguard Offshore. When Karan discovered this and demanded restitution, "
            "Kabir borrowed Rohit's sedan, sneaked into the building, and called Karan from a burner phone inside the flat corridor. "
            "When Karan rose to answer the 2:17 AM call, Kabir struck him from behind with the decanter and attempted to authorize the wire transfer."
        )
    },
    {
        "id": "CASE-002",
        "title": "The Last Local to Kasara",
        "location": "Central Railway Line, Mumbai",
        "time": "01:45 AM",
        "category": "Indian Mystery",
        "difficulty": "Challenging",
        "victim": "Devendra Joshi (51, Railway Land Inspector)",
        "cause_of_death": "Strychnine poisoning disguised in thermos tea",
        "synopsis": (
            "During the last midnight slow train to Kasara, Devendra Joshi collapsed in the first-class compartment "
            "as the train crossed the dark Kalyan-Titwala viaduct. The compartment contained only four other passengers."
        ),
        "scene_details": [
            "Compartment illuminated by flickering fluorescent tube lights.",
            "Spilled stainless steel thermos flask rolling on the floor.",
            "Devendra's leather briefcase forced open; surveyor maps of Thane creek missing.",
            "Train conductor confirms no one boarded or leapt between Kalyan and Titwala stations."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Stainless Steel Thermos",
                "desc": "Contains ginger tea mixed with lethal amounts of strychnine alkaloid.",
                "details": "Fingerprints around the thermos lid show two distinct handlers: Devendra and an unidentified palm print."
            },
            {
                "id": "E-02",
                "name": "Platform Vendor Receipt",
                "desc": "Issued at Kalyan Platform 4 at 01:12 AM for three cups of cutting chai and bottled water.",
                "details": "Signed by ticket clerk indicating Pradeep Kadam bought the round of beverages."
            },
            {
                "id": "E-03",
                "name": "Torn Blue Ledger Page",
                "desc": "Crumpled inside the victim's sock listing illegal slum clearance kickbacks in Kalwa.",
                "details": "Mentions initials 'A.S.' and 'P.K.' receiving ₹50 Lakhs in cash installments."
            },
            {
                "id": "E-04",
                "name": "Surgical Eye Dropper",
                "desc": "Found tucked inside the compartment gap between window seats 12 and 14.",
                "details": "Chemical residue matches the concentrated liquid strychnine used in the poisoning."
            },
            {
                "id": "E-05",
                "name": "First-Class Season Pass",
                "desc": "Registered to Anjali Sawant, senior legal officer for the suburban land registry.",
                "details": "Her handbag contained a chemical catalogue from a pharmaceutical distributor in Kurla."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Pradeep Kadam",
                "role": "Railway Infrastructure Contractor",
                "alibi": "Claims he fell asleep near the doorway after leaving Kalyan.",
                "motive": "Devendra was about to cancel his multi-crore railway track contract for substandard gravel.",
                "dialogue": [
                    ("Did you buy tea at Kalyan?", "Yes, for myself and the ticket checker. I never touched Devendra's flask."),
                    ("Your initials are on the Kalwa slum ledger.", "Joshi was corrupt! He wrote down whoever refused to bribe him!"),
                    ("Why were your hands shaking when the police boarded?", "I just saw a man die in convulsions. Anyone would be shaken.")
                ]
            },
            {
                "id": "S2",
                "name": "Anjali Sawant",
                "role": "Suburban Land Registry Officer",
                "alibi": "States she was reading legal briefs with headphones on the entire journey.",
                "motive": "Devendra caught her falsifying coastal wetland clearance titles.",
                "dialogue": [
                    ("Why do you have a chemical catalogue in your bag?", "Our legal team represents a chemical firm in an arbitration case!"),
                    ("Did you leave your seat at any point?", "Never. Pradeep can verify I didn't get up."),
                    ("Did Devendra speak before he died?", "He gasped, reached for his throat, and looked directly towards the door.")
                ]
            },
            {
                "id": "S3",
                "name": "Ganesh Naik",
                "role": "Night Ticket Checker (TTE)",
                "alibi": "Claims he was checking passes in the second-class bogie until Kalyan.",
                "motive": "Devendra reported him for operating an extortion racket on midnight trains.",
                "dialogue": [
                    ("When did you enter the first-class coach?", "Just as we pulled out of Kalyan. Devendra was already coughing."),
                    ("Did you accept tea from Pradeep Kadam?", "He offered, but I refused. I don't take drinks on duty."),
                    ("Where was Devendra's briefcase when you saw him?", "It was open on the opposite seat. Papers were fluttering everywhere.")
                ]
            },
            {
                "id": "S4",
                "name": "Dr. Subhash Rao",
                "role": "Retired Government Botanist",
                "alibi": "Traveling to his farmhouse in Asangaon with medicinal herb samples.",
                "motive": "Devendra expropriated his family ancestral land without compensation.",
                "dialogue": [
                    ("You carry plant alkaloids in your luggage.", "I am a registered taxonomist. My specimens are sealed and labeled."),
                    ("Did you attempt CPR on Devendra?", "I checked his pulse. It was erratic, typical of severe neurotoxic shock."),
                    ("Did anyone tamper with the thermos?", "While Devendra was in the lavatory at Kalyan, someone reached across his table.")
                ]
            }
        ],
        "timeline": [
            ("01:05 AM", "Train reaches Kalyan Junction; Devendra steps into the station lavatory."),
            ("01:12 AM", "Pradeep Kadam buys tea; someone reaches across Devendra's vacant seat."),
            ("01:18 AM", "Train departs Kalyan towards Kasara."),
            ("01:32 AM", "Devendra takes several sips from his personal stainless steel thermos."),
            ("01:40 AM", "Violent spasms begin as the train crosses the Ulhas River viaduct."),
            ("01:45 AM", "Devendra collapses; passenger alarm chain is pulled near Titwala.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Pradeep Kadam",
        "hints": [
            "HINT 1: Cross-reference who had access to Devendra's thermos while the train stopped at Kalyan.",
            "HINT 2: The eye dropper was found between seats 12 and 14, where Pradeep sat before moving to the doorway.",
            "HINT 3: Pradeep claimed he bought tea for the TTE, but TTE Ganesh Naik explicitly confirmed he refused the drink."
        ],
        "solution_summary": (
            "Pradeep Kadam knew his fraudulent railway gravel contracts were being terminated by Devendra. "
            "When Devendra stepped out at Kalyan, Pradeep used a dropper to inject strychnine into the thermos nozzle, "
            "then manufactured a fake story about buying chai to explain why he was standing near the victim's berth."
        )
    },
    {
        "id": "CASE-003",
        "title": "The Sangeet Night Secret",
        "location": "Umaid Heritage Palace, Jaipur",
        "time": "11:55 PM",
        "category": "Indian Mystery",
        "difficulty": "Moderate",
        "victim": "Raghav Singhania (28, Groom & Industrialist Heir)",
        "cause_of_death": "Fall from the 4th-floor terrace pavilion",
        "synopsis": (
            "During a high-society destination wedding sangeet, the groom Raghav Singhania was found dead "
            "on the marble courtyard below the royal suite. The railing had snapped, but inspection revealed the bolts had been removed."
        ),
        "scene_details": [
            "Confetti and marigold garlands scattered across the courtyard stones.",
            "Victim's sherwani torn near the collar, suggesting a close struggle.",
            "A severed cufflink inscribed with the letter 'V' found on the rooftop balustrade.",
            "Heavy brass antique wrench hidden behind a marble fountain pillar."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Wrench with Thread Traces",
                "desc": "A 14mm brass wrench coated with freshly stripped paint from the pavilion railing bolts.",
                "details": "Found in the royal pantry towel bin, wrapped in linen bearing Vikram Singhania's initial."
            },
            {
                "id": "E-02",
                "name": "Severed Platinum Cufflink",
                "desc": "Custom engraved platinum with the initial 'V' and inset with a baguette diamond.",
                "details": "Vikram Singhania was photographed wearing the exact matching pair at 10:30 PM on stage."
            },
            {
                "id": "E-03",
                "name": "Prenuptial Agreement Draft",
                "desc": "Retrieved from bride Rhea Oberoi's vanity case with aggressive dispute clauses.",
                "details": "Raghav had refused to sign the clause transferring 30% of his shipping shares to the Oberoi trusts."
            },
            {
                "id": "E-04",
                "name": "Champagne Flute with Sedative",
                "desc": "Half-empty crystal glass recovered from the terrace ledge.",
                "details": "Contained traces of liquid ketamine, enough to severely disorient balance."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Vikram Singhania",
                "role": "Raghav's Estranged Stepbrother",
                "alibi": "Claims he was smoking in the palace cigar lounge from 11:30 PM onwards.",
                "motive": "Stood to become sole successor to the Singhania shipping fortune if Raghav died unwed.",
                "dialogue": [
                    ("Where is your other cufflink, Vikram?", "I must have lost it dancing during the bhangra performance."),
                    ("Why was the wrench wrapped in your napkin?", "Someone is framing me! Any waiter could grab my table linen!"),
                    ("Were you on the rooftop terrace?", "Raghav told me to meet him there to talk about our father's will, but I didn't go.")
                ]
            },
            {
                "id": "S2",
                "name": "Rhea Oberoi",
                "role": "The Bride",
                "alibi": "Claims she was changing outfits in the bridal suite with her makeup artists.",
                "motive": "Discovered Raghav had discovered her family's bankruptcy and threatened to cancel the wedding.",
                "dialogue": [
                    ("Raghav refused to sign the prenuptial agreement.", "We had disagreements, yes, but we were in love. I wouldn't push him!"),
                    ("Did you leave your dressing room?", "My stylists were with me until 11:45 PM when I went down to the buffet."),
                    ("Did you see Vikram upstairs?", "I saw him slipping up the back heritage staircase around 11:40 PM.")
                ]
            },
            {
                "id": "S3",
                "name": "Sameer Merchant",
                "role": "Event Architect & Wedding Planner",
                "alibi": "Overseeing fireworks display setup on the north lawn.",
                "motive": "Raghav owed him ₹80 Lakhs in unpaid staging fees and threatened his firm with ruin.",
                "dialogue": [
                    ("You had tools to unscrew the railing bolts.", "All our tools are catalogued in the main marquee tent."),
                    ("Were you on the roof?", "I was synchronizing the 12:00 AM firework mortars with the DJ console."),
                    ("Did you hear an argument?", "The bass from the music was so loud you couldn't hear a gunshot, let alone an argument.")
                ]
            },
            {
                "id": "S4",
                "name": "Devika Singhania",
                "role": "Family Matriarch",
                "alibi": "Seated at the VIP banquet table with royal guests.",
                "motive": "Furious that Raghav was breaking generational trust conventions.",
                "dialogue": [
                    ("How was Raghav acting tonight?", "Agitated. He had words with both Vikram and Rhea before dinner."),
                    ("Did you notice Vikram leaving?", "Vikram disappeared after 11:20 PM. He reeked of panic when he came back down."),
                    ("Who controlled access to the rooftop pavilion?", "Only family members had keycards to the royal rooftop.")
                ]
            }
        ],
        "timeline": [
            ("10:45 PM", "Heated argument between Raghav and Vikram overheard near the banquet bar."),
            ("11:25 PM", "Railing bolts on the 4th-floor pavilion loosened with an antique brass wrench."),
            ("11:42 PM", "Raghav goes to the rooftop terrace to take an urgent private phone call."),
            ("11:50 PM", "A struggle ensues; a cufflink is ripped off near the weakened balustrade."),
            ("11:55 PM", "Railing gives way; Raghav falls into the central courtyard."),
            ("12:00 AM", "Fireworks launch, drowning out the initial commotion.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Vikram Singhania",
        "hints": [
            "HINT 1: The cufflink torn from the killer's sleeve has a specific initial directly matching the heir who inherits if Raghav dies before marriage.",
            "HINT 2: The wrench was wrapped in linen from Vikram's private reserved table.",
            "HINT 3: Vikram claimed he never went up to the rooftop, but the bride spotted him on the back stairs minutes before the fall."
        ],
        "solution_summary": (
            "Vikram faced total disinheritance once Raghav officially married Rhea. He loosened the balcony bolts earlier in the evening, "
            "then lured Raghav onto the terrace under the pretext of settling their father's estate. When Raghav refused to compromise, "
            "Vikram shoved him against the compromised railing, losing his cufflink during the brief struggle."
        )
    },
    {
        "id": "CASE-004",
        "title": "Offline at 03:00",
        "location": "Koramangala, Bengaluru",
        "time": "03:15 AM",
        "category": "Modern / Tech Mystery",
        "difficulty": "Challenging",
        "victim": "Tanmay Ghosh (26, Founder of AI Startup 'NeuralPay')",
        "cause_of_death": "Electrocution via modified VR headset",
        "synopsis": (
            "Tanmay was discovered slumped in his ergonomic chair inside NeuralPay's soundproof testing lab. "
            "His virtual reality headset had sustained a sudden capacitor surge, delivering a fatal jolt to his temples. "
            "His Discord status switched from 'In Lab - Do Not Disturb' to 'Offline' at exactly 03:00 AM."
        ),
        "scene_details": [
            "State-of-the-art startup lab with RGB ambient lighting and multiple server racks.",
            "Burnt smell of melted copper wiring and lithium batteries.",
            "Server log showed a forced Git push deleting the core NeuralPay codebase at 02:58 AM.",
            "A smart mug warmer on the desk still warm to the touch."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Modified VR Headset Wiring",
                "desc": "The device's power regulators had been bridged with a fine solder wire to bypass surge fuses.",
                "details": "Soldering kit in the workshop drawer tested positive for blue resin flux residue."
            },
            {
                "id": "E-02",
                "name": "Server Terminal Command History",
                "desc": "A terminal session executed 'rm -rf /neuralpay/core --no-preserve-root' at 02:58 AM.",
                "details": "The command was authenticated using the SSH key assigned to Lead Engineer Shreya Nambiar."
            },
            {
                "id": "E-03",
                "name": "NFC Keycard Access Logs",
                "desc": "Lab Door 2 was accessed by card #4092 (belonging to Arjun Rao) at 02:44 AM.",
                "details": "Arjun claims he lost his card in the pantry around 11 PM."
            },
            {
                "id": "E-04",
                "name": "Pantry Security Camera",
                "desc": "Footage shows someone wearing an oversized grey hoodie picking up Arjun's lost keycard from the counter at 01:15 AM.",
                "details": "Rohan Mehta was photographed wearing that identical grey hoodie during the hackathon."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Shreya Nambiar",
                "role": "Lead Systems Architect",
                "alibi": "States she was debugging neural weights from her flat in Indiranagar.",
                "motive": "Tanmay took sole credit for her neural algorithm in a $20M acquisition deal.",
                "dialogue": [
                    ("Your SSH key deleted the codebase.", "My SSH private key was stored on the office local server. Anyone with physical lab access could trigger it!"),
                    ("Did you know how the VR headset was modified?", "I warned Tanmay repeatedly that his overclocked bench setup was a fire hazard."),
                    ("Were you in Koramangala tonight?", "My Uber receipt proves I went home at 11:30 PM.")
                ]
            },
            {
                "id": "S2",
                "name": "Rohan Mehta",
                "role": "Hardware Co-Founder & CTO",
                "alibi": "Claims he was asleep on the office nap pod after a 36-hour sprint.",
                "motive": "Tanmay had secretly signed buyout papers to oust Rohan and take all investor equity.",
                "dialogue": [
                    ("You were wearing the grey hoodie seen stealing Arjun's keycard.", "Half the company wears the company hoodie! It's our official merchandise!"),
                    ("We found blue soldering flux on your desk.", "I build our hardware prototypes. Flux is on everything in my workspace!"),
                    ("Did you know Tanmay was using the VR rig at 3 AM?", "He always tested late at night. He said the quiet helped him focus.")
                ]
            },
            {
                "id": "S3",
                "name": "Arjun Rao",
                "role": "Junior Backend Developer",
                "alibi": "Playing online video games in the recreational breakroom.",
                "motive": "Threatened with immediate termination over an alleged intellectual property leak.",
                "dialogue": [
                    ("Why was your card used to unlock the lab?", "I left it on the cafeteria counter when getting Red Bull! I swear!"),
                    ("Did you hear anything from the lab?", "The lab is completely soundproof. You couldn't hear an explosion inside."),
                    ("What did you think of Tanmay?", "He was brutal to everyone. He fired our DevOps lead on Slack last week without warning.")
                ]
            },
            {
                "id": "S4",
                "name": "Meera Sen",
                "role": "Venture Capital Partner",
                "alibi": "At the Leela Palace dining with potential foreign LPs.",
                "motive": "Tanmay's company had fabricated user metrics to secure their seed round.",
                "dialogue": [
                    ("Did you visit NeuralPay tonight?", "I had no reason to visit their dingy garage lab. Our lawyers were preparing an injunction."),
                    ("Did Tanmay express fear of anyone?", "He was terrified of Rohan. He told me Rohan had threatened to wipe the company servers."),
                    ("Did you speak to him before midnight?", "He texted me: 'The code is safe, Rohan has no leverage.'")
                ]
            }
        ],
        "timeline": [
            ("01:15 AM", "The grey-hooded figure picks up Arjun's dropped access card in the cafeteria."),
            ("02:30 AM", "Tanmay puts on the high-voltage test VR rig to preview the new neural environment."),
            ("02:44 AM", "Access card #4092 unlocks Lab Door 2."),
            ("02:52 AM", "Hardware bypass wire applied across capacitor surge terminals."),
            ("02:58 AM", "Malicious code deletion executed from the local console using Shreya's workstation."),
            ("03:00 AM", "Surge triggered; victim electrocuted instantly; status goes Offline.")
        ],
        "murderer_id": "S2",
        "murderer_name": "Rohan Mehta",
        "hints": [
            "HINT 1: Only someone with deep electrical hardware expertise could intentionally rig a capacitor surge on the VR headset.",
            "HINT 2: The killer stole Arjun's keycard while wearing the hoodie, then framed Shreya by executing the terminal wipe from her unlocked local desk.",
            "HINT 3: Rohan was inside the premises (sleeping pod), had access to the solder tools, and stood to lose his life's equity in the buyout."
        ],
        "solution_summary": (
            "Rohan discovered Tanmay's plan to sign away the company and push him out. Utilizing his deep hardware mastery, "
            "Rohan stole Arjun's badge, bridged the surge fuses on Tanmay's custom VR helmet, triggered the wipe using Shreya's terminal to frame her, "
            "and watched as the test rig electrocuted Tanmay the moment the simulated environment launched."
        )
    },
    {
        "id": "CASE-005",
        "title": "The Locked Penthouse of Montmartre",
        "location": "Paris, France",
        "time": "10:15 PM",
        "category": "International Mystery",
        "difficulty": "Hard",
        "victim": "Julien Laurent (47, High-End Art Dealer)",
        "cause_of_death": "Stab wound to the carotid artery via antique fencing foil",
        "synopsis": (
            "In an opulent 6th-floor Montmartre penthouse, Julien Laurent was found dead inside his study. "
            "The heavy oak door was bolted from the inside with a solid steel slide latch. The windows were sealed shut "
            "with intact security tape, and the fireplace flue was blocked by an iron grating."
        ),
        "scene_details": [
            "Floor-to-ceiling bookshelves lined with rare Renaissance manuscripts.",
            "An empty picture frame where a newly authenticated Caravaggio sketch was previously displayed.",
            "The internal sliding deadbolt engaged; the key was found inside the room on the mantelpiece.",
            "A spool of high-tensile transparent nylon fishing line found behind the radiator."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Nylon Fishing Line & Magnet",
                "desc": "Traces of 0.4mm monofilament looped through the gap beneath the antique oak door.",
                "details": "Microscopic scuff marks on the steel latch prove the bolt was pulled shut from outside using tension."
            },
            {
                "id": "E-02",
                "name": "Antique Fencing Foil",
                "desc": "Part of a decorative wall display. The triangular blade is stained with Julien's blood.",
                "details": "No fingerprints found; wiped down with oil-soaked rag."
            },
            {
                "id": "E-03",
                "name": "Insurance Appraisal Document",
                "desc": "Valuing the missing Caravaggio sketch at €4.8 Million, payable immediately upon theft or destruction.",
                "details": "Julien had named art restorer Claire Moreau as secondary beneficiary in case of total gallery insolvency."
            },
            {
                "id": "E-04",
                "name": "Train Ticket to Geneva",
                "desc": "Discovered in appraiser Henri Dubois's overcoat pocket, scheduled for departure at 11:45 PM tonight.",
                "details": "Dubois's briefcase contained a forged export license for an unnamed 17th-century Italian drawing."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Claire Moreau",
                "role": "Master Art Restorer",
                "alibi": "Restoring an oil canvas in the ground floor workshop.",
                "motive": "Julien refused to pay her studio fees and blackmailed her over prior forgery work.",
                "dialogue": [
                    ("How could the study door be locked from inside?", "Julien was paranoid. He always latched it whenever he examined high-value pieces."),
                    ("Were you aware of the insurance policy?", "Julien mentioned it, but I never signed any agreement!"),
                    ("Did you hear Julien cry out?", "I had headphones on while operating the varnish drying lamps.")
                ]
            },
            {
                "id": "S2",
                "name": "Henri Dubois",
                "role": "Auction House Valuer",
                "alibi": "Claims he left the building at 09:30 PM after valuing the Caravaggio.",
                "motive": "Julien exposed Dubois for certifying fakes to wealthy international syndicates.",
                "dialogue": [
                    ("Why do you have a midnight ticket to Geneva?", "I am traveling for an international estate appraisal. It was planned for months!"),
                    ("Where is the Caravaggio sketch?", "It was still on his easel when I left at 9:30. Julien let me out himself!"),
                    ("Do you fish, Monsieur Dubois?", "What kind of ridiculous question is that? I haven't held a rod in thirty years.")
                ]
            },
            {
                "id": "S3",
                "name": "Marcelle Blanc",
                "role": "Julien's Building Concierge",
                "alibi": "Sitting in the ground floor lodge watching television.",
                "motive": "Julien had filed eviction papers against her family after a rent dispute.",
                "dialogue": [
                    ("Did anyone enter the building after 9:30 PM?", "Only Monsieur Dubois, who claimed he forgot his gloves and went back up around 9:55 PM!"),
                    ("Did you see Dubois leave again?", "He ran out past my window at 10:20 looking pale as a ghost."),
                    ("Did Julien have any other visitors?", "No one. The elevator was parked on the 6th floor the entire evening.")
                ]
            },
            {
                "id": "S4",
                "name": "Lucie Laurent",
                "role": "Julien's Estranged Sister",
                "alibi": "Dining at a brasserie in Saint-Germain-des-Prés.",
                "motive": "Dispute over their late father's French estate inheritance.",
                "dialogue": [
                    ("When did you last speak with Julien?", "Three weeks ago when his lawyers sent me another threatening cease-and-desist."),
                    ("Did you know about the Caravaggio?", "Julien boasted about it constantly on his social feeds."),
                    ("Could anyone have climbed the balcony?", "It's six stories above the cobblestones. Only a bird could get in through the balcony.")
                ]
            }
        ],
        "timeline": [
            ("09:30 PM", "Henri Dubois concludes initial valuation and leaves the penthouse."),
            ("09:55 PM", "Dubois returns, claiming forgotten gloves; concierge lets him in."),
            ("10:05 PM", "Heated struggle in study; Dubois grabs the antique foil from the wall mount."),
            ("10:12 PM", "Julien killed; sketch rolled into cardboard tube."),
            ("10:15 PM", "Dubois strings nylon wire through latch, steps out, closes door, and pulls latch shut."),
            ("10:20 PM", "Dubois flees concierge lodge towards Gare de Lyon.")
        ],
        "murderer_id": "S2",
        "murderer_name": "Henri Dubois",
        "hints": [
            "HINT 1: The 'locked room' was a mechanical trick executed with nylon wire and an external pull.",
            "HINT 2: The concierge directly contradicted Dubois's claim that he departed at 9:30 PM and never returned.",
            "HINT 3: Dubois had an imminent midnight one-way ticket to Geneva and a forged export certificate for the stolen sketch."
        ],
        "solution_summary": (
            "Henri Dubois returned to steal the multi-million euro Caravaggio sketch before fleeing to Switzerland. "
            "When Julien confronted him, Dubois impaled him with the decorative fencing foil. He staged the locked room trick "
            "by looping nylon thread under the door to pull the slide bolt shut, deceiving investigators into thinking Julien died alone."
        )
    },
    {
        "id": "CASE-006",
        "title": "The Deleted Story",
        "location": "Bandra West, Mumbai",
        "time": "02:30 AM",
        "category": "Modern / Gen-Z Mystery",
        "difficulty": "Moderate",
        "victim": "Zoya Mirza (23, Lifestyle Influencer)",
        "cause_of_death": "Anaphylactic shock triggered by hidden peanut extract",
        "synopsis": (
            "At an exclusive rooftop afterparty, Zoya Mirza collapsed after taking a sip of a bespoke cocktail. "
            "Minutes before her collapse, she posted an Instagram story showing a blurred figure in the background with the caption "
            "'Someone brought uninvited energy tonight 💀'—a story deleted from her account four minutes later."
        ),
        "scene_details": [
            "Infinity pool reflection decorated with neon signs and cocktail shakers.",
            "Zoya's customized bedazzled cocktail tumbler on the deck table.",
            "EpiPen in her clutch bag had been discharged and emptied prior to the party.",
            "High-end mixology bar stocked with artisanal almond and nut extracts."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Tampered EpiPen Auto-Injector",
                "desc": "Recovered from Zoya's purse. The chamber contained sterile saline solution instead of epinephrine.",
                "details": "Micro-puncture marks indicate the medication was drawn out and substituted with a syringe."
            },
            {
                "id": "E-02",
                "name": "Recovered Deleted Instagram Story",
                "desc": "Cloud cache snapshot shows a sleeve with distinctive yellow embroidery spiking a drink behind the DJ booth.",
                "details": "Fashion stylist Veer Kapoor was wearing a designer yellow-embroidered jacket at the party."
            },
            {
                "id": "E-03",
                "name": "Phone IP Audit Log",
                "desc": "Zoya's Instagram account was logged into at 02:34 AM from a Samsung Galaxy S24 on the pool Wi-Fi.",
                "details": "MAC address ties directly to Natasha Roy's registered personal device."
            },
            {
                "id": "E-04",
                "name": "Brand Endorsement Contract",
                "desc": "A ₹2.5 Crore global cosmetics ambassadorship signed yesterday.",
                "details": "Contract contained a clause: if Zoya was unable to fulfill duties, runner-up Natasha Roy would step in."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Natasha Roy",
                "role": "Rival Influencer",
                "alibi": "Claims she was dancing on the main dance floor with friends.",
                "motive": "Directly replaces Zoya for a multi-crore international brand deal.",
                "dialogue": [
                    ("Why was Zoya's story deleted from your phone?", "Zoya asked me to manage her social feed! She had given me her password weeks ago!"),
                    ("Did you touch her EpiPen?", "I didn't even know she had a severe allergy!"),
                    ("Why did you delete that specific story?", "It was unflattering and blurred! Our agency always curates clean aesthetics.")
                ]
            },
            {
                "id": "S2",
                "name": "Veer Kapoor",
                "role": "Fashion Stylist",
                "alibi": "States he was at the dessert buffet chatting with the pastry chef.",
                "motive": "Zoya publicly mocked his debut collection, destroying his investor funding.",
                "dialogue": [
                    ("The deleted video showed your embroidered sleeve.", "I was reaching for a lime wedge near the bar! I never touched her glass!"),
                    ("Were you aware of her peanut allergy?", "Everyone in the fashion circle knew she was deathly allergic to nuts."),
                    ("Why was your syringe in the washroom dustbin?", "What syringe? I'm diabetic, I use insulin needles! That doesn't make me a killer!")
                ]
            },
            {
                "id": "S3",
                "name": "Sameer Joshi",
                "role": "Zoya's Ex-Boyfriend & Content Manager",
                "alibi": "Editing video reels in the rooftop lounge corner.",
                "motive": "Zoya fired him this afternoon and threatened him with legal action over stolen ad revenue.",
                "dialogue": [
                    ("You had access to her purse and EpiPen.", "I carried her purse for two years. Why would I kill the person who paid my bills?"),
                    ("Did you see Veer near her tumbler?", "Veer was hovering around the drink station all night whispering with Natasha."),
                    ("Did you know Natasha logged into Zoya's phone?", "Natasha was obsessively checking Zoya's engagement metrics every five minutes.")
                ]
            },
            {
                "id": "S4",
                "name": "Kavita Rao",
                "role": "Rooftop Party Host",
                "alibi": "Greeting VIP guests at the terrace entrance elevator.",
                "motive": "Zoya refused to promote Kavita's new club after demanding high appearance fees.",
                "dialogue": [
                    ("Who prepared Zoya's drink?", "Our mixologist prepared her signature passionfruit cocktail; no nuts were in the bar recipe."),
                    ("Did you see anyone tamper with it?", "I saw Veer lean over the tumbler when the DJ turned down the lights for the midnight countdown."),
                    ("Did Zoya ask for help?", "She clutched her throat, reached into her purse, and then collapsed onto the pool deck.")
                ]
            }
        ],
        "timeline": [
            ("01:30 AM", "Zoya places her clutch bag on the VIP lounge sofa."),
            ("01:45 AM", "Her EpiPen is swapped with a saline-filled counterfeit in the washroom."),
            ("02:15 AM", "Peanut extract concentrate is stirred into her tumbler at the bar."),
            ("02:26 AM", "Zoya posts the candid story noticing the suspicious figure behind the bar."),
            ("02:30 AM", "Zoya sips the drink and suffers acute anaphylaxis; injector fails."),
            ("02:34 AM", "Natasha deletes the incriminating story using her cached session.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Natasha Roy",
        "hints": [
            "HINT 1: Look at who had everything to gain financially from Zoya's permanent absence.",
            "HINT 2: The killer knew Zoya's password and purged the visual evidence within four minutes of the attack.",
            "HINT 3: Natasha swapped the EpiPen beforehand to ensure any accidental exposure would prove fatal, securing her the ₹2.5 Crore contract."
        ],
        "solution_summary": (
            "Natasha Roy coveted Zoya's career and cosmetics contract. Knowing Zoya's deadly peanut allergy, Natasha swapped her EpiPen with "
            "sterile saline earlier in the week, slipped nut syrup into her tumbler during the party, and immediately deleted the candid "
            "video post from her phone when she realized Zoya had inadvertently captured the setup."
        )
    },
    {
        "id": "CASE-007",
        "title": "The Highland Loch Mystery",
        "location": "Inverness, Scotland",
        "time": "06:30 AM",
        "category": "International Mystery",
        "difficulty": "Moderate",
        "victim": "Alastair MacLeod (63, Scottish Whisky Baron)",
        "cause_of_death": "Drowning preceded by blunt head trauma",
        "synopsis": (
            "The body of distillery patriarch Alastair MacLeod was discovered floating in the icy shallows "
            "of Loch Ness near his estate pier. His antique brass rowboat was drifting 300 yards offshore with one oar missing."
        ),
        "scene_details": [
            "Chilly mist hanging over the dark peat-stained loch water.",
            "Stone pier stained with fresh scuff marks from heavy rubber boots.",
            "Alastair's tweed jacket recovered from the water; wallet and heirloom signet ring untouched.",
            "The missing heavy wooden ash oar found submerged beneath the pier pilings."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Submerged Ash Oar",
                "desc": "Heavy boat oar with blood and skin tissue dried into the grain before immersion.",
                "details": "Splinters match cranial fracture fragments removed from Alastair's skull."
            },
            {
                "id": "E-02",
                "name": "Distillery Succession Will",
                "desc": "Executed 48 hours prior, disinheriting son Callum in favor of the Highland Heritage Trust.",
                "details": "Lawyer confirmed Callum had not yet been formally notified of the change."
            },
            {
                "id": "E-03",
                "name": "Pair of Hunter Wellies (Size 10)",
                "desc": "Found wet in the distillery boiler house with traces of shoreline peat moss.",
                "details": "Belonging to master distiller Hamish Campbell."
            },
            {
                "id": "E-04",
                "name": "Cell Phone Recording",
                "desc": "Recovered from Alastair's waterproof phone pouch; audio records a violent argument at 05:45 AM.",
                "details": "A voice threatens: 'If you sell the single malt reserve to the American conglomerate, you won't leave this loch alive.'"
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Callum MacLeod",
                "role": "Alastair's Prodigal Son",
                "alibi": "Sleeping off heavy drinking at the local village pub inn.",
                "motive": "Massive gambling debts across Edinburgh bookmakers.",
                "dialogue": [
                    ("Were you at the estate pier this morning?", "I was passed out at the Black Dog Inn until the village constable knocked on my door."),
                    ("Did you know about the revised will?", "What revised will?! My father wouldn't dare give our family heritage to a bloody trust!"),
                    ("Did you argue with your father yesterday?", "We argued every day. But I didn't smash his head with an oar.")
                ]
            },
            {
                "id": "S2",
                "name": "Hamish Campbell",
                "role": "Master Distiller (35 years of service)",
                "alibi": "Tending the mash tuns in the copper stillhouse since 5:00 AM.",
                "motive": "Alastair planned to shut down the traditional distillery and sell the brand to a corporate conglomerate.",
                "dialogue": [
                    ("Your muddy boots were hidden in the boiler room.", "I walk the loch trail every dawn to inspect the water intake pipes!"),
                    ("That voice on the audio recording matches your brogue.", "I told him the truth! Selling our heritage to Americans was suicide. That doesn't make me a killer!"),
                    ("Why was the oar hidden under the pier?", "How the devil would I know where the oars were?")
                ]
            },
            {
                "id": "S3",
                "name": "Fiona Craig",
                "role": "Distillery Operations Manager",
                "alibi": "Reviewing export manifests in the office.",
                "motive": "Embezzled £400,000 through fraudulent cask storage fees.",
                "dialogue": [
                    ("Did you see Alastair take the boat out?", "He went out every morning at 5:30 to clear his thoughts on the water."),
                    ("Did you hear any shouts from the loch?", "The wind was howling from the north. You couldn't hear anything over the waves."),
                    ("Were you aware of the American buyout?", "Yes. It would have triggered a full external forensic audit of our cask reserves.")
                ]
            },
            {
                "id": "S4",
                "name": "Dr. Ian Boyd",
                "role": "Local Estate Physician",
                "alibi": "Attending an emergency delivery at the cottage hospital.",
                "motive": "Long-standing rivalry over ancestral highland land deeds.",
                "dialogue": [
                    ("What caused Alastair's death?", "He was struck hard with a blunt wooden instrument, knocking him unconscious into the water."),
                    ("Could he have hit his head on the gunwale?", "The impact angle is from above and behind—impossible from an accidental tumble."),
                    ("Who saw him last alive?", "Hamish was seen storming down towards the boathouse at 5:35 AM.")
                ]
            }
        ],
        "timeline": [
            ("05:30 AM", "Alastair walks to the boathouse to ready his rowboat."),
            ("05:38 AM", "Hamish Campbell confronts Alastair over the corporate sale on the pier."),
            ("05:45 AM", "Argument escalates; audio recording captures death threat."),
            ("05:50 AM", "Alastair struck from behind with the ash oar and pushed into the water."),
            ("06:00 AM", "Boat pushed adrift into the loch; oar wedged under pilings."),
            ("06:30 AM", "Body sighted by local fishing charter.")
        ],
        "murderer_id": "S2",
        "murderer_name": "Hamish Campbell",
        "hints": [
            "HINT 1: Listen closely to the exact words uttered on the phone recording regarding the American buyout.",
            "HINT 2: The boots with fresh loch mud were found in Hamish's immediate boiler house domain.",
            "HINT 3: Hamish's alibi of being at the mash tuns was disproven by the physician who saw him heading to the boathouse at 5:35 AM."
        ],
        "solution_summary": (
            "Hamish Campbell dedicated 35 years to the craft distillery and could not bear Alastair selling out to an American corporate firm. "
            "He confronted Alastair on the pier, lost control in an outburst of rage, struck the baron with an oar, pushed him into the freezing loch, "
            "and shoved the boat into the current to simulate an accidental fall."
        )
    },
    {
        "id": "CASE-008",
        "title": "The Crimson Canvas",
        "location": "Kala Ghoda, Mumbai",
        "time": "08:45 PM",
        "category": "Indian Mystery",
        "difficulty": "Moderate",
        "victim": "Madhur Sen (58, Renowned Modernist Painter)",
        "cause_of_death": "Ingestion of potassium cyanide dissolved in red cadmium paint",
        "synopsis": (
            "Madhur Sen was found dead in front of his final masterpiece on the eve of his retrospective gallery opening. "
            "His paintbrush was still in his hand, and streaks of toxic cadmium crimson were smeared across his lips."
        ),
        "scene_details": [
            "Studio smelling strongly of linseed oil, turpentine, and faint bitter almonds.",
            "Massive canvas displaying an abstract crimson vortex.",
            "A cup of black coffee sitting next to the paint palette.",
            "A torn piece of canvas in the dustbin showing an earlier signature in graphite."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Jar of Crimson Pigment",
                "desc": "Artisan pigment imported from Germany, heavily laced with potassium cyanide powder.",
                "details": "Madhur had a well-known eccentric habit of wetting the tip of his sable brushes with his tongue."
            },
            {
                "id": "E-02",
                "name": "Gallery Consignment Agreement",
                "desc": "Signed contract showing gallery curator Sunita Bhowmick had mortgaged the gallery to finance this show.",
                "details": "If the show was canceled or deemed counterfeit, the gallery faced immediate bankruptcy."
            },
            {
                "id": "E-03",
                "name": "Ghost-Painter Invoices",
                "desc": "Bank statements proving Sen paid young student painter Nikhil Roy ₹25,000 monthly for 'background work'.",
                "details": "Nikhil claimed he painted 90% of Sen's acclaimed canvases over the last four years."
            },
            {
                "id": "E-04",
                "name": "Laboratory Grade Cyanide Bottle",
                "desc": "Discovered in the chemical locker of the adjacent art preservation studio.",
                "details": "The preservation locker keys were issued exclusively to Sunita Bhowmick."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Nikhil Roy",
                "role": "Art Prodigy & Studio Apprentice",
                "alibi": "Stretching canvases in the lower workshop.",
                "motive": "Madhur refused to give him co-credit and threatened to blacklist him from the art fraternity.",
                "dialogue": [
                    ("Did you paint the final canvas?", "Madhur couldn't even steady his hands anymore! I created that painting from scratch!"),
                    ("Did you know he licked his brushes?", "Everyone who studied under him knew that filthy habit."),
                    ("Where were you at 8:30 PM?", "I went out to get tea from the corner stall.")
                ]
            },
            {
                "id": "S2",
                "name": "Sunita Bhowmick",
                "role": "Art Gallery Owner",
                "alibi": "Greeting art critics in the front reception foyer.",
                "motive": "Discovered Madhur had signed an exclusive contract with a rival London gallery.",
                "dialogue": [
                    ("The cyanide came from your restoration chemical cabinet.", "Anyone in the building could pick the lock on that wooden cabinet!"),
                    ("Did you enter his private studio tonight?", "I brought him his black coffee at 8:15 PM and told him the critics were arriving."),
                    ("Were you aware he was signing with London?", "Madhur would never abandon the gallery that made him famous!")
                ]
            },
            {
                "id": "S3",
                "name": "Rekha Sen",
                "role": "Victim's Estranged Daughter",
                "alibi": "Sitting at a café across Rampart Row.",
                "motive": "Excluded from Madhur's will; he pledged his entire art collection to a museum trust.",
                "dialogue": [
                    ("Why were you outside the studio tonight?", "I came to confront him one last time to fund my mother's medical care."),
                    ("Did he let you inside?", "He slammed the door in my face at 8:00 PM and told me to get a job."),
                    ("Did you see anyone enter after you?", "I saw Nikhil running up the back staircase with a small paper packet.")
                ]
            },
            {
                "id": "S4",
                "name": "Farhan Qureshi",
                "role": "Art Critic & Historian",
                "alibi": "Interviewing guests near the main exhibition hall.",
                "motive": "Madhur had threatened to expose Farhan's blackmailing of young debutante artists.",
                "dialogue": [
                    ("What do you think of Sen's final work?", "It was derivative. You could tell his masterly touch was completely missing."),
                    ("Did you know he had a ghost-painter?", "The entire art market whispered about it, but no one dared print it."),
                    ("Did you go into his studio?", "I stayed in the cocktail hall surrounded by fifty patrons.")
                ]
            }
        ],
        "timeline": [
            ("07:45 PM", "Madhur enters his studio to apply the final strokes to the crimson canvas."),
            ("08:00 PM", "Confrontation with Rekha at the studio door; Rekha is turned away."),
            ("08:15 PM", "Sunita delivers black coffee; Madhur brushes her off."),
            ("08:25 PM", "Someone sprinkles potassium cyanide directly into the wet red pigment jar."),
            ("08:40 PM", "Madhur dips his brush, licks the tip to sharpen the bristles, and ingests the poison."),
            ("08:45 PM", "Madhur collapses dead; brush clatters to the floor.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Nikhil Roy",
        "hints": [
            "HINT 1: The killer knew Madhur's specific, personal habit of licking his sable paintbrush tips to form a fine point.",
            "HINT 2: The apprentice was desperate to expose that he was the real author of the masterpiece before it was credited to Madhur.",
            "HINT 3: Witness testimony spotted Nikhil heading up the back stairwell with a packet minutes before the pigment was adulterated."
        ],
        "solution_summary": (
            "Nikhil Roy had painted the entire retrospective, only for Madhur to take all the accolades and threaten to ruin his future career. "
            "Exploiting his intimate knowledge of Madhur's habit of licking paintbrush tips, Nikhil laced the red pigment jar with cyanide, "
            "knowing Madhur would ingest it while applying the finishing touches."
        )
    },
    {
        "id": "CASE-009",
        "title": "The Kyoto Tea Pavilion",
        "location": "Gion District, Kyoto, Japan",
        "time": "05:10 PM",
        "category": "International Mystery",
        "difficulty": "Challenging",
        "victim": "Master Kenjiro Sato (71, Grand Tea Master)",
        "cause_of_death": "Aconite (monkshood) neurotoxicity",
        "synopsis": (
            "During an ultra-formal traditional tea ceremony inside a historic wooden teahouse, Grand Master Sato collapsed "
            "after whisking and drinking the ceremonial koicha (thick green tea). The three distinguished guests present were seated across from him."
        ),
        "scene_details": [
            "Pristine tatami mats with sliding shoji paper screens overlooking a tranquil zen garden.",
            "Black raku ceramic tea bowl containing remnants of dark matcha foam.",
            "Traditional bamboo whisk (chasen) and bamboo scoop (chashaku) placed neatly on the hearth.",
            "No one entered or exited the small 4.5-mat teahouse during the ritual."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Bamboo Whisk (Chasen)",
                "desc": "Delicate bamboo bristles treated with an oily herbal residue containing aconitine.",
                "details": "Aconite extracted from wild monkshood grows plentifully in the northern Kyoto hills."
            },
            {
                "id": "E-02",
                "name": "Raku Tea Bowl (Black)",
                "desc": "Centuries-old family heirloom; internal ceramic glaze is completely inert.",
                "details": "The tea powder in the lacquer caddy was tested and found completely pure."
            },
            {
                "id": "E-03",
                "name": "School Lineage Scroll",
                "desc": "Antique calligraphy naming the successor to the Sato Tea School.",
                "details": "Master Sato had announced he would bypass his senior pupil Yuto Tanaka in favor of younger prodigy Haruto Mori."
            },
            {
                "id": "E-04",
                "name": "Silk Furoshiki Cloth",
                "desc": "Used to transport the bamboo utensils; belonging to Yuto Tanaka.",
                "details": "Traces of crushed aconite root fibers discovered woven into the silk hem."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Yuto Tanaka",
                "role": "Senior Disciple (30 years under Sato)",
                "alibi": "Seated as first guest on the tatami mat.",
                "motive": "Infuriated by being passed over as school successor in favor of a 22-year-old.",
                "dialogue": [
                    ("You brought the bamboo whisk to the ceremony.", "As senior disciple, it was my sacred duty to prepare the master's utensils!"),
                    ("Why was aconite residue on the whisk bristles?", "I cleaned it with pure mountain spring water this morning! Someone must have tampered with it!"),
                    ("Did you know the Master was going to announce Haruto?", "A master's decision is absolute... even if it was made in senility.")
                ]
            },
            {
                "id": "S2",
                "name": "Haruto Mori",
                "role": "Young Prodigy Disciple",
                "alibi": "Seated as second guest observing the whisking.",
                "motive": "Impatient to take control and modernize the school with corporate sponsorship.",
                "dialogue": [
                    ("Did you touch any utensils?", "Guests are strictly forbidden from touching the master's hearth tools until after the tea is received."),
                    ("Were you expecting to be named successor today?", "Sensei hinted at it, but the formal scroll was to be unsealed at dusk."),
                    ("Did you see Yuto touch the whisk before the ceremony?", "Yuto was alone in the prep alcove for twenty minutes before we entered.")
                ]
            },
            {
                "id": "S3",
                "name": "Meiko Sato",
                "role": "Grand Master's Daughter-in-Law",
                "alibi": "Tending the garden lantern outside the shoji screen.",
                "motive": "Massive financial debt tied to the maintenance of the ancient wooden estate.",
                "dialogue": [
                    ("Did you prepare the boiling kettle water?", "Yes, the water came from our deep well. We all drank it in plain water cups beforehand."),
                    ("Did you see anyone in the tea garden earlier?", "Yuto was walking near the north bamboo grove where wild monkshood grows."),
                    ("Did Master Kenjiro suffer from any illnesses?", "His heart was strong. He had the vitality of a man twenty years younger.")
                ]
            },
            {
                "id": "S4",
                "name": "Kazuo Endo",
                "role": "Antiques Collector & Patron",
                "alibi": "Seated as third guest in the pavilion.",
                "motive": "Master Sato refused to sell the legendary Black Raku bowl to Endo's museum.",
                "dialogue": [
                    ("Did you observe anything unusual during the whisking?", "The Master paused momentarily when smelling the tea foam, then drank out of respect for ritual."),
                    ("Did you handle any teaware?", "Only the bowl after it had been offered, but the Master had already collapsed by then."),
                    ("Do you have access to aconite?", "I collect porcelain, not poisonous flora.")
                ]
            }
        ],
        "timeline": [
            ("04:30 PM", "Yuto prepares the ceremonial utensils alone in the mizuya (prep alcove)."),
            ("04:45 PM", "Guests enter the teahouse through the low sliding door."),
            ("05:00 PM", "Master Sato begins the sacred preparation; scoops matcha into the raku bowl."),
            ("05:05 PM", "Sato uses the contaminated bamboo whisk; poison dissolves into the warm froth."),
            ("05:08 PM", "Sato consumes the tea as ritual prescribes; sudden paralysis sets in."),
            ("05:10 PM", "Grand Master collapses onto the hearthstones.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Yuto Tanaka",
        "hints": [
            "HINT 1: The poison was not in the tea powder or water, but on the bristles of the bamboo whisk.",
            "HINT 2: Only one person had sole, unmonitored custody of the utensils in the prep alcove before the ceremony.",
            "HINT 3: Crushed aconite root fibers were found in Yuto's personal silk wrapping cloth."
        ],
        "solution_summary": (
            "Yuto Tanaka spent thirty years subservient to Grand Master Sato, only to learn he would be passed over for a young upstart. "
            "He coated the inner bamboo bristles of the tea whisk with aconite concentrate in the prep room. The warm water dissolved "
            "the lethal neurotoxin straight into the foam, ensuring the Master would drink it during the ritual."
        )
    },
    {
        "id": "CASE-010",
        "title": "Close Friends Only",
        "location": "Indiranagar, Bengaluru",
        "time": "01:20 AM",
        "category": "Modern / Gen-Z Mystery",
        "difficulty": "Moderate",
        "victim": "Aarav Kapoor (24, Crypto Trader & Podcaster)",
        "cause_of_death": "Carbon monoxide inhalation inside private sauna",
        "synopsis": (
            "Aarav Kapoor was found dead inside the custom infrared and wood-fired cedar sauna of his rented villa. "
            "The external wooden latch of the sauna door had been wedged shut with a graphite tennis racket, "
            "and the ventilation damper was locked from the outside."
        ),
        "scene_details": [
            "Luxury cedar wood sauna room filled with thick, suffocating soot and fumes.",
            "A high-end Babolat graphite tennis racket jammed tightly between the door handle and the wall bracket.",
            "Victim's phone on the patio table outside displaying a 5-member 'Close Friends' story.",
            "Charcoal briquettes drenched in kerosene were found stacked inside the electric sauna heating unit."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Babolat Tennis Racket",
                "desc": "Stenciled with custom initials 'K.S.' on the grip tape.",
                "details": "Used as an improvised wedge to bar the sauna door from outside."
            },
            {
                "id": "E-02",
                "name": "Villa Security DVR",
                "desc": "Power cable unplugged at 12:45 AM from the villa main hall breaker.",
                "details": "Circuit breaker panel had smudged fingerprints matching Kunal Shah."
            },
            {
                "id": "E-03",
                "name": "Close Friends Instagram Story",
                "desc": "Posted at 12:55 AM showing Aarav entering the sauna with caption: 'Clearing toxins after making 200 ETH.'",
                "details": "Only five accounts had access to this story: Kunal, Riya, Varun, Simran, and Aarav himself."
            },
            {
                "id": "E-04",
                "name": "Cold Storage Hardware Wallet",
                "desc": "A Ledger Nano X missing from Aarav's bedroom safe; recovered from Kunal Shah's duffel bag.",
                "details": "Contained private seed phrases controlling $1.2 Million in crypto assets."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Kunal Shah",
                "role": "Childhood Friend & Tennis Partner",
                "alibi": "Claims he drove to a 24/7 drive-thru in Koramangala.",
                "motive": "Lost his life savings in a meme coin token Aarav promoted and dumped.",
                "dialogue": [
                    ("Your tennis racket locked the sauna door.", "I left my racket in the patio hallway days ago! Anyone could pick it up!"),
                    ("Why was Aarav's Ledger wallet in your gym bag?", "He gave it to me for safekeeping! We were partners!"),
                    ("Why were your fingerprints on the breaker box?", "I tried to turn the outdoor pool lights back on when they flickered.")
                ]
            },
            {
                "id": "S2",
                "name": "Riya Sen",
                "role": "Aarav's Current Girlfriend",
                "alibi": "Asleep in the upstairs guest bedroom with air conditioning on.",
                "motive": "Discovered Aarav was cheating on her and had taken secret loans in her name.",
                "dialogue": [
                    ("Did you see the Close Friends story?", "I saw it when I woke up around 2 AM. Aarav loved showing off his sauna."),
                    ("Did you hear banging on the sauna glass?", "The sauna is across the garden patio; the AC upstairs is very loud."),
                    ("Did Kunal leave the villa?", "I heard a car engine rev around 1 AM, but I didn't get up to look.")
                ]
            },
            {
                "id": "S3",
                "name": "Varun Singhal",
                "role": "Podcast Co-Host",
                "alibi": "Livestreaming on Twitch from his personal studio apartment.",
                "motive": "Aarav had signed a solo broadcast contract, kicking Varun off their top-charting show.",
                "dialogue": [
                    ("You had access to the Close Friends list.", "Everyone knows Aarav posted every bowel movement to his close friends."),
                    ("Were you at the villa tonight?", "Check my Twitch VOD! I was live streaming Minecraft from 11 PM to 2 AM!"),
                    ("Could the stream be pre-recorded?", "Twitch chat was responding to live comments in real-time.")
                ]
            },
            {
                "id": "S4",
                "name": "Simran Walia",
                "role": "Villa Landlord & Influencer",
                "alibi": "Attending a midnight yoga retreat in Whitefield.",
                "motive": "Aarav caused major structural damage to the rental and owed 6 months of unpaid rent.",
                "dialogue": [
                    ("Who installed the sauna door latch?", "The previous tenant installed an emergency bracket. It wasn't meant to have a lock."),
                    ("Did you speak to Aarav tonight?", "I texted him demanding our rent arrears. He left me on read as usual."),
                    ("Did you see Kunal's tennis racket?", "Kunal was swinging that racket on the lawn all afternoon.")
                ]
            }
        ],
        "timeline": [
            ("12:30 AM", "Kunal and Aarav drink beers on the villa patio."),
            ("12:45 AM", "Kunal disables the CCTV power at the circuit breaker."),
            ("12:55 AM", "Aarav posts his 'Close Friends' story and steps into the sauna."),
            ("01:05 AM", "Kunal jams his tennis racket into the door latch and shuts the chimney flue."),
            ("01:10 AM", "Kunal steals the Ledger crypto wallet from the upstairs bedroom safe."),
            ("01:20 AM", "Aarav succumbs to carbon monoxide asphyxiation.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Kunal Shah",
        "hints": [
            "HINT 1: The item used to jam the door had specific initials belonging to Aarav's childhood friend.",
            "HINT 2: The victim's stolen cold storage crypto wallet was recovered directly from Kunal's duffel bag.",
            "HINT 3: Kunal cut the security camera power breaker, leaving fresh fingerprint traces on the box."
        ],
        "solution_summary": (
            "Kunal Shah was ruined after Aarav dumped a fraudulent crypto token. Knowing Aarav's midnight sauna routine, "
            "Kunal cut the security cameras, loaded charcoal into the heater, trapped Aarav inside by wedging his Babolat tennis racket "
            "into the latch, and looted the cold-storage wallet containing $1.2M in crypto before attempting to leave."
        )
    },
    {
        "id": "CASE-011",
        "title": "The Swiss Chalet Avalanche",
        "location": "Zermatt, Switzerland",
        "time": "03:40 AM",
        "category": "International Mystery",
        "difficulty": "Hard",
        "victim": "Maximilian Vance (52, Hedge Fund Titan)",
        "cause_of_death": "Exsanguination via severed femoral artery",
        "synopsis": (
            "During a snowstorm that trapped four guests inside an ultra-luxury ski chalet in Zermatt, "
            "Maximilian Vance was found dead in the private wine cellar. A minor controlled avalanche had severed the road outside, "
            "guaranteeing the killer was one of the stranded occupants inside."
        ),
        "scene_details": [
            "Subterranean temperature-controlled cellar surrounded by rare Bordeaux vintages.",
            "A shattered 1945 Romanée-Conti bottle with dark red wine pooled with arterial blood.",
            "The victim's ski poles stood neatly in the ski room above.",
            "Snow boots drying on the heated rack; one pair still had damp cellar dust on the soles."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Shattered Heavy Wine Bottle",
                "desc": "Heavy glass magnum used to bludgeon the victim before a jagged shard severed the femoral artery.",
                "details": "The bottle neck retained bloody palm impressions belonging to a left-handed individual."
            },
            {
                "id": "E-02",
                "name": "Satellite Phone Call Log",
                "desc": "Chalet satellite phone logged an outgoing call at 02:15 AM to the Zurich police fraud division.",
                "details": "Maximilian was giving a formal statement exposing an international tax avoidance conspiracy."
            },
            {
                "id": "E-03",
                "name": "Torn Ski Glove (Left Hand)",
                "desc": "Found stuffed behind the cellar wine racks, soaked in blood with glass punctures.",
                "details": "Branded 'Bogner Ski Wear', customized with monogram 'E.W.' for Elena Weiss."
            },
            {
                "id": "E-04",
                "name": "Cellar Electronic Lock Audit",
                "desc": "The digital wine cellar lock recorded passkey 004 (issued to Elena Weiss) unlocking the door at 03:22 AM.",
                "details": "Elena is left-handed and was the fund's Chief Legal Officer."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Elena Weiss",
                "role": "Chief Legal Officer of Vance Capital",
                "alibi": "Claims she was asleep in the master guest suite after taking herbal tea.",
                "motive": "Maximilian's whistleblowing statement would send Elena to federal prison for thirty years.",
                "dialogue": [
                    ("Your keycard opened the wine cellar at 3:22 AM.", "I misplaced my keycard during dinner! Anyone could pick it up from the dining table!"),
                    ("You are left-handed and wear Bogner gloves.", "I lost one of my gloves on the ski slopes yesterday afternoon!"),
                    ("Did you know about the 2:15 AM police call?", "Maximilian had been talking crazy all weekend. I didn't know he actually called them.")
                ]
            },
            {
                "id": "S2",
                "name": "Gaston Mercier",
                "role": "Private Chalet Chef",
                "alibi": "Prepping breakfast pastries in the commercial kitchen.",
                "motive": "Vance was withholding Gaston's seasonal wages and threatened him with deportation.",
                "dialogue": [
                    ("Did you hear anything in the wine cellar?", "The kitchen ventilation fans run all night. You cannot hear footsteps downstairs."),
                    ("Were you in the wine cellar tonight?", "I retrieved two bottles of Riesling at 8 PM for dinner. I haven't been down since."),
                    ("Is Elena left-handed?", "Oui, she signs all documents with her left hand. I noticed it when she reviewed my contract.")
                ]
            },
            {
                "id": "S3",
                "name": "Bruno Vance",
                "role": "Maximilian's Younger Brother",
                "alibi": "Sitting by the great room fireplace reading a biography.",
                "motive": "Deeply in debt to Zurich loan sharks who demanded repayment by Monday.",
                "dialogue": [
                    ("Did you see anyone head to the cellar?", "I saw Elena walking towards the basement stairs around 3:15 AM wearing her ski pullover."),
                    ("Did you speak with Maximilian?", "We talked about our mother's trust fund at midnight. He seemed terrified."),
                    ("Are you left-handed?", "No, I am completely right-handed, as are all the Vance brothers.")
                ]
            },
            {
                "id": "S4",
                "name": "Dr. Sophie Bernard",
                "role": "Family Physician & Guest",
                "alibi": "Asleep in the east wing bedroom.",
                "motive": "Falsified medical records for Maximilian's offshore disability claims.",
                "dialogue": [
                    ("Could Maximilian have survived the wound?", "The femoral artery bleeds out in under three minutes without an immediate tourniquet."),
                    ("Did you hear the bottle smash?", "No, the floorboards are insulated against sound and sub-zero temperatures."),
                    ("Did Elena ask you for sedatives?", "Elena asked for migraine medicine around 1 AM, but she appeared completely lucid.")
                ]
            }
        ],
        "timeline": [
            ("02:15 AM", "Maximilian dials the Zurich police fraud bureau via satellite phone."),
            ("03:10 AM", "Elena discovers Maximilian has betrayed the firm's offshore conspiracy."),
            ("03:22 AM", "Elena uses passkey 004 to follow Maximilian into the wine cellar."),
            ("03:30 AM", "Heated argument; Elena strikes him with a vintage wine bottle; glass severs artery."),
            ("03:35 AM", "Elena stashes her torn left glove behind the wine racks and slips upstairs."),
            ("03:40 AM", "Maximilian expires; discovered at 06:00 AM by the chef.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Elena Weiss",
        "hints": [
            "HINT 1: The bloody palm prints on the weapon were conclusively from a left-handed assailant.",
            "HINT 2: The punctured ski glove discovered at the scene had the exact initials of the Chief Legal Officer.",
            "HINT 3: Her electronic passkey unlocked the cellar minutes before the estimated time of death, disproving her sleep alibi."
        ],
        "solution_summary": (
            "Elena Weiss faced criminal prosecution and financial destruction after Maximilian phoned Swiss fraud authorities. "
            "Using her passkey to corner him in the wine cellar, the left-handed attorney struck him with a heavy wine bottle. "
            "The jagged glass severed his femoral artery, after which she discarded her torn monogrammed glove behind the vintage racks."
        )
    },
    {
        "id": "CASE-012",
        "title": "The Metro Line 3 Ghost",
        "location": "BKC Underground Station, Mumbai",
        "time": "02:40 AM",
        "category": "Indian Mystery",
        "difficulty": "Moderate",
        "victim": "Sunil Kamble (44, Senior Metro Tunnel Engineer)",
        "cause_of_death": "High-pressure hydraulic nail gun trauma",
        "synopsis": (
            "Sunil Kamble was discovered dead inside an incomplete ventilation shaft 80 feet beneath the BKC station. "
            "A pneumatic construction nail gun had been discharged directly into his chest. The tunnel was restricted "
            "to certified safety personnel with biometric clearance."
        ),
        "scene_details": [
            "Damp subterranean concrete tunnel with yellow work lights humming overhead.",
            "Industrial pneumatic nail gun connected to a portable air compressor.",
            "Sunil's clipboard contained a handwritten note: 'Fault line bypass under Mithi river is forged.'",
            "A safety helmet with blood splatters on the clear visor."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Pneumatic Nail Gun",
                "desc": "Heavy-duty steel fastening tool capable of penetrating concrete.",
                "details": "Serial number assigned to subcontractor Rajiv Mhatre's engineering firm."
            },
            {
                "id": "E-02",
                "name": "Geological Survey Report",
                "desc": "Stamped 'DRAFT - REJECTED'. Proved tunnel sector 4 was structurally unstable.",
                "details": "Rajiv Mhatre had billed ₹18 Crores for reinforcement work that was never performed."
            },
            {
                "id": "E-03",
                "name": "Biometric Shaft Turnstile Log",
                "desc": "Shaft 12 turnstile logged Rajiv Mhatre entering at 02:18 AM and leaving at 02:50 AM.",
                "details": "Rajiv claimed he gave his biometric fingerprint silicone duplicate to an intern."
            },
            {
                "id": "E-04",
                "name": "Dust-Coated High-Vis Jacket",
                "desc": "Found in Rajiv's locker with concrete slurry and microscopic blood droplets.",
                "details": "DNA analysis confirmed the blood belonged to Sunil Kamble."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Rajiv Mhatre",
                "role": "Structural Subcontractor",
                "alibi": "Claims he was reviewing blueprints in his air-conditioned surface trailer.",
                "motive": "Facing immediate criminal fraud charges and contract blacklisting.",
                "dialogue": [
                    ("The nail gun belonged to your tool pool.", "Hundreds of laborers use my tools every single shift!"),
                    ("Your biometric ID logged you into Shaft 12 at 2:18 AM.", "My badge was copied! The turnstiles have been malfunctioning for weeks!"),
                    ("Why was Sunil's blood on your jacket?", "I must have brushed against the stretcher when the medics brought him up!")
                ]
            },
            {
                "id": "S2",
                "name": "Deepa Kulkarni",
                "role": "Chief Environmental Safety Inspector",
                "alibi": "Conducting water table salinity tests at the riverbank.",
                "motive": "Sunil threatened to expose that Deepa had accepted kickbacks to clear the tunnel.",
                "dialogue": [
                    ("Did you know the Mithi river fault was forged?", "Sunil was an alarmist. The rock integrity met all safety parameters."),
                    ("Did you enter Shaft 12 tonight?", "I have no reason to crawl through dusty ventilation shafts."),
                    ("Did you see Rajiv go underground?", "Yes, Rajiv took the work lift down around 2:15 AM looking furious.")
                ]
            },
            {
                "id": "S3",
                "name": "Mahesh Solanki",
                "role": "Tunnel Boring Machine Operator",
                "alibi": "Operating boring machine unit 3 on the northbound line.",
                "motive": "Blamed Sunil for an industrial accident that injured his brother last year.",
                "dialogue": [
                    ("Did you hear the nail gun discharge?", "The boring machine makes a 110-decibel roar. You couldn't hear an earthquake down here."),
                    ("Where was Rajiv when the shift ended?", "Rajiv rushed into the surface lift with his jacket zipped up to his chin."),
                    ("Did Sunil seem worried tonight?", "Sunil told me he was meeting Rajiv to make him sign the shutdown order.")
                ]
            },
            {
                "id": "S4",
                "name": "Vikram Shinde",
                "role": "Project Director",
                "alibi": "At an executive dinner in Bandra until 1 AM, then sleeping at home.",
                "motive": "Deadlines were delayed by eight months, costing his consortium millions daily.",
                "dialogue": [
                    ("Did you pressure Sunil to approve the report?", "I urged him to be realistic. We have international consortium commitments."),
                    ("Did you order Rajiv to handle it?", "I told Rajiv to resolve the technical disagreements with Sunil immediately."),
                    ("Who had access to Shaft 12?", "Only senior certified engineers: myself, Sunil, Deepa, and Rajiv.")
                ]
            }
        ],
        "timeline": [
            ("02:00 AM", "Sunil writes the audit memo refusing to authorize the fraudulent fault clearance."),
            ("02:18 AM", "Rajiv logs through the biometric turnstile into Shaft 12."),
            ("02:30 AM", "Heated confrontation in the unlit ventilation shaft."),
            ("02:38 AM", "Rajiv grabs the pneumatic nail gun and fires point-blank into Sunil's chest."),
            ("02:50 AM", "Rajiv logs out of the shaft and conceals his bloody jacket in his locker."),
            ("03:15 AM", "Maintenance shift discovers Sunil's body.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Rajiv Mhatre",
        "hints": [
            "HINT 1: Cross-reference the biometric turnstile access time with the tool serial assignment.",
            "HINT 2: The suspect claimed his jacket touched the stretcher, but the jacket was already locked inside his locker before paramedics were called.",
            "HINT 3: Deepa and Mahesh confirmed Rajiv went down to Shaft 12 specifically to confront Sunil over the shutdown memo."
        ],
        "solution_summary": (
            "Rajiv Mhatre had defrauded the metro project of ₹18 Crores by faking structural bedrock reinforcement. "
            "When Sunil Kamble refused to sign off on the fake survey, Rajiv descended into Shaft 12, took an industrial pneumatic nail gun, "
            "and killed Sunil to prevent the catastrophic fraud from reaching regulatory authorities."
        )
    },
    {
        "id": "CASE-013",
        "title": "The Old Bailey Barrister",
        "location": "Temple, London, UK",
        "time": "11:20 PM",
        "category": "International Mystery",
        "difficulty": "Moderate",
        "victim": "Sir Arthur Pendelton (67, Senior King's Counsel)",
        "cause_of_death": "Thallium sulfate poisoning administered via vintage snuff",
        "synopsis": (
            "Inside his private chambers in the Middle Temple, Sir Arthur Pendelton collapsed clutching his throat "
            "after a long cross-examination prep session. The silver snuffbox on his mahogany desk contained fine tobacco "
            "laced with colorless, odorless thallium sulfate."
        ),
        "scene_details": [
            "Dark wood-paneled chambers lined with antique English law volumes.",
            "An open silver snuffbox hallmarked 1892 with powdered tobacco spilled across judicial papers.",
            "A fire dying in the marble hearth.",
            "A newly rewritten will naming junior barrister Clara Vance as executor."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Antique Silver Snuffbox",
                "desc": "Traces of thallium sulfate mixed into the gourmet dark tobacco blend.",
                "details": "Thallium was purchased through an online agricultural supplier using an account linked to Oliver Reed."
            },
            {
                "id": "E-02",
                "name": "Chambers Ledger Book",
                "desc": "Sir Arthur had scheduled an ethics tribunal hearing to disbar Oliver Reed for tampering with jury lists.",
                "details": "The disciplinary petition was to be submitted to the Bar Council at 9 AM the next morning."
            },
            {
                "id": "E-03",
                "name": "Security CCTV - Fleet Street Gate",
                "desc": "Camera records Oliver Reed entering the Temple precinct at 10:45 PM carrying a leather folio.",
                "details": "Reed claimed he was in Greenwich all evening."
            },
            {
                "id": "E-04",
                "name": "Leather Folio with Residue",
                "desc": "Discovered in the boot of Reed's Jaguar with microscopic chemical traces of thallium.",
                "details": "Reed is an amateur pesticide collector with certified chemical handling permits."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Oliver Reed",
                "role": "Junior Partner Barrister",
                "alibi": "Claims he was dining in Greenwich with a solicitor until midnight.",
                "motive": "Facing immediate disbarment, public disgrace, and prison for witness bribing.",
                "dialogue": [
                    ("Fleet Street CCTV caught you entering at 10:45 PM.", "I dropped off court filings in the chambers letterbox. I never entered Sir Arthur's room!"),
                    ("Thallium residue was found inside your car.", "I maintain an allotment garden! Thallium derivatives are standard rodent controls!"),
                    ("Did you know Arthur was disbarring you tomorrow?", "Arthur was a vindictive old tyrant who hated seeing younger men succeed.")
                ]
            },
            {
                "id": "S2",
                "name": "Clara Vance",
                "role": "Pupil Barrister",
                "alibi": "Researching case law in the Middle Temple Library until 11 PM.",
                "motive": "Sir Arthur held absolute power over her tenancy approval.",
                "dialogue": [
                    ("Did you prepare his tea or snuff?", "Sir Arthur never allowed anyone to touch his grandfather's snuffbox."),
                    ("Did you see Oliver Reed tonight?", "Oliver was pacing in the courtyard around 10:50 PM looking agitated."),
                    ("Were you named in his will?", "He appointed me executor because he knew I was honest, not because I stood to inherit.")
                ]
            },
            {
                "id": "S3",
                "name": "Giles Thorne",
                "role": "Senior Chambers Clerk",
                "alibi": "Locking the outer courtyard gates and balancing clerk fees.",
                "motive": "Arthur discovered Thorne was skimming 15% off junior barristers' brief fees.",
                "dialogue": [
                    ("Who had keys to Arthur's chambers?", "Arthur, myself, and Oliver Reed, who had an emergency duplicate."),
                    ("Did Arthur take his snuff regularly?", "Every evening at 11 PM before reviewing his closing speeches."),
                    ("What did Oliver do when he arrived?", "He hurried upstairs claiming he had urgent disclosure documents for Arthur.")
                ]
            },
            {
                "id": "S4",
                "name": "Lady Eleanor Pendelton",
                "role": "Sir Arthur's Estranged Wife",
                "alibi": "At the Royal Opera House in Covent Garden.",
                "motive": "Protracted divorce settlement over ancestral country homes in Surrey.",
                "dialogue": [
                    ("Did you visit the chambers today?", "I have not stepped foot in that dreary crypt for seven months."),
                    ("Were you aware of Arthur's daily habits?", "Arthur's entire life was snuff, port, and cross-examinations."),
                    ("Who did Arthur fear?", "He despised Oliver Reed. He called him a charlatan in silk.")
                ]
            }
        ],
        "timeline": [
            ("10:30 PM", "Sir Arthur prepares his closing arguments for tomorrow's murder trial."),
            ("10:45 PM", "Oliver Reed enters Temple grounds via Fleet Street, caught on camera."),
            ("10:52 PM", "Reed enters Arthur's chambers under guise of delivering disclosure papers."),
            ("10:58 PM", "While Arthur steps to the adjoining lavatory, Reed laces the snuffbox with thallium."),
            ("11:15 PM", "Arthur returns, inhales his ceremonial pinch of snuff."),
            ("11:20 PM", "Acute respiratory failure and collapse; Arthur dies within minutes.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Oliver Reed",
        "hints": [
            "HINT 1: The CCTV timestamp conclusively disproves Reed's Greenwich dining alibi.",
            "HINT 2: The clerk verified that Reed went upstairs claiming to bring papers, knowing Arthur took snuff at 11 PM.",
            "HINT 3: Microscopic thallium traces were discovered in Reed's personal leather folio and vehicle boot."
        ],
        "solution_summary": (
            "Oliver Reed was about to be disbarred and prosecuted the next morning for bribing jurors. "
            "Leveraging his knowledge of Sir Arthur's strict 11 PM snuff habit, Reed used his chambers key to slip upstairs, "
            "adulterated the silver snuffbox with lethal thallium sulfate while Arthur stepped away, and fled back to his car."
        )
    },
    {
        "id": "CASE-014",
        "title": "The Goa Beach Shack Mystery",
        "location": "Anjuna Beach, Goa",
        "time": "04:15 AM",
        "category": "Indian Mystery",
        "difficulty": "Moderate",
        "victim": "Marcus Vance (38, International Trance DJ & Music Producer)",
        "cause_of_death": "Drowning preceded by blunt head trauma from a scuba cylinder",
        "synopsis": (
            "Marcus Vance was found floating face down in the low tide near an abandoned Anjuna beach shack. "
            "His custom gold Pioneer DJ headphones were still draped around his neck. An aluminum scuba cylinder "
            "with blood on the valve was discovered buried in the nearby sand dunes."
        ),
        "scene_details": [
            "Warm tropical breeze with crashing surf; shoreline littered with rave flyers.",
            "The buried scuba tank valve showed dried blood and gold flecks matching Marcus's headphone plating.",
            "Victim's pockets turned inside out; his passport was found half-burnt in a bonfire pit nearby.",
            "Motorcycle tire tracks (CEAT knobby tires) speeding away towards the Chapora road."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Aluminum Scuba Cylinder",
                "desc": "Marked with registration #GOA-DIV-88 belonging to 'Oceanic Ventures' dive school.",
                "details": "Dive school equipment rental logs show Neil Pinto checked out this tank at 6 PM yesterday."
            },
            {
                "id": "E-02",
                "name": "Laptop with Unreleased Tracks",
                "desc": "Marcus's hard drive containing his unreleased album was found in Neil Pinto's scooter storage.",
                "details": "Neil had already uploaded two tracks to a European distributor under his own stage name."
            },
            {
                "id": "E-03",
                "name": "Royal Enfield Himalayan Motorcycle",
                "desc": "Parked behind Neil's shack with knobby CEAT tires matching the dune tracks exactly.",
                "details": "Front mudguard bore microscopic sand containing bone fragments and sea salt."
            },
            {
                "id": "E-04",
                "name": "Blood-Splattered Beach Towel",
                "desc": "Found in the shack dumpster with blood type AB-positive (matching Marcus Vance).",
                "details": "Wrapped around a broken pair of sunglasses belonging to Neil Pinto."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Neil Pinto",
                "role": "Local DJ & Shack Co-Owner",
                "alibi": "Claims he was sleeping behind the bar counter after the party ended.",
                "motive": "Marcus stole his original beats and signed a multimillion-euro contract with an Amsterdam label.",
                "dialogue": [
                    ("Your scuba tank was the murder weapon.", "Someone stole that tank from my dive rack outside the shack!"),
                    ("Marcus's laptop was in your motorcycle boot.", "He asked me to back up his audio files! I didn't steal them!"),
                    ("Why were you riding across the dunes at 4 AM?", "I went to look for my stray dog on the beach.")
                ]
            },
            {
                "id": "S2",
                "name": "Chloe Bennett",
                "role": "Marcus's Tour Manager",
                "alibi": "In her hotel room at Vagator counting the gate ticket revenue.",
                "motive": "Marcus was firing her for skimming 20% off European ticket tours.",
                "dialogue": [
                    ("Did you see Marcus leave the DJ booth?", "He walked down to the beach with Neil around 3:30 AM to smoke a joint."),
                    ("Did you hear any fight?", "The sound of the ocean swells drowns out everything on that side of the rocks."),
                    ("Did you touch the scuba tank?", "I don't dive. I despise deep water.")
                ]
            },
            {
                "id": "S3",
                "name": "Rocco D'Souza",
                "role": "Nightclub Promoter & Bouncer",
                "alibi": "Clearing the dance floor and packing audio amps until 4:30 AM.",
                "motive": "Marcus refused to pay Rocco's security staff their agreed festival bonus.",
                "dialogue": [
                    ("Did you confront Marcus tonight?", "I asked him for our cash at 2 AM. He told me to talk to Chloe."),
                    ("Did you see Neil's motorcycle leave?", "Neil kicked his Royal Enfield into gear like a madman around 4:10 AM near the dunes."),
                    ("Did you see the scuba cylinder?", "Neil was showing off that new cylinder to tourists yesterday afternoon.")
                ]
            },
            {
                "id": "S4",
                "name": "Zoe Martins",
                "role": "Sound Engineer",
                "alibi": "Packing mixing consoles and coiled audio snakes.",
                "motive": "Romantic rejection; Marcus publicly humiliated her on social media.",
                "dialogue": [
                    ("Did Marcus have any enemies?", "Marcus treated every collaborator like disposable garbage."),
                    ("Where was Neil around 4 AM?", "Neil wasn't at the bar. His scooter was gone from the lot."),
                    ("Did Chloe leave her room?", "Chloe stayed at the front counter counting banknotes with the festival accountant.")
                ]
            }
        ],
        "timeline": [
            ("03:15 AM", "Marcus finishes his headline DJ set to massive applause."),
            ("03:30 AM", "Marcus and Neil walk to the dark rocks near the deserted beach shack."),
            ("03:50 AM", "Violent altercation over intellectual property and stolen music rights."),
            ("04:00 AM", "Neil strikes Marcus with the heavy scuba cylinder valve and rolls him into the surf."),
            ("04:10 AM", "Neil speeds away on his Royal Enfield, hiding the laptop in his seat boot."),
            ("04:15 AM", "Marcus drowns in the incoming tide; discovered at dawn.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Neil Pinto",
        "hints": [
            "HINT 1: The murder weapon was an aluminum scuba tank directly registered and rented by the shack owner.",
            "HINT 2: The victim's stolen laptop with unreleased masters was located inside Neil's personal motorcycle storage.",
            "HINT 3: Promoters spotted Neil fleeing on his motorcycle at 4:10 AM, matching the fresh tire tracks on the sand dunes."
        ],
        "solution_summary": (
            "Neil Pinto was consumed by bitter jealousy after Marcus Vance took his music productions and sold them as his own. "
            "Luring Marcus to the dark beach shack, Neil struck him in the head with his rented scuba cylinder, looted the laptop "
            "containing the unreleased master tracks, and left Marcus to drown in the rising tide."
        )
    },
    {
        "id": "CASE-015",
        "title": "The Last Seen at 04:04",
        "location": "Cyber City, Gurugram",
        "time": "04:15 AM",
        "category": "Modern / Tech Mystery",
        "difficulty": "Challenging",
        "victim": "Meera Tandon (29, Investigative Journalist)",
        "cause_of_death": "High-velocity vehicular impact (hit-and-run)",
        "synopsis": (
            "Meera Tandon was struck and killed by a speeding SUV while crossing an illuminated skywalk ramp in Cyber City. "
            "Her WhatsApp 'Last Seen' was recorded at 04:04 AM, sending a cloud link containing an investigative exposé on "
            "illegal pharmaceutical price-fixing syndicates."
        ),
        "scene_details": [
            "Rain-slicked asphalt near the Cyber City skywalk underpass.",
            "Shattered black automotive headlamp casing bearing OEM parts code 'HY-CRETA-22'.",
            "Meera's audio dictaphone crushed by tire treads; micro-SD card intact.",
            "Skid marks indicating acceleration rather than braking before the collision."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Micro-SD Card Audio File",
                "desc": "Dictaphone recording at 04:02 AM: 'Vikram Grover just threatened to run me down if I publish the test results.'",
                "details": "Audio forensics authenticated the background engine sound as a 1.5L turbocharged petrol engine."
            },
            {
                "id": "E-02",
                "name": "Damaged Black SUV in Basement 3",
                "desc": "A black Hyundai Creta parked in an unmonitored basement bay with a shattered left headlamp.",
                "details": "Registered to Grover Pharma Corp, assigned exclusively to Managing Director Vikram Grover."
            },
            {
                "id": "E-03",
                "name": "Toll Plaza Fastag Records",
                "desc": "Vikram Grover's Fastag bypassed the Kherki Daula toll booth at 04:32 AM at high speed.",
                "details": "Disproved Vikram's claim that his SUV was parked at his DLF Phase 5 villa all night."
            },
            {
                "id": "E-04",
                "name": "Fiber Analysis on Radiator Grille",
                "desc": "Synthetic wool fibers wedged into the cracked front grille match Meera's yellow overcoat.",
                "details": "Forensic lab detected Meera's DNA on the bumper paint fracture."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Vikram Grover",
                "role": "Pharma Managing Director",
                "alibi": "Claims he was home asleep; says his driver must have taken the car.",
                "motive": "Meera's exposé would result in his arrest for selling counterfeit cardiac medication.",
                "dialogue": [
                    ("Your SUV's headlamp was shattered at the scene.", "My chauffeur had an accident two days ago! It had nothing to do with tonight!"),
                    ("The audio dictaphone records your voice threatening her at 4:02 AM.", "I told her to stop harassing my family! I never threatened her life!"),
                    ("Your car's Fastag was scanned at 4:32 AM.", "Someone must have stolen my vehicle from my open driveway!")
                ]
            },
            {
                "id": "S2",
                "name": "Rajesh Chawla",
                "role": "Meera's Senior Editor",
                "alibi": "Working the dawn desk at the news office in Noida.",
                "motive": "Meera bypassed him and sent the scoop directly to an international wire syndicate.",
                "dialogue": [
                    ("Did you know Meera was in Cyber City at 4 AM?", "She called me saying she had obtained the lab audit documents from a whistleblower."),
                    ("Did you tell Vikram Grover about the exposé?", "I am a professional editor. I would never betray my own reporter."),
                    ("Where was Vikram's car parked?", "Vikram's office is three hundred meters from where Meera was struck.")
                ]
            },
            {
                "id": "S3",
                "name": "Inspector Ajay Rathore",
                "role": "Local Police Station Officer",
                "alibi": "On highway patrol duty near Shankar Chowk.",
                "motive": "On Vikram Grover's payroll to suppress municipal drug complaints.",
                "dialogue": [
                    ("Who reached the hit-and-run scene first?", "A taxi driver called our PCR van at 4:20 AM. She was already dead on the pavement."),
                    ("Did you inspect Grover's building basement?", "We didn't have a warrant to enter private corporate basements until the morning."),
                    ("Did you see a black SUV flee?", "Multiple dark vehicles were speeding down the highway to beat the morning truck restrictions.")
                ]
            },
            {
                "id": "S4",
                "name": "Pooja Kashyap",
                "role": "Whistleblower Pharmacist",
                "alibi": "Hiding in a transit hostel near the metro station.",
                "motive": "Terrified that Meera would reveal her identity in the published story.",
                "dialogue": [
                    ("Did you hand Meera the documents?", "I met her at 3:45 AM at the coffee kiosk and gave her the flash drive."),
                    ("Did anyone follow you?", "A black SUV was parked with its engine idling with tinted windows. It looked like Vikram's car."),
                    ("Did Meera see the car?", "Meera walked towards the skywalk while typing on her phone. She looked anxious.")
                ]
            }
        ],
        "timeline": [
            ("03:45 AM", "Meera receives the whistleblower flash drive near Cyber Hub."),
            ("04:02 AM", "Vikram calls Meera and screams death threats over her mobile phone."),
            ("04:04 AM", "Meera posts the cloud link to her editors; Last Seen status recorded."),
            ("04:08 AM", "Vikram Grover accelerates his SUV down the ramp, striking Meera at 70 km/h."),
            ("04:12 AM", "Grover conceals the damaged vehicle in Basement 3 before taking a company cab."),
            ("04:32 AM", "His personal Fastag is triggered on the toll expressway.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Vikram Grover",
        "hints": [
            "HINT 1: The broken headlamp plastic matches the specific OEM part code of Vikram's personal SUV.",
            "HINT 2: The victim's overcoat fibers and DNA were embedded directly into the radiator grille of Grover's vehicle.",
            "HINT 3: Grover's claim of being asleep was destroyed by the Fastag toll plaza scanner and the whistleblower's eyewitness account."
        ],
        "solution_summary": (
            "Vikram Grover knew the impending exposé on his counterfeit drug ring would trigger lifetime imprisonment. "
            "Tracking Meera to the Cyber City skywalk underpass, Grover weaponized his corporate SUV, accelerated into her as she "
            "sent the files, hid the damaged vehicle in the basement, and attempted to manufacture an alibi using his driver."
        )
    },
    {
        "id": "CASE-016",
        "title": "The Manhattan Penthouse Heist",
        "location": "Upper East Side, New York, USA",
        "time": "09:40 PM",
        "category": "International Mystery",
        "difficulty": "Hard",
        "victim": "Sterling Vance (61, Wall Street Diamond Magnate)",
        "cause_of_death": "Smothering via down pillow preceded by chloroform",
        "synopsis": (
            "Inside his ultra-secure triplex penthouse on 5th Avenue, Sterling Vance was discovered dead on his bed. "
            "His walk-in vault had been emptied of the 112-carat 'Star of Bengal' diamond. The state-of-the-art retinal "
            "scanner had opened the vault door at 09:25 PM without triggering any silent alarms."
        ),
        "scene_details": [
            "Luxurious penthouse overlooking Central Park; heavy silk curtains drawn shut.",
            "Traces of sweet chloroform vapors lingering around the bed pillows.",
            "The biometric laser safe stood wide open with velvet jewel displays cleared.",
            "A glass of 30-year single malt on the nightstand containing microscopic chemical residues."
        ],
        "evidence": [
            {
                "id": "E-01",
                "name": "Chloroform-Soaked Down Pillow",
                "desc": "Heavy goose feather pillow used to suffocate the unconscious magnate.",
                "details": "Chemical analysis identified industrial stabilizer hexylene glycol, traced to a lab supply order by Dr. Karen Croft."
            },
            {
                "id": "E-02",
                "name": "Retinal Scanner Access Log",
                "desc": "Vault unlocked at 09:25 PM using Sterling Vance's living eye pattern.",
                "details": "Medical examiner proved Sterling's eyes were forced open under chemical paralysis while he was still alive."
            },
            {
                "id": "E-03",
                "name": "Diamond Appraiser Loupe",
                "desc": "Left behind in the vault entryway engraved with the trademark of Croft Fine Jewels.",
                "details": "Belongs to Dr. Karen Croft, Sterling's private gemologist and mistress."
            },
            {
                "id": "E-04",
                "name": "Private Jet Flight Plan to Antwerp",
                "desc": "Filed at Teterboro Airport for a private Gulfstream departing at 11:30 PM tonight.",
                "details": "Passenger manifest lists Dr. Karen Croft traveling under an assumed passport."
            }
        ],
        "suspects": [
            {
                "id": "S1",
                "name": "Dr. Karen Croft",
                "role": "Private Gemologist & Appraiser",
                "alibi": "Claims she was grading diamonds in her Midtown laboratory.",
                "motive": "Massive financial debt and opportunity to steal the untraceable $40M Star of Bengal diamond.",
                "dialogue": [
                    ("Your engraved loupe was on the vault floor.", "I must have dropped it during our inventory review yesterday!"),
                    ("Why do you have a private jet booked to Antwerp tonight?", "I had international diamond conferences scheduled for weeks!"),
                    ("The retinal scanner required Sterling's living eye.", "Sterling was obsessed with that vault. He opened it every evening to admire his jewels!")
                ]
            },
            {
                "id": "S2",
                "name": "Julian Vance",
                "role": "Sterling's Disinherited Son",
                "alibi": "Drinking at a hotel lounge on 57th Street.",
                "motive": "Completely excluded from the will; desperately needed funds to pay offshore debts.",
                "dialogue": [
                    ("Did you visit your father tonight?", "The doorman wouldn't even let me past the lobby! He had strict orders!"),
                    ("Did you know the vault combination?", "The vault didn't use combinations. It used his own retinal scan. Only someone with him could open it."),
                    ("What did you think of Karen Croft?", "She was a vulture wrapping my father around her little finger.")
                ]
            },
            {
                "id": "S3",
                "name": "Raymond Cross",
                "role": "Head of Building Security",
                "alibi": "Monitoring the ground lobby CCTV bank.",
                "motive": "Fired earlier this week for taking bribes from paparazzi.",
                "dialogue": [
                    ("Did anyone use the private elevator to the triplex?", "Dr. Croft entered at 8:45 PM and took the express elevator straight to the penthouse."),
                    ("Did you see her leave?", "She walked out at 9:35 PM carrying a locked leather vanity case and wearing large sunglasses."),
                    ("Did any alarm trigger?", "Not a single sensor beeped. The penthouse remained completely green on my board.")
                ]
            },
            {
                "id": "S4",
                "name": "Marcus Stone",
                "role": "Sterling's Wealth Manager",
                "alibi": "Attending a charity gala at the Metropolitan Museum.",
                "motive": "Embezzled $12M from Vance trusts and needed the heist to cover his shortfall.",
                "dialogue": [
                    ("Did you know about the Antwerp trip?", "I knew Karen was urging Sterling to move the collection to Swiss vaults."),
                    ("Were you in contact with Sterling tonight?", "I texted him at 9 PM. He replied: 'Karen is here with the appraisal papers.'"),
                    ("Could anyone bypass the retinal scanner?", "Impossible. The manufacturer confirmed it requires real pupillary capillary blood flow.")
                ]
            }
        ],
        "timeline": [
            ("08:45 PM", "Dr. Karen Croft arrives via private penthouse elevator carrying appraisal tools."),
            ("09:05 PM", "Karen slips liquid chloroform into Sterling's vintage scotch."),
            ("09:20 PM", "Sterling is paralyzed; Karen drags him to the biometric safe and forces his eyelid open."),
            ("09:25 PM", "Retinal scanner accepts living eye; safe opens; Star of Bengal stolen."),
            ("09:30 PM", "Karen smothers the paralyzed magnate with the down pillow to prevent witness testimony."),
            ("09:35 PM", "Karen departs with the diamond in her vanity case heading towards Teterboro Airport.")
        ],
        "murderer_id": "S1",
        "murderer_name": "Dr. Karen Croft",
        "hints": [
            "HINT 1: The vault could only open using living retinal capillaries, proving Sterling was alive when the killer opened it.",
            "HINT 2: The chemical stabilizer in the chloroform matched orders from Karen Croft's registered laboratory.",
            "HINT 3: Building security logs and the victim's final text verified Karen Croft was inside the penthouse during the exact window of the murder."
        ],
        "solution_summary": (
            "Dr. Karen Croft plotted the ultimate gem heist. She paralyzed Sterling Vance with stabilized chloroform, "
            "dragged him to the vault to force his eyelid open against the retinal scanner, looted the $40M Star of Bengal diamond, "
            "smothered him to death with the down pillow, and headed towards Teterboro Airport for a private flight to Antwerp."
        )
    }
]

def get_all_cases():
    return CASES

def get_case_by_id(case_id):
    for c in CASES:
        if c["id"] == case_id:
            return c
    return None