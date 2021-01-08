---
title: ImageInputStream.readFully()
permalink: Java/ImageInputStream/readFully
date: 2021-01-04
key: JavaJava.I.ImageInputStream
category: java
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
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **long[] l**,  {% include w3api/param_description.html metodo=_data parametro="long[] l" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **short[] s**,  {% include w3api/param_description.html metodo=_data parametro="short[] s" %}
* **double[] d**,  {% include w3api/param_description.html metodo=_data parametro="double[] d" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int[] i**,  {% include w3api/param_description.html metodo=_data parametro="int[] i" %}
* **float[] f**,  {% include w3api/param_description.html metodo=_data parametro="float[] f" %}
* **char[] c**,  {% include w3api/param_description.html metodo=_data parametro="char[] c" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [EOFException](/Java/EOFException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

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
