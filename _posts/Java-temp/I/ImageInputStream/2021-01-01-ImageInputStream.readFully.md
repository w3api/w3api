---
title: ImageInputStream.readFully()
permalink: /Java/ImageInputStream/readFully/
date: 2021-01-11
key: Java.I.ImageInputStream
category: Java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageInputStream.metodos valor="readFully" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readFully(byte[] b) throws IOException
void readFully(byte[] b, int off, int len) throws IOException
void readFully(char[] c, int off, int len) throws IOException
void readFully(double[] d, int off, int len) throws IOException
void readFully(float[] f, int off, int len) throws IOException
void readFully(int[] i, int off, int len) throws IOException
void readFully(long[] l, int off, int len) throws IOException
void readFully(short[] s, int off, int len) throws IOException
~~~

## Parámetros
* **double[] d**,  {% include w3api/param_description.html metodo=_dato parametro="double[] d" %}
* **float[] f**,  {% include w3api/param_description.html metodo=_dato parametro="float[] f" %}
* **short[] s**,  {% include w3api/param_description.html metodo=_dato parametro="short[] s" %}
* **int[] i**,  {% include w3api/param_description.html metodo=_dato parametro="int[] i" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}
* **char[] c**,  {% include w3api/param_description.html metodo=_dato parametro="char[] c" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **long[] l**,  {% include w3api/param_description.html metodo=_dato parametro="long[] l" %}

## Excepciones
[IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [EOFException](/Java/EOFException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ImageInputStream](/Java/ImageInputStream/)

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
