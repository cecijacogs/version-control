from datetime import datetime

# Define the output file path
output_file = "version.md"

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to the file
with open(output_file, "w") as f:
    f.write(f"Version generated on: {current_time}\n")

print(f"Version info written to {output_file}")
