TODOs for jasper-install
========================

- extract version numbers of packages to variables
  * openfst
  * m2m-aligner
  * mitlm
  * phonetisaurus
  * phonetisaurus_fst (?)
  * julius

- add install-scripts for other engines
  * Julius STT (add install for acoustic model and lexicon)
  * Festival TTS
  * Flite TTS
  * SVOX Pico TTS
  * Google TTS
  * Ivona TTS

- check number of processors and feed -j x to make-invocations

- verify modules
  * update
  * upgrade
  * devtools
  * alsa
  * user
  * jasper
  * pocketsphinx
  * pocketsphinx_src
  * CMUCLMTK
  * openfst
  * m2m_aligner
  * mitlm
  * phonetisaurus
  * phonetisaurus_fst
  * phonetisaurus_exp
  * julius
  * espeak

- move configuration to separate file

- install_jasper
  * yaml.h not found! (check if libyaml-dev solves this)

- create default profile for user jasper

Later
-----

- check if packages from base are runtime or pure buildtime
  (python-pyaudio seems only runtime package)

- add module init (add to init-system)

- add module devtools_rm

- move all downloads to separate module