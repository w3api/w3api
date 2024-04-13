---
title: ResultSetMetaData.isWritable()
permalink: /Java/ResultSetMetaData/isWritable/
date: 2021-01-11
key: Java.R.ResultSetMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSetMetaData.metodos valor="isWritable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isWritable(int column) throws SQLException
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[ResultSetMetaData](/Java/ResultSetMetaData/)

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
