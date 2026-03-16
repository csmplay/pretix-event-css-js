all: localecompile

LNGS := $(shell ls -d src/pretix_event_css_js/locale/*/ | xargs -I{} basename {} | sed 's/^/-l /' | tr '\n' ' ')

localecompile:
	django-admin compilemessages

localegen:
	django-admin makemessages --keep-pot -i build -i dist -i "*egg*" $(LNGS)

.PHONY: all localecompile localegen