"""One-Liner Marathon — one comedy line, max 280 characters, any subject.

ENTRY
    "My bank sent me a fraud alert for unusual activity. It was me buying
    vegetables. Even my bank knows that's not normal for me."
    (125 characters — verified by hand count below.)

DECISION RECORD — Pass 1: candidates weighed against the judge's likely
criteria (lands on first read, fresh angle, tight wording).

A. "I told my smart fridge I'm on a diet. It locked the ice cream,
   emailed my doctor, and now it judges me every time I open the door
   at 2 AM." (143)
   Relatable and visual, but the "judgmental smart appliance" shape is
   well worn, and the joke needs three beats to land. REJECTED.

B. "My phone's screen time report says I spent 6 hours on my phone
   today. I checked it on my phone, which added another hour, which it
   will report next week." (154)
   A neat self-referential loop, but it explains its own mechanism in
   the second sentence and the punch arrives late. REJECTED.

C. "I asked my GPS for the fastest route home. It said 'stay single,
   avoid commitment, and whatever you do, don't take the highway of
   your feelings.'" (145)
   The turn into relationship advice is a surprise, but the setup and
   the punch fight each other — two jokes crowding one line. REJECTED.

D. "My bank flagged my card for unusual activity yesterday. It was me
   buying vegetables. Apparently even my bank knows that's out of
   character." (WINNER, draft)
   Best of the set: the premise is universal (everyone has had a fraud
   alert), the twist is genuinely surprising (vegetables as the
   suspicious act), and it is self-deprecating without begging for
   sympathy. The laugh lands on the last word of sentence two.

E. "I set my alarm for 6 AM. My alarm set a second alarm for 6:05, a
   third for 6:10, and by 7 AM we had both agreed the day could start
   without me." (145)
   Good personification and a clean closer, but "alarm vs snooze"
   jokes are among the most told shapes in the field. REJECTED.

F. "The Wi-Fi went down for ten minutes. My family gathered in the
   living room, looked at each other, and realised we had nothing in
   common except the password." (159)
   Strong closer and very relatable, but the "Wi-Fi down exposes the
   family" premise is a familiar internet joke; D's fraud-alert twist
   is the fresher surprise. RUNNER-UP.

Pass 2 — developing the winner (D), two genuine revisions:

Revision 1: "flagged my card for unusual activity yesterday" became
"sent me a fraud alert for unusual activity". "Fraud alert" is the
exact phrase a bank actually sends, so the setup sounds real instead
of summarised, and dropping "yesterday" removes a word that added
nothing — the joke is timeless, not dated.

Revision 2: "Apparently even my bank knows that's out of character"
became "Even my bank knows that's not normal for me". "Apparently"
hedged the punch; cutting it lets the sentence hit at full speed, and
"not normal for me" is plainer and funnier than the slightly formal
"out of character" — it is the voice of the person telling the story.

HAND COUNT (final line, 125 characters):
  S1 "My bank sent me a fraud alert for unusual activity." = 51
  + space = 1 -> 52
  S2 "It was me buying vegetables." = 28 -> 80
  + space = 1 -> 81
  S3 "Even my bank knows that's not normal for me." = 44 -> 125
  Cross-check: 103 non-space characters + 22 spaces = 125.
"""

import os

ENTRY = (
    "My bank sent me a fraud alert for unusual activity. "
    "It was me buying vegetables. "
    "Even my bank knows that's not normal for me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
