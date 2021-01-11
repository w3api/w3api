---
title: AttributedString.addAttribute()
permalink: Java/AttributedString/addAttribute
date: 2021-01-11
key: JavaJava.A.AttributedString
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributedString.metodos valor="addAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addAttribute(AttributedCharacterIterator.Attribute attribute, Object value)
public void addAttribute(AttributedCharacterIterator.Attribute attribute, Object value, int beginIndex, int endIndex)
~~~

## Parámetros
* **int beginIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginIndex" %}
* **AttributedCharacterIterator.Attribute attribute**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator.Attribute attribute" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **int endIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int endIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
