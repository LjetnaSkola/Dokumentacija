import argparse
# kreiraj parser
parser = argparse.ArgumentParser(description='Skript koji kalkulise ukupnu cijenu od kolicine, jedinicne cijene'
                                             ' i eventualno popusta')
# dodaj argumente
parser.add_argument('-q', '--quantity', type=int, required=True, help='Kolicina')
parser.add_argument('-p', '--price', type=float, dest='cijena', required=True, help='Jedinicna cijena')
parser.add_argument('-d', '--discount', type=float, help='Popust')
parser.add_argument('-v', '--verbose', help='Omoguci debug printove', action='store_true', default=False)
# zbog ovog action store_true ne treba se upisivati vrijednost, samo -v i ako ima /v onda je true, ako ga nema onda je False
# isparsiraj
args = parser.parse_args()

# ne treba ona provjera da li su argumenti prazni

if args.verbose:
    print("[DBG] izracunavanje popusta")

discount = 0.0 if args.discount is None else args.discount # ako argument nije unesen, onda 0

if args.verbose:
    print(f"[DBG] Popust: ${discount}")

if args.verbose:
    print("[DBG] ukupne cijene")
# izracunaj ukupno kostanje
total_cost = args.quantity * args.cijena * (1 - discount / 100)
# obratiti paznju na liniju 7 i parametar dest. nema ga u drugim dodavanjima argumenata u parser
# Ako parametra dest nema, kao sto je slucaj kod quantity ili discount, onda se naziv uzima iz dugackog imena
# Ako ima parametra dest, onda je to naziv. zato imamo args.cijena, a ne args.price

# obratiti paznju na ovaj print
print(f"Ukupna cijena: ${total_cost:.2f}")

# python 15_parser_argumenata2.py -h
# python 15_parser_argumenata2.py -q 2 -p 10
# python 15_parser_argumenata2.py -q 3 -p 11.4 -d 10 -v