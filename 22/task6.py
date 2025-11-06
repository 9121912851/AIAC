def estimate_energy_and_emissions(gpu_hours, power_kw=0.3, carbon_intensity=0.4):
    """
    Estimate energy usage and CO₂ emissions for AI workloads.

    Parameters:
    - gpu_hours: Total GPU usage in hours
    - power_kw: Average power draw per GPU in kilowatts (default 0.3 kW = 300W)
    - carbon_intensity: CO₂ per kWh in kg (default 0.4 kg CO₂/kWh)

    Returns:
    - energy_kwh: Total energy consumed
    - emissions_kg: Estimated CO₂ emissions
    """
    energy_kwh = gpu_hours * power_kw
    emissions_kg = energy_kwh * carbon_intensity
    return energy_kwh, emissions_kg

# Example usage
gpu_usage_hours = 1000  # e.g., 1000 GPU hours for training or inference
energy, emissions = estimate_energy_and_emissions(gpu_usage_hours)

print(f"🔋 Estimated Energy Consumption: {energy:.2f} kWh")
print(f"🌍 Estimated CO₂ Emissions: {emissions:.2f} kg CO₂")