---
title: DatabaseMetaData.getProcedureColumns()
permalink: /Java/DatabaseMetaData/getProcedureColumns/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getProcedureColumns" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getProcedureColumns(String catalog, String schemaPattern, String procedureNamePattern, String columnNamePattern) throws SQLException
~~~

## Parámetros
* **String procedureNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String procedureNamePattern" %}
* **String columnNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String columnNamePattern" %}
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
