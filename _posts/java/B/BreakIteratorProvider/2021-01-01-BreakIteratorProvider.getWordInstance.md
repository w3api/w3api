---
title: BreakIteratorProvider.getWordInstance()
permalink: Java/BreakIteratorProvider/getWordInstance
date: 2021-01-11
key: JavaJava.B.BreakIteratorProvider
category: java
tags: ['java se', 'java.text.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BreakIteratorProvider.metodos valor="getWordInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract BreakIterator getWordInstance(Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BreakIteratorProvider](/Java/BreakIteratorProvider/)

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
