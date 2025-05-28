# Meta-training plastic networks for transitive inference

This is the code for the paper [Neural mechanisms of relational learning and fast knowledge reassembly in plastic neural networks](https://thomasmiconi.github.io/NN.pdf), Nature Neuroscience, by Thomas Miconi and Kenneth Kay (previous preprint [here](https://www.biorxiv.org/content/10.1101/2023.07.27.550739)).

We also include parameter files for two pre-trained networks, representing each of the two strategies (active, list-linking and passive, not list-linking) described in the paper.

The code consists of two notebooks. These notebooks are immediately usable on Google Colab, as-is.

If you just want to understand how the system works, it is **highly** recommended to look at `simple.ipynb` first. 

The code actually used for the paper is in `main.ipynb`. This code includes a lot of additional code for running the various experiments from the paper. By contrast, the code in `simple.ipynb` (which only contains one large code cell) is a simplified version that only includes the basic code for meta-training a plastic network for transitive inference. The network structure and experimental settings are essentially idenctical between the two, with only the additional code for the various side experiments removed.

Note that the networks produced by `simple.ipynb` can be used in the EVAL (figure-producing) mode of `main.ipynb`.

Consult the respecitve notebooks for more details.

### To generate the figures from the paper

1- Copy `net_active.dat` to `net.dat` and upload it to where the notebook can access it.

2- In line 207 of `main.ipynb`, set EVAL to `True`

3- Run `main.ipynb` (making sure that `net.dat` is in the path of your notebook)

This produces figures for the active strategy (capable of list-linking). Other figures may need more modifications, consult the relevant cells in `main.ipynb`. 

To produce similar figures for the passive strategy (not capable of list-linking), use `net_passive.dat` (and rename it to `net.dat`) instead.

### To train your own networks from scratch

1- In line 207 of `main.ipynb`, set EVAL to `False`

2- Run `main.ipynb` 

This will run for 30000 iterations (which might take a few hours) and produce a fully meta-trained plastic network, stored in `net.dat`. You can then use `main.ipynb` (with EVAL set to `True` in line 207) to produce figures for this trained network.

