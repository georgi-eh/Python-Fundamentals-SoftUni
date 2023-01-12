num_of_snowballs = int(input())
snowball_scores = []
snowball_weights = []
snowball_times = []
snowball_qualities = []

for snowball in range(num_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    score = (weight / time_needed) ** quality

    snowball_scores.append(score)
    snowball_weights.append(weight)
    snowball_times.append(time_needed)
    snowball_qualities.append(quality)

best_ball_idx = snowball_scores.index(max(snowball_scores))
best_weight = snowball_weights[best_ball_idx]
best_time = snowball_times[best_ball_idx]
best_quality = snowball_qualities[best_ball_idx]
best_score = snowball_scores[best_ball_idx]

print(f"{best_weight} : {best_time} = {int(best_score)} ({best_quality})")
