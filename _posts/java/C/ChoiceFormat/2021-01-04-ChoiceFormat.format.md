---
title: ChoiceFormat.format()
permalink: Java/ChoiceFormat/format
date: 2021-01-04
key: JavaJava.C.ChoiceFormat
category: java
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
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_data parametro="StringBuffer toAppendTo" %}
* **long number**,  {% include w3api/param_description.html metodo=_data parametro="long number" %}
* **FieldPosition status**,  {% include w3api/param_description.html metodo=_data parametro="FieldPosition status" %}
* **double number**,  {% include w3api/param_description.html metodo=_data parametro="double number" %}

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
{%- for _ldc in site.data.Java.C.ChoiceFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
