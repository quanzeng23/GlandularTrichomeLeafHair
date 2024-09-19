import os
import subprocess

# Define input and output directories
input_dir = "/Volumes/T7 Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/Resequenced_Trimmed_RNAseq"
output_dir = "/Volumes/T7 Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/FastQC_After_Trim_Resequenced"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

input_files = [
    "GlandularTrichome2_merged_R1_paired.fastq.gz",
    "GlandularTrichome2_merged_R2_paired.fastq.gz",
    "GlandularTrichome6_merged_R1_paired.fastq.gz",
    "GlandularTrichome6_merged_R2_paired.fastq.gz",
    "GlandularTrichome8_merged_R1_paired.fastq.gz",
    "GlandularTrichome8_merged_R2_paired.fastq.gz",
    "GlandularTrichome9_merged_R1_paired.fastq.gz",
    "GlandularTrichome9_merged_R2_paired.fastq.gz",
    "GlandularTrichome10_merged_R1_paired.fastq.gz",
    "GlandularTrichome10_merged_R2_paired.fastq.gz",
    "LeafHair2_merged_R1_paired.fastq.gz",
    "LeafHair2_merged_R2_paired.fastq.gz",
    "LeafHair3_merged_R1_paired.fastq.gz",
    "LeafHair3_merged_R2_paired.fastq.gz",
    "LeafHair8_merged_R1_paired.fastq.gz",
    "LeafHair8_merged_R2_paired.fastq.gz",
    "LeafHair9_merged_R1_paired.fastq.gz",
    "LeafHair9_merged_R2_paired.fastq.gz"
]

# Run FastQC for each input file
for input_file in input_files:
    input_path = os.path.join(input_dir, input_file)
    subprocess.run(["fastqc", "-t", "8", "-o", output_dir, input_path])

print("FastQC analysis completed.")
