
import random
import time

player = {
    "ism": "",
    "hp": 100,
    "max_hp": 100,
    "coin": 100,
    "level": 1,
    "xp": 0,
    "damage": 15,
    "potion": 3
}

dushmanlar = [
    {"ism": "Goblin", "hp": 30, "damage": 8, "coin": 20},
    {"ism": "Ork", "hp": 50, "damage": 12, "coin": 35},
    {"ism": "Ajdar", "hp": 100, "damage": 20, "coin": 70},
    {"ism": "Skelet", "hp": 40, "damage": 10, "coin": 25}
]


def kutish():
    time.sleep(1)


def menyu():
    print("\n========== RPG O'YINI ==========")
    print("1. Jang qilish")
    print("2. Do'kon")
    print("3. Qahramon haqida")
    print("4. Davolanish")
    print("5. Inventar")
    print("6. Sarguzasht")
    print("0. O'yindan chiqish")
    print("================================")


def profil():
    print("\n======= QAHRAMON =======")
    print("Ism:", player["ism"])
    print("HP:", player["hp"], "/", player["max_hp"])
    print("Level:", player["level"])
    print("XP:", player["xp"])
    print("Coin:", player["coin"])
    print("Damage:", player["damage"])
    print("========================")


def level_up():
    kerakli_xp = player["level"] * 50

    if player["xp"] >= kerakli_xp:
        player["xp"] -= kerakli_xp
        player["level"] += 1
        player["max_hp"] += 20
        player["damage"] += 5
        player["hp"] = player["max_hp"]

        print("\n🎉 LEVEL OSHDI!")
        print("Yangi level:", player["level"])
        print("Damage oshdi!")
        print("HP tiklandi!")


def jang():
    dushman = random.choice(dushmanlar).copy()

    print("\n⚔️", dushman["ism"], "paydo bo'ldi!")

    while dushman["hp"] > 0 and player["hp"] > 0:

        print("\nSening HP:", player["hp"])
        print(dushman["ism"], "HP:", dushman["hp"])

        print("1. Hujum")
        print("2. Qochish")

        tanlov = input("Tanlov: ")

        if tanlov == "1":
            zarba = random.randint(
                player["damage"] - 5,
                player["damage"] + 5
            )

            dushman["hp"] -= zarba

            print("Sen", zarba, "damage berding!")

            if dushman["hp"] <= 0:
                print("\n🏆 Dushman mag'lub bo'ldi!")
                player["coin"] += dushman["coin"]
                player["xp"] += 30

                print("Coin olindi:", dushman["coin"])
                print("30 XP olindi!")

                level_up()
                break

            zarar = random.randint(1, dushman["damage"])
            player["hp"] -= zarar

            print("Dushman senga", zarar, "damage berdi!")

        elif tanlov == "2":
            print("Sen jangdan qochding!")
            break

        else:
            print("Noto'g'ri tanlov!")

    if player["hp"] <= 0:
        player["hp"] = 1
        print("\n💀 Qahramon mag'lub bo'ldi!")
        print("Senga 1 HP qoldi!")


def dokon():
    while True:
        print("\n======= DO'KON =======")
        print("1. HP potion - 30 coin")
        print("2. Damage +5 - 100 coin")
        print("3. HP +20 - 60 coin")
        print("0. Chiqish")

        tanlov = input("Tanlov: ")

        if tanlov == "1":
            if player["coin"] >= 30:
                player["coin"] -= 30
                player["potion"] += 1
                print("Potion sotib olindi!")
            else:
                print("Coin yetarli emas!")

        elif tanlov == "2":
            if player["coin"] >= 100:
                player["coin"] -= 100
                player["damage"] += 5
                print("Damage oshirildi!")
            else:
                print("Coin yetarli emas!")

        elif tanlov == "3":
            if player["coin"] >= 60:
                player["coin"] -= 60
                player["max_hp"] += 20
                player["hp"] += 20
                print("HP oshirildi!")
            else:
                print("Coin yetarli emas!")

        elif tanlov == "0":
            break

        else:
            print("Xato tanlov!")


def davolanish():
    if player["potion"] > 0:
        player["potion"] -= 1
        player["hp"] += 40

        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]

        print("❤️ HP tiklandi!")
    else:
        print("Potion qolmagan!")


def inventar():
    print("\n======= INVENTAR =======")
    print("HP potion:", player["potion"])
    print("Coin:", player["coin"])
    print("Damage:", player["damage"])
    print("========================")


def sarguzasht():
    print("\n🌲 Sen sirli o'rmonga kirding...")
    kutish()

    hodisa = random.randint(1, 3)

    if hodisa == 1:
        print("Dushman uchradi!")
        jang()

    elif hodisa == 2:
        mukofot = random.randint(20, 60)
        player["coin"] += mukofot
        print("💰", mukofot, "coin topding!")

    else:
        print("Sehrli buloq topding!")
        player["hp"] = player["max_hp"]
        print("HP to'liq tiklandi!")


def game():
    print("🔥 RPG O'YINIGA XUSH KELIBSAN!")
    player["ism"] = input("Qahramoning ismini yoz: ")

    print("\nSalom,", player["ism"])
    print("Sarguzashtlar boshlanmoqda...")

    while True:
        menyu()

        tanlov = input("Tanlovni kiriting: ")

        if tanlov == "1":
            jang()

        elif tanlov == "2":
            dokon()

        elif tanlov == "3":
            profil()

        elif tanlov == "4":
            davolanish()

        elif tanlov == "5":
            inventar()

        elif tanlov == "6":
            sarguzasht()

        elif tanlov == "0":
            print("O'yin tugadi. Xayr!")
            break

        else:
            print("Noto'g'ri buyruq!")


game()
