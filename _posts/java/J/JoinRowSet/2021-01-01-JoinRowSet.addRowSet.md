---
title: JoinRowSet.addRowSet()
permalink: Java/JoinRowSet/addRowSet
date: 2021-01-11
key: JavaJava.J.JoinRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JoinRowSet.metodos valor="addRowSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addRowSet(Joinable rowset) throws SQLException
void addRowSet(RowSet[] rowset, int[] columnIdx) throws SQLException
void addRowSet(RowSet[] rowset, String[] columnName) throws SQLException
void addRowSet(RowSet rowset, int columnIdx) throws SQLException
void addRowSet(RowSet rowset, String columnName) throws SQLException
~~~

## Parámetros
* **String[] columnName**,  {% include w3api/param_description.html metodo=_dato parametro="String[] columnName" %}
* **Joinable rowset**,  {% include w3api/param_description.html metodo=_dato parametro="Joinable rowset" %}
* **RowSet rowset**,  {% include w3api/param_description.html metodo=_dato parametro="RowSet rowset" %}
* **int columnIdx**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIdx" %}
* **String columnName**,  {% include w3api/param_description.html metodo=_dato parametro="String columnName" %}
* **RowSet[] rowset**,  {% include w3api/param_description.html metodo=_dato parametro="RowSet[] rowset" %}
* **int[] columnIdx**,  {% include w3api/param_description.html metodo=_dato parametro="int[] columnIdx" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[JoinRowSet](/Java/JoinRowSet/)

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
