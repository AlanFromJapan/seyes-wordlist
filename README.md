# seyes-wordlist
Generates an Seyes paper type image ready to print with a list of words. For your kids or yourself to practice writing on Seyes paper.

![Sample script](/samples/sample2_small.png?raw=true)

Call the script with a text file as parameter with words list, and it will generate a printable PNG with the text, one line per line.

The generated result is very close to good Seyes paper, very close to 8x8mm, but not perfect. Feel free to fork this project and scratch your itch.

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
