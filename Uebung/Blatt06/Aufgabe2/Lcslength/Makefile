.PHONY:test
test:test_small test_large
	@echo "Congratulations. $@ passed."

.PHONY:test_small
test_small:
	@./lcslength_mn.py --filename lcs_testcases_small.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test_large
test_large:
	@./lcslength_mn.py --filename lcs_testcases_large.tsv
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -r __pycache__
