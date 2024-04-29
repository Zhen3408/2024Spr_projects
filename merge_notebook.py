import nbformat

# Load the notebooks
nb1 = nbformat.read('Final_Project_zl.ipynb', as_version=4)
nb2 = nbformat.read('Final_Project_wjh.ipynb', as_version=4)

# Combine the notebooks
nb1.cells.extend(nb2.cells)

# Save the new notebook
with open('merged_notebook.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb1, f)


