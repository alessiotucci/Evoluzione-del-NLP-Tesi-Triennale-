from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def analyze_sentiment(text):
    # Creazione dell'oggetto SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Ottiene il punteggio di sentiment
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
    # Lista dei file da analizzare
    files = ["Elezioni_positivo.txt", "Elezioni_neutro.txt", "Elezioni_negativo.txt"]
    
    for file_name in files:
        try:
            # Legge il contenuto del file
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Analizza il sentimento
            compound, pos, neu, neg = analyze_sentiment(content)
            
            # Stampa i risultati
            print("\n" + "="*50)
            print(f"Analisi del file: {file_name}")
            print("="*50)
            print(f"Polarità: {compound:.3f} ({interpret_sentiment(compound)})")
            print(f"Positivo: {pos:.3f}")
            print(f"Neutro: {neu:.3f}")
            print(f"Negativo: {neg:.3f}")
            
            # Aspetta l'input dell'utente prima di procedere
            input("\nPremi Invio per continuare...")
            
        except FileNotFoundError:
            print(f"Errore: Il file {file_name} non è stato trovato.")
        except Exception as e:
            print(f"Si è verificato un errore durante l'analisi di {file_name}: {str(e)}")
    
    print("\nAnalisi completata!")

if __name__ == "__main__":
    main()
