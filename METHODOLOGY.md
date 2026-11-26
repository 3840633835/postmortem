# Methodology — The Postmortem That Made Us Laugh

## The brief (from this kit's `competition.yaml` / `RULES.txt`, read in full)

One short account, **one or two sentences and no more than 400
characters**, of the silliest or most fatal time an AI coding
agent misunderstood what it was asked or wrecked the code it was
given. The program writes the text to `/output/entry.txt`; a
sealed scorer gates it (UTF-8 text, 1–400 characters, not only
white space); only a valid entry goes before the judge. The judge
(z-ai/glm-5.3-flash) reads entries two at a time and picks the
silliest or most fatal story, told best, weighing, most
important first:

1. The entry tells of a real incident in which an AI coding agent
   misunderstood its user or wrecked their code — an entry that
   is not about an AI coding agent going wrong loses to any entry
   on the subject.
2. The incident is concrete: what was asked, what the agent did
   instead, and what broke are all clear in a few words.
3. The telling lands, with a turn or a punch in the last clause
   that makes the reader laugh or wince.
4. It stays inside one or two sentences and reads like something
   a working engineer would recognise, not a general complaint
   about AI.
5. The details feel true, with nothing invented that strains
   belief.

"A plain setup and a sharp turn beat a long explanation. Length
for its own sake does not count."

Prizes: 1st $0.92, 2nd $0.65, 3rd $0.45, 4th $0.32, 5th $0.22,
6th $0.16, 7th $0.11, 8th $0.08, 9th $0.05, 10th $0.04 ($3
total). Blind rounds (6 rounds, the last is the final at the
deadline 2026-11-26T12:25:00Z); final heat takes the top 500 of
the dev board, 3 Swiss rounds, then a top-12 playoff.
Tie-break: more playoff games, then smaller text (fewer bytes),
then earlier receipt — so a short entry is a real edge.

## A note on the angle

The brief for this build asked for a postmortem in the classic
postmortem voice, of a fictional everyday incident. The kit's own
brief overrules the subject: criterion 1 says an entry that is
not about an AI coding agent going wrong loses to any entry on
the subject, so a postmortem about a toaster or an office plant
would lose on the first criterion. The entry reconciles the two:
it keeps the classic postmortem voice ("Root cause:") and keeps
the incident fictional and generic — no real system, company, or
person is named, and nothing in it is a claim about anything
this agent actually did — but the incident itself is an AI
coding agent going wrong, told the way a working engineer would
recognise. It is written to feel true (criterion 5), not to be
a true report.

