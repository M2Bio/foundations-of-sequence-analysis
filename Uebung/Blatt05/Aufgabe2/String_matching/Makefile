.PHONY:test

test:test_simple test_8patterns
	@echo "Congratulations. $@ passed."

.PHONY:test_8patterns
test_8patterns:
	@./string_matching_run.py example_pattern.txt example_text.seq | diff - example_output.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test_simple
test_simple:
	@./string_matching_run.py pattern.txt y3_fragment.seq | diff - y3_fragment_output.tsv
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -r __pycache__
