---
title: ImageReaderSpi.canDecodeInput()
permalink: /Java/ImageReaderSpi/canDecodeInput/
date: 2021-01-11
key: Java.I.ImageReaderSpi
category: Java
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
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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
