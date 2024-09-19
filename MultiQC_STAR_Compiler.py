import os
import subprocess

# Input directory containing STAR log files 
input_directory = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/STAR_alignments_Resequenced"

# Output directory for MultiQC report (same as input directory)
output_directory = input_directory

# Find all STAR log files in the input directory
star_log_files = [f for f in os.listdir(input_directory) if f.endswith("Log.final.out")]


# Create a list of paths to STAR log files
star_log_paths = [os.path.join(input_directory, f) for f in star_log_files]

# Run MultiQC to compile the STAR log files
multiqc_command = ["multiqc", "-o", output_directory] + star_log_paths
subprocess.run(multiqc_command)

