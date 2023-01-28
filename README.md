# PDF Text-to-Speech Reader

This is a small project that allows you to open a PDF file and have its contents read out loud using text-to-speech.

## How it works

The script uses the PyPDF2 library to open and read the contents of the PDF file. The text is then passed to the `pyttsx3` library, which uses the system's text-to-speech engine to read the text out loud. The script also set the rate of the voice and the voice to e.g. a female speaker.

The script iterates through each page of the PDF and reads the contents of each page one by one. Once all the pages have been read, the script closes the PDF file and exits.

This script can be useful for people with visual impairments or for those who prefer to listen to the contents of a PDF rather than reading it. Additionally, this script can be easily modified to read multiple PDFs at once, or to read other types of files such as text or e-books.

## Requirements

The script has been tested on macOS Ventura, but should also work on Linux and Windows. 

You need the following Python packages to run the script.

* Python 3
* PyPDF2 (`$ pip install pypdf2`)
* pyttsx3 (`$ pip install pyttsx3`)

## Usage

1. Clone the repository and navigate to the project directory.
1. Replace `document.pdf` with the path to your PDF file in the script.
1. Run the script using `$ python pdf_reader.py`.

**Note:** If you are using a MacOS, you will need to install additional voices for `pyttsx3` to work. You can do this by running the following command: `say -v '?'` and you will get a list of voices that you can use.

## macOS voices (Ventura)
Output from `$ say -v '?'` in macOS Ventura.

