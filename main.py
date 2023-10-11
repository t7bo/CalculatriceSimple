from division import division
from addition import addition
from soustraction import soustraction
from multiplication import multiplication

nombre1, operateur, nombre2 = float(input("Entre un premier nombre : ")), input("choisis ton opérateur de calcul : "), float(input("Entre un deuxième nombre : "))

if operateur == "/":
    # print(division(nombre1,nombre2))
    print(f""" .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  Texas Instruments     T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | {nombre1} {operateur} {nombre2}   
| | |                                   | | |
| | |     {division(nombre1,nombre2)}   
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---


""")
elif operateur == "+":
    # print(addition(nombre1,nombre2))
    print(f""" .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  Texas Instruments     T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | {nombre1} {operateur} {nombre2}   
| | |                                   | | |
| | |     {addition(nombre1,nombre2)}   
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---


""")
elif operateur == "-":
    #print(soustraction(nombre1,nombre2))
    print(f""" .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  Texas Instruments     T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | {nombre1} {operateur} {nombre2}   
| | |                                   | | |
| | |     {soustraction(nombre1,nombre2)}   
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---


""")
elif operateur == "*":
    #print(multiplication(nombre1,nombre2))
    print(f""" .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  Texas Instruments     T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | {nombre1} {operateur} {nombre2}   
| | |                                   | | |
| | |     {multiplication(nombre1,nombre2)}   
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---


""")
else:
    #print("Erreur d'opérateur")
    print(f""" .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  Texas Instruments     T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | {nombre1} {operateur} {nombre2}   
| | |                                   | | |
| | |        Erreur d'opérateur   
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---


""")
