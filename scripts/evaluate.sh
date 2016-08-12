# Take in a  problem name and team number outputs all incorrect output

# Input checking:

if [[ $1 == "" || $2 == "" ]]
then
	echo "Invalid usage!"
	echo "bash $0 problem_name team_num"
	echo "Example:"
	echo "bash $0 sum 1"
else
	SOURCES_DIR="../sources"
	BINARY_DIR="../binary"
	OUTPUTS_DIR="../outputs"
	PROBLEMS_DIR="../problems"

	SOURCE_FILE_NAME_STEM="${SOURCES_DIR}/$1_$2"
	BINARY_FILE_NAME="${BINARY_DIR}/$1_$2.o"
	OUTPUTS_FILE_NAME="${OUTPUTS_DIR}/$1_$2.txt"
	QUESTION_FILE_NAME="${PROBLEMS_DIR}/$1_qn.txt"
	SOLUTION_FILE_NAME="${PROBLEMS_DIR}/$1_sn.txt"
	COMPILE_OUTPUT_FILENAME="_compile_output_filename.txt"

	touch $OUTPUTS_FILE_NAME
	
	# C++:
	if [[ -f "$SOURCE_FILE_NAME_STEM.cpp" ]]
	then
		SOURCE_FILE_NAME="$SOURCE_FILE_NAME_STEM.cpp"

		# Compiling Program
		if g++ $SOURCE_FILE_NAME -o $BINARY_FILE_NAME
		then
			echo "Compilation Success"
			$BINARY_FILE_NAME < $QUESTION_FILE_NAME &> $OUTPUTS_FILE_NAME

        else
			echo "Compilation Fail"
			echo $COMPILE_OUTPUT_FILENAME
		fi
	
	# Java
	elif [[ -f "$SOURCE_FILE_NAME_STEM.java" ]]
	then
	    echo "Java! TODO!"	
	else 

		if [[ -f "$SOURCE_FILE_NAME_STEM.py" ]]
		then
		    python < $QUESTION_FILE_NAME &> $OUTPUTS_FILE_NAME
		else	
			echo "Invalid! Only files of extension .cpp, .py and .java are accepted!"
            exit 2
        fi
	
	fi

    # Common: Evaluating if the solution is correct!

    TMP_F_NAME="tmp.txt"
    python whitespace_cleaner.py $OUTPUTS_FILE_NAME $TMP_F_NAME

    DIFF=$(diff tmp.txt $SOLUTION_FILE_NAME)

    if [ "$DIFF" ==  "" ] 
    then
        echo "Solution Accepted"
    else
        echo "Incorrect Solution"
    fi

    # Removing the temp file:
    rm $TMP_F_NAME

fi

