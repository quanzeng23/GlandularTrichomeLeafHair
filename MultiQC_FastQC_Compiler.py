import os
import subprocess

# Input directory containing FastQC zip files
input_directory = "/Volumes/T7 Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/FastQC_After_Trim_Resequenced"

# Output directory for MultiQC report (same as input directory)
output_directory = input_directory

# Find all FastQC zip files in the input directory
fastqc_files = [f for f in os.listdir(input_directory) if f.endswith("_fastqc.zip")]

# Create a list of paths to FastQC zip files
fastqc_paths = [os.path.join(input_directory, f) for f in fastqc_files]

# Run MultiQC to compile the FastQC reports
multiqc_command = ["multiqc", "-o", output_directory] + fastqc_paths
subprocess.run(multiqc_command)
