---
title: BreakIterator.following()
permalink: Java/BreakIterator/following
date: 2021-01-04
key: JavaJava.B.BreakIterator
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BreakIterator.metodos valor="following" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int following(int offset)
~~~

## Parámetros
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BreakIterator](/Java/BreakIterator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BreakIterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
