---
title: AttributedString.addAttributes()
permalink: Java/AttributedString/addAttributes
date: 2021-01-11
key: JavaJava.A.AttributedString
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributedString.metodos valor="addAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addAttributes(Map<? extends AttributedCharacterIterator.Attribute,?> attributes, int beginIndex, int endIndex)
~~~

## Parámetros
* **?&gt; attributes**,  {% include w3api/param_description.html metodo=_dato parametro="?> attributes" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginIndex" %}
* **Map&lt;? extends AttributedCharacterIterator.Attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends AttributedCharacterIterator.Attribute" %}
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
