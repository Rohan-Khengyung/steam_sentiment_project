# src/prepare_dataset.py
import os
import random
import pandas as pd

random.seed(42)

POSITIVE_TEMPLATES = [
    "Absolutely love this game, the graphics are stunning and gameplay is smooth.",
    "Best game I have played in years. Highly recommended!",
    "The story is amazing and the characters are well written.",
    "Great value for money. Hours of fun and still not bored.",
    "Multiplayer is fantastic and the community is friendly.",
    "Beautiful soundtrack and immersive world. 10/10.",
    "I can't stop playing. Truly a masterpiece.",
    "The combat system is deep and rewarding.",
    "Updates keep coming and the devs actually listen.",
    "Perfect for relaxing after a long day.",
    "Ran perfectly on my PC, no crashes at all.",
    "The open world feels alive and full of detail.",
    "Fun with friends, fun solo, just fun overall.",
    "Addictive gameplay loop with lots of content.",
    "One of the best indie games I have ever bought.",
    "Genuinely surprised by how good this turned out.",
    "Great modding support and active community.",
    "Controls are responsive and the UI is clean.",
    "The ending was emotional and satisfying.",
    "Definitely worth full price, would buy again.",
]

NEGATIVE_TEMPLATES = [
    "Terrible optimization, it crashes every ten minutes.",
    "Waste of money. Boring gameplay and bad graphics.",
    "Full of bugs, unplayable on my system.",
    "The devs abandoned this game after launch.",
    "Pay to win mechanics ruin the experience.",
    "Repetitive missions and lazy level design.",
    "Multiplayer is dead, can't find a single match.",
    "Story makes no sense and the voice acting is awful.",
    "Constant lag and desync in online mode.",
    "Feels like an unfinished early access game.",
    "Refunded after 30 minutes. Do not buy.",
    "Ads everywhere, even after paying full price.",
    "Terrible controls, no way to remap keys.",
    "The game is a broken mess on PC.",
    "Boring, empty world with nothing to do.",
    "Crashes on startup, no fix from developers.",
    "Bad AI, enemies just stand there.",
    "Overpriced for what is basically a mobile game.",
    "Save files get corrupted randomly.",
    "Worst purchase of the year. Avoid.",
]

POSITIVE_PREFIX = ["", "Honestly, ", "Seriously, ", "Just, ", "Man, ", "Dude, ", "Wow, "]
NEGATIVE_PREFIX = ["", "Honestly, ", "Seriously, ", "Just, ", "Man, ", "Dude, ", "Wow, "]

def build_rows(n_per_class=1000):
    rows = []
    for _ in range(n_per_class):
        p = random.choice(POSITIVE_PREFIX) + random.choice(POSITIVE_TEMPLATES)
        rows.append({"review": p, "sentiment": "positive"})
        n = random.choice(NEGATIVE_PREFIX) + random.choice(NEGATIVE_TEMPLATES)
        rows.append({"review": n, "sentiment": "negative"})
    random.shuffle(rows)
    return rows

def main():
    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", "steam_reviews.csv")

    if os.path.exists(out_path):
        print(f"[INFO] Dataset already exists at {out_path}. Skipping generation.")
        return

    print("[INFO] Generating synthetic Steam review dataset...")
    rows = build_rows(n_per_class=1000)
    df = pd.DataFrame(rows)
    df.to_csv(out_path, index=False)
    print(f"[INFO] Saved {len(df)} rows to {out_path}")

if __name__ == "__main__":
    main()
