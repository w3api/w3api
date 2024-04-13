---
title: ImageWriterSpi
permalink: /Java/ImageWriterSpi/
date: 2021-01-11
key: Java.I.ImageWriterSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.ImageWriterSpi.description }}

## Sintaxis
~~~java
public abstract class ImageWriterSpi extends ImageReaderWriterSpi
~~~

## Constructores
* [ImageWriterSpi()](/Java/ImageWriterSpi/ImageWriterSpi/)

## Campos
* [outputTypes](/Java/ImageWriterSpi/outputTypes)
* [readerSpiNames](/Java/ImageWriterSpi/readerSpiNames)
* [STANDARD_OUTPUT_TYPE](/Java/ImageWriterSpi/STANDARD_OUTPUT_TYPE)

## Métodos
* [canEncodeImage()](/Java/ImageWriterSpi/canEncodeImage)
* [createWriterInstance()](/Java/ImageWriterSpi/createWriterInstance)
* [getImageReaderSpiNames()](/Java/ImageWriterSpi/getImageReaderSpiNames)
* [getOutputTypes()](/Java/ImageWriterSpi/getOutputTypes)
* [isFormatLossless()](/Java/ImageWriterSpi/isFormatLossless)
* [isOwnWriter()](/Java/ImageWriterSpi/isOwnWriter)

## Ejemplo
~~~java
{{ site.data.Java.I.ImageWriterSpi.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.ImageWriterSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
