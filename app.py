from logo import logo
from widget import *

clear_terminal()

if __name__ == "__main__":
    print(logo)
    loader("initializing...")
    print("\r>>> ⚪ Server is Live now!\n")
    
    try:
        print(">>> Describe your need")
        while True:
            # input
            prompt = input(">>> ")
            # output
            print("\n>>> 💭 Insight...\n")            
            for chunk in ask_llm(prompt):
                print(chunk, end="", flush=True)
            print("\n")

    except KeyboardInterrupt:
        print("\r>>> Stopping server...")
        loader("Stoping...")
        print("\rServer down. Standing by for future requests. Goodbye! ✨")


