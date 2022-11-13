def textSp(text1, langs):

        import gtts 
        
        language = langs
        
        speech = gtts.tts.gTTS(text=text1, lang=language, slow=False)
        speech.save("mario.mp3")
        
       
        

textSp("Hello")
