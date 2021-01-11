---
title: ImageOutputStream.writeBits()
permalink: Java/ImageOutputStream/writeBits
date: 2021-01-11
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
* **int numBits**,  {% include w3api/param_description.html metodo=_dato parametro="int numBits" %}
* **long bits**,  {% include w3api/param_description.html metodo=_dato parametro="long bits" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageOutputStream](/Java/ImageOutputStream/)

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
