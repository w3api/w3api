---
title: BreakIterator.setText()
permalink: /Java/BreakIterator/setText/
date: 2021-01-11
key: Java.B.BreakIterator
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BreakIterator.metodos valor="setText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setText(String newText)
public abstract void setText(CharacterIterator newText)
~~~

## Parámetros
* **String newText**,  {% include w3api/param_description.html metodo=_dato parametro="String newText" %}
* **CharacterIterator newText**,  {% include w3api/param_description.html metodo=_dato parametro="CharacterIterator newText" %}

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
