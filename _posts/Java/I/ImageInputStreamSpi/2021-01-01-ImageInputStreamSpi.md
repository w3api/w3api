---
title: ImageInputStreamSpi
permalink: /Java/ImageInputStreamSpi/
date: 2021-01-11
key: Java.I.ImageInputStreamSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.ImageInputStreamSpi.description }}

## Sintaxis
~~~java
public abstract class ImageInputStreamSpi extends IIOServiceProvider
~~~

## Constructores
* [ImageInputStreamSpi()](/Java/ImageInputStreamSpi/ImageInputStreamSpi/)

## Campos
* [inputClass](/Java/ImageInputStreamSpi/inputClass/)

## Métodos
* [canUseCacheFile()](/Java/ImageInputStreamSpi/canUseCacheFile/)
* [createInputStreamInstance()](/Java/ImageInputStreamSpi/createInputStreamInstance/)
* [getInputClass()](/Java/ImageInputStreamSpi/getInputClass/)
* [needsCacheFile()](/Java/ImageInputStreamSpi/needsCacheFile/)

## Ejemplo
~~~java
{{ site.data.Java.I.ImageInputStreamSpi.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.ImageInputStreamSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
