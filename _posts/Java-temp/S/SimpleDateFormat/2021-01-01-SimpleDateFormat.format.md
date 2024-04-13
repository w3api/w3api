---
title: SimpleDateFormat.format()
permalink: /Java/SimpleDateFormat/format/
date: 2021-01-11
key: Java.S.SimpleDateFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleDateFormat.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuffer format(Date date, StringBuffer toAppendTo, FieldPosition pos)
~~~

## Parámetros
* **Date date**,  {% include w3api/param_description.html metodo=_dato parametro="Date date" %}
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_dato parametro="StringBuffer toAppendTo" %}
* **FieldPosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="FieldPosition pos" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SimpleDateFormat](/Java/SimpleDateFormat/)

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
