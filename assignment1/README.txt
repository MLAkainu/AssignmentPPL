Download antlr-4.9.2-complete.jar from antlr.org
Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Open terminal and type: pip3 install antlr4-python3-runtime
Change current directory to cslang-initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite

Then type: python run.py test ASTGenSuite
Then type: python run.py test CheckerSuite
Then type: python run.py test CodeGenSuite



