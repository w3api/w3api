---
title: DatabaseMetaData.getPseudoColumns()
permalink: Java/DatabaseMetaData/getPseudoColumns
date: 2021-01-04
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getPseudoColumns" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getPseudoColumns(String catalog, String schemaPattern, String tableNamePattern, String columnNamePattern) throws SQLException
~~~

## Parámetros
* **String tableNamePattern**,  {% include w3api/param_description.html metodo=_data parametro="String tableNamePattern" %}
* **String catalog**,  {% include w3api/param_description.html metodo=_data parametro="String catalog" %}
* **String schemaPattern**,  {% include w3api/param_description.html metodo=_data parametro="String schemaPattern" %}
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
