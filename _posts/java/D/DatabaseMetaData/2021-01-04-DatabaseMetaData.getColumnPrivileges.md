---
title: DatabaseMetaData.getColumnPrivileges()
permalink: Java/DatabaseMetaData/getColumnPrivileges
date: 2021-01-04
key: JavaJava.D.DatabaseMetaData
category: java
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
* **String table**,  {% include w3api/param_description.html metodo=_data parametro="String table" %}
* **String schema**,  {% include w3api/param_description.html metodo=_data parametro="String schema" %}
* **String catalog**,  {% include w3api/param_description.html metodo=_data parametro="String catalog" %}
* **String columnNamePattern**,  {% include w3api/param_description.html metodo=_data parametro="String columnNamePattern" %}

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
{%- for _ldc in site.data.Java.D.DatabaseMetaData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
