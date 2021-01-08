---
title: ImageReaderWriterSpi.ImageReaderWriterSpi()
permalink: Java/ImageReaderWriterSpi/ImageReaderWriterSpi
date: 2021-01-04
key: JavaJava.I.ImageReaderWriterSpi
category: java
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
* **boolean supportsStandardStreamMetadataFormat**,  {% include w3api/param_description.html metodo=_data parametro="boolean supportsStandardStreamMetadataFormat" %}
* **String[] extraImageMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] extraImageMetadataFormatClassNames" %}
* **String[] extraStreamMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] extraStreamMetadataFormatClassNames" %}
* **String nativeImageMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_data parametro="String nativeImageMetadataFormatClassName" %}
* **String nativeStreamMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_data parametro="String nativeStreamMetadataFormatClassName" %}
* **String pluginClassName**,  {% include w3api/param_description.html metodo=_data parametro="String pluginClassName" %}
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
[ImageReaderWriterSpi](/Java/ImageReaderWriterSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageReaderWriterSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
