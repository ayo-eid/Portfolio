import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import re, string
import speech_recognition as sr
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import speech_recognition as sr

stemmer = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

training_data = []

training_data.append({"class":"sports", "sentence":"Team sports are probably one of the most popular kinds of sports all over the world, and the most famous and highest-paid athletes usually come from sports teams"})
training_data.append({"class":"sports", "sentence":"Team sports include basketball, football, soccer, hockey, and volleyball. Among these, basketball, football and soccer account for the largest teams in the world."})
training_data.append({"class":"sports", "sentence":"Famous leagues include the NBA for basketball, the NFL for football, and the Premiere League and UEFA Champion’s League for soccer."})
training_data.append({"class":"sports", "sentence":"These are sports such as tennis, archery, gymnastics and running that are usually played by a single individual."})
training_data.append({"class":"sports", "sentence":"Although there are teams depending on the tournament, which usually happens during the Olympics, for the most part, these kinds of sports are played by an individual against another person, sometimes even belonging from the same team as they are."})
training_data.append({"class":"sports", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"sports", "sentence":"want, need, have, thinking, always,a, an, as, such as, for example, like."})

training_data.append({"class":"dieting", "sentence":"By eating a balanced diet, people can get the nutrients and calories they need and avoid eating junk food, or food without nutritional value"})
training_data.append({"class":"dieting", "sentence":"A healthful, balanced diet includes foods from these five groups: Vegetables, fruits, grains, protein, dairy."})
training_data.append({"class":"dieting", "sentence":"A poor diet is a common reason why people struggle with weight loss."})
training_data.append({"class":"dieting", "sentence":"When combined with a regular exercise routine, a balanced diet can help a person reduce their risk factors for obesity or gaining weight."})
training_data.append({"class":"dieting", "sentence":"lose weight, calories needed."})
training_data.append({"class":"dieting", "sentence":"you need ton start calculating calories in every thing you eat so you can plan your diet well, you also need to calulate the needed calories per day"})
training_data.append({"class":"dieting", "sentence":"stop eating junk food every day, try eating healthy food and you will see the differnce in your weight"})
training_data.append({"class":"dieting", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"dieting", "sentence":"want, need, have, thinking,always, a, an, as, such as, for example, like."})

training_data.append({"class":"programming", "sentence":"Most popular programming languages are C, C++, C#, JAVA, Python, JavaScript /TypeScript, Objective-C, PHP, Ruby, Scala."})
training_data.append({"class":"programming", "sentence":"How are you going to choose a language for development on iPhone, if there are only two of them?"})
training_data.append({"class":"programming", "sentence":"How are you going to choose a language for development on Android, if there is only one of them?"})
training_data.append({"class":"programming", "sentence":"There is still some kind of a choice in Web-development."})
training_data.append({"class":"programming", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"programming", "sentence":"want, need, have, thinking,always, a, an, as, such as, for example, like."})

