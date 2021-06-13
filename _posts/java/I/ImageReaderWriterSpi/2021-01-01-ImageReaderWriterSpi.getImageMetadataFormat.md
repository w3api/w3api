---
title: ImageReaderWriterSpi.getImageMetadataFormat()
permalink: /Java/ImageReaderWriterSpi/getImageMetadataFormat/
date: 2021-01-11
key: Java.I.ImageReaderWriterSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReaderWriterSpi.metodos valor="getImageMetadataFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IIOMetadataFormat getImageMetadataFormat(String formatName)
~~~

## Parámetros
* **String formatName**,  {% include w3api/param_description.html metodo=_dato parametro="String formatName" %}

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
