# Config
path_input = "tracyImageProcessing-input.txt"
path_output = "tracyImageProcessing-output.txt"

# Get input:
restored_matrix = []
with open(path_input, "r") as file:
    for line in file:
        row = line.strip().split(",")
        restored_matrix.append(row)

# Now to figure out how to actually process the data :/
print(restored_matrix)
processed_matrix = restored_matrix

# Write output:
with open(path_output, "w") as file:
    for row in processed_matrix:
        line = ",".join(row)
        file.write(line + "\n")