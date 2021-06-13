---
title: ImageReaderSpi
permalink: /Java/ImageReaderSpi/
date: 2021-01-11
key: Java.I.ImageReaderSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.ImageReaderSpi.description }}

## Sintaxis
~~~java
public abstract class ImageReaderSpi extends ImageReaderWriterSpi
~~~

## Constructores
* [ImageReaderSpi()](/Java/ImageReaderSpi/ImageReaderSpi/)

## Campos
* [inputTypes](/Java/ImageReaderSpi/inputTypes)
* [STANDARD_INPUT_TYPE](/Java/ImageReaderSpi/STANDARD_INPUT_TYPE)
* [writerSpiNames](/Java/ImageReaderSpi/writerSpiNames)

## Métodos
* [canDecodeInput()](/Java/ImageReaderSpi/canDecodeInput)
* [createReaderInstance()](/Java/ImageReaderSpi/createReaderInstance)
* [getImageWriterSpiNames()](/Java/ImageReaderSpi/getImageWriterSpiNames)
* [getInputTypes()](/Java/ImageReaderSpi/getInputTypes)
* [isOwnReader()](/Java/ImageReaderSpi/isOwnReader)

## Ejemplo
~~~java
{{ site.data.Java.I.ImageReaderSpi.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageReaderSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
