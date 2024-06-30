import openai 
openai.api_key= [Your secret api key]
def chatbot (prompt):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[{"role":"user", "content":prompt}]
      
    )
    return(response.choice[0].message.content.strip())
if __name__=="__main__":
    while True:
        input= input("You:")
        if input.lower() in ["quit","exit","bye"]:
            break
        response=chatbot(input)
        print("chatbot :" , response)

