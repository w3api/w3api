---
title: ImageOutputStream.writeLongs()
permalink: Java/ImageOutputStream/writeLongs
date: 2021-01-11
key: JavaJava.I.ImageOutputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="writeLongs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeLongs(long[] l, int off, int len) throws IOException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **long[] l**,  {% include w3api/param_description.html metodo=_dato parametro="long[] l" %}

## Excepciones
[IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

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
