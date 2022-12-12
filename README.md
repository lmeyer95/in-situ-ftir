# in-situ-Raman
Overview: This code is designed to work with jack-palm/in-situ-ftir code and adapt it for use with Raman spectroscopy. The code adapted for Raman is designed to handle 36 spectra in a map rather than one individual spectrum. 

Code 1: This script sorts a Raman map containing 36 spectra into 36 individual spectra. 

Code 2: This code pulls in the 36 individual spectra and corrects the baseline using the Pybaselines package. This code then normalizes the spectra to a specified peak location. 

Code 3: This code uses the multispec fitting algorithm developed in jack-palm/in-situ-ftir to fit Gaussians to spectroscopy data. There are slight deveiations from the multipeak fitting code developed for FTIR.

Code 5: This script meaausres the fluorescence background from a Raman spectrum and plots changes over time. 
