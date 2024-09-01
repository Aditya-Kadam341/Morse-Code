from flask import Flask, render_template, request

app = Flask(__name__)

def data_morse():
    morse_To_English = {
        ".-":"A",    "-...":"B",    "-.-.":"C",    "-..":"D",    ".":"E",    "..-.":"F",    "--.":"G",    "....":"H",    "..":"I",    ".---":"J",    "-.-":"K", 
        ".-..":"L",  "--":"M",      "-.":"N",      "---":"O",    ".--.":"P", "--.-":"Q",    ".-.":"R",    "...":"S",     "-":"T",     "..-":"U",     "...-":"V",
        ".--":"W",   "-..-":"X",    "-.--":"Y",    "--..":"Z",   
        "/":" ",
        ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0",  
        "..--..":"?", "-.-.--":"!", ".-.-.-":".", "--..--":",", "-.-.-.":";", "---...":":", ".-.-.":"+", "-....-":"8", "-..-.":"/", "-...-":"="
    }    
    
    english_To_Morse = {
    "A":".-",    "B":"-...",    "C":"-.-.",    "D":"-..",    "E":".",    "F":"..-.",    "G":"--.",      "H":"....",      "I":"..",      "J":".---",    "K":"-.-", 
    "L":".-..",    "M":"--",    "N":"-.",     "O":"---",    "P":".--.",    "Q":"--.-",     "R":".-.",      "S":"...",      "T":"-",        "U":"..-",      "V":"...-",
    "W":".--",      "X":"-..-",     "Y":"-.--",     "Z":"--..",   
    " ":"/",   
    "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----",
    "?":"..--..", "!":"-.-.--", ".":".-.-.-",",":"--..--", ";":"-.-.-.",":":"---...","+":".-.-.", "*":"-....-", "/":"-..-.", "=":"-...-"
    }
    return morse_To_English, english_To_Morse

@app.route('/')
def home():
    return render_template('MorE.html')


@app.route('/EnglishToMorse')
def EnglishToMorse():
    return render_template('EnglishToMorse.html')


@app.route('/MorseToEnglish')
def MorseToEnglish():
    return render_template('MorseToEnglish.html')


@app.route('/E2M')
def E2M():
    morse_To_English, english_To_Morse = data_morse()
    English_String = request.args['English'].upper()
    print("English : ",English_String,"\n")

    Morse_List = [*English_String]
    Morse_Converted = []
    for i in Morse_List:
        Morse_Converted.append(english_To_Morse[i])

    Final_Morse_Conversion = " ".join(Morse_Converted)
    # print("Morse : ",Final_Morse_Conversion,"\n")
    return render_template('E2M.html', Morse=Final_Morse_Conversion)



@app.route('/M2E')
def M2E():
    morse_To_English, english_To_Morse = data_morse()
    Morse_String =request.args['Morse']
    print("Morse : ",Morse_String,"\n")

    Morse_List = Morse_String.split()
    English_Converted = []
    for i in Morse_List:
        English_Converted.append(morse_To_English[i])

    Final_English_Conversion = "".join(English_Converted)
    # print("English : ",Final_English_Conversion,"\n")
    return render_template('M2E.html', English=Final_English_Conversion)




#end of code to run it
if __name__ == "__main__":
  app.run(port=8083,debug=True)
  





























# def data_morse():
#     morse_To_English = {
#         ".-":"A",    "-...":"B",    "-.-.":"C",    "-..":"D",    ".":"E",    "..-.":"F",    "--.":"G",    "....":"H",    "..":"I",    ".---":"J",    "-.-":"K", 
#         ".-..":"L",  "--":"M",      "-.":"N",      "---":"O",    ".--.":"P", "--.-":"Q",    ".-.":"R",    "...":"S",     "-":"T",     "..-":"U",     "...-":"V",
#         ".--":"W",   "-..-":"X",    "-.--":"Y",    "--..":"Z",   
#         "/":" ",
#         ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0",  
#         "..--..":"?", "-.-.--":"!", ".-.-.-":".", "--..--":",", "-.-.-.":";", "---...":":", ".-.-.":"+", "-....-":"8", "-..-.":"/", "-...-":"="
#     }    
    
#     english_To_Morse = {
#     "A":".-",    "B":"-...",    "C":"-.-.",    "D":"-..",    "E":".",    "F":"..-.",    "G":"--.",      "H":"....",      "I":"..",      "J":".---",    "K":"-.-", 
#     "L":".-..",    "M":"--",    "N":"-.",     "O":"---",    "P":".--.",    "Q":"--.-",     "R":".-.",      "S":"...",      "T":"-",        "U":"..-",      "V":"...-",
#     "W":".--",      "X":"-..-",     "Y":"-.--",     "Z":"--..",   
#     " ":"/",   
#     "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----",
#     "?":"..--..", "!":"-.-.--", ".":".-.-.-",",":"--..--", ";":"-.-.-.",":":"---...","+":".-.-.", "*":"-....-", "/":"-..-.", "=":"-...-"
#     }
#     return morse_To_English, english_To_Morse

# def M2E():
#     morse_To_English, english_To_Morse = data_morse()
#     Morse_String = input("Type in Morse Code : ")
#     print("Morse : ",Morse_String,"\n")

#     Morse_List = Morse_String.split()
#     English_Converted = []
#     for i in Morse_List:
#         English_Converted.append(morse_To_English[i])

#     Final_English_Conversion = "".join(English_Converted)
#     # print("English : ",Final_English_Conversion,"\n")
#     return Final_English_Conversion


# def E2M():
#     morse_To_English, english_To_Morse = data_morse()
#     English_String = input("Type in English : ").upper()
#     print("English : ",English_String,"\n")

#     Morse_List = [*English_String]
#     Morse_Converted = []
#     for i in Morse_List:
#         Morse_Converted.append(english_To_Morse[i])

#     Final_Morse_Conversion = " ".join(Morse_Converted)
#     # print("Morse : ",Final_Morse_Conversion,"\n")
#     return Final_Morse_Conversion
    

# print(M2E())
# print(E2M())