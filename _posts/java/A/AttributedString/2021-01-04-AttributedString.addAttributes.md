---
title: AttributedString.addAttributes()
permalink: Java/AttributedString/addAttributes
date: 2021-01-04
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
* **int endIndex**,  {% include w3api/param_description.html metodo=_data parametro="int endIndex" %}
* **Map&lt;? extends AttributedCharacterIterator.Attribute**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends AttributedCharacterIterator.Attribute" %}
* **?&gt; attributes**,  {% include w3api/param_description.html metodo=_data parametro="?> attributes" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_data parametro="int beginIndex" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AttributedString](/Java/AttributedString/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttributedString.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
