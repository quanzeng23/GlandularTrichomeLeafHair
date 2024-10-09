# Load necessary libraries
library(ggplot2)
library(readr)
library(dplyr)
library(cowplot)

# Define consistent font sizes for all plots
axis_title_size <- 18
axis_text_size <- 16
plot_title_size <- 20
legend_text_size <- 16
legend_title_size <- 18

# Define consistent x-axis limits for alignment
x_limit <- c(-10, 10)  # Adjust this limit based on your data

# Define consistent y-axis limit for volcano plots (if needed)
y_limit <- c(0, 250)  # Adjust this limit based on your data

# --------------------------------------
# Plot A: Glandular Trichome Volcano Plot
# --------------------------------------
data_gt <- read_delim("~/Downloads/GT_LH_Data/GT_All_Genes.txt", delim = "\t")
data_gt$Significance <- ifelse(data_gt$Padj > 0.05,
                               "Not Statistically Significant",
                               ifelse(abs(data_gt$log2_FC) < 1,
                                      "Not Differentially Expressed",
                                      ifelse(data_gt$log2_FC > 1, "Upregulated", "Downregulated")))
data_gt$Ams_Gene <- ifelse(data_gt$Old_Locus_Tag %in% paste0("EAM_", 2163:2174), "Ams Gene", "Not Ams Gene")
highlighted_genes <- c(paste0("EAM_", 2871:2911), "EAM_2190", "EAM_2697", "EAM_0423")
data_gt$T3SS_Gene <- ifelse(data_gt$Old_Locus_Tag %in% highlighted_genes, "T3SS Gene", "Not T3SS Gene")
data_gt$Gene_Type <- ifelse(data_gt$Ams_Gene == "Ams Gene", "Ams Gene",
                            ifelse(data_gt$T3SS_Gene == "T3SS Gene", "T3SS Gene", "Other"))
data_gt$Significance <- factor(data_gt$Significance, levels = c("Not Differentially Expressed", "Not Statistically Significant", "Upregulated", "Downregulated"))
data_gt$Gene_Type <- factor(data_gt$Gene_Type, levels = c("Ams Gene", "T3SS Gene", "Other"))

volcano_plot_gt <- ggplot(data_gt) +
  geom_point(aes(x = log2_FC, y = -log10(Padj), color = Significance, shape = Gene_Type, alpha = ifelse(Gene_Type == "Other", 0.5, 1)), size = 2) +
  scale_color_manual(values = c("Not Differentially Expressed" = "black", "Not Statistically Significant" = "yellow", "Upregulated" = "red", "Downregulated" = "blue")) +
  scale_shape_manual(values = c("Ams Gene" = 17, "T3SS Gene" = 15, "Other" = 16)) +
  geom_hline(yintercept = -log10(0.05), linetype = "dashed") +
  geom_vline(xintercept = c(-1, 1), linetype = "dashed") +
  theme_minimal() +
  theme(axis.title = element_text(size = axis_title_size),
        axis.text = element_text(size = axis_text_size),
        plot.title = element_text(size = plot_title_size, face = "bold"),
        legend.text = element_text(size = legend_text_size),
        legend.title = element_text(size = legend_title_size)) +
  labs(title = expression(DEGs~of~italic(E.~amylovora)~","~Glandular~Trichomes),
       x = "Log2 Fold Change",
       y = "-Log10 Adjusted P-value",
       color = "Significance") +
  xlim(x_limit)

# --------------------------------------
# Plot B: Glandular Trichome Kegg Plot
# --------------------------------------
data_kegg_gt <- read.csv("/Users/jamesstandish/Downloads/GT_LH_Data/GlandularTrichomeKeggCatsInterest.tsv", sep = "\t")
data_kegg_gt$Regulation <- factor(data_kegg_gt$Regulation, levels = c("down", "up"))

counts_gt <- data_kegg_gt %>%
  group_by(Kegg_Pathway) %>%
  summarize(down_count = sum(Log2FoldChange < -1, na.rm = TRUE), up_count = sum(Log2FoldChange > 1, na.rm = TRUE), total_count = down_count + up_count) %>%
  arrange(total_count)

data_kegg_gt$Kegg_Pathway <- factor(data_kegg_gt$Kegg_Pathway, levels = counts_gt$Kegg_Pathway)

keggplot_gt <- ggplot(data_kegg_gt, aes(x = Log2FoldChange, y = Kegg_Pathway)) +
  geom_point(aes(size = abs(Log2FoldChange), fill = padj), shape = 21, position = position_jitter(width = 0, height = 0.15)) +
  scale_fill_gradient(low = "lightblue", high = "darkblue") +
  geom_vline(xintercept = 0, linetype = "dashed") +
  theme_minimal() +
  theme(axis.title.x = element_text(size = axis_title_size),
        axis.title.y = element_text(size = axis_title_size),
        axis.text.y = element_text(size = axis_text_size),
        axis.text.x = element_text(size = axis_text_size),
        plot.title = element_text(size = plot_title_size, hjust = 0.5),
        plot.margin = margin(10, 10, 30, 10),
        legend.text = element_text(size = legend_text_size),
        legend.title = element_text(size = legend_title_size)) +
  labs(x = "Log2 Fold Change",
       y = "KEGG Pathway",
       fill = "padj",
       title = "DEGs Within Selected Kegg Pathways, Glandular Trichomes") +
  xlim(x_limit)

