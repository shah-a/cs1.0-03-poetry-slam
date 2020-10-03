# CS1.0 Assignment 3: Poetry Slam

Written in: Python 3.7.9

## Description

This program reads the lines of a poem (or any lines of text, for that matter) from a text file, manipulates the input in various ways, then prints the results.

## What does each function do?

### [`get_file_lines(filename)`](https://github.com/shah-a/cs1.0-03-poetry-slam/blob/1179d3cca7e950be010419939cda5ca4cdafea56/poetry_slam.py#L10)

This function reads the poem from a text file named `tanka.txt`. The file needs to be in the same directory as `poetry_slam.py`. Newline chars (`\n`) are stripped from the right ends of each line, then the poem lines are returned as a list of strings.

### [`lines_printed_backwards(lines_list)`](https://github.com/shah-a/cs1.0-03-poetry-slam/blob/1179d3cca7e950be010419939cda5ca4cdafea56/poetry_slam.py#L21)

This function adds line numbers to the left ends of each lines, then reverses the line order and prints the result.

### [`lines_printed_random(lines_list)`](https://github.com/shah-a/cs1.0-03-poetry-slam/blob/1179d3cca7e950be010419939cda5ca4cdafea56/poetry_slam.py#L37)

This function prints random lines from the poem until the number of lines printed is equal to the total line count of the poem. Lines may be printed repeatedly.

### [`equivalence_cycles(lines_list)`](https://github.com/shah-a/cs1.0-03-poetry-slam/blob/1179d3cca7e950be010419939cda5ca4cdafea56/poetry_slam.py#L46)

This function repeatedly fills a list with random lines from the poem until every line in the list is equivalent (i.e. the same poem line occupies every list index). Then, it prints the resultant strings backwards. For this to happen, the same random number needs to be generated len(list) times.

To maximize the likelihood for most number of cycles, each line in poem should be unique. If a poem has lines that repeat, the likelihood of generating equivalent strings greatly increases because the indices of *any* repeating lines can be generated instead of just *one* number needing to be repeatedly generated.

If the loops cycles [`max_cycles`](https://github.com/shah-a/cs1.0-03-poetry-slam/blob/4984b4f1955a90fe4a2fc630234c23914cf7c21f/poetry_slam.py#L55) times, the loop breaks and the final generation attempt of strings is printed. Otherwise, the function counts and prints how many cycles it took to successfully fill the list with equivalent strings.

## The poem I used...

...is a (translated) concatenation of two old Japanese romantic poems. The first one is a question, and the second is its response.

From what I understand, these poems are in the form of "tanka" poetry, which is similar to "haiku" poetry in that its written to satisfy a set number of syllables (in this case, 31 syllables each).

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
<br>

<img alt="Garden of Words/Kotonoha no Niwa" src="/img/garden.gif" width="200" />
