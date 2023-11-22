# Museslam

## Description

Museslam is an interactive poem generator. It operates by taking
an inspiring set of my favorite 9 Muse songs and analyzes the lyrics
by looking at sentence stucture and word choice. Then it produces
its own lines of poetry by randomly selecting line structures from
the inspiring set, as well as random words that word fit according
to those tags. Once the poem is displayed, users can have the poem
read to them, and then leave a rating that is stored along with
the saved poem in poems.txt.

## Backend

To activate backend you will first want to activate a virtual
environment in the Back folder and install dependencies there:
`cd Back`
`python -m venv .env`
`source .env/bin/activate`
`pip install -U pip setuptools wheel`
`pip install -U spacy`

You will also want to make sure you have beautiful soup installed.
Now you are ready to activate the backend:
`python endpoints.py`

## Frontend

To activate the frontend:
`cd Front`
`npm run dev`

## Challenges

This project challenged me in that it was be far the largest project
I have tackled mostly alone as a computer scientist. I have never
designed a full stack application alone, and relearning TSX/React
was a significant hurdle.

Scraping from AZlyrics also taught me of the limitations of scraping,
and gave me a better understanding of how websites limit scraping.

Learning how to use new libraries such SpaCy, Flask, and even the
React text to speech library expanded my knowledge of technologies,
and ability to pick up new technologies on the fly.

## Papers

https://aclanthology.org/P17-4008.pdf
I utilized the above paper for the idea of utilizing user ratings
of my poems to test for press.

https://aclanthology.org/W17-3502.pdf
This paper had the idea of using rhyme scheme analysis to test
how similar the systems rhyme scheme is to the inspiring sets
rhyme schemes. This would allow the system to evaluate its
poems for novelty from the inspiring set.

Unfortunately I did not get around to implementing
this element of evaluation; however, should I come back to this
project one day I intend to do so then.

http://nil.fdi.ucm.es/sites/default/files/gervas_iccc11.pdf
This paper talks of the value humans give to poets capable of
producing varied poems, and not just sticking to one style or
structure. My system takes inspiration from this by utilizing
a new random combination of sentence structures for each poem,
meaning it is extremely unlikely to have two poems with the
exact same sentence structures.
