import os
import subprocess

# Define input and output directories
input_dir = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/Resequenced_Raw_Data"
output_dir = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/Resequenced_Trimmed_RNAseq"
adapter_file = "/Users/jamesstandish/Downloads/Coding_Stuff/Trimmomatic-0.39/adapters/TruSeq3-PE.fa"
quality_settings = [
    "LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:20", "MINLEN:100"
]

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define a list of sample names (without file extensions)
sample_names = [
    "GlandularTrichome2",
	"GlandularTrichome6",
	"GlandularTrichome8",
	"GlandularTrichome9",
	"GlandularTrichome10",
	"LeafHair2",
	"LeafHair3",
	"LeafHair8",
	"LeafHair9"  
]

for sample_name in sample_names:
    # Modify input and output file paths for R1 and R2 for both lanes
    input_file_R1_lane1 = os.path.join(input_dir, f"{sample_name}_L001_R1.fastq.gz")
    input_file_R2_lane1 = os.path.join(input_dir, f"{sample_name}_L001_R2.fastq.gz")
    input_file_R1_lane2 = os.path.join(input_dir, f"{sample_name}_L002_R1.fastq.gz")
    input_file_R2_lane2 = os.path.join(input_dir, f"{sample_name}_L002_R2.fastq.gz")
    
    output_file_R1_paired_lane1 = os.path.join(output_dir, f"{sample_name}_L001_R1_paired.fastq.gz")
    output_file_R1_unpaired_lane1 = os.path.join(output_dir, f"{sample_name}_L001_R1_unpaired.fastq.gz")
    output_file_R2_paired_lane1 = os.path.join(output_dir, f"{sample_name}_L001_R2_paired.fastq.gz")
    output_file_R2_unpaired_lane1 = os.path.join(output_dir, f"{sample_name}_L001_R2_unpaired.fastq.gz")

    output_file_R1_paired_lane2 = os.path.join(output_dir, f"{sample_name}_L002_R1_paired.fastq.gz")
    output_file_R1_unpaired_lane2 = os.path.join(output_dir, f"{sample_name}_L002_R1_unpaired.fastq.gz")
    output_file_R2_paired_lane2 = os.path.join(output_dir, f"{sample_name}_L002_R2_paired.fastq.gz")
    output_file_R2_unpaired_lane2 = os.path.join(output_dir, f"{sample_name}_L002_R2_unpaired.fastq.gz")

    # Build the Trimmomatic command for both lanes
    trimmomatic_command_lane1 = [
        "trimmomatic", "PE", "-threads", "4",
        input_file_R1_lane1, input_file_R2_lane1,
        output_file_R1_paired_lane1, output_file_R1_unpaired_lane1,
        output_file_R2_paired_lane1, output_file_R2_unpaired_lane1,
        "ILLUMINACLIP:" + adapter_file + ":2:30:10:2:keepBothReads"
    ] + quality_settings
    
    trimmomatic_command_lane2 = [
        "trimmomatic", "PE", "-threads", "4",
        input_file_R1_lane2, input_file_R2_lane2,
        output_file_R1_paired_lane2, output_file_R1_unpaired_lane2,
        output_file_R2_paired_lane2, output_file_R2_unpaired_lane2,
        "ILLUMINACLIP:" + adapter_file + ":2:30:10:2:keepBothReads"
    ] + quality_settings

    # Run Trimmomatic for both lanes
    subprocess.run(trimmomatic_command_lane1)
    subprocess.run(trimmomatic_command_lane2)

    # Merge the trimmed files from both lanes into one file
    merged_output_R1_paired = os.path.join(output_dir, f"{sample_name}_merged_R1_paired.fastq.gz")
    merged_output_R2_paired = os.path.join(output_dir, f"{sample_name}_merged_R2_paired.fastq.gz")
    
    with open(output_file_R1_paired_lane1, "rb") as file1, open(output_file_R1_paired_lane2, "rb") as file2, open(merged_output_R1_paired, "wb") as outfile:
        outfile.write(file1.read())
        outfile.write(file2.read())
    
    with open(output_file_R2_paired_lane1, "rb") as file1, open(output_file_R2_paired_lane2, "rb") as file2, open(merged_output_R2_paired, "wb") as outfile:
        outfile.write(file1.read())
        outfile.write(file2.read())

print("Trimming and merging complete")
