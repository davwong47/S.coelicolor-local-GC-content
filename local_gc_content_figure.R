library ("ggplot2")

df = read.csv("local_gc_content.csv", header=T)

g1 = ggplot(df, aes(x=middle, y=gc_content))
g2 = g1 + geom_line()
g3 = g2 + ylim(0, 100)
g4 = g3 + coord_cartesian(expand=FALSE)
g5 = g4 + scale_x_continuous(labels=function(x) x/1000)
g6 = g5 + xlab("Nucleotide position (KB)") + ylab("GC content (%)")

ggsave("local_gc_content.png", width=89, height=50, units="mm")
