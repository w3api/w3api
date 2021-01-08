---
title: DatabaseMetaData.getImportedKeys()
permalink: Java/DatabaseMetaData/getImportedKeys
date: 2021-01-04
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getImportedKeys" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getImportedKeys(String catalog, String schema, String table) throws SQLException
~~~

## Parámetros
* **String table**,  {% include w3api/param_description.html metodo=_data parametro="String table" %}
* **String schema**,  {% include w3api/param_description.html metodo=_data parametro="String schema" %}
* **String catalog**,  {% include w3api/param_description.html metodo=_data parametro="String catalog" %}

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
