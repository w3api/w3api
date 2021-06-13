---
title: DatabaseMetaData.getBestRowIdentifier()
permalink: /Java/DatabaseMetaData/getBestRowIdentifier/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getBestRowIdentifier" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getBestRowIdentifier(String catalog, String schema, String table, int scope, boolean nullable) throws SQLException
~~~

## Parámetros
* **String schema**,  {% include w3api/param_description.html metodo=_dato parametro="String schema" %}
* **boolean nullable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean nullable" %}
* **String table**,  {% include w3api/param_description.html metodo=_dato parametro="String table" %}
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}
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
