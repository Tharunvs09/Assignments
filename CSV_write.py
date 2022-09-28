import csv
feilds=['Name','Branch','Year','CGPA']
rows=[  ['cholan', 'Civil', '2', '9.0'],
        ['arulmolzi', 'Cse', '2', '9.1'],
        ['karikaln', 'Cse', '2', '9.3'],
        ['Nandini', 'Cse', '1', '9.5'],
        ['Kundavai', 'IT', '3', '7.8'],
        ['vanthiyathevan', 'Mech', '2', '9.1']]
filename = "university_records.csv"
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(feilds)
    csvwriter.writerows(rows)