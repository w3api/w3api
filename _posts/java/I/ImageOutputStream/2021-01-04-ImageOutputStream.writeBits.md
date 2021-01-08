---
title: ImageOutputStream.writeBits()
permalink: Java/ImageOutputStream/writeBits
date: 2021-01-04
key: JavaJava.I.ImageOutputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="writeBits" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeBits(long bits, int numBits) throws IOException
~~~

## Parámetros
* **long bits**,  {% include w3api/param_description.html metodo=_data parametro="long bits" %}
* **int numBits**,  {% include w3api/param_description.html metodo=_data parametro="int numBits" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageOutputStream](/Java/ImageOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
