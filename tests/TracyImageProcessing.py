# Config
path_input = "tracyImageProcessing-input.txt"
path_outputClusters = "tracyImageProcessing-output_clusters.txt"
path_outputInstructions = "tracyImageProcessing-output_instructions.txt"

# Get input:
restored_matrix = []
with open(path_input, "r") as file:
    for line in file:
        row = line.strip().split(",")
        restored_matrix.append(row)

print(restored_matrix)

# Process Matrix into Clusters
def find_clusters(grid):
    height = len(grid)
    width = len(grid[0])

    visited = set()
    clusters = []

    for y in range(height):
        for x in range(width):

            if (x, y) in visited:
                continue

            value = grid[y][x]
            cluster = []

            stack = [(x, y)]

            while stack:
                cx, cy = stack.pop()

                if (cx, cy) in visited:
                    continue

                if grid[cy][cx] != value:
                    continue

                visited.add((cx, cy))
                cluster.append((cx, cy))

                for dx, dy in [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ]:
                    nx = cx + dx
                    ny = cy + dy

                    if 0 <= nx < width and 0 <= ny < height:
                        stack.append((nx, ny))

            clusters.append({
                "value": value,
                "points": cluster
            })

    return clusters

cluster_matrix = find_clusters(restored_matrix)
print(cluster_matrix)

# Create instructions


# Write output:
#with open(path_output, "w") as file:
#    for row in cluster_matrix:
#        line = ",".join(row)
#        file.write(line + "\n")
with open(path_outputClusters, "w") as file:
    for cluster in cluster_matrix:
        val = cluster["value"]
        # Convert points tuple list [(0,0), (1,0)] to string format "0:0 1:0"
        points_str = " ".join([f"{x}:{y}" for x, y in cluster["points"]])
        
        # Write formatted row: value, followed by its pixel coordinates
        file.write(f"Value: {val} | Points: {points_str}\n")