training_data.append({"class":"natural language processing", "sentence":"Natural Language Processing is the technology used to aid computers to understand the human’s natural language."})
training_data.append({"class":"natural language processing", "sentence":"It’s not an easy task teaching machines to understand how we communicate."})
training_data.append({"class":"natural language processing", "sentence":"A human talk to the machine"})
training_data.append({"class":"natural language processing", "sentence":"The machine captures the audio."})
training_data.append({"class":"natural language processing", "sentence":"Audio to text conversion takes place."})
training_data.append({"class":"natural language processing", "sentence":"Processing of the text’s data."})
training_data.append({"class":"natural language processing", "sentence":"Data to audio conversion takes place."})
training_data.append({"class":"natural language processing", "sentence":"The machine responds to the human by playing the audio file."})
training_data.append({"class":"natural language processing", "sentence":"Language translation applications such as Google Translate."})
training_data.append({"class":"natural language processing", "sentence":"Data to audio conversion takes place."})
training_data.append({"class":"natural language processing", "sentence":"Word Processors such as Microsoft Word and Grammarly that employ NLP to check grammatical accuracy of texts."})
training_data.append({"class":"natural language processing", "sentence":"Interactive Voice Response (IVR) applications used in call centers to respond to certain users’ requests."})
training_data.append({"class":"natural language processing", "sentence":"Personal assistant applications such as OK Google, Siri, Cortana, and Alexa."})
training_data.append({"class":"natural language processing", "sentence":"Here are some syntax techniques that can be used: Morphological segmentation, Word segmentation, Part-of-speech tagging, Parsing, tokenizing, Stemming, Lemmatization. "})
training_data.append({"class":"natural language processing", "sentence":"preprocessing the text, choosing one classifier, naive bays classifier, there are differnt types of classifier, supervisied and unsupervisied"})
training_data.append({"class":"natural language processing", "sentence":"i will be doing some preprocessing on the resulted text then i am going to classify that text. "})
training_data.append({"class":"natural language processing", "sentence":"i need a suitable dataset to match my target."})
training_data.append({"class":"natural language processing", "sentence":"I have found some datasets such as brown, wordnet"})
training_data.append({"class":"natural language processing", "sentence":"what is nltk, it it used for dealing with natural language processing projects, i guess it's like a library."})
training_data.append({"class":"natural language processing", "sentence":"i have to figure out what is the best classifier to use, i also have to figure out what is the best to use from nltk, stanford NLP, IBM watson to use in the stage of preprocessing."})
training_data.append({"class":"natural language processing", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"natural language processing", "sentence":"want, need, have, thinking, always, a, an, as, such as, for example, like."})

training_data.append({"class":"Psychology ", "sentence":"The Beginnings of Psychology as a Discipline."})
training_data.append({"class":"Psychology ", "sentence":"Psychology perspectives are behaviorism, Psychodynamic approach, humanistic approach, cognitive psychology, biological approach. "})
training_data.append({"class":"Psychology ", "sentence":"Psychology is the study of the mind, how it works, and how it affects behavior."})
training_data.append({"class":"Psychology ", "sentence":"There are different types of psychology, such as clinical, health, occupational, cognitive, forensic, social, and developmental psychology."})
training_data.append({"class":"Psychology", "sentence":"A person with a condition that affects their mental health may benefit from assessment and treatment with a psychologist."})
training_data.append({"class":"Psychology", "sentence":"A psychologist may offer treatment that focuses on behavioral adaptations."})
training_data.append({"class":"Psychology", "sentence":"A psychiatrist is a medical doctor who is more likely to focus on medical management of mental health issues."})
training_data.append({"class":"Psychology", "sentence":"It’s the most interesting because it’s about us, it’s about the most important and intimate aspects of our lives, it’s about language and perception, it’s about our memory of things, it’s about our dreams, love, hate, it’s about morality, our sense of right and wrong, it’s about when things go wrong as in depression, our anxiety, it’s about happiness. "})
training_data.append({"class":"Psychology", "sentence":"fraud theories "})
training_data.append({"class":"Psychology", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"Psychology", "sentence":"want, need, have, thinking,always, a, an, as, such as, for example, like."})


training_data.append({"class":"Philosophy", "sentence":"History is Philosophy teaching by examples."})
training_data.append({"class":"Philosophy", "sentence":"Metaphysics is a dark ocean without shores or lighthouse, strewn with many a philosophic wreck."})
training_data.append({"class":"Philosophy", "sentence":"Science is what you know. Philosophy is what you don't know."})
training_data.append({"class":"Philosophy", "sentence":"here is only one thing a philosopher can be relied upon to do, and that is to contradict other philosophers."})
training_data.append({"class":"Philosophy", "sentence":"If God did not exist, it would be necessary to invent Him."})
training_data.append({"class":"Philosophy", "sentence":"Socrates, William of Ockham, Thomas Hobbes, René Descartes, Bishop George Berkeley."})
training_data.append({"class":"Philosophy", "sentence":"Does God have supreme power?"})
training_data.append({"class":"Philosophy", "sentence":"Will the world be a better place if caste and religion cease to exist?"})
training_data.append({"class":"Philosophy", "sentence":"What is the meaning of true love?"})
training_data.append({"class":"Philosophy", "sentence":"Why do we strive for perfection if it is not attainable?"})
training_data.append({"class":"Philosophy", "sentence":"Does free will exist, or is every action predetermined?"})
training_data.append({"class":"Philosophy", "sentence":"What is human consciousness?"})
training_data.append({"class":"Philosophy", "sentence":"Why do we do things we do not like to do?"})
training_data.append({"class":"Philosophy", "sentence":"Do atheists make their own gods?"})
training_data.append({"class":"Philosophy", "sentence":"Can artificial intelligence be creative?"})
training_data.append({"class":"Philosophy", "sentence":"If judgment is for God, why do we pass judgment?"})
training_data.append({"class":"Philosophy", "sentence":"Can religious beliefs affect scientific thinking?"})
training_data.append({"class":"Philosophy", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"Philosophy", "sentence":"want, need, have, thinking,always, deep, a, an, as, such as, for example, like."})

