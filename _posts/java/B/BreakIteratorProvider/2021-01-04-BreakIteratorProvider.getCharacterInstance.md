---
title: BreakIteratorProvider.getCharacterInstance()
permalink: Java/BreakIteratorProvider/getCharacterInstance
date: 2021-01-04
key: JavaJava.B.BreakIteratorProvider
category: java
tags: ['java se', 'java.text.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BreakIteratorProvider.metodos valor="getCharacterInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract BreakIterator getCharacterInstance(Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BreakIteratorProvider](/Java/BreakIteratorProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BreakIteratorProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
