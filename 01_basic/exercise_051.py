import cProfile

def main():
    file_name = "exercise_050.py"
    file = open(file_name,mode="r")

    all_lines = file.read()
    
    file.close()

    prof = cProfile.run(all_lines)
    print(prof)

if __name__ == '__main__': main()