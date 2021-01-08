---
title: DatabaseMetaData.getIndexInfo()
permalink: Java/DatabaseMetaData/getIndexInfo
date: 2021-01-04
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getIndexInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getIndexInfo(String catalog, String schema, String table, boolean unique, boolean approximate) throws SQLException
~~~

## Parámetros
* **String schema**,  {% include w3api/param_description.html metodo=_data parametro="String schema" %}
* **String table**,  {% include w3api/param_description.html metodo=_data parametro="String table" %}
* **boolean unique**,  {% include w3api/param_description.html metodo=_data parametro="boolean unique" %}
* **boolean approximate**,  {% include w3api/param_description.html metodo=_data parametro="boolean approximate" %}
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
