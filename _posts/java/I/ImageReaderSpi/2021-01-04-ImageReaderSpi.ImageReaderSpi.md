---
title: ImageReaderSpi.ImageReaderSpi()
permalink: Java/ImageReaderSpi/ImageReaderSpi
date: 2021-01-04
key: JavaJava.I.ImageReaderSpi
category: java
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
* **boolean supportsStandardStreamMetadataFormat**,  {% include w3api/param_description.html metodo=_data parametro="boolean supportsStandardStreamMetadataFormat" %}
* **String[] extraImageMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] extraImageMetadataFormatClassNames" %}
* **String[] extraStreamMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] extraStreamMetadataFormatClassNames" %}
* **String nativeImageMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_data parametro="String nativeImageMetadataFormatClassName" %}
* **String nativeStreamMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_data parametro="String nativeStreamMetadataFormatClassName" %}
* **String readerClassName**,  {% include w3api/param_description.html metodo=_data parametro="String readerClassName" %}
* **Class&lt;?&gt;[] inputTypes**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>[] inputTypes" %}
* **String[] writerSpiNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] writerSpiNames" %}
* **String version**,  {% include w3api/param_description.html metodo=_data parametro="String version" %}
* **String[] suffixes**,  {% include w3api/param_description.html metodo=_data parametro="String[] suffixes" %}
* **String nativeStreamMetadataFormatName**,  {% include w3api/param_description.html metodo=_data parametro="String nativeStreamMetadataFormatName" %}
* **String[] extraStreamMetadataFormatNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] extraStreamMetadataFormatNames" %}
* **String[] MIMETypes**,  {% include w3api/param_description.html metodo=_data parametro="String[] MIMETypes" %}
* **String[] names**,  {% include w3api/param_description.html metodo=_data parametro="String[] names" %}
* **boolean supportsStandardImageMetadataFormat**,  {% include w3api/param_description.html metodo=_data parametro="boolean supportsStandardImageMetadataFormat" %}
* **String[] extraImageMetadataFormatNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] extraImageMetadataFormatNames" %}
* **String vendorName**,  {% include w3api/param_description.html metodo=_data parametro="String vendorName" %}
* **String nativeImageMetadataFormatName**,  {% include w3api/param_description.html metodo=_data parametro="String nativeImageMetadataFormatName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageReaderSpi](/Java/ImageReaderSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageReaderSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
