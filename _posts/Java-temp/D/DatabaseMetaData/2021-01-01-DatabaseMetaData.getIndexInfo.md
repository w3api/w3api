---
title: DatabaseMetaData.getIndexInfo()
permalink: /Java/DatabaseMetaData/getIndexInfo/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
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
* **boolean approximate**,  {% include w3api/param_description.html metodo=_dato parametro="boolean approximate" %}
* **String schema**,  {% include w3api/param_description.html metodo=_dato parametro="String schema" %}
* **String table**,  {% include w3api/param_description.html metodo=_dato parametro="String table" %}
* **boolean unique**,  {% include w3api/param_description.html metodo=_dato parametro="boolean unique" %}
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
