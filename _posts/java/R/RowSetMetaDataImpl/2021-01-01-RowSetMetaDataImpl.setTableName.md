---
title: RowSetMetaDataImpl.setTableName()
permalink: /Java/RowSetMetaDataImpl/setTableName/
date: 2021-01-11
key: Java.R.RowSetMetaDataImpl
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetMetaDataImpl.metodos valor="setTableName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTableName(int columnIndex, String tableName) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **String tableName**,  {% include w3api/param_description.html metodo=_dato parametro="String tableName" %}

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
