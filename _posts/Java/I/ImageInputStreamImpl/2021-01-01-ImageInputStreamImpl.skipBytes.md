---
title: ImageInputStreamImpl.skipBytes()
permalink: /Java/ImageInputStreamImpl/skipBytes/
date: 2021-01-11
key: Java.I.ImageInputStreamImpl
category: Java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageInputStreamImpl.metodos valor="skipBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int skipBytes(int n) throws IOException
public long skipBytes(long n) throws IOException
~~~

## Parámetros
* **int n**,  {% include w3api/param_description.html metodo=_dato parametro="int n" %}
* **long n**,  {% include w3api/param_description.html metodo=_dato parametro="long n" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ImageInputStreamImpl](/Java/ImageInputStreamImpl/)

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
