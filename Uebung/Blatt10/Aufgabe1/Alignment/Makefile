.PHONY:test

test:editgraph.py aligntype.py alignment.py alignments.txt
	@./alignment_unit_test.py
	@echo "Congratulations. $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
