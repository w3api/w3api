---
title: ImageOutputStream.writeChars()
permalink: /Java/ImageOutputStream/writeChars/
date: 2021-01-11
key: Java.I.ImageOutputStream
category: Java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="writeChars" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeChars(char[] c, int off, int len) throws IOException
void writeChars(String s) throws IOException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **char[] c**,  {% include w3api/param_description.html metodo=_dato parametro="char[] c" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

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
