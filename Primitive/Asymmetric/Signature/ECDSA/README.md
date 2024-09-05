# Elliptic curve digital signature algorithm (ECDSA)

ECDSA is the elliptic-curve analog of the digital signature algorithm, specified in [FIPS 186-5](https://doi.org/10.6028/NIST.FIPS.186-5). The security of ECDSA depends on two primitives: the elliptic curve and the hash function. At this time, the implementation is generic over elliptic curve but fixes the hash function to SHA-256.

Structurally, there are two separate specification files:
- `Specification.cry` matches the spec as closely as possible;
- `UnconstrainedSpec.cry` implements the same algorithms but omits some of the top-level domain parameter constraints (e.g. on the size of the curve; on the relative security of the curve and hash function)

We recommend using `Specification.cry` for most applications to ensure compliance with FIPS 186-5.
The FIPS 186-5 compliant implementation has been instantiated and tested with curve P-256 and SHA256 (see `Instantiations/` and `Tests/`, respectively). Both versions rely on the curve implementation in `Common/EC/PrimeField/`.

This is one of many implementations of ECDSA that have been written in Cryptol over the years. One grandparent of particular interest is a 2011 version that was used to verify a Java implementation in combination with [SAWScript](https://github.com/GaloisInc/saw-script/). This implementation no longer lives in this repo, but it can be seen together with the Java code and the SAW scripts used in the full verification toolchain [in the examples directory of the SAWScript repository](https://github.com/GaloisInc/saw-script/tree/master/examples/ecdsa). Additional information can be found in [an article by Galois](https://galois.com/blog/2012/03/verifying-ecc-implementations/) and [a talk from HCSS 2012](https://sos-vo.org/node/3405).

Several other implementations of ECDSA used to live in this repository. If you would like to explore these, they were removed in the commit with hash:
> [c0bf03f3a3f322d33ac574d2f93267965b967929](https://github.com/GaloisInc/cryptol-specs/commit/c0bf03f3a3f322d33ac574d2f93267965b967929)
