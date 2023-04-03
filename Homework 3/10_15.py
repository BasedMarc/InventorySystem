# Marco Lopez 1537013
# CIS 2348-17255

class Team:
    def __init__(self, team_names='none', team_win=0, team_loss=0):
        self.team_name = team_names
        self.team_wins = team_win
        self.team_losses = team_loss

    def get_win_percentage(self):
        # Calculate win percentage using floating-point division
        win_percentages = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentages


if __name__ == "__main__":
    # Read input values
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    # Create Team object with input values
    team = Team(team_name, team_wins, team_losses)

    # Get win percentage
    win_percentage = team.get_win_percentage()

    # Print the result based on the win percentage
    if win_percentage >= 0.5:
        print("Congratulations, Team {} has a winning average!".format(team_name))
    else:
        print("Team {} has a losing average.".format(team_name))
