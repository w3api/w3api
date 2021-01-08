---
title: RowSetMetaData.setColumnTypeName()
permalink: Java/RowSetMetaData/setColumnTypeName
date: 2021-01-04
key: JavaJava.R.RowSetMetaData
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetMetaData.metodos valor="setColumnTypeName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setColumnTypeName(int columnIndex, String typeName) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_data parametro="String typeName" %}

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