training_data.append({"class":"Drawing and painting ", "sentence":"HOW TO DRAW & PAINT FASTER?"})
training_data.append({"class":"Drawing and painting ", "sentence":"Are you struggling to get your Art projects done on time? Some students – even those who are dedicated and hard-working – find it challenging to work at the pace required in a Visual Art course."})
training_data.append({"class":"Drawing and painting", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"Drawing and painting", "sentence":"want, need, have, thinking, always, a, an, as, such as, for example, like."})

training_data.append({"class":"Playing music ", "sentence":"I have always maintained that learning how to play an instrument is beneficial."})
training_data.append({"class":"Playing music ", "sentence":"Have you ever felt chills down your spine while listening to music?"})
training_data.append({"class":"Playing music ", "sentence":"How powerful the effects of music, though, depends on your personality."})
training_data.append({"class":"Playing music ", "sentence":"Music has impacted me helping my ability to do math and to read, and to think critically."})
training_data.append({"class":"Playing music", "sentence":"When you play a musical instrument, you have to learn about tone and about scores and your ability to store audio information becomes better."})
training_data.append({"class":"Playing music", "sentence":"Popular Woodwind Instruments: Flute, Piccolo, Shakuhachi, Clarinet, Bassoon, Conch, English horn, Oboe, Saxophone, Shehnai, Bagpipe, Pianica, Harmonica."})
training_data.append({"class":"Playing music", "sentence":"Popular Percussion Instruments: Drum, Congo, Djembe, Duff, Tabla, Dhol, Nagara, Cymbals, Bells, Xylophone, Marimba, Triangle, Tambourine."})
training_data.append({"class":"Playing music", "sentence":"Popular Brass Instruments: Trumpet, Trombone, Bugle, French horn, Tuba, Alto Horn, Bazooka, Cimbasso, Flatt trumpet."})
training_data.append({"class":"Playing music", "sentence":"Popular String Instruments: Guitar, Violin, Viola, Sitar, Cello, Double Bass, Mandolin, Banjo, Harp, Sarod, Santoor."})
training_data.append({"class":"Playing music", "sentence":"Popular Electronic Instruments: Piano keyboards, Octopads, Rhythm machines, Samplers, Synthesizers, Synclavier, Theremin, Eigenharp, Mellotron, Omnichord."})
training_data.append({"class":"Playing music", "sentence":"I, you, him, her, she, he, they, their, us, a, an, as, such as, for example, like."})
training_data.append({"class":"Playing music", "sentence":"want, need, have, thinking, always, take."})
training_data.append({"class":"Playing music", "sentence":"music course, music sessions."})

