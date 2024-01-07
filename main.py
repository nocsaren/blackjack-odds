from bj_functions import initial_deal                       # (num_players=1, deck_size=6)  -> df, remaining_cards
from bj_functions import calculate_hand_value               # hand                          -> total_value
from bj_functions import is_blackjack                       # hand                          -> bool
from bj_functions import hit, double_down                   # remaining_cards               -> card



num_players = 16
deck_size = 1
initial_deal_df, remaining_cards = initial_deal(num_players, deck_size)
print("\n--- First Phase: Simulating Deal ---")
print(initial_deal_df)

for player in initial_deal_df.columns:
    hand = initial_deal_df[player]
    total_value = calculate_hand_value(hand)
    if is_blackjack(hand):
        print(f"{player} has a blackjack!")
    else: 
        print(f"{player} is at {total_value}.")
num_rem_cards = len(remaining_cards)
print(f"\n Remaining Cards:({num_rem_cards})\n {remaining_cards}")

print("\n--- Second Phase: Simulating Hits and Double Downs ---")

for player in initial_deal_df.columns:
    hand = initial_deal_df[player].tolist()
    total_value = calculate_hand_value(hand)

    if total_value < 17:
        new_card = hit(remaining_cards)
        hand.append(new_card)
        total_value = calculate_hand_value(hand)
        initial_deal_df.at[1, player] = hand
        print(initial_deal_df)
        print(f"{player} hits and gets {new_card}. New total: {total_value}")

    if total_value == 21:
        print(f"{player} has 21!")
    elif 9 <= total_value <= 11:
        new_card = double_down(remaining_cards)
        hand.append(new_card)
        total_value = calculate_hand_value(hand)
        initial_deal_df.at[1, player] = hand
        print(f"{player} doubles down, gets {new_card}. New total: {total_value}")

    if total_value > 21:
        print(f"{player} busts!")
    elif total_value != 21:
        print(f"{player} stands at {total_value}.")

# Print updated hands after hits and double downs
print("\n--- Updated Hands after Hits and Double Downs ---")
for player in initial_deal_df.columns:
    hand = initial_deal_df[player].tolist()
    print(f"{player}: {hand}")

print("\n--- Remaining Cards after Hits and Double Downs ---")
num_rem_cards = len(remaining_cards)
print(f"\n Remaining Cards:({num_rem_cards})\n {remaining_cards}")