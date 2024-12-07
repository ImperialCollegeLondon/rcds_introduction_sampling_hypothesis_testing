# Load necessary library
library(ggplot2)

# Set seed for reproducibility
set.seed(42)

# The Law of Large Numbers (LLN) .....................................................................
cat("The law of large numbers (LLN)\n")

# Parameters
# num_samples <- 50 # Number of samples for LLN
# num_samples <- 500 # Number of samples for LLN
num_samples <- 5000 # Number of samples for LLN

# True mean for comparison
dice_mean <- 3.5 # True mean for a six-sided die

# Dice Running Mean
dice_rolls <- sample(1:6, num_samples, replace = TRUE) # Simulate 5000 dice rolls
dice_running_mean <- cumsum(dice_rolls) / seq_along(dice_rolls)

# Prepare data for plotting
df <- data.frame(
  RollNumber = 1:num_samples,
  RunningMean = dice_running_mean
)

# Plot running mean
ggplot(df, aes(x = RollNumber, y = RunningMean)) +
  geom_line(color = "skyblue", size = 1) +
  geom_hline(yintercept = dice_mean, color = "red", linetype = "dashed", size = 1) +
  labs(
    title = "Law of Large Numbers - Dice Roll Running Mean",
    x = "Number of Rolls",
    y = "Mean of Dice Rolls"
  ) +
  theme_minimal() +
  annotate("text", x = num_samples * 0.8, y = dice_mean + 0.2, 
           label = paste("True Mean =", dice_mean), color = "red")
