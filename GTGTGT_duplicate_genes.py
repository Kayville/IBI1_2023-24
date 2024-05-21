# Combine the code from the two questions, first identify all duplicate sequences, and then search for duplicate fragments from them
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

# Define a duplicate function with two parameters
def duplicates(output_folder, target):
    count = 0
    start = 0
    output_folder_path = duplicate_genes.fa
    target=‘GTGTGT’

# Within the loop, continuously search for the index of a specific field in the text to calculate the number of overlapping repetitions until the index no longer exists
    if start < len(output_folder):
        index = output_folder.find(target, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break
            return count
  print(count)

