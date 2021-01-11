---
title: DatabaseMetaData.supportsResultSetConcurrency()
permalink: Java/DatabaseMetaData/supportsResultSetConcurrency
date: 2021-01-11
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="supportsResultSetConcurrency" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean supportsResultSetConcurrency(int type, int concurrency) throws SQLException
~~~

## Parámetros
* **int concurrency**,  {% include w3api/param_description.html metodo=_dato parametro="int concurrency" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}

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
