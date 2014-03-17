"test-story" by "Louis Ades"

[Initializing some basic stuff]

The Testing Chamber is a room. "You find yourself in a room that takes on the appearance of a test chamber. All there is are two doors along the walls, and a small crate lying in the center of the room. On the southern wall, '1:00 AM' is painted to fill up nearly the whole wall. There is silence. Suddenly, you hear over a loudspeaker, 'Ah, another test subject! Welcome! You don't know who I am, but I know everything there is to know about you.' Perhaps we should keep it that way. You're objective is to get out of here and find me. How will you do that? Well, heheh, I can't tell you that. But maybe you shouldn't try to figure it out right now...maybe you should just sit down...and relax...and rest...heheheheh...oh, and just for your reference, it's currently midnight.' The voice cuts out. Suddenly, you hear the audible sounds of the air ventilation system speeding up outside of the room. A strange yellow-colored gas fills the room. After some time, you feel it fill your lungs, and you cough a bit. You are left alone in the room."

The time of day is 12:00 AM.

[The key to the game is realizing that you should perhaps listen and rest up. It's impossible to finish the game without taking moments to rest. Call it cheating--I call it following through with the rest of the game of, "Stop being paranoid, listen to any help offered, and think outside the box."]

Health is a number that varies. Health is 18.

The maximum score is 100.

Resting is an action applying to nothing. Understand "rest" as resting.
Check resting:
	Increase the time of day by 20 minutes;
	say "You rest for 20 minutes. The time of day is now [time of day]. [line break] [line break] The strange voice exclaims, 'Ah, so you've decided to take my advice...heheheh. But perhaps you should continue on your way? That illness of yours isn't waiting on you to kill you...or is it?'";

Every turn:
	Unless resting:
		Decrease health by 1;
		If health is 16:
			say "You begin to feel woozy, and your vision blurs for a second, but then you feel normal again.";
		if health is 14:
			say "Once again, the gas hasn't felt that impacting to your health, but your previous symptoms get stronger, and you start to sweat uncontrollably as hyperthermia takes over.";
		If health is 12:
			say "A stinging pain hits your throat, and you begin to cough violently.";
		If health is 8:
			say "Your stomach suddenly feels inflamed. This disease is catching up on you. You get sick and stumble to the floor. You pick yourself back up, but you begin to feel yourself weakening.";
		If health is 4:
			say "Your vision begins to blur, but this time it doesn't go away. You can still see ahead of you, but just barely. Your muscles weaken, and every further movement requires limping.";
		If health is 0:
			end the story saying "The pain is too much for you to handle. The poison has stretched to every part of your body, and you collapse to the ground. The voice in the loudspeakers says, calmly, 'Ah, that's a shame. I was really rooting for him. Oh well, onto the next test subject.'";

Material is a kind of value. The materials are metal, wood, and plastic. Everything has a material.

[All of this sets up the first room.]

A crate is a metal closed openable container.

There is a crate in the Testing Chamber.

The True Door is a locked door. The True Door is south of the Testing Chamber and north of the Winning Room.

The Challenge Door is a locked door.

The wooden Challenge Key unlocks the Challenge Door.

The wooden Challenge Key is in the crate.

The Challenge Door is east of the Testing Chamber and west of the First Riddle Room.

[The first riddle room is all set up here.]

Check1 is a number that varies. Check1 is 1.

Kinder Gardener is a person. Kinder Gardener is in the First Riddle Room.

The First Riddle Door is a locked door.

Box #1 is a closed metal openable container. Box #1 is in the First Riddle Room. Box #2 is a closed metal openable container. Box #2 is in the First Riddle Room. Box #3 is a closed metal openable container. Box #3 is in the First Riddle Room. Box #4 is a closed metal openable container. Box #4 is in the First Riddle Room. Box #5 is a closed metal openable container. Box #5 is in the First Riddle Room.

The First Riddle Key unlocks the First Riddle Door. The First Riddle Key is in Box #4.

Every turn:
	if Box #1 is open:
		end the story saying "As you open the crate, the strange voice says, 'I am truly disappointed in you. Perhaps the next test subject can do better.' Inside the box is a small bomb with a clown face labeled on it. It detonates as soon as the strange voice stops. You die instantly.";
	if Box #2 is open:
		end the story saying "As you open the crate, the strange voice says, 'I am truly disappointed in you. Perhaps the next test subject can do better.' Inside the box is a small bomb with a clown face labeled on it. It detonates as soon as the strange voice stops. You die instantly.";
	if Box #3 is open:
		end the story saying "As you open the crate, the strange voice says, 'I am truly disappointed in you. Perhaps the next test subject can do better.' Inside the box is a small bomb with a clown face labeled on it. It detonates as soon as the strange voice stops. You die instantly.";
	if Box #5 is open:
		end the story saying "As you open the crate, the strange voice says, 'I am truly disappointed in you. Perhaps the next test subject can do better.' Inside the box is a small bomb with a clown face labeled on it. It detonates as soon as the strange voice stops. You die instantly.";
	if Box #4 is open:
		Now Box #1 is locked;
		Now Box #2 is locked;
		Now Box #3 is locked;
		Now Box #5 is locked;
	if player is in the First Riddle Room: 
		if Check1 is 1:
			say "Once in the First Riddle Room, the strange voice says, 'Oh, I'm not sure if I'd like you to take on this challenge--you may hurt yourself, after all. But if you insist, you must know that each room contains a riddle that you'll need to solve. Solve it, and the door connecting to the next room will unlock. It's very possible that there is an end to this maze after, possibly, the seventh room. Will it lead you to safety? It looks like you'll have to find that out yourself. If it were up to me, I wish you'd just sit down...and rest...but regardless, try not to hurt yourself, heheheh.' The loudspeaker cuts out.";
			say "A man stands in the center of the room in a white button-down, khaki pants, and a large name tag with the name written, 'Kinder Gardener'. He says as you approach him, 'I really wish you wouldn't try this door, but if you insist, two plus two must equal...'. There are five closed boxes in front of him, each with a button on the top that opens it.";
			Increase score by 5;
			Now Check1 is 0;

The First Riddle Door is east of the First Riddle Room and west of the Second Riddle Room.

[The second riddle room. This requires thinking through the logical statements carefully and realizing that something doesn't add up, so finding that the right room is the room that neither of them go through involves thinking outside the box.]

Mindasa Gasho is a female person. Mindasa is in the Second Riddle Room. Wendy Gasho is a female person. Wendy is in the Second Riddle Room.

The Blue Door is a door. The Green Door is a door. The Red Door is a door.

The Blue Door is north of the Second Riddle Room and south of the First Wrong Room. The Green Door is east of the Second Riddle Room and west of the Second Wrong Room. The Red Door is south of the Second Riddle Room and north of the Room of Despair.

Check2 is a number that varies. Check2 is 1. Check3 is a number that varies. Check3 is 1.

Every turn:
	if player is in the Second Riddle Room: 
		if Check2 is 1:
			say "Two women stand side by side in the next room. To the north is a blue door, to the east is a green door, and to the south is a red door (the door you entered through is to the west). Both are dressed identically, in black button-down blouses, white sports jackets and white pants. The woman on the left has blond hair and wears a name tag that says, 'Mindasa'. The woman on the right has brown hair and wears a name tag that says, 'Wendy.' Other than these differences, both are nearly identical in every way. Both women say, perfectly in unison, 'Welcome to the second room! We're so ecstatic you made it through the first riddle! It was designed for kindergarteners, so we wouldn't expect any less from you! And don't worry, this one won't be nearly as deadly if you fail. Simply FOLLOW OUR INSTRUCTIONS EXACTLY to find out which door to enter through, and you will make it to the next room in this wondrous maze!'";
			say "[line break] Mindasa recites, in such monotony that she could be mistaken for an android, 'There is a zero percent chance that you'll want to follow me if your intention is to pass through to what will be the wrong room. But then again, I have been known to lie one hundred percent of the time.' Mindasa then turns her back towards you and walks towards the blue door to the north. She opens it, walks through, and closes it behind her.";
			Now Mindasa is in the First Wrong Room;
			say "[line break] Wendy recites, in an identical tone and voice, 'Mindasa is correct, and I will lead you to the right room room. One of these two things I just said is a lie, but this following statement is absolutely true: there is only one correct room.' Wendy then turns her back towards you and walks towards the green door to the east. She opens it, walks through, and closes it behind her.";
			Now Wendy is in the Second Wrong Room;
			Increase score by 5;
			Now Check2 is 0;
	if player is in the First Wrong Room:
		say "Mindasa says, in an almost gleeful tone, 'Oh! I'm sorry! It seems you guessed...wrong...' Suddenly her eyes glow red. Your eyes start to blur, and you begin to feel dizzy. You can overhear her continue as your vision fades, 'But, I'm feeling a bit merciful today! I won't kill you today! But try to return to the Second Riddle Room, and guess right this time!' You awaken moments later, back in your previous condition, in the Testing Chamber. Deja vu ensues as the voice on the loudspeaker repeats itself, yet you feel just as sick as before:";
		Now the player is in the Testing Chamber;
	if player is in the Second Wrong Room:
		say "Wendy says, in an almost gleeful tone, 'Oh! I'm sorry! It seems you guessed...wrong...' Suddenly her eyes glow red. Your eyes start to blur, and you begin to feel dizzy. You can overhear her continue as your vision fades, 'But, I'm feeling a bit merciful today! I won't kill you today! But try to return to the Second Riddle Room, and guess right this time!' You awaken moments later, back in your previous condition, in the Testing Chamber. Deja vu ensues as the voice on the loudspeaker repeats itself, yet you feel just as sick as before:";
		Now the player is in the Testing Chamber;
	if player is in the Room of Despair:
		if Check3 is 1:
			say "You overhear the creepy voice on the loudspeaker say, in his usual calm and overbearing voice, 'Congratulations. While your first test may have been straightforward, this one required you to think...outside the box. Now, why don't you take a break on this nice bed in front of you? I can't think of any harm in taking a rest in the Room of Despair, after all...heheheh.' The room is lighted to a very strange degree, giving off a creepy tone throughout the room. At the other end of the room is a white door.";
			Increase score by 5;
			Now Check3 is 0;
			Now the Blue Door is locked;
			Now the Green Door is locked;
			
[The following, and the previous check, helps set up the first state of the Room of Despair. The player will need to backtrack through here to move on.]

The bed is an object. The bed is in the Room of Despair.

The White Door is a door. The White Door is west of the Room of Despair and east of the Nightmare Room.

The Blood Door is a door. The Blood Door is west of the Nightmare Room and east of the Dead Room.

The Silver Staircase is a locked door. The Silver Staircase is south of the Room of Despair and north of the Yellow Room.

The Wooden Door is a door. The Wooden Door is south of the Yellow Room and north of the Dead End.

Check4 is a number that varies. Check4 is 1. Check5 is a number that varies. Check5 is 1.

[This is where the game moves a bit nonlinearly, by making you enter a room, and realize that the answer may not just be walking through it.]

Every turn:
	if player is in the Nightmare Room and Check4 is 1:
		Increase score by 5;
		say "As you enter the room, labeled by the White Door as the 'Nightmare Room,' the fluorescent lights in the room begin to dim, and then suddenly black out. The sound of air pressure filling the air vents begins to sound. You notice as you keep breathing, that there is something in the air of this room. You begin to trip, and stumble. Suddenly, images on the walls begin to shine out of the black. They are writing scribbled in what looks to be blood dripping down to the ground. The writings get filled in and become legible in front of your eyes...'KCABNRUT' is what is written, over and over again on these walls. The words begin to cascade, until all you can see are the walls completely painted in blood, and the words 'KCABNRUT' inscribed in gigantic letters, crooked and slanted as they line the ceiling, the only slate not left completely filled. [line break] [line break] Suddenly, two lights turn back on, one in front of a blood red door right in front of you, and another lighting up the white door right behind you.";
		Now Check4 is 0;
		Now the bed is in the Second Wrong Room;
		Now the Silver Staircase is unlocked;
	if player is in the Dead Room:
		end the story saying "As you jolt to the other end of the room and open the door there, you find no solace at the other end of the bloody door. A room so heavily concentrated in that same noxious gas you had just experienced awaits at the other end: the Dead Room. In small concentrations, it's a powerful hallucinogen. In higher concentrations, it drives the mind so mad to the point where the brain shuts down almost immediately. You collapse, dying instantly. The strange voice says, 'If only he had been better at following instructions. Perhaps the next test subject can do better.'";
	if the player is in the Room of Despair:
		if Check4 is 0:
			if Check5 is 1:
				say "As you desperately TURN BACK and as the walls instruct, you jolt right back to where you last left off, the Room of Despair. But something is different; the bed has disappeared, and you notice that the Silver Staircase is no longer locked.";
				Increase score by 5;
				Now Check5 is 0;
	if the player is in the Yellow Room:
		say "You walk up the silver staircase. You enter an empty, yellow room. Nothing is in the room except a plain wooden door at the other end, and the silver staircase you just walked up.";
	if the player is in the Dead End:
		say "You walk into the next room. There is nothing in it. There's a silver door at the other end, but it is locked. White fluorescent light fills the room, almost blinding compared to the much dimmer light in the yellow room. The strange voice comes back on-line. You can hear disgust in his tone as he says, 'Hmph, it seems you've reached the dead end. That's a shame--I had hoped you would be able to make it further. And for all the help I tried to *lend* you. Oh well--the next test subject should be here soon. You should be dead from your illness soon enough. Just don't leave a mess for the next subject.' The voice cuts out. There is a deadening silence in the room.";

The Silver Door is a locked door. The Silver Door is west of the Dead End and east of the Winning Room.

[Victory conditions]

FinalCheck is a number that varies. FinalCheck is 1.

Every turn:
	if the time of day is 1:00 AM or the time of day is after 1:00 AM:
		if FinalCheck is 1:
			Now the Silver Door is unlocked;
			Now the True Door is unlocked;
			Now health is 100;
			say "You hear gears turn. There is metal churning, string clinks and clanks to be heard. All debilitations your sickness has caused suddenly go away. The voice returns to the loudspeakers: 'Well done, sir! It seems that we have another test subject that has passed and not, well, dropped dead! Why don't you come meet me in the Winning Room? You'll find that both the Silver Door and the True Door are now opened for you.'";
			Now FinalCheck is 0;
	if player is in the Winning Room:
		Now score is 100;
		end the story saying "As you enter this mysterious final room, you see a man of great bulk in a black suit standing in the center of the room. He wears a big smile, and in both hands he holds two peculiar documents. 'Congratulations, young lad! Here's your diploma! Now walk out the exit behind me so you can get out there and tackle the real world!' Enraged that you just realized that this was meant to be a sadistic way of teaching you about thinking outside the box and following specific instructions no matter how peculiar they seem, yet powerless to do anything because you realize that you have no real sway over what just happened, you resign yourself and trudge out the back door. Congratulations, you just passed some arbitrary tests to prove your worth to a bunch of people who didn't care about you in the long run! Are you happy with yourself?";
	