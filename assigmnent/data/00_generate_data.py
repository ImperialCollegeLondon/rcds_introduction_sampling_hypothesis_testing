# Generate a set of measurements for the Higgs boson mass
# One set simulates the results from CMS, the other from ATLAS

# Import libraries
import numpy as np
import pandas as pd

# Parameters for the simulated measurements
cms_mean = 125.09  # Mean Higgs mass from CMS (in GeV)
cms_std_dev = 0.24  # Standard deviation for CMS (in GeV)
atlas_mean = 125.36  # Mean Higgs mass from ATLAS (in GeV)
atlas_std_dev = 0.18  # Standard deviation for ATLAS (in GeV)
lhcb_mean = 125.50  # Hypothetical mean Higgs mass from LHCb (in GeV)
lhcb_std_dev = 0.22  # Hypothetical standard deviation for LHCb (in GeV)

# Number of measurements to simulate
num_measurements = 1000  # You can adjust this number

# Generate simulated Higgs mass measurements for CMS, ATLAS, LHCb
cms_measurements = np.random.normal(cms_mean, cms_std_dev, num_measurements)
atlas_measurements = np.random.normal(atlas_mean, atlas_std_dev, num_measurements)
lhcb_measurements = np.random.normal(lhcb_mean, lhcb_std_dev, num_measurements)

# Create pandas dataframe
cms_df = pd.DataFrame(cms_measurements, columns = ["Higgs_Mass_CMS"])
atlas_df = pd.DataFrame(atlas_measurements, columns = ["Higgs_Mass_ATLAS"])
lhcb_df = pd.DataFrame(lhcb_measurements, columns = ["Higgs_Mass_LHCb"])

# Save measurements to csv files
cms_df.to_csv("higgs_mass_cms.csv", index = False)
atlas_df.to_csv("higgs_mass_atlas.csv", index = False)
lhcb_df.to_csv("higgs_mass_lhcb.csv", index = False)

# Print output statement
print("Generated CMS Higgs mass measurements")
print("Generated ATLAS Higgs mass measurements")
print("Generated LHCb Higgs mass measurements")
