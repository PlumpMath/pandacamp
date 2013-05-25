
# Simple collection idea:

# Add a model to the collection
# When the model exits, remove it.  Or remove directly.
# use an "any" to see if anything in the collection satisfies a condition

# Shooting gallery:
#  Objects have a reaction to any projectile
#  Firing adds the object to the collection
#  When objects hit the floor they exit and are removed from the collection
# We seem to need a new reaction function (react / when)
# Can we avoid n x n running signals by doing this with instantanous values?