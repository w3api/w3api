---
title: ImageInputStream.readBits()
permalink: Java/ImageInputStream/readBits
date: 2021-01-04
key: JavaJava.I.ImageInputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageInputStream.metodos valor="readBits" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long readBits(int numBits) throws IOException
~~~

## Parámetros
* **int numBits**,  {% include w3api/param_description.html metodo=_data parametro="int numBits" %}

## Excepciones
[IOException](/Java/IOException/), [EOFException](/Java/EOFException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageInputStream](/Java/ImageInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
