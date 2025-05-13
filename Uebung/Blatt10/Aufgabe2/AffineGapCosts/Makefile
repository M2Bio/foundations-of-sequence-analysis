.PHONY:test
test:test_lect test_small test_medium
	@echo "Congratulations. $@ passed"

.PHONY:test_lect
test_lect:
	@./affinealign_mn.py --show_matrix --onlycost seqpair_lect.fna | diff -  seqpair_lect_matrix.txt
	@echo "Congratulations. $@ passed"

.PHONY:test_medium
test_medium:
	@./affinealign_mn.py --onlycost medium_sequences.fna > my_scores.tsv
	@grep '^#' medium_affinealign.txt | diff - my_scores.tsv
	@${RM} my_scores.tsv
	@echo "Congratulations. $@ passed"

.PHONY:test_small
test_small:
	@for num in 0 1 2 3 4; do \
	  echo "test seqpair$${num}.fna";\
	  ./affinealign_mn.py --onlycost seqpair$${num}.fna > my_scores.tsv; \
	  grep '^\#' seqpair$${num}_affinealign.txt | diff - my_scores.tsv;\
	done
	@${RM} my_scores.tsv
	@echo "Congratulations. $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
