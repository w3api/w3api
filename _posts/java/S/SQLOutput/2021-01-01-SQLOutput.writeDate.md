---
title: SQLOutput.writeDate()
permalink: Java/SQLOutput/writeDate
date: 2021-01-11
key: JavaJava.S.SQLOutput
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutput.metodos valor="writeDate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeDate(Date x) throws SQLException
~~~

## Parámetros
* **Date x**,  {% include w3api/param_description.html metodo=_dato parametro="Date x" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[SQLOutput](/Java/SQLOutput/)

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
