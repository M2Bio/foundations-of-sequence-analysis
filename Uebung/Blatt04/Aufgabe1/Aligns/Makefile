.PHONY:test
test:test_recursive test_dp
	@echo "Congratulations. $@ passed"

.PHONY:test_recursive
test_recursive:
	@echo "test_recursive takes several seconds"
	@./run.sh './aligns.py -r' | diff - aligns_out.txt
	@echo "Congratulations. $@ passed"

.PHONY:test_dp
test_dp:
	@./run.sh ./aligns.py | diff - aligns_out.txt
	@echo "Congratulations. $@ passed"

.PHONY:clean
clean:
