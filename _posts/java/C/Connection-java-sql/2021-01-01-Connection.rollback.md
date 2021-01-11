---
title: Connection.rollback()
permalink: Java/Connection-java-sql/rollback
date: 2021-01-11
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="rollback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void rollback() throws SQLException
void rollback(Savepoint savepoint) throws SQLException
~~~

## Parámetros
* **Savepoint savepoint**,  {% include w3api/param_description.html metodo=_dato parametro="Savepoint savepoint" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>