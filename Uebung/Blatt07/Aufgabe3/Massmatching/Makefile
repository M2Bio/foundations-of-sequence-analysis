.PHONY:test
test:test_tiny test_small test_large

.PHONY:test_tiny
test_tiny:
	@./massmatching.py -f tiny_testdata.txt | diff - tiny_testdata_matches.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_small
test_small:
	@./massmatching.py -f small_testdata.txt | diff - small_testdata_matches.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_large
test_large:
	@./massmatching.py -f large_testdata.txt | diff - large_testdata_matches.txt
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -r __pycache__