training_data.append({"class":"Shopping and online shopping", "sentence":"Here are some shopping tips to help you get the most from the money you spend."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Keep your receipts."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Don’t use a credit card if you can’t afford the price."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Try before you buy."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Ask family and friends"})
training_data.append({"class":"Shopping and online shopping", "sentence":"Confirm the full price."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Watch for sales, coupons and rebates."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Consider negotiating."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Find the best overall value — quality, service and price."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Inspect products before you buy."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Understand the warranty."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Know the return policy."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Save your receipt."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Take advantage of membership discounts."})
training_data.append({"class":"Shopping and online shopping", "sentence":"When you shop online, you have to start by searching for a product. This can be done by visiting a store's website"})
training_data.append({"class":"Shopping and online shopping", "sentence":"some sites like Amazon and Yahoo! make it possible for them to display products or build their own online stores for a monthly fee."})
training_data.append({"class":"Shopping and online shopping", "sentence":"Other websites like eBay and Bidz provide an auction format, in which sellers can display items for a minimum price and buyers can bid on these items until the listing ends or the seller chooses to award it to a buyer."})
training_data.append({"class":"Shopping and online shopping", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"Shopping and online shopping", "sentence":"want, need, have, thinking, always, a, an, as, such as, for example, like."})
training_data.append({"class":"Shopping and online shopping", "sentence":"shopping, in the mall, in the store, dresses, blouses, shirts, pants, shorts, bras, swimsuits, hats, belts, sunglasses, accessories, slippers, shoes, boots, sandals, sneakers, sketchers, heels, socks, tops, trousers, jeans, coats, jacckets, pullovers, pjamas, t-shirts."})

training_data.append({"class":"Perfumes", "sentence":"How to Choose the Right Perfume or Cologne."})
training_data.append({"class":"Perfumes", "sentence":"Comforting fragrance for cold winter days."})
training_data.append({"class":"Perfumes", "sentence":"Is body odor a big turn off for you."})
training_data.append({"class":"Perfumes", "sentence":"Do you like to wear your favorite perfume for that crucial meeting?"})
training_data.append({"class":"Perfumes", "sentence":"Well, if you can relate to the above situations, it means you love fragrance."})
training_data.append({"class":"Perfumes", "sentence":"Perfumes and deodorants are popular today."})
training_data.append({"class":"Perfumes", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"Perfumes", "sentence":"want, need, have, thinking,always, a, an, as, such as, for example, like."})

training_data.append({"class":"Cooking ", "sentence":"I love cooking"})
training_data.append({"class":"Cooking ", "sentence":"I am following some amazing cooking recipes"})
training_data.append({"class":"Cooking ", "sentence":"The kitchen not only taught me the art of food, but also prepared me to be a better developer."})
training_data.append({"class":"Cooking ", "sentence":"prepare home-cooked meals can seem like a daunting task."})
training_data.append({"class":"Cooking ", "sentence":"Food brings people together and cooking at home is a great way to unite your family over the dining table. "})
training_data.append({"class":"Cooking ", "sentence":"It is a passion of mine. Having spent almost 25 years in kitchens and catering events. "})
training_data.append({"class":"Cooking ", "sentence":"Personally, I love to cook and bake."})
training_data.append({"class":"Cooking ", "sentence":"There is something magical about taking some flour, yeast, salt and water and coming out with a delicious, sustaining bread"})
training_data.append({"class":"Cooking ", "sentence":"Taking day old mashed potatoes and leftover meatloaf to make Potato Balls."})
training_data.append({"class":"Cooking ", "sentence":"Hunting through the refrigerator, collecting the ingredients, preparing them and putting them together to make something delicious."})
training_data.append({"class":"Cooking ", "sentence":"Seeing how different veggies, meat and spices combine to give those gorgeous flavors, makes you really happy."})
training_data.append({"class":"Cooking", "sentence":"I, you, him, her, she, he, they, their, us."})
training_data.append({"class":"Cooking", "sentence":"want, need, have, thinking, always, a, an, as, such as, for example, like."})

corpus_words = {}
class_words = {}
# turn a list into a set (of unique items) and then a list again (this removes duplicates)
classes = list(set([a['class'] for a in training_data]))
for c in classes:
    # prepare a list of words within each class
    class_words[c] = []

# loop through each sentence in our training data
for data in training_data:
    # tokenize each sentence into words
    for word in nltk.word_tokenize(data['sentence']):
        # ignore a some things
        if word not in ["?", "'s"]:
            # stem and lowercase each word
            stemmed_word = stemmer.stem(word.lower())
            # have we not seen this word already?
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            # add the word to our words in class list
            class_words[data['class']].extend([stemmed_word])

