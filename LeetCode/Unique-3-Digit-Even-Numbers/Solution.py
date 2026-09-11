func totalNumbers(digits []int) int {
	var m uint32
	for _, d := range digits { m |= (m<<1 | 1<<(d*3)) & (7 << (d * 3)) }
	c := func(x uint32) int { return bits.OnesCount32(m & x) }
	a, e, z := c(0x9249249), c(0x1041041), int(m&1)
	return (e*(a-z-1)+z)*(a-2) + int(m>>1&1)*(a-1) + c(0x10410410)*e + c(0x2082080)*(2*a+e-z-3) + c(0x4104100)
}