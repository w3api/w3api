---
title: JdbcRowSet
permalink: Java/JdbcRowSet
date: 2021-01-11
key: JavaJava.J.JdbcRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JdbcRowSet.description }}

## Sintaxis
~~~java
public interface JdbcRowSet extends RowSet, Joinable
~~~

## Métodos
* [commit()](/Java/JdbcRowSet/commit)
* [getAutoCommit()](/Java/JdbcRowSet/getAutoCommit)
* [getRowSetWarnings()](/Java/JdbcRowSet/getRowSetWarnings)
* [getShowDeleted()](/Java/JdbcRowSet/getShowDeleted)
* [rollback()](/Java/JdbcRowSet/rollback)
* [setAutoCommit()](/Java/JdbcRowSet/setAutoCommit)
* [setShowDeleted()](/Java/JdbcRowSet/setShowDeleted)

## Ejemplo
~~~java
{{ site.data.Java.J.JdbcRowSet.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JdbcRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