# we now have each stemmed word and the number of occurances of the word in our training corpus (the word's commonality)
#print ("Corpus words and counts: %s \n" % corpus_words)
# also we have all words in each class
#print ("Class words: %s" % class_words)

######################################3
def get_wordnet_pos(word):

    '''Map POS tag to first character lemmatize() accepts'''
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def ie_preprocess(sentence):
    #print (sentence)
    #doc_content = sentence
    filtered_sentence = []
    categories = {}


    #convert text to lowercase
    sentence = sentence.lower()

    #remove numbers
    sentence = re.sub(r'[\d-]+ ', '', sentence)

    #remove punctuation
    sentence = re.sub(r'[!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~]+', '', sentence)

    #set stop words and tokenize sentences
    stop_words = set(stopwords.words('english'))
    sentence_tokens = nltk.sent_tokenize(sentence)

    #perform word tokenization
    for word in sentence_tokens:
        word_tokens = nltk.word_tokenize(word)

    #remove stopwords, apply POS tagging
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    #NER, do we need this
    st = StanfordNERTagger('stanford-ner/classifiers/english.muc.7class.distsim.crf.ser.gz',
					   'stanford-ner/stanford-ner.jar',
					   encoding='utf-8')
    #print(st.tag(filtered_sentence))


    #lemmatize
    result = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in filtered_sentence]

    return result

# calculate a score for a given class
def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word in class_words[class_name]):
            # treat each word with same weight
            score += 1

            if show_details:
                print ("   match: %s" % stemmer.stem(word))
    return score

# we can now calculate a score for a new sentence
#sentence = "good day to start exercising"

# now we can find the class with the highest score
#for c in class_words.keys():
    #print ("Class: %s  Score: %s \n" % (c, calculate_class_score(sentence, c)))

#############################

#sentence = " good day to start exercising?"
def calculate_class_score_commonality(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for data in ie_preprocess(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(data) in class_words[class_name]:
            # treat each word with relative weight
            score += (1 / corpus_words[stemmer.stem(data)])

            if show_details:
                print ("   match: %s (%s)" % (stemmer.stem(data, 1 / corpus_words[stemmer.stem(data)])))
    return score

#for c in class_words.keys():
#   print ("Class: %s  Score: %s \n" % (c, calculate_class_score_commonality(sentence, c)))



def classify_interest(sentence):
    high_class = None
    high_score = 0
    # loop through our classes
    for c in class_words.keys():
        # calculate score of sentence for each class
        score = calculate_class_score_commonality(sentence, c, show_details=False)
        # keep track of highest score
        if score > high_score:
            high_class = c
            high_score = score

    return high_class
def convertSpeech():
    #refactor
    r = sr.Recognizer()
    mic = sr.Microphone()

    #record
    with mic as source:
        print("Say Something:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    #recognize & convert
        try:
            text = r.recognize_google(audio)

            if str is bytes:
                result = u"{}".format(text).encode("utf-8")
            else:
                result = "{}".format(text)
        except:
            result = "Sorry could not recognize your voice."
    print (result)
    return result
#print (classify_interest("i want to start regular exercising "))
#print (classify_interest("what is the oldest known picasso painting"))
#print (classify_interest("do you like coding in java "))
#print (classify_interest("i played basketball last week "))
#print (classify_interest("what does fraud said about rods "))
#print (classify_interest("i was wonering how many calories needed for me per day"))
#print (classify_interest(" i am done preprocessing the text but still figuring out the classifier"))
#print (classify_interest("i always have these deep thoughts about the universe and god."))
#print (classify_interest("what do you think of that dress on me?"))
#print (classify_interest("i have cooked an amazing cake yesterday."))
#print (classify_interest("you smelled very nice today, what was the perfume you were wearing?"))
#print (classify_interest("i am thinking of taking the music course as an elective"))
#print (classify_interest("i will eat chicken"))

speechTxt = convertSpeech()
if speechTxt == 'Sorry could not recognize your voice.':
    print ("error")
else:
    print ("we think you might be interested in: %s" % classify_interest(speechTxt))