# --------------------------------------
# Plot C: Leaf Hair Volcano Plot
# --------------------------------------
data_lh <- read_delim("~/Downloads/GT_LH_Data/LH_All_Genes.txt", delim = "\t")
data_lh$Significance <- ifelse(data_lh$Padj > 0.05, "Not Statistically Significant", ifelse(abs(data_lh$log2_FC) < 1, "Not Differentially Expressed", ifelse(data_lh$log2_FC > 1, "Upregulated", "Downregulated")))
data_lh$Ams_Gene <- ifelse(data_lh$Old_Locus_Tag %in% paste0("EAM_", 2163:2174), "Ams Gene", "Not Ams Gene")
highlighted_genes_lh <- c(paste0("EAM_", 2871:2911), "EAM_2190", "EAM_2697", "EAM_0423")
data_lh$T3SS_Gene <- ifelse(data_lh$Old_Locus_Tag %in% highlighted_genes_lh, "T3SS Gene", "Not T3SS Gene")
data_lh$Gene_Type <- ifelse(data_lh$Ams_Gene == "Ams Gene", "Ams Gene", ifelse(data_lh$T3SS_Gene == "T3SS Gene", "T3SS Gene", "Other"))

volcano_plot_lh <- ggplot(data_lh) +
  geom_point(aes(x = log2_FC, y = -log10(Padj), color = Significance, shape = Gene_Type, alpha = ifelse(Gene_Type == "Other", 0.5, 1)), size = 2) +
  scale_color_manual(values = c("Not Differentially Expressed" = "black", "Not Statistically Significant" = "yellow", "Upregulated" = "red", "Downregulated" = "blue")) +
  scale_shape_manual(values = c("Ams Gene" = 17, "T3SS Gene" = 15, "Other" = 16)) +
  geom_hline(yintercept = -log10(0.05), linetype = "dashed") +
  geom_vline(xintercept = c(-1, 1), linetype = "dashed") +
  theme_minimal() +
  theme(axis.title = element_text(size = axis_title_size),
        axis.text = element_text(size = axis_text_size),
        plot.title = element_text(size = plot_title_size, face = "bold"),
        legend.text = element_text(size = legend_text_size),
        legend.title = element_text(size = legend_title_size)) +
  labs(title = expression(DEGs~of~italic(E.~amylovora)~","~Non-glandular~Trichomes),
       x = "Log2 Fold Change",
       y = "-Log10 Adjusted P-value",
       color = "Significance") +
  xlim(x_limit) +
  ylim(y_limit)

# --------------------------------------
# Plot D: Leaf Hair Kegg Plot
# --------------------------------------
data_kegg_lh <- read.csv("/Users/jamesstandish/Downloads/GT_LH_Data/LeafHairKeggCatsInterest.tsv", sep = "\t")
data_kegg_lh$Regulation <- factor(data_kegg_lh$Regulation, levels = c("down", "up"))

counts_lh <- data_kegg_lh %>%
  group_by(Kegg_Pathway) %>%
  summarize(down_count = sum(Log2FoldChange < -1, na.rm = TRUE), up_count = sum(Log2FoldChange > 1, na.rm = TRUE), total_count = down_count + up_count) %>%
  arrange(total_count)

data_kegg_lh$Kegg_Pathway <- factor(data_kegg_lh$Kegg_Pathway, levels = counts_lh$Kegg_Pathway)

keggplot_lh <- ggplot(data_kegg_lh, aes(x = Log2FoldChange, y = Kegg_Pathway)) +
  geom_point(aes(size = abs(Log2FoldChange), fill = padj), shape = 21, position = position_jitter(width = 0, height = 0.15)) +
  scale_fill_gradient(low = "lightblue", high = "darkblue") +
  geom_vline(xintercept = 0, linetype = "dashed") +
  theme_minimal() +
  theme(axis.title.x = element_text(size = axis_title_size),
        axis.title.y = element_text(size = axis_title_size),
        axis.text.y = element_text(size = axis_text_size),
        axis.text.x = element_text(size = axis_text_size),
        plot.title = element_text(size = plot_title_size, hjust = 0),
        legend.text = element_text(size = legend_text_size),
        legend.title = element_text(size = legend_title_size)) +
  labs(x = "Log2 Fold Change",
       y = "KEGG Pathway",
       fill = "padj",
       title = "DEGs Within Selected Kegg Pathways, Non-glandular Trichomes") +
  xlim(x_limit)

# --------------------------------------
# Combine Plots
# --------------------------------------
combined_plot <- plot_grid(
  plot_grid(volcano_plot_gt, keggplot_gt, labels = c("A", "B"), ncol = 2, rel_widths = c(1, 1)),
  plot_grid(volcano_plot_lh, keggplot_lh, labels = c("C", "D"), ncol = 2, rel_widths = c(1, 1)),
  ncol = 1, rel_heights = c(1, 1.2)  # Adjust overall heights for both rows
)

# Save the combined plot as a PDF with increased figure size
pdf("/Users/jamesstandish/Downloads/GT_LH_Data/Plots/Combined_Plot.pdf", width = 30, height = 16)
print(combined_plot)  # Use print to render the plot within the PDF device
dev.off()  # Close the PDF device
