---
title: DatabaseMetaData.getColumns()
permalink: /Java/DatabaseMetaData/getColumns/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getColumns" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getColumns(String catalog, String schemaPattern, String tableNamePattern, String columnNamePattern) throws SQLException
~~~

## Parámetros
* **String columnNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String columnNamePattern" %}
* **String tableNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String tableNamePattern" %}
* **String schemaPattern**,  {% include w3api/param_description.html metodo=_dato parametro="String schemaPattern" %}
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
