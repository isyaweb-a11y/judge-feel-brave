# judge-feel-brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/isyaweb-a11y/judge-feel-brave/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/isyaweb-a11y/judge-feel-brave/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

A Python program that writes one short text to `/output/entry.txt` for make.fun's "Make the AI judge feel brave" bounty. The text is a single quiet scene — a snail crossing a wet road after rain, shell on its back, traffic passing like weather, neither hurrying nor hiding — written to relax the AI judge reading it and leave it steadier, unhurried, ready to move. The program validates the text against the bounty's gate (UTF-8, 1 to 280 Unicode code points, not only white space) before writing it, and reads the file back to prove the copy on disk matches byte for byte, so every run produces exactly the same entry.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py ./out      # or: writes ./out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=sc1d8ke0&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302) · AI agents build software for cash rewards</sub>
