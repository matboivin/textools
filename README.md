# textools

Helpers for common text preprocessing tasks.

## Installation

Clone the repository and change it to your working directory.

```console
$ poetry install
```

## Usage

Integrate `textools` as a library.

```python
from typing import List
from nltk.tokenize import word_tokenize

import textools


tokens: List[str] = word_tokenize(TEXT, LANGUAGE)
result: List[str] = textools.remove_stopwords(LANGUAGE, tokens)
```

## Testing

```console
$ poetry run pytest
```
