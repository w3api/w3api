---
title: ImageReaderSpi.ImageReaderSpi()
permalink: /Java/ImageReaderSpi/ImageReaderSpi/
date: 2021-01-11
key: Java.I.ImageReaderSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReaderSpi.constructores valor="ImageReaderSpi" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ImageReaderSpi()
public ImageReaderSpi(String vendorName, String version, String[] names, String[] suffixes, String[] MIMETypes, String readerClassName, Class<?>[] inputTypes, String[] writerSpiNames, boolean supportsStandardStreamMetadataFormat, String nativeStreamMetadataFormatName, String nativeStreamMetadataFormatClassName, String[] extraStreamMetadataFormatNames, String[] extraStreamMetadataFormatClassNames, boolean supportsStandardImageMetadataFormat, String nativeImageMetadataFormatName, String nativeImageMetadataFormatClassName, String[] extraImageMetadataFormatNames, String[] extraImageMetadataFormatClassNames)
~~~

## Parámetros
* **String[] writerSpiNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] writerSpiNames" %}
* **String readerClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String readerClassName" %}
* **String nativeStreamMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeStreamMetadataFormatClassName" %}
* **String nativeImageMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeImageMetadataFormatClassName" %}
* **String[] extraStreamMetadataFormatNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraStreamMetadataFormatNames" %}
* **String vendorName**,  {% include w3api/param_description.html metodo=_dato parametro="String vendorName" %}
* **String[] extraImageMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraImageMetadataFormatClassNames" %}
* **String[] MIMETypes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] MIMETypes" %}
* **String[] names**,  {% include w3api/param_description.html metodo=_dato parametro="String[] names" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}
* **String[] suffixes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] suffixes" %}
* **boolean supportsStandardStreamMetadataFormat**,  {% include w3api/param_description.html metodo=_dato parametro="boolean supportsStandardStreamMetadataFormat" %}
* **String nativeStreamMetadataFormatName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeStreamMetadataFormatName" %}
* **String nativeImageMetadataFormatName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeImageMetadataFormatName" %}
* **Class&lt;?&gt;[] inputTypes**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>[] inputTypes" %}
* **boolean supportsStandardImageMetadataFormat**,  {% include w3api/param_description.html metodo=_dato parametro="boolean supportsStandardImageMetadataFormat" %}
* **String[] extraStreamMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraStreamMetadataFormatClassNames" %}
* **String[] extraImageMetadataFormatNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraImageMetadataFormatNames" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageReaderSpi](/Java/ImageReaderSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
