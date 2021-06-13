---
title: SQLOutput.writeTime()
permalink: /Java/SQLOutput/writeTime/
date: 2021-01-11
key: Java.S.SQLOutput
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutput.metodos valor="writeTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeTime(Time x) throws SQLException
~~~

## Parámetros
* **Time x**,  {% include w3api/param_description.html metodo=_dato parametro="Time x" %}

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
