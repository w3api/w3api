---
title: ImageReaderWriterSpi.ImageReaderWriterSpi()
permalink: /Java/ImageReaderWriterSpi/ImageReaderWriterSpi/
date: 2021-01-11
key: Java.I.ImageReaderWriterSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReaderWriterSpi.constructores valor="ImageReaderWriterSpi" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageReaderWriterSpi()
public ImageReaderWriterSpi(String vendorName, String version, String[] names, String[] suffixes, String[] MIMETypes, String pluginClassName, boolean supportsStandardStreamMetadataFormat, String nativeStreamMetadataFormatName, String nativeStreamMetadataFormatClassName, String[] extraStreamMetadataFormatNames, String[] extraStreamMetadataFormatClassNames, boolean supportsStandardImageMetadataFormat, String nativeImageMetadataFormatName, String nativeImageMetadataFormatClassName, String[] extraImageMetadataFormatNames, String[] extraImageMetadataFormatClassNames)
~~~

## Parámetros
* **String pluginClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String pluginClassName" %}
* **String nativeStreamMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeStreamMetadataFormatClassName" %}
* **String nativeImageMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeImageMetadataFormatClassName" %}
* **String[] extraStreamMetadataFormatNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraStreamMetadataFormatNames" %}
* **String vendorName**,  {% include w3api/param_description.html metodo=_dato parametro="String vendorName" %}
* **String[] extraImageMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraImageMetadataFormatClassNames" %}
* **String[] MIMETypes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] MIMETypes" %}
* **String[] names**,  {% include w3api/param_description.html metodo=_dato parametro="String[] names" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}
* **String[] suffixes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] suffixes" %}
* **String nativeStreamMetadataFormatName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeStreamMetadataFormatName" %}
* **String nativeImageMetadataFormatName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeImageMetadataFormatName" %}
* **boolean supportsStandardStreamMetadataFormat**,  {% include w3api/param_description.html metodo=_dato parametro="boolean supportsStandardStreamMetadataFormat" %}
* **boolean supportsStandardImageMetadataFormat**,  {% include w3api/param_description.html metodo=_dato parametro="boolean supportsStandardImageMetadataFormat" %}
* **String[] extraStreamMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraStreamMetadataFormatClassNames" %}
* **String[] extraImageMetadataFormatNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraImageMetadataFormatNames" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageReaderWriterSpi](/Java/ImageReaderWriterSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
