---
title: RowSetMetaData.setColumnCount()
permalink: Java/RowSetMetaData/setColumnCount
date: 2021-01-04
key: JavaJava.R.RowSetMetaData
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetMetaData.metodos valor="setColumnCount" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setColumnCount(int columnCount) throws SQLException
~~~

## Parámetros
* **int columnCount**,  {% include w3api/param_description.html metodo=_data parametro="int columnCount" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetMetaData](/Java/RowSetMetaData/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RowSetMetaData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
