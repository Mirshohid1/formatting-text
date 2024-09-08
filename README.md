# Text Formatting Script

This Python script formats a given text according to specific rules, including adding/removing spaces around commas and wrapping text to fit within a line based on the length of the longest word. It also handles comma placement and line breaking to ensure clean text formatting.

## Project Description

The script performs the following tasks:
1. **Splits text**: Finds the longest word and uses it to determine the maximum allowed line length (3 times the length of the longest word).
2. **Handles commas and spaces**: Ensures commas are "stuck" to the word before them, and adds spaces after commas if necessary.
3. **Text wrapping**: Breaks lines when the maximum line length is reached, ensuring words and punctuation are properly wrapped onto the next line.

### Key Functions

- **`longest_word(text: str) -> str`**:
  Finds the longest word in the text and returns it.

- **`add_remove_spaces(text: str) -> str`**:
  Adjusts spaces around commas, removing unnecessary spaces before commas and adding spaces after them where appropriate.

- **`formatting_text(text: str) -> str`**:
  Formats the text by wrapping it within a maximum line length, taking into account the length of the longest word. Also ensures commas are properly placed without introducing extra spaces before them.

## Example Usage

To run the script with a text argument from the command line:

```bash
python script.py "your text here"
```

You can also run the provided examples in the script:
```python
# Example usage
print(formatting_text("once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched"))
print(formatting_text("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex"))
```
# Project Conditions
The conditions for the project were taken from the contest task
"Text Formatting" in Contest Yandex Uzbekistan 2024: Backend. 
The requirements specify:
1. Formatting text such that the length of each line is no longer 
than three times the length of the longest word.
2. Proper handling of commas, ensuring that there are no spaces before 
them, and that a space is added after them unless they are the last 
character in the line.

Full details can be found in the contest problem description, which is 
included in the following PDF document:

[Contest PDF](./A_Форматирование_текста_—_Contest_Yandex_Uzbekistan_2024_Backend.pdf)

# License
This project is open-source and free to use.