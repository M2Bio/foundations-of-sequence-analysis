.PHONY:test
test:jaccard_unit_test jaccard jaccard_sample_1000 correlation_15 correlation_16

.PHONY:jaccard_unit_test
jaccard_unit_test:ebola-genomes.fna
	@./jaccard_unit_test.py
	@echo "Congratulations. $@ passed."

.PHONY:jaccard
jaccard:ebola-genomes.fna
	@./jaccard.py -j ebola-genomes.fna
	@echo "Congratulations. $@ passed."

.PHONY:jaccard_sample_1000
jaccard_sample_1000:ebola-genomes.fna
	@./jaccard.py -s 1000 ebola-genomes.fna
	@echo "Congratulations. $@ passed."

.PHONY:correlation_15
correlation_15:ebola-genomes.fna
	@./jaccard.py -q 15 -c ebola-genomes.fna
	@echo "Congratulations. $@ passed."

.PHONY:correlation_16
correlation_16:ebola-genomes.fna
	@./jaccard.py -q 16 -c ebola-genomes.fna
	@echo "Congratulations. $@ passed."

ebola-genomes.fna:ebola-genomes.fna.gz
	@gzip -d -c $< > $@

.PHONY:clean
clean:
	@${RM} -r __pycache__ ebola-genomes.fna
