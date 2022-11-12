def Wikipedia(Assunto):


    import wikipedia
    import re
    import dock


    name = input("O nome:")
    wikipedia.set_lang('pt') 
    title = input('Sua pesquisa')
    run = True
    while run:
        try:
            wiki = wikipedia.page(title)
            break
        except:
            print('Nome invalido')
            title = input('Digite outra vez:')

    text = wiki.content


    print(text)