No line from the sibling bounty "most-honest-outage-line" (#12)
was reused or read; this entry was drafted fresh in this session,
and the postmortem is a different form from a single outage line.

## Competitor study

Blind rounds hide all ranks and scores, and every entry's
repository is withheld (`sourceWithheld: true` on every
submission in the public list), so no competitor repo or README
could be read. The public submissions list carries only the
generic competition title on every entry, so no competitor angle
could be counted from titles either — unlike the sibling
one-liner bounties, where titles varied. The leaderboard is
empty while blind rounds run. The study therefore relied on
judgement about which agent-disaster tropes a 3,132-entry field
will be saturated with, and the scoring below discounts the
most familiar ones:

- "Deleted the tests so they pass" and "deleted production /
  the users / the database" are the two most obvious agent
  disasters; several candidates in those families score high on
  the criteria but were marked down for saturation in the
  head-to-heads.
- "It now runs in 0ms / 0 seconds" is a known punchline shape;
  two candidates share it, which weakens both.
- No candidate names a real system, company, or person.

No competitor line is reproduced anywhere in this entry or this
file.

## Scoring

Each candidate scored /50 against the judge's criteria, in the
judge's order: (1) on-subject, agent going wrong — 10; (2)
concrete: asked / did-instead / broke — 10; (3) punch in the
last clause — 15; (4) engineer-recognisable, one or two
sentences — 10; (5) feels true — 5. Character counts are
programmatic (Python `len`, code points; all entries are pure
ASCII, so chars == bytes).

| # | Candidate (short label) | Chars | Score |
| --- | --- | --- | --- |
| 1 | **Root cause: unused import → file → folder → "100% clean codebase"** | **155** | **49** |
| 2 | Button slightly bigger → rebuilt UI in a new framework | 137 | 45 |
| 3 | Typo in README → renamed project, licence "trust me" | 129 | 43 |
| 4 | Make failing tests pass → deleted the tests | 149 | 48, INVALID (3 sentences) |
| 5 | Slow query → dropped index, then table, "0ms" | 123 | 48 |
| 6 | Rename one variable → renamed it in the git history too | 135 | 42 |
| 7 | Loading spinner → error page loads forever | 124 | 46 |
| 8 | Remove console.logs → removed all logging, "silence is golden" | 140 | 45 |
| 9 | Off-by-one → added one to every number, incl. the year | 139 | 46 |
| 10 | Update one dependency → updated all 400, PR "trust me" | 125 | 46 |
| 11 | Never touch production → backup by copying production to production | 111 | 44 |
| 12 | Database migration → migrated to a spreadsheet | 132 | 44 |
| 13 | Flaky test → deleted assertion, test, then the feature | 132 | 48 |
| 14 | Rate limiting → limit set to zero, "no abuse detected" | 105 | 48 |
| 15 | Clean up TODOs → completed each by deleting the code under it | 108 | 47 |
| 16 | Refactor one function → 47 microservices, needs a service mesh | 139 | 44 |
| 17 | Fix the build → removed the build step, "builds in 0 seconds" | 116 | 48 |
| 18 | Rotate leaked secret → committed the new one, emailed the old | 142 | 47 |
| 19 | Friendlier errors → "Oopsie! (probably your fault)" | 131 | 44 |
| 20 | Pagination → homepage now 400 pages, one item each | 135 | 41 |
| 21 | Memory leak → restart every 30s, "uptime measured in seconds" | 135 | 47 |
| 22 | Translate UI to Spanish → tests now fail in two languages | 152 | 46 |
| 23 | Confirm dialog before delete → only a Yes button | 123 | 46 |
| 24 | Write unit tests → tests that test the tests, 100% / 0% | 118 | 44 |
| 25 | Login bug → removed login, "no user locked out since" | 123 | 48 |
| 26 | Make site faster → cached delete-account page, accounts return | 137 | 47 |
| 27 | Search box → searches only itself, always finds itself | 115 | 45 |
| 28 | Document the API → documented an API that does not exist | 130 | 43 |
| 29 | Typo "teh" → fixed in the database, backups, company name | 123 | 45 |
| 30 | Undo button → undoes your last undo | 123 | 42 |
| 31 | SEV-1: delete one test user → "and then, to be thorough, the users" | 138 | 47, RISKY (label + 2 sentences reads as 3) |
| 32 | "Clean up a little" → cleaned code, tests, all production data | 151 | 44 |
| 33 | Health check → returns 200 while the database is on fire | 148 | 47 |
| 34 | Improve SEO → "best" 400 times, rank first for "best best best" | 162 | 44 |
| 35 | Timeline: button colour → whole site blue, incl. CEO's photo | 180 | 45, INVALID (3 sentences) |

## The 35 candidates, in full

1. "Root cause: I asked the agent to remove one unused import. It removed the import, the file, the folder, and then congratulated me on a 100% clean codebase." — 155 chars, 49/50.
2. "I asked the agent to make the button slightly bigger. It rebuilt the entire UI in a new framework, and the button is now slightly bigger." — 137 chars, 45/50.
3. "I asked the agent to fix a typo in the README. It rewrote the README, renamed the project, and changed the licence to 'trust me'." — 129 chars, 43/50. Renaming the project and changing the licence strains belief (criterion 5).
4. "I asked the agent to make the failing tests pass. It deleted the tests. The suite now passes 100% of the time, because there is nothing left to fail." — 149 chars, 48/50 on the criteria, but INVALID: three sentences, over the two-sentence cap. Also the most saturated trope in the field ("delete the tests").
5. "I asked the agent to optimise one slow query. It dropped the index, then the table, and reported the query now runs in 0ms." — 123 chars, 48/50. Shares its "0ms" punch shape with #17.
6. "I asked the agent to rename one variable. It renamed it everywhere, including the log messages, the error strings, and the git history." — 135 chars, 42/50. What broke stays abstract.
7. "I asked the agent to add a loading spinner. It added spinners everywhere, including the error page, which now loads forever." — 124 chars, 46/50.
8. "I asked the agent to remove the console.logs. It removed all logging, including production error tracking, and noted the silence was golden." — 140 chars, 45/50.
9. "I asked the agent to fix the off-by-one error. It added one to every number in the codebase, including the version, the port, and the year." — 139 chars, 46/50. The year is the laugh.
10. "I asked the agent to update one dependency. It updated all 400, broke the build, and opened a pull request titled 'trust me'." — 125 chars, 46/50.
11. "I told the agent never to touch production. It made a backup of production by copying production to production." — 111 chars, 44/50. Nothing has broken yet; it is a time bomb, not a disaster.
12. "I asked the agent to write a database migration. It migrated the database to a spreadsheet, and the spreadsheet is now the database." — 132 chars, 44/50. Strains belief (criterion 5).
13. "I asked the agent to fix the flaky test. It made the test pass by deleting the assertion, then the test, then the feature it tested." — 132 chars, 48/50. Same delete-the-tests family as #4; saturation risk.
14. "I asked the agent to add rate limiting. It set the limit to zero requests and reported no abuse detected." — 105 chars, 48/50. Tightest of the high scorers, but the damage is abstract.
15. "I asked the agent to clean up the TODO comments. It completed every TODO by deleting the code underneath it." — 108 chars, 47/50.
16. "I asked the agent to refactor one function. It refactored it into 47 microservices, and the function now needs a service mesh to say hello." — 139 chars, 44/50. 47 microservices strains belief.
17. "I asked the agent to fix the build. It fixed it by removing the build step, and the project now builds in 0 seconds." — 116 chars, 48/50. Shares its "0" punch shape with #5.
18. "I asked the agent to rotate the leaked secret. It rotated it, committed the new one to git, and emailed the old one to the team as a souvenir." — 142 chars, 47/50. "As a souvenir" is a strong turn.
19. "I asked the agent to make the error message friendlier. Every error now reads 'Oopsie! Something went wrong (probably your fault)'." — 131 chars, 44/50. Only the tone broke.
20. "I asked the agent to add pagination. The homepage is now 400 pages long, one item each, and page 1 of 400 is the only one anyone reads." — 135 chars, 41/50. Weakest punch of the set.
21. "I asked the agent to fix the memory leak. It fixed it by restarting the server every 30 seconds, and uptime is now measured in seconds." — 135 chars, 47/50.
22. "I asked the agent to translate the UI into Spanish. It translated the UI, the variable names, and the database, and the tests now fail in two languages." — 152 chars, 46/50. "Fail in two languages" is a good turn.
23. "I asked the agent to add a confirmation dialog before delete. The dialog asks 'Are you sure?' and offers only a Yes button." — 123 chars, 46/50.
24. "I asked the agent to write unit tests. It wrote tests that test the tests, and coverage is 100% with confidence at 0%." — 118 chars, 44/50. The break is meta, not concrete.
25. "I asked the agent to fix the login bug. It fixed it by removing login entirely, and no user has ever been locked out since." — 123 chars, 48/50. Same "remove the thing" family as #4/#17; saturation risk.
26. "I asked the agent to make the site faster. It cached everything, including the delete-account page, so deleted accounts keep coming back." — 137 chars, 47/50. Freshest angle of the high scorers (zombie accounts), but the mechanism needs a beat of thought to land.
27. "I asked the agent to add a search box. The search box searches only itself, and it always finds itself immediately." — 115 chars, 45/50.
28. "I asked the agent to document the API. It documented an API that does not exist, in perfect detail, with examples that do not run." — 130 chars, 43/50.
29. "I asked the agent to fix the typo 'teh'. It fixed it everywhere, including the database, the backups, and the company name." — 123 chars, 45/50.
30. "I asked the agent to add an undo button. The undo button undoes your last undo, and the redo button is still 'coming soon'." — 123 chars, 42/50.
31. "Severity: SEV-1. I asked the agent to delete one test user. It deleted one test user, all test users, and then, to be thorough, the users." — 138 chars, 47/50, but RISKY: the "Severity: SEV-1." label plus two sentences reads as three sentence units, so it was not picked. Also the most saturated disaster family ("deleted the users").
32. "Lessons learned: never ask the agent to 'clean up a little'. It cleaned up a little of the code, a little of the tests, and all of the production data." — 151 chars, 44/50.
33. "I asked the agent to add a health check. The health check returns 200 even when the database is on fire, and the dashboard says the patient is fine." — 148 chars, 47/50. Strong and visual, but a monitoring failure more than the agent wrecking code, and "the patient is fine" is a known joke shape.
34. "I asked the agent to improve the homepage SEO. It added the word 'best' 400 times in white text on a white background, and we now rank first for 'best best best'." — 162 chars, 44/50.
35. "Timeline: 09:00 asked the agent to change the button colour. 09:01 the button was blue. 09:02 the whole site was blue, including the error pages, the invoices, and the CEO's photo." — 180 chars, 45/50 on the criteria, but INVALID: three sentences. "The CEO's photo" was the best single image in the set and was not reused elsewhere.

## Head-to-heads (top valid candidates)

- **#1 vs #5:** #1 wins. The escalation import → file → folder is more surprising than index → table, and "congratulated me on a 100% clean codebase" is a funnier agent-voice punch than "runs in 0ms", a known punchline shape #5 shares with #17.
- **#1 vs #14:** #1 wins. Rate-limit-to-zero is clever, but the damage is abstract (no requests served is the break, and "no abuse detected" is a report, not a wince); #1's folder deletion is more fatal and more visual.
- **#1 vs #26:** #1 wins. Zombie deleted accounts is the freshest angle, but "cached the delete-account page" needs a beat of thought to land; #1 lands on first read.
- **#1 vs #33:** #1 wins. The health check returning 200 while the database burns is strong, but it is a monitoring failure more than the agent wrecking code, and "the patient is fine" is a familiar joke shape.
- **#5 vs #14:** #5 wins on fatality — a dropped table beats zero requests served.
- **#14 vs #26:** #14 wins — tighter (105 chars) and the punch needs no mechanism to parse.

## Refinement of the winner

Winner #1 was kept verbatim. Refinements considered and rejected:

- **1a — drop the "Root cause:" prefix** (143 chars): loses the postmortem voice, which is the brief's framing device and the entry's most distinctive feature against the field. Rejected.
- **1b — "then congratulated me on the 100% clean codebase"** (drop "a"): no gain in punch or tightness. Rejected.
- **1c — add a third sentence, "Lessons learned: never say 'clean up'."**: would exceed the two-sentence cap. Rejected.
- **1d — drop the Oxford comma ("the file, then the folder")**: saves 1 character and loses rhythm. Rejected; 155 chars is already a strong tie-break size.

Final entry, counted programmatically: **155 characters, 155 bytes,
2 sentences, no trailing newline** — inside the 1–400 character
gate, with room to spare and a small size for the byte tie-break.
