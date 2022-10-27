# okg_experiments

## To run
```
pip install -r requirements
cd oram
cd MP-SPDZ
make tldr
make bmr
make shamir-bmr-party.x
make real-bmr-party.x
make semi-bmr-party.x
./compile -B 64 ../okg.mpc
cd ..
python querying_player.py foaf.Person
```

## Overview

We implement a naive ORAM-based oblivious graph for storing RDF triples. It is possible to do a simple query of retrieving all (subject, object) pairs for a given predicate. We use the MP-SPDZ multiparty computation framework building out this prototype. It enables us to benchmark the implementation across a variety of MPC backends. For our purposes, we are mainly interested in the BMR-ORAM construction of Keller et al and as such provide build instructions for installing the 2 party and 3 party variants.
