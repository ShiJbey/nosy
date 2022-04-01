# Nosy: Neighborly Story Sifting Language

Nosy is a query language based on Datalog that is
specifically designed for story sifting Neighborly
worlds. It integrates with Neighborly's entity-component
system, and enables users to look for specific
relations/patterns in the data. The syntax is borrowed
from Datomic and DataScript.

Nosy does not support all the features that Datomic has.

This is not meant to be a standalone project. I am developing
it separately and plan to integrate it into the core
Neighborly code at a later date.

Nosy uses Antlr4 to generate a parser and abstract syntax
tree (AST) from a given text query. Then I plan to use the
AST to query the ECS for entities/values.
