---
title: DatabaseMetaData.getColumnPrivileges()
permalink: /Java/DatabaseMetaData/getColumnPrivileges/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getColumnPrivileges" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getColumnPrivileges(String catalog, String schema, String table, String columnNamePattern) throws SQLException
~~~

## Parámetros
* **String table**,  {% include w3api/param_description.html metodo=_dato parametro="String table" %}
* **String columnNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String columnNamePattern" %}
* **String schema**,  {% include w3api/param_description.html metodo=_dato parametro="String schema" %}
* **String catalog**,  {% include w3api/param_description.html metodo=_dato parametro="String catalog" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[DatabaseMetaData](/Java/DatabaseMetaData/)

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
