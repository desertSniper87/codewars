package kata

func ProductFib(final_prod uint64) [3]uint64 {
	n1 := uint64(0)
	n2 := uint64(1)

	prod1 := n1 * n2
	var prod2 uint64

	for prod1 < final_prod {
		prod1 = n1 * n2

		if prod1 == final_prod {
			return [3]uint64{n1, n2, 1}
		}

		t := n2
		n2 += n1
		n1 = t

		prod2 = n1 * n2

		if final_prod < prod2 {
			return [3]uint64{n1, n2, 0}
		}

	}
	return [3]uint64{n1, n2, 0}
}
