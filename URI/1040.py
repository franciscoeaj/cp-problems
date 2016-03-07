n1, n2, n3, n4 = map(float, raw_input().split())

average = ((2 * n1) + (3 * n2) + (4 * n3) + (1 * n4)) / 10

print "Media: %.1f" % average

if average >= 7.0:
	print "Aluno aprovado."
elif average < 5.0:
	print "Aluno reprovado."
elif 5.0 <= average <= 6.9:
	print "Aluno em exame."
	final_exam = float(raw_input())

	print "Nota do exame: %.1f" % final_exam

	final_average = (average + final_exam) / 2

	if final_average >= 5.0:
		print "Aluno aprovado."
	else:
		print "Aluno reprovado."

	print "Media final: %.1f" % final_average