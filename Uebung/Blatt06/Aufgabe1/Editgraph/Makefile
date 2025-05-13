.PHONY:test
test:
	@./run.sh | diff - editgraph_out.tsv
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -f __pycache__
