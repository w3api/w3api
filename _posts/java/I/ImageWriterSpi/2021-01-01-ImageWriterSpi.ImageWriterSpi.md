---
title: ImageWriterSpi.ImageWriterSpi()
permalink: Java/ImageWriterSpi/ImageWriterSpi
date: 2021-01-11
key: JavaJava.I.ImageWriterSpi
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriterSpi.constructores valor="ImageWriterSpi" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ImageWriterSpi()
public ImageWriterSpi(String vendorName, String version, String[] names, String[] suffixes, String[] MIMETypes, String writerClassName, Class<?>[] outputTypes, String[] readerSpiNames, boolean supportsStandardStreamMetadataFormat, String nativeStreamMetadataFormatName, String nativeStreamMetadataFormatClassName, String[] extraStreamMetadataFormatNames, String[] extraStreamMetadataFormatClassNames, boolean supportsStandardImageMetadataFormat, String nativeImageMetadataFormatName, String nativeImageMetadataFormatClassName, String[] extraImageMetadataFormatNames, String[] extraImageMetadataFormatClassNames)
~~~

## Parámetros
* **String nativeImageMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeImageMetadataFormatClassName" %}
* **String nativeStreamMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeStreamMetadataFormatClassName" %}
* **String[] extraStreamMetadataFormatNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraStreamMetadataFormatNames" %}
* **String vendorName**,  {% include w3api/param_description.html metodo=_dato parametro="String vendorName" %}
* **String[] extraImageMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraImageMetadataFormatClassNames" %}
* **String[] MIMETypes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] MIMETypes" %}
* **String[] readerSpiNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] readerSpiNames" %}
* **String[] names**,  {% include w3api/param_description.html metodo=_dato parametro="String[] names" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}
* **String[] suffixes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] suffixes" %}
* **String writerClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String writerClassName" %}
* **boolean supportsStandardStreamMetadataFormat**,  {% include w3api/param_description.html metodo=_dato parametro="boolean supportsStandardStreamMetadataFormat" %}
* **String nativeStreamMetadataFormatName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeStreamMetadataFormatName" %}
* **String nativeImageMetadataFormatName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeImageMetadataFormatName" %}
* **Class&lt;?&gt;[] outputTypes**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>[] outputTypes" %}
* **boolean supportsStandardImageMetadataFormat**,  {% include w3api/param_description.html metodo=_dato parametro="boolean supportsStandardImageMetadataFormat" %}
* **String[] extraStreamMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraStreamMetadataFormatClassNames" %}
* **String[] extraImageMetadataFormatNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraImageMetadataFormatNames" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageWriterSpi](/Java/ImageWriterSpi/)

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
