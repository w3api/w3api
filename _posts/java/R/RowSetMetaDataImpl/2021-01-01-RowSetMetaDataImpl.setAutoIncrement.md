---
title: RowSetMetaDataImpl.setAutoIncrement()
permalink: Java/RowSetMetaDataImpl/setAutoIncrement
date: 2021-01-11
key: JavaJava.R.RowSetMetaDataImpl
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetMetaDataImpl.metodos valor="setAutoIncrement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setAutoIncrement(int columnIndex, boolean property) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **boolean property**,  {% include w3api/param_description.html metodo=_dato parametro="boolean property" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetMetaDataImpl](/Java/RowSetMetaDataImpl/)

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