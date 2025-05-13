.PHONY:test

test:test_gsa_seqpair_score test_gsa_seqpair_matrix test_seq2_coords test_seq2_matrix test_seq18
	@echo "Congratulations. $@ passed."

.PHONY:test_gsa_seqpair_score
test_gsa_seqpair_score:
	@tail -n 1 gsa-seqpair-matrix.tsv > gsa-seqpair-coords.tsv
	@./swalign_mn.py -i 1 -s unitscore.txt gsa-seqpair.txt | diff -I '^#' - gsa-seqpair-coords.tsv
	@${RM} gsa-seqpair-coords.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test_gsa_seqpair_matrix
test_gsa_seqpair_matrix:
	@./swalign_mn.py -m -f -i 1 -s unitscore.txt gsa-seqpair.txt | diff -I '^#' - gsa-seqpair-matrix.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test_seq2_coords
test_seq2_coords:
	@./swalign_mn.py -i 4 -s blosum62.txt seq2.fasta | diff -I '^#' - seq2_coords.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test_seq2_matrix
test_seq2_matrix:
	@./swalign_mn.py -i 4 -m -s blosum62.txt seq2.fasta | diff -I '^#' - seq2_matrix.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test_seq18
test_seq18:
	@./swalign_mn.py -i 4 -s blosum62.txt seq18.fasta | diff -I '^#' - local-coords18.tsv
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -r __pycache__
