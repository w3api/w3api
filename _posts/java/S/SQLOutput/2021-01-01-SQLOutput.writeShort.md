---
title: SQLOutput.writeShort()
permalink: Java/SQLOutput/writeShort
date: 2021-01-11
key: JavaJava.S.SQLOutput
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutput.metodos valor="writeShort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeShort(short x) throws SQLException
~~~

## Parámetros
* **short x**,  {% include w3api/param_description.html metodo=_dato parametro="short x" %}

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
