.PHONY:test
test:
	@./checkedist.py ./lsp_dist_only.py edist-testcases.csv
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -r __pycache__
