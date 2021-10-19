# Barplot race chart creator

Code to create an .mp4 format barplot race chart. 

Command to build the image:

```
docker build -t bar_race .
```

The input for the program is a .csv file called **names_input.xlsx** which should be put in the data/ directory. An example file with the needed structure is located via **data/names_input_example.xlsx**.

The parameters for the drawing of the simulation are located in the **conf.yml** file. An example file structure is presented in **conf-example.yml**.

Command to create a bar race .mp4 file in the **output/** directory:

```
docker-compose up
```