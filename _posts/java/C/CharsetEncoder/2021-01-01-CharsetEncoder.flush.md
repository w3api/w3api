---
title: CharsetEncoder.flush()
permalink: Java/CharsetEncoder/flush
date: 2021-01-11
key: JavaJava.C.CharsetEncoder
category: java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetEncoder.metodos valor="flush" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CoderResult flush(ByteBuffer out)
~~~

## Parámetros
* **ByteBuffer out**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer out" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[CharsetEncoder](/Java/CharsetEncoder/)

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