# Z3city

Electricity price optimization using constraint solving.

This is at the moment just a proof of concept and very much WIP. It uses the
Z3 SMT solver to select a cost-optimal schedule for house and hotwater heating,
for a 24h period, given hourly prices and a set of constraints. This is achieved
using Z3's Optimize API and using the hourly prices as weights for soft constraints.
