import datetime

# Define sample system health check output
system_health_output = [
    "2024-06-07 11:48:45,256 - INFO - Starting system health check...",
    "2024-06-07 11:48:46,258 - INFO - CPU usage: 2.1%",
    "2024-06-07 11:48:46,274 - WARNING - High memory usage detected: 84.1%",
    "2024-06-07 11:48:46,274 - WARNING - Low disk space detected: 99.7% used",
    "2024-06-07 11:48:46,284 - WARNING - High number of running processes detected: 317",
    "2024-06-07 11:48:46,284 - INFO - System health check completed."
]

# Function to parse a single line of system health output
def parse_system_health_line(line):
  timestamp, level, message = line.split(" - ", 2)
  return {
    "timestamp": datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S,%f"),
    "level": level,
    "message": message
  }

# Parse all lines of system health output
parsed_output = [parse_system_health_line(line) for line in system_health_output]

# Analyze system health based on parsed output
for entry in parsed_output:
  if entry["level"] == "WARNING":
    print(f"Warning: {entry['message']}")

# Print overall system health status (assuming success if no warnings)
if not any(entry["level"] == "WARNING" for entry in parsed_output):
  print("System health check successful.")