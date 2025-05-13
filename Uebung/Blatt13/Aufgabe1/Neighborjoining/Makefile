.PHONY:test testln test10
test:testln test10
	@echo "Congratulations. $@ passed"

testln:
	@./nejo.py --precision 5 ln_example.mat | diff - ln_example.tsv
	@echo "Congratulations. $@ passed"

test10:
	@./nejo.py --precision 5 ebola10.mat | diff - ebola10.tsv
	@echo "Congratulations. $@ passed"

.PHONY:clean
clean:
	${RM} -r __pycache__
