import os
import shutil
input_folder_path=ftp://ftp.ensemblgenomes.org/pub/fungi/release-46/fasta/saccharomyces_cerevisiae/cdna/
output_folder_path = duplicate_genes.fa


def c(input_folder, output_folder,duplication):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

 # Use the os.walk function to find recognition sequences containing 'duplication' in the input folder   
  for root, _, files in os.walk(input_folder):
     for file in files:
      file_path = os.path.join(root, file)
      with open(file_path, 'r') as f:
      content = f.read()
      if 'duplication' in content:
      new_file_path = os.path.join(output_folder, file)
      shutil.copyfile(file_path, new_file_path)
