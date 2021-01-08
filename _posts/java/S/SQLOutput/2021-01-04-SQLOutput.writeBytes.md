---
title: SQLOutput.writeBytes()
permalink: Java/SQLOutput/writeBytes
date: 2021-01-04
key: JavaJava.S.SQLOutput
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutput.metodos valor="writeBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeBytes(byte[] x) throws SQLException
~~~

## Parámetros
* **byte[] x**,  {% include w3api/param_description.html metodo=_data parametro="byte[] x" %}

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
{%- for _ldc in site.data.Java.S.SQLOutput.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
