{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "soc561-HW8_GoogleColab.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPxBPCf4Y5Wf6axpvhGwFal",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/elliotcodes/soc561-Python/blob/main/soc561_HW8_GoogleColab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vOZai0GqLCzA"
      },
      "source": [
        "# Homework 8\n",
        "**Author:** Elliot Ramo  \n",
        "**Course:** FA21 SOC 561 - Programming for the Social Sciences  \n",
        "**Instructor:** Dr. Jennifer Earl  \n",
        "**Task:** Homework 8 - Python  \n",
        "**Related Program:** soc561-HW8.do  "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2tp1EVVqLCPq"
      },
      "source": [
        "**Notes**\n",
        "<p> 1. This file relates to a Stata .do file called \"soc561-HW8.do\"  </p>\n",
        "<p> 2. I took 2 approaches taken to completing the homework assignment to give myself more practice. The function that links all the pieces together loops is in Approach 2.  </p>\n",
        "<p> 3. Mac computers have something called \".DS_Store\" files which help Mac determine how to display folders when they are opened. These folders will break the code below if not cleared out using the relevant code provided in the script . <a href=\"https://macpaw.com/how-to/remove-ds-store-files-on-mac\">Read more here</a>.  </p>\n",
        "</br>\n",
        "\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FwFbTu3yK_X-"
      },
      "source": [
        "#### **&rarr;** **Getting Started**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zJFk7BmOLPu8"
      },
      "source": [
        "# Import packages\n",
        "import os\n",
        "import re\n",
        "import csv"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Rcqzh-FoLNmV"
      },
      "source": [
        "#### **&rarr;** **Working directory: call to online space**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G95n1pW6Lh0G",
        "outputId": "7ca94e26-ae9d-4351-8bda-dba3154650ec"
      },
      "source": [
        "# Clone GitHub Repo\n",
        "!git clone https://github.com/elliotcodes/soc561-Python"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'soc561-Python'...\n",
            "remote: Enumerating objects: 29, done.\u001b[K\n",
            "remote: Counting objects: 100% (29/29), done.\u001b[K\n",
            "remote: Compressing objects: 100% (24/24), done.\u001b[K\n",
            "remote: Total 29 (delta 9), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (29/29), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "UwwEWiqvLn8H",
        "outputId": "88b48df8-4559-4ceb-c47f-fb517658e6ed"
      },
      "source": [
        "# Changing directory\n",
        "os.chdir(r\"/content/soc561-Python/test\")\n",
        "os.getcwd()"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'/content/soc561-Python/test'"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bpfEDRYiLrUU"
      },
      "source": [
        "---\n",
        "# **In Python, do the following:**\n",
        "## Approach 1: Using Nested Loops\n",
        "#### &rarr; **Extract `year` and save as variable, then create dictionary and print to text file**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X5xWEs2jL3zL"
      },
      "source": [
        "# Opening files, extract year (slightly differently), and save as variable\n",
        "with open('babyNames.txt', 'w') as babyNames_File:\n",
        "    for rawfile in os.listdir():\n",
        "        if not rawfile.startswith(\".\"):\n",
        "            file= open(rawfile, 'r')\n",
        "            year= \"\"\n",
        "            for line in file:\n",
        "                ## remove any training characters (e.g., spaces)\n",
        "                line= line.rstrip()\n",
        "                searchYear= re.findall(r'Popularity in ([0-9][0-9][0-9][0-9])',line)\n",
        "                if len(searchYear) > 0: ## length of 'year' > 0\n",
        "                    year=searchYear[0]     \n",
        "            print(year)\n",
        "            \n",
        "            # Create dictionary where rank is the key and names are values associated with the rank key\n",
        "            dictionary= {}\n",
        "            file= open(rawfile, 'r')\n",
        "            for line in file:\n",
        "                line = line.rstrip()\n",
        "                ## string covers (rank)(name)(name) via (\\d+)(\\w+)(\\w+)\n",
        "                string= re.findall(r'<td>(\\d+)</td><td>(\\w+)</td><td>(\\w+)</td>', line)\n",
        "                if len(string) > 0:\n",
        "                    rank=string[0][0]\n",
        "                    male_name=string[0][1]\n",
        "                    female_name=string[0][2]\n",
        "                    ## Make dict where rank=key and names are values associated w key\n",
        "                    dictionary[rank]=(male_name, female_name)  \n",
        "            print(dictionary)\n",
        "            \n",
        "            # Print year + each line of dictionary in comma-delimited file\n",
        "            for key,value in dictionary.items():\n",
        "                rank=key\n",
        "                male_name=value[0]\n",
        "                female_name=value[1]\n",
        "                text= year + \",\" + rank + \",\" + male_name + \",\" + female_name + \"\\n\"\n",
        "                \n",
        "                # should result in 4 variables with 10,000 obvs each\n",
        "                babyNames_File.write(text) "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ISwCt6xXMPYj"
      },
      "source": [
        "---\n",
        "## Approach 2: Using a Tuple\n",
        "##### _Note: I know this is duplicative, but I wanted to practice different ways to do some of these things._"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eA6Kv9UkMYah"
      },
      "source": [
        "#### **&rarr;** **Create tuple for `rank`, `male_name`, `female_name` by year**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5GMWNdDrMOj0"
      },
      "source": [
        "# Tuple with rank, male names, female names\n",
        "for file in os.listdir():\n",
        "    file= open(file, 'r')\n",
        "    for line in file:\n",
        "        ## remove any training characters (e.g., spaces)\n",
        "        line= line.rstrip()\n",
        "        tuples= re.findall('<tr align=\"right\"><td>(\\d+)</td><td>(\\w+)</td><td>(\\w+)</td>',file.read())\n",
        "        ## make tuple for [(rank, male_name, female_name)]\n",
        "        print(tuples)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "A2B4FZuNM3C5"
      },
      "source": [
        "#### &rarr;&rarr; **Extract male names associated with each rank**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ooSssHYpM7Sr"
      },
      "source": [
        "# Extracting male names associated with each rank from tuple\n",
        "for babyName in tuples: print(babyName[1])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KgFDdMDZM6s3"
      },
      "source": [
        "#### &rarr;&rarr; **Extract female names associated with each rank**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cvkWaA-ONHjX"
      },
      "source": [
        "# Extracting female names associated with each rank from tuple\n",
        "for babyName in tuples: print(babyName[2])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ebI-0qC3NMoC"
      },
      "source": [
        "#### **&rarr;** **Create dictionary**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3nV0IFUKNPLV"
      },
      "source": [
        "# Put rank, male_name, female_name in a dictionary. key = rank, values = names\n",
        "# a = rank (key); b = male_names (value), c = female_names (value)\n",
        "dictionary=dict((a, (b, c)) for a, b, c in tuples)   \n",
        "print(dictionary)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i9FKxJP3NaG-"
      },
      "source": [
        "#### &rarr;&rarr;  **Print keys**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YMCfPhrgNasZ"
      },
      "source": [
        "# Print key (rank) \n",
        "print(dictionary.keys())"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EaZNXWt4NJwW"
      },
      "source": [
        "#### &rarr;&rarr; **Print values**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2vVIicUJNmZx"
      },
      "source": [
        "# Print values (male names, female names)\n",
        "print(dictionary.values())"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZHqNo9PDNwSn"
      },
      "source": [
        "#### **&rarr;** **Print year + each line of the dictionary into comma-delimited text file**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0QAlbzvbNuIx"
      },
      "source": [
        "# Print year + each line of dictionary in comma-delimited file\n",
        "with open('babyNames2.txt', 'w') as babyNames_File2:\n",
        "    for key,value in dictionary.items():\n",
        "        rank=key\n",
        "        male_name=value[0]\n",
        "        female_name=value[1]\n",
        "        text= year + \",\" + rank + \",\" + male_name + \",\" + female_name + \"\\n\"\n",
        "        # should result in 4 variables with 10,000 obvs each\n",
        "        babyNames_File2.write(text) "
      ],
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LqIg0QX1N7SB"
      },
      "source": [
        "_Note: Jennifer Lee helped me with below because I couldn't figure out how to get the CSV files or generally how to complete the function. Credit goes to Jennifer for sure!_"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "l_hL-Fy3OKnf"
      },
      "source": [
        "#### **&rarr;** **Function for putting it all together**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dCkVllmJN-qT"
      },
      "source": [
        "# Write function to put it all together\n",
        "def babyNames(x) :\n",
        "    with open('baby'+str(x)+'.html') as file:\n",
        "        lines_x = file.readlines()\n",
        "        string_x = str(lines_x)\n",
        "        year = re.findall(r'Popularity in ([0-9][0-9][0-9][0-9])', string_x)\n",
        "        year = str(year)\n",
        "        year = year.replace(\"'\", \"\")\n",
        "        year = year.replace(\"[\", \"\")\n",
        "        year = year.replace(\"]\", \"\")\n",
        "        tuples=re.findall(r\"<td>(\\d+)</td><td>(\\w+)</td><td>(\\w+)</td>\", string_x)\n",
        "        if tuples:\n",
        "            dictionary=dict((x, (y, z)) for x, y, z in tuples)\n",
        "    with open(str(year)+'.csv','w',newline=\"\") as output:\n",
        "        writer = csv.writer(output)\n",
        "        writer.writerow(['year','rank','male_name','female_name'])\n",
        "        for rank in dictionary:\n",
        "            writer.writerow([year, rank, dictionary[rank][0], dictionary[rank][1]])"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hWuZTJifOYcN"
      },
      "source": [
        "# Export CSV files\n",
        "years= [1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008]\n",
        "for year in years:\n",
        "    babyNames(year)"
      ],
      "execution_count": 16,
      "outputs": []
    }
  ]
}