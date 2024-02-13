def translate():
    while True:
        from translate import Translator
        import time as t
        text=input("\nEnter word to be translated:")
        fr=input("Which is the language of the word inputed:")
        rs=input("Which language is the word be translated:")
        translator= Translator(from_lang=fr,to_lang=rs)
        translation = translator.translate(text)
        print('''
OUTPUT:''')
        print(translation)
        t.sleep(2)
        x=input("\nContinue? [Y/N]:")
        if x in 'Nn':
            break
translate() 
