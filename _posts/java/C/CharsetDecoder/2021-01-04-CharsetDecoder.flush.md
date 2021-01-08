---
title: CharsetDecoder.flush()
permalink: Java/CharsetDecoder/flush
date: 2021-01-04
key: JavaJava.C.CharsetDecoder
category: java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetDecoder.metodos valor="flush" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CoderResult flush(CharBuffer out)
~~~

## Parámetros
* **CharBuffer out**,  {% include w3api/param_description.html metodo=_data parametro="CharBuffer out" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[CharsetDecoder](/Java/CharsetDecoder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharsetDecoder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
