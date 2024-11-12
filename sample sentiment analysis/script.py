from textblob import TextBlob
import os

def analyze_sentiment(text):
    # Creazione dell'oggetto TextBlob
    analysis = TextBlob(text)
    
    # Ottiene il punteggio di polarità (-1 molto negativo, +1 molto positivo)
    polarity = analysis.sentiment.polarity
    
    # Ottiene il punteggio di soggettività (0 oggettivo, 1 soggettivo)
    subjectivity = analysis.sentiment.subjectivity
    
    return polarity, subjectivity

def interpret_sentiment(polarity):
    if polarity > 0:
        return "Positivo"
    elif polarity < 0:
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
            polarity, subjectivity = analyze_sentiment(content)
            
            # Stampa i risultati
            print("\n" + "="*50)
            print(f"Analisi del file: {file_name}")
            print("="*50)
            print(f"Polarità: {polarity:.3f} ({interpret_sentiment(polarity)})")
            print(f"Soggettività: {subjectivity:.3f}")
            
            # Aspetta l'input dell'utente prima di procedere
            input("\nPremi Invio per continuare...")
            
        except FileNotFoundError:
            print(f"Errore: Il file {file_name} non è stato trovato.")
        except Exception as e:
            print(f"Si è verificato un errore durante l'analisi di {file_name}: {str(e)}")
    
    print("\nAnalisi completata!")

if __name__ == "__main__":
    # Verifica che TextBlob sia installato
    try:
        import textblob
    except ImportError:
        print("TextBlob non è installato. Installalo usando:")
        print("pip install textblob")
        exit(1)
        
    main()