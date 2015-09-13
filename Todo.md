TODOs for jasper-install
========================

- user
  * make jasper a system-user
  * move configuration to /etc/jasper/profile.yml

- create default profile for user jasper

- add install-scripts for other engines
  * add module initd (add to init-system)
  * Julius STT (add install for acoustic model and lexicon)
  * German acoustic modules?

- verify modules
  * swap
  * update (182s) ok
  * upgrade ??
  * devtools (1438s) ok
  * alsa (4s) ok
  * user (6s) ok
  * jasper (443s) ok
  * pocketsphinx (316s) ok
  * pocketsphinx_src
  * CMUCLMTK (637s) ok
  * openfst (ok)
  * m2m_aligner (67s) ok
  * mitlm (348s) ok
  * phonetisaurus (405s) ok
  * phonetisaurus_fst (166s) ok
  * espeak (103) ok

  * phonetisaurus_exp
  * julius
  * julius_modlex
  * festival (165s) ok
  * flite (64s) ok
  * svoxpico (2s) ok
  * google_tts (113s) ok
  * ivona (8s) ok

- add timing information to Readme.md

- patch jasper to use /etc/jasper.cfg as configuration (?)


Later
-----

- add configuration to only install packages using apt (for cloning
  of the installation to other systems)

- check if packages from base are runtime or pure buildtime
  (python-pyaudio seems the only runtime package)

- add module devtools_rm

- move all downloads to separate module

- install newer version of gcc and use openfst 1.5.0??
