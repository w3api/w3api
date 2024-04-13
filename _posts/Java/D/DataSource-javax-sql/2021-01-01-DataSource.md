---
title: DataSource
permalink: /Java/DataSource-javax-sql/
date: 2021-01-11
key: Java.D.DataSource-javax-sql
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DataSource-javax-sql.description }}

## Sintaxis
~~~java
public interface DataSource extends CommonDataSource, Wrapper
~~~

## Métodos
* [createConnectionBuilder()](/Java/DataSource-javax-sql/createConnectionBuilder)
* [getConnection()](/Java/DataSource-javax-sql/getConnection)
* [getLoginTimeout()](/Java/DataSource-javax-sql/getLoginTimeout)
* [getLogWriter()](/Java/DataSource-javax-sql/getLogWriter)
* [setLoginTimeout()](/Java/DataSource-javax-sql/setLoginTimeout)
* [setLogWriter()](/Java/DataSource-javax-sql/setLogWriter)

## Ejemplo
~~~java
{{ site.data.Java.D.DataSource-javax-sql.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataSource-javax-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
