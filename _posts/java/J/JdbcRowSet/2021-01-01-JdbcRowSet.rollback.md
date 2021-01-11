---
title: JdbcRowSet.rollback()
permalink: Java/JdbcRowSet/rollback
date: 2021-01-11
key: JavaJava.J.JdbcRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JdbcRowSet.metodos valor="rollback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void rollback() throws SQLException
void rollback(Savepoint s) throws SQLException
~~~

## Parámetros
* **Savepoint s**,  {% include w3api/param_description.html metodo=_dato parametro="Savepoint s" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[JdbcRowSet](/Java/JdbcRowSet/)

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
