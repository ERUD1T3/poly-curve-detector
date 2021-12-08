# poly-curve-detector
AI Project to detect polynomial curve and output the equation coefficients based on the curve image.

To run this project, you need to install PyTorch and use either Jupyter Notebook or VSCode to open the source files.

To prevent confusion, the source code is split between three files. One is a script for generating the data plots. And the other two are the same notebook adjusted so that one runs our custom network, and the other runs using dense net.

The primary files are plotGenerationScript and developmentCustomNetwork. developmentDenseNet is a modification of the custom network notebook to use dense net.

To run these scripts, you will need to change the root variables to match your machine.
For the plotGenerationScript, you should only have to change the first root variable at the beginning. This root will be where you want to create the dataset. There will also be a folder needed for adding the background images. This should be on the same level as the 'workingDir' folder and a download link will be provided in the report appendix.

 developmentCustomNetwork will require the dataset to be downloaded or generated, and the root and datapath variables will need to set to point to where it is stored on your machine. The developmentDenseNet should be the same, with the extra file path for storing the checkpoints.

Once file paths have been correctly set, each script can be run by running each cell in the notebook from the top to the bottom in order. The label for each cell will be in the header above it.

For the plotGenerationScript, you may want to adjust the numPlots variable to change the amount of plots that will be generated.

For the network notebooks, you may want to adjust the EPOCHS variable and numLoops variables to change how much the network runs. The last runnable cell in the notebook is used to test the network after running the training loop. You may want to change the imagenum variable to go between test items. (This cell will only run if the network has trained at least one batch of data.) Commented out code is not runnable.
