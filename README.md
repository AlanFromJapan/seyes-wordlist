# seyes-wordlist
Generates an Seyes paper type image ready to print with a list of words. For your kids or yourself to practice writing on Seyes paper.

![Sample script](/samples/sample2_small.png?raw=true)

Call the script with a text file as parameter with words list, and it will generate a printable PNG with the text, one line per line.

The generated result is very close to good Seyes paper, very close to 8x8mm, but not perfect. Feel free to fork this project and scratch your itch.

## Seyes paper?
A [French thing apparently](https://en.wikipedia.org/wiki/Ruled_paper#France), a paper where major lines are split in 4 equal parts. Major line are 8 mm high, each of the sub-lines are 2mm high. You CAPS should be 3 sub-division high, your "t"s raise 2 (didn't remember that!), and your "g" -2 below.

You can have also a left hand margin which I kept, and split the left side with vertical lines also 8mm wide, giving squares of 8x8mm.

## Dependencies
- Pillow

## Usage
```bash
python3 seys_wordlist.py <path_to_file>
```
Generates a *path_to_file* **.png** image with the content you wanted.

## Customization
All the settings are in **seyes_wordlist.py** at the top.

- You can change the font and use any you like, just edit the name of the font in seyes_wordlist at the top. The system should adapt to the font and still print ok (hopefully!)
- Change the quality factor to have better rendering. In my experience a quality factor of 2 once printed, I can't see the pixels
- Colors are there too
