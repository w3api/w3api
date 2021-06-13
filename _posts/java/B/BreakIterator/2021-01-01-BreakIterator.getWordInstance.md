---
title: BreakIterator.getWordInstance()
permalink: /Java/BreakIterator/getWordInstance/
date: 2021-01-11
key: Java.B.BreakIterator
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BreakIterator.metodos valor="getWordInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static BreakIterator getWordInstance()
public static BreakIterator getWordInstance(Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BreakIterator](/Java/BreakIterator/)

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
