---
title: ImageReaderSpi.canDecodeInput()
permalink: Java/ImageReaderSpi/canDecodeInput
date: 2021-01-04
key: JavaJava.I.ImageReaderSpi
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReaderSpi.metodos valor="canDecodeInput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean canDecodeInput(Object source) throws IOException
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
