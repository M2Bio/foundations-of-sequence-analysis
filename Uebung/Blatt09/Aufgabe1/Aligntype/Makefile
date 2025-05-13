.PHONY:test

.PHONY:test_short
test_short:aligntype.py
	@./aligntype.py | diff - short_alignment_out.txt
	@./verify_alignment.py short_alignment.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_alignment1
test_alignment1:aligntype.py
	@./verify_alignment.py alignment1.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_alignment2
test_alignment2:aligntype.py
	@./verify_alignment.py alignment2.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_long
test_long:aligntype.py
	@./verify_alignment.py sample_alignments.txt
	@echo "Congratulations. $@ passed."

test:test_short test_alignment1 test_alignment2 test_long

.PHONY:clean
clean:
	@${RM} -r __pycache__
