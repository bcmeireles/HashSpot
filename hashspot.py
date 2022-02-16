import os
import os.path


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

hash_lenghts = {
    4 : ["CRC16"],
    8 : ["CRC32b",
    "CRC32",
    "ADLER32"],
    16 : ["MD5-half",
    "MySQL 3.2.3",],
    32 : ["MD5",
    "LanManager Hash",
    "RIPEMD128",
    "MD5 HMAC"],
    40 : ["SHA1",
    "HAVAL160",
    "Tiger160",
    "RIPEMD160"],
    48 : ["Tiger192",
    "HAVAL192"],
    56 : ["SHA224",
    "HAVAL224"],
    64 : ["SHA256",
    "GOST Hash",
    "RIPEMD256",
    "HAVAL256"],
    80 : ["RIPEMD320"],
    96 : ["SHA384"],
    128 : ["Whirpool",
    "SHA512"]
}

def check_hash(h):
    l = len(h)

    if h[:3] == "0x0":
        if l == 54:
            return "MSSQL 2005"
        elif l == 94:
            return "MSSQL 2000"

    elif "$" in h:
        if l == 36:
            return "FreeBSD nthash"

    elif "/" in h:
        if l == 24:
            return "CRYPT16"

    elif (sum(1 for c in h if c.isupper())) == 1:
        if l == 13:
            return "DES Crypt"
    
    else:
        try:
            return hash_lenghts[l]
        except:
            return False

def logo():
    print("""
            ______              
         .-'      `-.           
       .'            `.         
      /                \        
     ;                 ;`       
     |     HashSpot    |;       
     ;                 ;|
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/



""")

def menu():
    an = input("""Choose an option:

[1] Check unique hash
[2] Bulk checking
[3] Exit

>> """)

    if an not in ["1", "2", "3"]:
        input("\nInvalid answer, press enter to continue")
        clear()
        logo()
        menu()

    if an == "1":
        h = input("\nPlease provide the hash to check: ")
        result = check_hash(h)

        if result:
            print(f"Possible results for {h}, in order from the most likely to the less likely:")
            print(*result, sep = ", ")

    elif an == "2":
        while True:
            filename = input("\nPlease provide the name of the text file with the hashes to check: ")

            if not ".txt" in filename:
                filename += ".txt"

            if os.path.exists(filename):
                break
            else:
                print(f"\n{filename} was not found. Please check the file name. ")

        filenameout = input("\nPlease provide the name of the text file to output the results to: ")

        if not ".txt" in filenameout:
            filenameout += ".txt"

        with open(filename, "r") as f:
            hashes = f.readlines()
            total = len(hashes)
            count = 0

        with open(filenameout, "a") as f:
            for h in hashes:
                result = check_hash(h.strip())
                if result:
                    count += 1
                    f.write(f"</.>\n{h.strip()}\n{result}\n")

        print("\nChecking...")
        print(f"\nSuccessfully checked {count} of {total} hashes. Results are ordered from most likely to less likely.")
            
logo()
menu()

input("\n\nPress ENTER to go back to the main menu.")
clear()
logo()
menu()