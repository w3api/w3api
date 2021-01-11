---
title: AttributedString.getIterator()
permalink: Java/AttributedString/getIterator
date: 2021-01-11
key: JavaJava.A.AttributedString
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributedString.metodos valor="getIterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttributedCharacterIterator getIterator()
public AttributedCharacterIterator getIterator(AttributedCharacterIterator.Attribute[] attributes)
public AttributedCharacterIterator getIterator(AttributedCharacterIterator.Attribute[] attributes, int beginIndex, int endIndex)
~~~

## Parámetros
* **AttributedCharacterIterator.Attribute[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator.Attribute[] attributes" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginIndex" %}
* **int endIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int endIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AttributedString](/Java/AttributedString/)

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
