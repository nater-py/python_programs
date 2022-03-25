# This lesson tests your skills in utilizing string methods correctly

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

highlighted_poems_list = highlighted_poems.split(',')
 
# Cleaning whitespace

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

# Breaking up all info for each poem into it's own list

highlighted_poems_details = []
for details in highlighted_poems_stripped:
  highlighted_poems_details.append(details.split(":"))

# Seperating titles, poets, and dates into a list

titles = []
poets = []
dates = []

# For each list in the list append the appropiate elemnts into titles, poets, and dates

for element in highlighted_poems_details:
  titles.append(element[0])
  poets.append(element[1])
  dates.append(element[2])
  
