---
title: DecimalFormat.formatToCharacterIterator()
permalink: /Java/DecimalFormat/formatToCharacterIterator/
date: 2021-01-11
key: Java.D.DecimalFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DecimalFormat.metodos valor="formatToCharacterIterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttributedCharacterIterator formatToCharacterIterator(Object obj)
~~~

## Parámetros
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArithmeticException](/Java/ArithmeticException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DecimalFormat](/Java/DecimalFormat/)

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
