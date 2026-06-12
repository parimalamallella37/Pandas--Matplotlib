import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df= pd.read_csv('student_marks.csv')

# Display basic information about the dataset
print(df.info())
#display the first-five rows
print(df.head())

#find the mising values in the dataset
print(df.isnull().sum())

#fill the missing value with 0 means the student did not attend the exam
df.fillna(0, inplace=True)

#find the best of 2 midsr each subject and create a new column for it
subjects = ["Maths", "Physics", "Chemistry", "English", "Telugu", "IT"]

for subject in subjects:
    mid_columns = [
        f"{subject}_Mid1",
        f"{subject}_Mid2",
        f"{subject}_Mid3"
    ]

    df[f"{subject}_Best2_Mids"] = (
        df[mid_columns]
        .apply(lambda row: row.nlargest(2).sum(), axis=1)
    )


#remove the mid columns
for subject in subjects:
    
    mid_columns = [ f"{subject}_Mid1", f"{subject}_Mid2", f"{subject}_Mid3" ]
    df.drop(columns=mid_columns, inplace=True)


#create the total marks of each subject for each person
for subject in subjects:
    df[f"{subject}_Total"] = df[f"{subject}_Best2_Mids"] + df[f"{subject}_Sem"]
    average_marks=df[f"{subject}_Total"].mean()
    #print(f"Average marks for {subject}: {average_marks}")


#grade to each subject for each person
for subject in subjects:
    if(f"{subject}_Total" in df.columns):
        df[f"{subject}_Grade"] = df[f"{subject}_Total"].apply(lambda x: 'Ex' if x >= 90 else 'A'
        if x >= 80 else 'B' 
        if x >= 70 else 'C' 
        if x >= 60 else 'D' 
        if x >= 50 else 'E' 
        if x>=40 else 'fail')



#pie chart representation to the average subjects marks of all the students
average_marks = [df[f"{subject}_Total"].mean() for subject in subjects]
highest_average = max(average_marks)
highest_subject = subjects[average_marks.index(highest_average)]

plt.figure(figsize=(4,4))
plt.pie(
    average_marks,labels=subjects,autopct='%1.1f%%',startangle=140
)
plt.title('Average Marks Distribution by Subject')
plt.text(
    0,-1.25,f"most students scored in {highest_subject}:({highest_average:.2f})",
    ha='center', fontsize=10 , fontweight='bold'
)

plt.axis('equal')
plt.show()


#grades analysis for each subject
grade_counts = {}
for subject in subjects:
    grade_counts[subject] = df[f"{subject}_Grade"].value_counts()

#bar chart representation of grade distribution for each subject
for subject in subjects:
    plt.figure(figsize=(8, 4))
    grade_counts[subject].plot(kind='bar', color='skyblue')
    plt.title(f'Grade Distribution for {subject}')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

#save the modified dataset
df.to_csv("student_marks_final_analysis.csv", index=False)
