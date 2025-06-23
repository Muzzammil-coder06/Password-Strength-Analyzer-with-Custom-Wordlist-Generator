import argparse
from analyzer import analyze_password
from wordlist_generator import generate_wordlist, export_wordlist

parser = argparse.ArgumentParser(description="Password Analyzer and Wordlist Generator")

parser.add_argument("--password", help="Password to analyze")
parser.add_argument("--inputs", nargs='+', help="Names, dates, pet names for custom wordlist")
parser.add_argument("--export", action="store_true", help="Export wordlist to file")

args = parser.parse_args()

if args.password:
    result = analyze_password(args.password)
    print("\n[+] Password Strength Analysis:")
    print(f"Score: {result['score']}/4")
    print(f"Crack Time Estimate: {result['crack_time']}")
    print(f"Feedback: {result['feedback']['warning']}")
    print(f"Suggestions: {', '.join(result['feedback']['suggestions'])}")

if args.inputs:
    print("\n[+] Generating Wordlist...")
    wordlist = generate_wordlist(args.inputs)
    print(f"Generated {len(wordlist)} words.")
    if args.export:
        export_wordlist(wordlist)
