---
title: StringJoiner.setEmptyValue()
permalink: /Java/StringJoiner/setEmptyValue/
date: 2021-01-11
key: Java.S.StringJoiner
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringJoiner.metodos valor="setEmptyValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringJoiner setEmptyValue(CharSequence emptyValue)
~~~

## Parámetros
* **CharSequence emptyValue**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence emptyValue" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[StringJoiner](/Java/StringJoiner/)

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