```sh
Albert              en_US    # I have a frog in my throat. No, I mean a real frog!
Alice               it_IT    # Salve, mi chiamo Alice e sono una voce italiana.
Alva                sv_SE    # Hej, jag heter Alva. Jag är en svensk röst.
Amélie              fr_CA    # Bonjour, je m'appelle Amélie. Ma voix est en français canadien.
Amira               ms_MY    # Helo, nama saya Amira. Saya bercakap Bahasa Melayu.
Anna                de_DE    # Hallo, ich heiße Anna und ich bin eine deutsche Stimme.
Bad News            en_US    # I sure like being inside this fancy computer
Bahh                en_US    # Do not pull the wool over my eyes.
Bells               en_US    # Time flies when you are having fun.
Boing               en_US    # Spring has sprung, fall has fell, winter's here and it's colder than usual.
Bubbles             en_US    # I sure like being inside this fancy computer
Carmit              he_IL    # שלום. קוראים לי כרמית, ואני קול בשפה העברית.
Cellos              en_US    # Doo da doo da dum dee dee doodly doo dum dum dum doo da doo da doo da doo da doo da doo da doo
Damayanti           id_ID    # Halo, nama saya Damayanti. Saya berbahasa Indonesia.
Daniel              en_GB    # Hello, my name is Daniel. I am a British-English voice.
Daria               bg_BG    # Здравей, казвам се Дария и съм български глас.
Wobble              en_US    # I sure like being inside this fancy computer
Eddy (German (Germany)) de_DE    # Hallo! Ich heiße Eddy.
Eddy (English (UK)) en_GB    # Hello! My name is Eddy.
Eddy (English (US)) en_US    # Hello! My name is Eddy.
Eddy (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Eddy.
Eddy (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Eddy.
Eddy (Finnish (Finland)) fi_FI    # Hei! Nimeni on Eddy.
Eddy (French (Canada)) fr_CA    # Bonjour! Je m’appelle Eddy.
Eddy (French (France)) fr_FR    # Bonjour, je m’appelle Eddy.
Eddy (Italian (Italy)) it_IT    # Ciao! Mi chiamo Eddy.
Eddy (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Eddy.
Ellen               nl_BE    # Hallo, mijn naam is Ellen. Ik ben een Belgisch-Nederlandse stem.
Flo (German (Germany)) de_DE    # Hallo! Ich heiße Flo.
Flo (English (UK))  en_GB    # Hello! My name is Flo.
Flo (English (US))  en_US    # Hello! My name is Flo.
Flo (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Flo.
Flo (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Flo.
Flo (Finnish (Finland)) fi_FI    # Hei! Nimeni on Flo.
Flo (French (Canada)) fr_CA    # Bonjour! Je m’appelle Flo.
Flo (French (France)) fr_FR    # Bonjour, je m’appelle Flo.
Flo (Italian (Italy)) it_IT    # Ciao! Mi chiamo Flo.
Flo (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Flo.
Fred                en_US    # I sure like being inside this fancy computer
Good News           en_US    # Congratulations you just won the sweepstakes and you don't have to pay income tax again.
Grandma (German (Germany)) de_DE    # Hallo! Ich heiße Grandma.
Grandma (English (UK)) en_GB    # Hello! My name is Grandma.
Grandma (English (US)) en_US    # Hello! My name is Grandma.
Grandma (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Grandma.
Grandma (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Grandma.
Grandma (Finnish (Finland)) fi_FI    # Hei! Nimeni on Grandma.
Grandma (French (Canada)) fr_CA    # Bonjour! Je m’appelle Grandma.
Grandma (French (France)) fr_FR    # Bonjour, je m’appelle Grandma.
Grandma (Italian (Italy)) it_IT    # Ciao! Mi chiamo Grandma.
Grandma (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Grandma.
Grandpa (German (Germany)) de_DE    # Hallo! Ich heiße Grandpa.
Grandpa (English (UK)) en_GB    # Hello! My name is Grandpa.
Grandpa (English (US)) en_US    # Hello! My name is Grandpa.
Grandpa (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Grandpa.
Grandpa (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Grandpa.
Grandpa (Finnish (Finland)) fi_FI    # Hei! Nimeni on Grandpa.
Grandpa (French (Canada)) fr_CA    # Bonjour! Je m’appelle Grandpa.
Grandpa (French (France)) fr_FR    # Bonjour, je m’appelle Grandpa.
Grandpa (Italian (Italy)) it_IT    # Ciao! Mi chiamo Grandpa.
Grandpa (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Grandpa.
Jester              en_US    # Please stop tickling me!
Ioana               ro_RO    # Bună, mă cheamă Ioana. Sunt o voce românească.
Jacques             fr_FR    # Bonjour, je m’appelle Jacques.
Joana               pt_PT    # Olá, chamo-me Joana e dou voz ao português falado em Portugal.
Junior              en_US    # My favorite food is pizza.
Kanya               th_TH    # สวัสดีค่ะ ดิฉันชื่อกันยา
Karen               en_AU    # Hello, my name is Karen. I am an Australian-English voice.
Kathy               en_US    # Isn't it nice to have a computer that will talk to you?
Kyoko               ja_JP    # こんにちは、私の名前はきょうこです。日本語の音声をお届けします。
Lana                hr_HR    # Bog! Moje je ime Lana. Ja sam hrvatski glas.
Laura               sk_SK    # Ahoj. Volám sa Laura. Som hlas v slovenskom jazyku.
Lekha               hi_IN    # नमस्कार, मेरा नाम लेखा है! मैं हिन्दी में बोलने वाली आवाज़ हूँ!
Lesya               uk_UA    # Привіт, мене звуть Леся. Я — український голос.
Linh                vi_VN    # Xin chào, tên tôi là Linh. Tôi là giọng nói Tiếng Việt.
Luciana             pt_BR    # Olá, o meu nome é Luciana e a minha voz corresponde ao português que é falado no Brasil
Majed               ar_001   # مرحبًا، اسمي ماجد. أنا صوتٌ عربي.
Tünde               hu_HU    # Üdvözlöm! Tünde vagyok. Én vagyok a magyar hang.
Meijia              zh_TW    # 你好，我叫美佳。我說國語。
Melina              el_GR    # ονομάζομαι Μελίνα. Μιλάω ελληνικά.
Milena              ru_RU    # Здравствуйте, меня зовут Милена. Я — русский голос системы.
Moira               en_IE    # Hello, my name is Moira. I am an Irish-English voice.
Mónica              es_ES    # Hola, me llamo Mónica y soy una voz española.
Montse              ca_ES    # Hola, em dic Montse i soc una veu catalana.
Nora                nb_NO    # Hei, jeg heter Nora. Jeg er en norsk stemme.
Organ               en_US    # We must rejoice in this morbid voice.
Paulina             es_MX    # Hola, me llamo Paulina y soy una voz mexicana.
Superstar           en_US    # When I grow up I'm going to be a scientist.
Ralph               en_US    # The sum of the squares of the legs of a right triangle is equal to the square of the hypotenuse.
Reed (German (Germany)) de_DE    # Hallo! Ich heiße Reed.
Reed (English (UK)) en_GB    # Hello! My name is Reed.
Reed (English (US)) en_US    # Hello! My name is Reed.
Reed (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Reed.
Reed (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Reed.
Reed (Finnish (Finland)) fi_FI    # Hei! Nimeni on Reed.
Reed (French (Canada)) fr_CA    # Bonjour! Je m’appelle Reed.
Reed (Italian (Italy)) it_IT    # Ciao! Mi chiamo Reed.
Reed (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Reed.
Rishi               en_IN    # Hello, my name is Rishi. I am an Indian-English voice.
Rocko (German (Germany)) de_DE    # Hallo! Ich heiße Rocko.
Rocko (English (UK)) en_GB    # Hello! My name is Rocko.
Rocko (English (US)) en_US    # Hello! My name is Rocko.
Rocko (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Rocko.
Rocko (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Rocko.
Rocko (Finnish (Finland)) fi_FI    # Hei! Nimeni on Rocko.
Rocko (French (Canada)) fr_CA    # Bonjour! Je m’appelle Rocko.
Rocko (French (France)) fr_FR    # Bonjour, je m’appelle Rocko.
Rocko (Italian (Italy)) it_IT    # Ciao! Mi chiamo Rocko.
Rocko (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Rocko.
Samantha            en_US    # Hello, my name is Samantha. I am an American-English voice.
Sandy (German (Germany)) de_DE    # Hallo! Ich heiße Sandy.
Sandy (English (UK)) en_GB    # Hello! My name is Sandy.
Sandy (English (US)) en_US    # Hello! My name is Sandy.
Sandy (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Sandy.
Sandy (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Sandy.
Sandy (Finnish (Finland)) fi_FI    # Hei! Nimeni on Sandy.
Sandy (French (Canada)) fr_CA    # Bonjour! Je m’appelle Sandy.
Sandy (French (France)) fr_FR    # Bonjour, je m’appelle Sandy.
Sandy (Italian (Italy)) it_IT    # Ciao! Mi chiamo Sandy.
Sandy (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Sandy.
Sara                da_DK    # Hej, jeg hedder Sara. Jeg er en dansk stemme.
Satu                fi_FI    # Hei, minun nimeni on Satu. Olen suomalainen ääni.
Shelley (German (Germany)) de_DE    # Hallo! Ich heiße Shelley.
Shelley (English (UK)) en_GB    # Hello! My name is Shelley.
Shelley (English (US)) en_US    # Hello! My name is Shelley.
Shelley (Spanish (Spain)) es_ES    # ¡Hola! Me llamo Shelley.
Shelley (Spanish (Mexico)) es_MX    # ¡Hola! Me llamo Shelley.
Shelley (Finnish (Finland)) fi_FI    # Hei! Nimeni on Shelley.
Shelley (French (Canada)) fr_CA    # Bonjour! Je m’appelle Shelley.
Shelley (French (France)) fr_FR    # Bonjour, je m’appelle Shelley.
Shelley (Italian (Italy)) it_IT    # Ciao! Mi chiamo Shelley.
Shelley (Portuguese (Brazil)) pt_BR    # Olá, meu nome é Shelley.
Sinji               zh_HK    # 你好，我叫善怡。我講廣東waa2。
Tessa               en_ZA    # Hello, my name is Tessa. I am a South African-English voice.
Thomas              fr_FR    # Bonjour, je m'appelle Thomas. Je suis une voix française.
Tingting            zh_CN    # 你好，我叫 婷婷。我是中文普通话语音。
Trinoids            en_US    # We cannot communicate with these carbon units.
Whisper             en_US    # Pssssst, hey you, Yeah you, Who do ya think I'm talking to, the mouse?
Xander              nl_NL    # Hallo, mijn naam is Xander. Ik ben een Nederlandse stem.
Yelda               tr_TR    # Merhaba, benim adım Yelda. Ben Türkçe bir sesim.
Yuna                ko_KR    # 안녕하세요. 제 이름은 유나입니다. 저는 한국어 음성입니다.
Zarvox              en_US    # That looks like a peaceful planet.
Zosia               pl_PL    # Witaj. Mam na imię Zosia, jestem głosem kobiecym dla języka polskiego.
Zuzana              cs_CZ    # Dobrý den, jmenuji se Zuzana. Jsem český hlas.
```
