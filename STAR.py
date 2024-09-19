import subprocess

# STAR command template
STAR_COMMAND = "STAR --runThreadN 16 --runMode alignReads --genomeDir /Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/STAR_Index_Genome"


# Array of sample names
samples = [
	"GlandularTrichome2_merged",
	"LeafHair2_merged",
	"LeafHair3_merged",
	"LeafHair8_merged",
	"LeafHair9_merged"
]

# Input directory for all samples
input_dir = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/Resequenced_Trimmed_RNAseq"

# Output directory for all samples
output_dir = "/Volumes/T7_Shield/Leaf_Hair_Glandular_Trichomes_Erwinia_Genome_RNAseq_Data/STAR_alignments_Resequenced"

# Process each sample
for sample in samples:
    # Process R1 and R2 files for the current sample simultaneously
    input_files = [
        f"{input_dir}/{sample}_R1_paired.fastq.gz",
        f"{input_dir}/{sample}_R2_paired.fastq.gz"
    ]
    
    # Decompress the input files
    subprocess.run(f"gunzip {' '.join(input_files)}", shell=True, check=True)
    decompressed_files = [input_file[:-3] for input_file in input_files]  # Remove ".gz" extension

    # Prepare STAR command with the decompressed input files
    star_command = f"{STAR_COMMAND} --readFilesIn {' '.join(decompressed_files)} --outFileNamePrefix {output_dir}/{sample}_"

    # Execute the STAR command
    try:
        subprocess.run(star_command, shell=True, check=True)
        print(f"STAR analysis for {sample} (R1 and R2) completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running STAR analysis for {sample} (R1 and R2): {e}")

    # Compress the input files again
    subprocess.run(f"gzip {' '.join(decompressed_files)}", shell=True, check=True)