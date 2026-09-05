from logo import logo
from widget import *

clear_terminal()

if __name__ == "__main__":
    print(logo)
    try:
        # getting inputs
        update_config_value()
        # setup
        
        loader("initializing...")
        print("\r>>> [●] Server is Live now!\n")

    except Exception:
        print("\r>>> Failure at setup...")
        loader("Stoping...", sec=3)
        print("\rServer down. Try any later!.")
        
    try:
        print(f">>> [?] {get_greeting()}! How can I assist you? ::")
        while True:
            # input
            prompt = input(">>> ").strip()
            if prompt:
                # output
                print("\n>>> 💭 Insight...\n")            
                for chunk in ask_llm(prompt):
                    print(chunk, end="", flush=True)
                print("\n")

    except KeyboardInterrupt:
        print("\r[!] /server/status   :: STOPPING...\n")
        loader("Stoping...", sec=5)
        print("\r>>> Standing by for future requests. Goodbye! ✨")

