---
title: CharArrayReader.skip()
permalink: Java/CharArrayReader/skip
date: 2021-01-04
key: JavaJava.C.CharArrayReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharArrayReader.metodos valor="skip" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long skip(long n) throws IOException
~~~

## Parámetros
* **long n**,  {% include w3api/param_description.html metodo=_data parametro="long n" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[CharArrayReader](/Java/CharArrayReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharArrayReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
