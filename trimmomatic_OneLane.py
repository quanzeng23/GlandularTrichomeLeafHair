import os
import subprocess

# Define input and output directories
input_dir = "/Users/jamesstandish/Downloads/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/Raw_RNAseq"
output_dir = "/Users/jamesstandish/Downloads/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/Trimmed_RNAseq"
adapter_file = "/Users/jamesstandish/Downloads/Coding_Stuff/Trimmomatic-0.39/adapters/TruSeq3-PE.fa"
quality_settings = [
    "LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:20", "MINLEN:100"
]

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define a list of sample names (without file extensions)
sample_names = [	
	"GlandularTrichome1_S1",
	"GlandularTrichome2_S2",
	"GlandularTrichome3_S3",
	"GlandularTrichome4_S4",
	"GlandularTrichome5_S5",
	"GlandularTrichome6_S6",
	"GlandularTrichome7_S7",
	"GlandularTrichome8_S8",
	"GlandularTrichome9_S9",
	"GlandularTrichome10_S10",
	"GlandularTrichome11_S11",
	"GlandularTrichome12_S12",
	"LeafHair1_S13",
	"LeafHair2_S14",
	"LeafHair3_S15",
	"LeafHair4_S16",
	"LeafHair5_S17",
	"LeafHair6_S18",
	"LeafHair7_S19",
	"LeafHair8_S20",
	"LeafHair9_S21",
	"PureEa1_S22",
	"PureEa2_S23",
	"PureEa3_S24",
	"PureEa4_S25"
	]

for sample_name in sample_names:
    input_file_R1 = os.path.join(input_dir, f"{sample_name}_R1.fastq.gz")
    input_file_R2 = os.path.join(input_dir, f"{sample_name}_R2.fastq.gz")
    output_file_R1_paired = os.path.join(output_dir, f"{sample_name}_R1_paired.fastq.gz")
    output_file_R1_unpaired = os.path.join(output_dir, f"{sample_name}_R1_unpaired.fastq.gz")
    output_file_R2_paired = os.path.join(output_dir, f"{sample_name}_R2_paired.fastq.gz")
    output_file_R2_unpaired = os.path.join(output_dir, f"{sample_name}_R2_unpaired.fastq.gz")

    # Build the Trimmomatic command
    trimmomatic_command = [
        "trimmomatic", "PE", "-threads", "4",
        input_file_R1, input_file_R2,
        output_file_R1_paired, output_file_R1_unpaired,
        output_file_R2_paired, output_file_R2_unpaired,
        "ILLUMINACLIP:" + adapter_file + ":2:30:10:2:keepBothReads"
    ] + quality_settings

    # Run Trimmomatic using subprocess
    subprocess.run(trimmomatic_command)

print("Trimming complete")

# 	"S001_6dash11_2022",
#	"S001_6dash11_2022",
#	"S002_6dash11dash2_2022",
#	"S002_6dash11dash2_2022",
#	"S003_BPdash3_2022",
#	"S003_BPdash3_2022",
#	"S004_BPdash2_2022",
#	"S004_BPdash2_2022",
#	"S005_NTB_2022",
#	"S005_NTB_2022",
#	"S006_NT_2022",
#	"S006_NT_2022",
#	"S007_9dash6dash1_2022",
#	"S007_9dash6dash1_2022",
#	"S008_9dash6dash2_2022",
#	"S008_9dash6dash2_2022",
#	"S009_1dash2dash3_2023",
#	"S010_1dash2dash4_2023",
#	"S010_1dash2dash4_2023",
#	"S011_1dash2dash5_2023",
#	"S011_1dash2dash5_2023",
#	"S012_6dash11dash1_2023",
#	"S013_6dash11dash2_2023",
#	"S013_6dash11dash2_2023",
#	"S014_6dash11dash4_2023",
#	"S014_6dash11dash4_2023",
#	"S015_9dash6dash2_2023",
#	"S015_9dash6dash2_2023",
#	"S016_9dash6dash6_2023",
#	"S016_9dash6dash6_2023",
#	"S017_9dash6dash7_2023",
#	"S018_BPdash3_2023",
#	"S018_BPdash3_2023",
#	"S019_BPdash4_2023",
#	"S019_BPdash4_2023",
#	"S020_BPdash5_2023",
#	"S020_BPdash5_2023",
#	"S021_NTdash1_2023",
#	"S021_NTdash1_2023",
#	"S022_NTdash4_2023",
#	"S022_NTdash4_2023",
#	"S023_NTdash5_2023",
#	"S023_NTdash5_2023",
#	"S024_NTdash6_2023",
#	"S024_NTdash6_2023"
