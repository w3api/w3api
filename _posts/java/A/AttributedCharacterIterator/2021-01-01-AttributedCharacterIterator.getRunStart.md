---
title: AttributedCharacterIterator.getRunStart()
permalink: Java/AttributedCharacterIterator/getRunStart
date: 2021-01-11
key: JavaJava.A.AttributedCharacterIterator
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributedCharacterIterator.metodos valor="getRunStart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int getRunStart()
int getRunStart(AttributedCharacterIterator.Attribute attribute)
int getRunStart(Set<? extends AttributedCharacterIterator.Attribute> attributes)
~~~

## Parámetros
* **Set&lt;? extends AttributedCharacterIterator.Attribute&gt; attributes**,  {% include w3api/param_description.html metodo=_dato parametro="Set<? extends AttributedCharacterIterator.Attribute> attributes" %}
* **AttributedCharacterIterator.Attribute attribute**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator.Attribute attribute" %}

## Clase Padre
[AttributedCharacterIterator](/Java/AttributedCharacterIterator/)

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
