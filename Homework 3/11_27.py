# Marco Lopez 1537013
# CIS 2348-17255

def add_player(roster):
    jersey_number = int(input("Enter a new player's jersey number: "))
    rating = int(input("Enter the player's rating: "))
    roster[jersey_number] = rating


def remove_player(roster):
    jersey_number = int(input("Enter a jersey number: "))
    if jersey_number in roster:
        del roster[jersey_number]


def update_player_rating(roster):
    jersey_number = int(input("Enter a jersey number: "))
    if jersey_number in roster:
        new_rating = int(input("Enter a new rating for player: "))
        roster[jersey_number] = new_rating


def output_players_above_rating(roster):
    rating_threshold = int(input("Enter a rating: "))
    print("\nABOVE", rating_threshold)
    for jersey_number, rating in sorted(roster.items()):
        if rating > rating_threshold:
            print("Jersey number: {}, Rating: {}".format(jersey_number, rating))


def output_roster(roster):
    print("ROSTER")
    for jersey_number, rating in sorted(roster.items()):
        print("Jersey number: {}, Rating: {}".format(jersey_number, rating))


def main():
    roster = {}

    for i in range(5):
        print("Enter player {}'s jersey number:".format(i + 1))
        jersey_number = int(input())
        print("Enter player {}'s rating:".format(i + 1))
        rating = int(input())
        print()  # Add a newline after entering each player's details
        roster[jersey_number] = rating

    output_roster(roster)

    while True:
        print("\nMENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")

        choice = input("\nChoose an option:\n")

        if choice == 'a':
            add_player(roster)
        elif choice == 'd':
            remove_player(roster)
        elif choice == 'u':
            update_player_rating(roster)
        elif choice == 'r':
            output_players_above_rating(roster)
        elif choice == 'o':
            output_roster(roster)
        elif choice == 'q':
            break


if __name__ == "__main__":
    main()

