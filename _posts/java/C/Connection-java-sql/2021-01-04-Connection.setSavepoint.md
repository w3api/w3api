---
title: Connection.setSavepoint()
permalink: Java/Connection-java-sql/setSavepoint
date: 2021-01-04
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="setSavepoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Savepoint setSavepoint() throws SQLException
Savepoint setSavepoint(String name) throws SQLException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Connection-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
