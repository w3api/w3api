---
title: ChoiceFormat.format()
permalink: /Java/ChoiceFormat/format/
date: 2021-01-11
key: Java.C.ChoiceFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceFormat.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuffer format(double number, StringBuffer toAppendTo, FieldPosition status)
public StringBuffer format(long number, StringBuffer toAppendTo, FieldPosition status)
~~~

## Parámetros
* **FieldPosition status**,  {% include w3api/param_description.html metodo=_dato parametro="FieldPosition status" %}
* **long number**,  {% include w3api/param_description.html metodo=_dato parametro="long number" %}
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_dato parametro="StringBuffer toAppendTo" %}
* **double number**,  {% include w3api/param_description.html metodo=_dato parametro="double number" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ChoiceFormat](/Java/ChoiceFormat/)

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
