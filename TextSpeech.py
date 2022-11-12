




def textSp(text1):

        import gtts 
        
        language = "en"
        
        speech = gtts.tts.gTTS(text=text1, lang=language, slow=False)
        speech.save("mario.mp3")
        
       
        

textSp("Hello")
