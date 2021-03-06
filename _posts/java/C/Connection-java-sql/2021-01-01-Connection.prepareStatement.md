---
title: Connection.prepareStatement()
permalink: /Java/Connection-java-sql/prepareStatement/
date: 2021-01-11
key: Java.C.Connection-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="prepareStatement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
PreparedStatement prepareStatement(String sql) throws SQLException
PreparedStatement prepareStatement(String sql, int autoGeneratedKeys) throws SQLException
PreparedStatement prepareStatement(String sql, int[] columnIndexes) throws SQLException
PreparedStatement prepareStatement(String sql, int resultSetType, int resultSetConcurrency) throws SQLException
PreparedStatement prepareStatement(String sql, int resultSetType, int resultSetConcurrency, int resultSetHoldability) throws SQLException
PreparedStatement prepareStatement(String sql, String[] columnNames) throws SQLException
~~~

## Parámetros
* **int autoGeneratedKeys**,  {% include w3api/param_description.html metodo=_dato parametro="int autoGeneratedKeys" %}
* **int[] columnIndexes**,  {% include w3api/param_description.html metodo=_dato parametro="int[] columnIndexes" %}
* **int resultSetHoldability**,  {% include w3api/param_description.html metodo=_dato parametro="int resultSetHoldability" %}
* **String sql**,  {% include w3api/param_description.html metodo=_dato parametro="String sql" %}
* **int resultSetType**,  {% include w3api/param_description.html metodo=_dato parametro="int resultSetType" %}
* **String[] columnNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] columnNames" %}
* **int resultSetConcurrency**,  {% include w3api/param_description.html metodo=_dato parametro="int resultSetConcurrency" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
