from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import colorama
from colorama import Fore, Style

def analyze_sentiment(text):
    # Creazione dell'oggetto SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound'], sentiment['pos'], sentiment['neu'], sentiment['neg']

def interpret_sentiment(compound):
    if compound > 0:
        return "Positivo"
    elif compound < 0:
        return "Negativo"
    else:
        return "Neutro"

def main():
    files = ["Elezioni_positivo.txt", "Elezioni_neutro.txt", "Elezioni_negativo.txt"]
    for file_name in files:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
            
            compound, pos, neu, neg = analyze_sentiment(content)
            print(f"{Style.BRIGHT}{Fore.BLUE}\n{'='*50}")
            print(f"{Style.BRIGHT}{Fore.BLUE}Analisi del file: {file_name}")
            print(f"{Style.BRIGHT}{Fore.BLUE}{'='*50}{Style.RESET_ALL}")
            print(f"Polarità: {compound:.3f} ({interpret_sentiment(compound)})")
            print(f"Positivo: {pos:.3f}")
            print(f"Neutro: {neu:.3f}")
            print(f"Negativo: {neg:.3f}")
            input("\nPremi Invio per continuare...")
            
        except FileNotFoundError:
            print(f"Errore: Il file {file_name} non è stato trovato.")
        except Exception as e:
            print(f"Si è verificato un errore durante l'analisi di {file_name}: {str(e)}")
    
    print("\nAnalisi completata!")

if __name__ == "__main__":
    main()
