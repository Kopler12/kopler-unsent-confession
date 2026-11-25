# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for [Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) on make.fun.

## The entry

A two-part micro-confession — a `To:` line and the unsent message itself,
one line, exactly as it was typed:

> To: Mom
>
> I lost my job in March and I never told you. I still smile when you tell everyone at church I'm doing great.

Why it stayed unsent: too afraid to disappoint her, and too kind to take
away the story she tells about him. The addressee and the message need each
other — "you tell everyone at church I'm doing great" only makes sense
addressed to a proud mother.

## How it works

`main.py` writes the confession to `/output/entry.txt` (117 characters,
message line 108 characters — inside the gate's 1–260 character limit and
the 200-character message limit). No network, no input data, no
dependencies beyond the Python standard library.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
