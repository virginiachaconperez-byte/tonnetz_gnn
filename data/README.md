# Data

The pilot uses [The Annotated Mozart Sonatas](https://github.com/DCMLab/mozart_piano_sonatas)
from DCML, starting with the first movement of Sonata K. 279 (`K279-1`).
Dataset files are downloaded separately and kept out of Git.

## Download

From the project root, download the revision selected for the pilot:

```sh
git clone --depth 1 https://github.com/DCMLab/mozart_piano_sonatas.git data/raw/dcml-mozart
git -C data/raw/dcml-mozart fetch --depth 1 origin 5337257a5318711e6302cfe85c3f1a6ade3c6271
git -C data/raw/dcml-mozart checkout --detach 5337257a5318711e6302cfe85c3f1a6ade3c6271
git -C data/raw/dcml-mozart rev-parse HEAD
```

The last command should print `5337257a5318711e6302cfe85c3f1a6ade3c6271`.
If the source is already downloaded, skip the clone command.

## Files and storage

| Location | Contents |
|---|---|
| `data/raw/dcml-mozart/` | Downloaded corpus, including its original documentation and licence. |
| `data/processed/` | Generated input representations. |

Both locations are ignored by Git. The first piece uses these files inside
`data/raw/dcml-mozart/`:

- `notes/K279-1.notes.tsv`
- `harmonies/K279-1.harmonies.tsv`
- `measures/K279-1.measures.tsv`

Use `harmonies/` for the reference chord labels. When preparing the data:

- Interpret chord labels using their musical key; they are not absolute note numbers.
- Keep note and harmony tables consistent when handling repeated sections.
- Keep the actual notes separate from the reference chords. Grace notes and tied
  notes also need handling during conversion.

The preparation script and reusable tests are not implemented yet.

## Licence and attribution

The dataset uses [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
Its terms include attribution,
non-commercial use, and share-alike conditions for redistributed adaptations
and are separate from the project's code licence. Retain the source licence
and cite:

Hentschel, Neuwirth, and Rohrmeier (2021), *The Annotated Mozart Sonatas: Score,
Harmony, and Cadence*. [DOI: 10.5334/tismir.63](https://transactions.ismir.net/articles/10.5334/tismir.63).
