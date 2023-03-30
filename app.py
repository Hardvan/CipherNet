from flask import Flask, render_template, request

app = Flask(__name__)


def morse_to_eng(morse):

    # .... .. = hi
    morse_alpha = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
                   "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                   "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
                   "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                   "y": "-.--", "z": "--.."}

    morse_num = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                 "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}

    morse_symbols = {"!": "-.-.--", "\"": ".-..-.", "&": ".-...", "\'": ".----.",
                     "(": "-.--.", ")": "-.--.-", "+": ".-.-.", ",": "--..--",
                     "-": "-....-", ".": ".-.-.-", "/": "-..-.", ":": "---...",
                     "=": "-...-", "?": "..--..", "@": ".--.-."}

    final_text = ""

    morse_words = morse.split('/')  # ['.... ..','-- -.--']
    for morse_word in morse_words:

        morse_letters = morse_word.split()  # ['....','..']
        text = ""

        for morse_letter in morse_letters:

            if morse_letter in morse_alpha.values():
                key_list = list(morse_alpha.keys())
                values_list = list(morse_alpha.values())
                index = values_list.index(morse_letter)
                text += key_list[index].upper()

            elif morse_letter in morse_num.values():
                key_list = list(morse_num.keys())
                values_list = list(morse_num.values())
                index = values_list.index(morse_letter)
                text += key_list[index]

            elif morse_letter in morse_symbols.values():
                key_list = list(morse_symbols.keys())
                values_list = list(morse_symbols.values())
                index = values_list.index(morse_letter)
                text += key_list[index]

        final_text += text
        final_text += ' '

    return final_text


def eng_to_morse(text):

    morse_alpha = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
                   "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                   "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
                   "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                   "y": "-.--", "z": "--.."}

    morse_num = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                 "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}

    morse_symbols = {"!": "-.-.--", "\"": ".-..-.", "&": ".-...", "\'": ".----.",
                     "(": "-.--.", ")": "-.--.-", "+": ".-.-.", ",": "--..--",
                     "-": "-....-", ".": ".-.-.-", "/": "-..-.", ":": "---...",
                     "=": "-...-", "?": "..--..", "@": ".--.-."}

    final_morse = ""

    words = text.split()  # "my name is" --- ["my","name","is"]
    for word in words:  # Each Word
        morse_word = ""

        # Finding morse for that particular word
        for ch in word:  # Each Letter
            ch = ch.lower()
            if ch.isalpha():
                morse_word += morse_alpha[ch]

            elif ch.isnumeric():
                morse_word += morse_num[ch]

            else:
                morse_word += morse_symbols[ch]

            morse_word += ' '  # Space between letters

        final_morse += morse_word
        final_morse += '/'  # Slash after words

    return final_morse


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/morse', methods=['GET', 'POST'])
def morse():

    if request.method == 'POST':

        morse_to_eng_text = request.form.get('morse_to_eng', None)
        eng_to_morse_text = request.form.get('eng_to_morse', None)
        result = {}
        if morse_to_eng_text:
            # print(morse_to_eng_text)
            result['morse_to_eng'] = morse_to_eng(morse_to_eng_text)
            # print(result['morse_to_eng'])
        if eng_to_morse_text:
            # print(eng_to_morse_text)
            result['eng_to_morse'] = eng_to_morse(eng_to_morse_text)
            # print(result['eng_to_morse'])

        return render_template('morse.html', result=result)

    return render_template('morse.html', result=None)


@app.route('/rsa')
def rsa():

    return render_template('rsa.html')


if __name__ == "__main__":
    app.run(debug=True)
