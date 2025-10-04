# Quiz

#### Video Demo:  ``

#### Description
This quiz application is a small, terminal-based program written in Python that converts a two-column CSV file into an interactive practice tool. The program reads a CSV file where each row contains a question and its answer, stores the data in memory, and presents a live table view showing all questions. Until you answer a question correctly, the answer column shows `???` to hide the solution. When a question is answered correctly, the program reveals the answer in subsequent table refreshes.

The application is designed to be simple, robust, and easy to extend. It normalizes both stored answers and user input by trimming whitespace and converting text to lowercase, which reduces accidental mismatches. A background timer thread provides optional timed sessions while keeping the main input loop responsive. The program prints your final score when the session finishes, whether that is because the timer expired, the user answered all questions, or the user canceled the session with Ctrl+C.

#### How to Play
1. Prepare a CSV file with exactly two headers. The first header must be `question` and the second must be `answer`. An example file, `example.csv`, is included in the repository and can be used as a template.
2. If you want to use a different file, change the `file_name` variable at the top of `project.py` to point to your CSV file, or replace the provided `example.csv` with your own file in the same directory.
3. Run the program from the terminal with:

```
python project.py
```

4. When prompted for a time limit, enter either `inf` for infinite time or specify a value in `M:SS` format (for example, `1:30` for one minute and thirty seconds).
5. Answer questions at the prompt. When your input matches the normalized stored answer, the corresponding question is marked as answered and its answer will appear in the table on the next refresh. To exit early, press Ctrl+C; the program will print your score and then exit. If you complete all questions, the program will congratulate you and print your score before exiting automatically.

The table view updates every loop iteration, so you always see the current state of progress. This makes it easy to track which questions remain unanswered and which ones you have already completed.

#### CSV format
The CSV file must contain exactly two headers. Example content:

```
question,answer
1 * 3,3
5 + 6,11
0 / 5,0
10 - 15,-5
```

- The first column header must be `question` and the second must be `answer`.
- Each subsequent row contains a single question and its corresponding answer.
- When importing, the program lowercases and trims values so that answers are matched case-insensitively and are tolerant of leading/trailing whitespace.


#### Design notes
- Data model: Each question is stored as a dictionary with keys for the question text, the normalized answer, and a boolean `correct` flag. These dictionaries are stored in instance-level lists (`data` and `visual_data`) to avoid shared state between separate quiz instances.

- Display: The program uses the `tabulate` library to present a clear table in the terminal. `visual_data` is rebuilt each loop so the printed table always reflects the latest state.

- Input normalization: User input is normalized using `strip().lower()` to reduce false negatives caused by capitalization or stray spaces.

- Timer: A separate background thread runs the countdown so the main input loop is not blocked. A threading event signals the main loop to stop when time runs out.

- Exit behavior: When the quiz completes (all questions answered, time out, or user cancellation), the program prints the final score and exits.

#### Acknowledgements
This project was built as a final project for CS50P. It is provided for educational and personal use and can be adapted or extended for learning and practice.
