# davidhu3141.github.io

I use github to host some of my pages:

1. Startup page for my internet browser, *personal use*
2. A page to post my articles. (as blog) http://davidhu3141.github.io/anthology2/

I'll do some coding to manage my blog, and log here.

--------------------------------------


Jekyll Tweak Log
================

### LaTeX

I use sed to process LaTeX in MD. KramDown doesn't recognize single dollor sign so I wrote my own script to preprocess LaTeX.



Anthology Generator Developer Note
==================================

> This proj is no longer progress. Jekyll is just what I really need.


TODO
----

- A '/' in CSS import path should be removed.
- Generate renewable list of article as JSON, with modification date and comparison.
- Make CSS test easy.
- *[Restruct folders]*
- *[Extract methods]*
- use filecmp to compare file, and use replace to generate real replication.

Architecture
------------

### Command Organization

#### -s --status

status

> outdated article list, [n] articles to be renewed. 

> all up to date.

#### -r --renew

renew all

renew [n]

renew list
