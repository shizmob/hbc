INSTALLER_VER_MAJOR = 1
INSTALLER_VER_MINOR = 2

PYTHON = python2
TOOLS = $(CURDIR)/../../pywii/pywii-tools
CERTS = $(CURDIR)/dpki/certs
DPKI_ISSUER_TIK = Root-CA00000002-XS00000006
DPKI_ISSUER_TMD = Root-CA00000002-CP00000007

all: channel_retail.wad

dpki: channel_dpki.wad

channel_retail.wad: retail/cetk retail/tmd 00000000 00000001
	@$(PYTHON) $(TOOLS)/wadpack.py $@ retail/

channel_dpki.wad: dpki/cetk dpki/tmd 00000000 00000001
	@$(PYTHON) $(TOOLS)/wadpack.py -dpki $@ dpki/

00000000: ../banner/channel.imet
	@cat footer $< > $@

00000001: ../channelapp/channelapp-channel.dol
	@cp $< $@

retail/cetk: cetk.template
	@cp $< $@
	@$(PYTHON) $(TOOLS)/tikfix.py $@

dpki/cetk: retail/cetk
	@$(PYTHON) $(TOOLS)/dpkisign.py -cetk $< $@ $(CERTS) $(DPKI_ISSUER_TIK)

retail/tmd: tmd.template 00000000 00000001
	@cp $< $@
	@$(PYTHON) $(TOOLS)/tmdupdatecr.py $@ $(CURDIR)
	@$(PYTHON) $(TOOLS)/tmdvers.py $@ $(INSTALLER_VER_MAJOR) $(INSTALLER_VER_MINOR)

dpki/tmd: retail/tmd
	@$(PYTHON) $(TOOLS)/dpkisign.py -tmd $< $@ $(CERTS) $(DPKI_ISSUER_TMD)

check: all dpki
	@echo ===== RETAIL =====
	@$(PYTHON) $(TOOLS)/tikinfo.py retail/cetk retail/certs
	@$(PYTHON) $(TOOLS)/tmdinfo.py retail/tmd retail/certs
	@echo ===== DPKI =====
	@$(PYTHON) $(TOOLS)/tikinfo.py -dpki dpki/cetk dpki/certs
	@$(PYTHON) $(TOOLS)/tmdinfo.py -dpki dpki/tmd dpki/certs

clean:
	rm -f retail/cetk dpki/cetk retail/tmd retail/tmd 00000000 00000001 channel_retail.wad channel_dpki.wad

