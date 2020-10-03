# CS1.0 Assignment 3: Poetry Slam

Written in: Python 3.7.9

## Description

This program reads poem lines (or any text, for that matter) from a file and prints them in various manipulated ways.

## What does each function do?

**get_file_lines(filename):**
This function reads the poem from a text file.
Text file needs to be in the same directory as `poetry_slam.py`.
removes newline char, and returns lines in a list

**lines_printed_backwards(lines_list):**
Adds numbers to poem's lines and reverses line order; prints result

**lines_printed_random(lines_list):**

Prints random lines from poem until reaching original line count number of prints

**equivalence_cycles(lines_list):**

Fills list with random lines from poem, loops until the same line occupies
every index in the list, and then prints result backwards. If loop cycles max_cycle
times, loop stops and prints final generation of lines backwards. To maximize
likelihood for most number of cycles, each line in poem should be unique

## The poem I used...

...is a (translated) mixup of two old Japanese poems. The first one is a question, and the second is its response. From what I understand, these poems are in the form of "tanka" poetry, which is similar to haiku poetry in that its written to fit a number of syllables (in this case, 31 syllables each).

**The translation I used:**

> A faint clap of thunder,<br>
> Clouded skies,<br>
> Perhaps rain will come,<br>
> If so, will you stay here with me?<br>
>
> A faint clap of thunder,<br>
> Even if rain comes not,<br>
> I will stay here,<br>
> Together with you.<br>
<br>

**The original poems:**

> なるかみの　すこしとよみて<br>
> *Narukami no sukoshi toyomite,*<br>
> さしくもり<br>
>*Sashi kumori,*<br>
> あめもふらぬか<br>
> *Ame mo furanu ka,*<br>
> きみをとどめむ<br>
> *Kimi wo todomemu?*<br>
>
> なるかみの　すこしとよみて<br>
> *Narukami no sukoshi toyomite,*<br>
> ふらずとも<br>
> *Furazu to mo,*<br>
> われはとまらむ<br>
> *Warewa tomaramu,*<br>
> いもしとどめば<br>
> *Imoshi todomeba.*
