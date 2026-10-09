def get_infra_metrify():
    return {
        "cpu_usage": 0.5,
        "memory_usage": 0.5,
        "disk_usage": 0.5,
        "network_usage": 0.5,
        "cpu_temperature": 0.5,
        "memory_temperature": 0.5,
        "disk_temperature": 0.5,
        "network_temperature": 0.5,
        "cpu_frequency": 0.5,
        "memory_frequency": 0.5,
        "disk_frequency": 0.5,
    }

## Run the code if the file is run directly
if __name__ == "__main__":
    print(get_infra_metrify())