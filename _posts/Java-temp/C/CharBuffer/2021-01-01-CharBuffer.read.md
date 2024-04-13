---
title: CharBuffer.read()
permalink: /Java/CharBuffer/read/
date: 2021-01-11
key: Java.C.CharBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharBuffer.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int read(CharBuffer target) throws IOException
~~~

## Parámetros
* **CharBuffer target**,  {% include w3api/param_description.html metodo=_dato parametro="CharBuffer target" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IOException](/Java/IOException/)

## Clase Padre
[CharBuffer](/Java/CharBuffer/)

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
