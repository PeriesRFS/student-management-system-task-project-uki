#get the student marks as user input
def get_valid_marks():
    
    marks = []
    
    print("Please Enter student Marks - Mark per Line")
    print("Press Enter twice to complete the marks input\n")
    
    while True:
        user_input = input("Mark: ").strip()
        
        #two empty line to stop the input
        if user_input == "":
            if marks:
                break
            else:
                print("Please Enter a Mark")
                continue
            
        #validate marks input
        try:
            mark = int(user_input)
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                print("Error-marks must be between 0 and 100.Try again")
        except ValueError:
            print("Error-Please Enter a valid Number!")
            
    return marks

#process the marks 
def process_marks(marks):
    if not marks :
        return None
    
    total = sum(marks)
    count = len(marks)
    average = total/count
    highest = max(marks)
    lowest = min(marks)
    
    pass_count = sum(1 for mark in marks if mark >= 50)
    fail_count = count - pass_count
    
    return{
        'count' : count,
        'average': average,
        'highest' : highest,
        'lowest' : lowest,
        'pass_count' : pass_count,
        'fail_count' : fail_count,
        'pass_percentage' : (pass_count/count * 100) if count > 0 else 0
    }
    
#display Results
def display_results(results):
    if results is None :
        print("No vadid marks were entered")
        return
    
    print("\n"+"-"*40)
    print("-"*9 +"STUDENT MARKS ANALYSIS"+"-"*9)
    print("="*40)
    print(f"Total Students      : {results['count']}")
    print(f"Average mark        : {results['average']:.2f}")
    print(f"Highest mark        : {results['highest']}")
    print(f"Lowest mark         : {results['lowest']}")
    print("-"*40)
    
    print(f"Passed (≥50)        : {results['pass_count']} ({results['pass_percentage']:.1f}%)")
    print(f"Failed Students     : {results['fail_count']}")
    print("-"*40)

#calling main functions    
def main():
    print("Students Marks Sheet")
    print("-"*30)
    
    # get the marks
    marks_list = get_valid_marks()
    
    #Display the list of marks entered
    if marks_list:
        print("\nMarks Entered -",marks_list)
        
    #process the marks
    results = process_marks(marks_list)
    
    #display Results
    display_results(results)
    
if __name__ == "__main__":
    main()