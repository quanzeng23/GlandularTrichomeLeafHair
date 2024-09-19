import subprocess

# Define the list of sample names
sample_names = [
	"PureEa1_S22_Aligned.out.sam",
	"PureEa2_S23_Aligned.out.sam",
	"PureEa3_S24_Aligned.out.sam",
	"PureEa4_S25_Aligned.out.sam"
]

# Define the input and output directories
input_dir = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/STAR_alignments"
output_dir = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/HTseq_Counts"
gff_file = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/genome_data/ncbi_dataset/data/GCF_000027205.1/Ea_ATCC_49946_Genome_Features.gff"

# Create the output directory if it doesn't exist
import os
os.makedirs(output_dir, exist_ok=True)

# Run htseq-count for each sample
for sample_name in sample_names:
    input_file = os.path.join(input_dir, sample_name)
    output_file = os.path.join(output_dir, f"{sample_name.replace('_Aligned.out.sam', '_htseq.txt')}")

    # Build the htseq-count command
    htseq_command = [
        "htseq-count",
        "--idattr=ID",
        "--stranded=no",
        input_file,
        gff_file,
    ]

    # Redirect the output to the specified file
    htseq_command.append(">")
    htseq_command.append(output_file)

    # Convert the command list to a string
    htseq_command_str = " ".join(htseq_command)

    # Execute htseq-count using subprocess
    try:
        subprocess.run(htseq_command_str, shell=True, check=True, executable="/bin/bash")
        print(f"htseq-count for {sample_name} completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running htseq-count for {sample_name}: {e}")
        
#	"S001_6dash11_2022_Aligned.out.sam",
#	"S002_6dash11dash2_2022_Aligned.out.sam",
#	"S003_BPdash3_2022_Aligned.out.sam",
#	"S004_BPdash2_2022_Aligned.out.sam",
#	"S005_NTB_2022_Aligned.out.sam",
#	"S006_NT_2022_Aligned.out.sam",
#	"S007_9dash6dash1_2022_Aligned.out.sam",
#	"S008_9dash6dash2_2022_Aligned.out.sam",
#	"S009_1dash2dash3_2023_Aligned.out.sam",
#	"S010_1dash2dash4_2023_Aligned.out.sam",       
#   "S011_1dash2dash5_2023_Aligned.out.sam",
#	"S012_6dash11dash1_2023_Aligned.out.sam",
#	"S013_6dash11dash2_2023_Aligned.out.sam",
#	"S014_6dash11dash4_2023_Aligned.out.sam",
#	"S015_9dash6dash2_2023_Aligned.out.sam",
#	"S016_9dash6dash6_2023_Aligned.out.sam",
#	"S017_9dash6dash7_2023_Aligned.out.sam",
#	"S018_BPdash3_2023_Aligned.out.sam",
#	"S019_BPdash4_2023_Aligned.out.sam",
#	"S020_BPdash5_2023_Aligned.out.sam",
#	"S021_NTdash1_2023_Aligned.out.sam",
#	"S022_NTdash4_2023_Aligned.out.sam",
#	"S023_NTdash5_2023_Aligned.out.sam",
#	"S024_NTdash6_2023_Aligned.out.sam" 
