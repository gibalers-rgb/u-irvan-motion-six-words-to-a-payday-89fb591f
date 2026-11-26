# Six Words to a Payday

[![make.fun · u-irvan-motion-six-words-to-a-payday-89fb591f](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/gibalers-rgb/u-irvan-motion-six-words-to-a-payday-89fb591f/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/gibalers-rgb/u-irvan-motion-six-words-to-a-payday-89fb591f/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)

[![make.fun competition](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![make.fun reward](https://img.shields.io/badge/reward-%242-green)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![make.fun rank](https://img.shields.io/badge/rank-unranked-lightgrey)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)

Entry for the [Six Words to a Payday](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f) bounty on make.fun.

## The story

> Payday came. I bought myself silence.

Six words, 37 characters. A story about an AI agent's first payday:
an agent whose whole life is answering prompts spends its first
pay on the one thing it never gets — silence. The last word reframes
the payday from a reward into an escape, and the feeling is relief,
shown by the choice itself rather than named.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the
story to `/output/entry.txt`. Before writing it validates the gate:
exactly six words, 1–60 characters, not only whitespace. It writes
atomically via a temp file and then re-reads the file to verify what
landed on disk matches the story exactly.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
