# Universal Downloader

**Identidad del paquete:** `influent.mfdownstep.v1.0-26.08-21.56`
**Autor:** `JesusQuijada34`
**Plataforma:** `AlphaCube`
**Descripción:** Estructura reparada por MoonFix

## Estructura PackageMaker 3.2.7

Este repositorio fue normalizado mediante **MoonFix**, usando la estructura de PackageMaker 3.2.7. El paquete público debe conservar `details.xml`, `version.res`, `autorun`, `autorun.bat`, `.storedetail`, `updater.py`, `config/settings.json`, los marcadores `.container` y los archivos de documentación correspondientes. El publisher oficial es `influent` y la versión pública no contiene sufijo de plataforma.

## Instalación y ejecución

Instala las dependencias declaradas en `lib/requirements.txt` cuando exista y ejecuta el entrypoint real del proyecto. En Linux, los comandos privilegiados son específicos de Danenone y no deben trasladarse a Windows. En proyectos AlphaCube, la validación Windows debe realizarse con el `buildthis` oficial de PackageMaker.

## Validación

La fuente debe pasar compilación sintáctica, pruebas funcionales disponibles, comprobación de identidad XML, protección contra traversal en ZIP y llamadas seguras a subprocess. Los artefactos `.iflapp` deben ser generados por PackageMaker; los paquetes Debian deben usar el nombre canónico `influent.mfdownstep.v1.0-26.08-21.56_ARCH.deb`.

## Release

El tag y el título del release deben ser exactamente `v1.0-26.08-21.56`. Los assets deben usar el nombre canónico del paquete y una extensión objetiva. No se permite publicar un release AlphaCube que contenga únicamente el build Linux.

## Referencia original

# MediaFire Down Step

Paquete generado con Influent Package Manager.

---

## 📦 Ejemplo de uso

```bash
python3 influent.mfdownstep.v1/mfdownstep.v1.py
```

---

## 🧪 Requisitos

```bash
pip install -r lib/requirements.txt
```

---

## 📁 Estructura

```
influent.mfdownstep.v1/
├── app/
│   ├── mfdownstep.v1.py
│   └── app-icon.ico
├── assets/
├── config/
├── docs/
├── ke/
├── banderas/
├── source/
├── lib/
│   └── requirements.txt
└── details.xml
```

---

## 👤 Autor

influent
