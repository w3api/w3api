---
title: ImageOutputStream.writeFloats()
permalink: Java/ImageOutputStream/writeFloats
date: 2021-01-11
key: JavaJava.I.ImageOutputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="writeFloats" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeFloats(float[] f, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **float[] f**,  {% include w3api/param_description.html metodo=_dato parametro="float[] f" %}

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
