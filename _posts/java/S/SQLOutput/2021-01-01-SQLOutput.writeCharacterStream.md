---
title: SQLOutput.writeCharacterStream()
permalink: Java/SQLOutput/writeCharacterStream
date: 2021-01-11
key: JavaJava.S.SQLOutput
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutput.metodos valor="writeCharacterStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeCharacterStream(Reader x) throws SQLException
~~~

## Parámetros
* **Reader x**,  {% include w3api/param_description.html metodo=_dato parametro="Reader x" %}

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