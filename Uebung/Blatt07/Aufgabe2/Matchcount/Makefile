.PHONY:test
test:test_tiny test_small test_medium test_large
	@echo "Congratulations. $@ passed."

.PHONY:test_tiny
test_tiny:
	@./matchcount.py --check --matrix aaaba baaba 5 | diff - matchcount_tiny.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_small
test_small:
	@./matchcount.py --check --matrix aaaba baaba 3 | diff - matchcount_small.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_medium
test_medium:
	@./matchcount.py --check --matrix agctactactcagcagcatactcag  actactccatcagacgcatcatcagacg 7 | diff - matchcount_medium.txt
	@echo "Congratulations. $@ passed."

.PHONY:test_large
test_large:
	@./matchcount.py --check agattaccgcgcatcatcatcatcatcatcagcagcatcatcatca  ggtttatatatatatatatattatatatatattataatatatatata 9 | diff - matchcount_large.txt
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -r __pycache__
