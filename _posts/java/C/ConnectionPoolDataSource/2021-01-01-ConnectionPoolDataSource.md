---
title: ConnectionPoolDataSource
permalink: Java/ConnectionPoolDataSource
date: 2021-01-11
key: JavaJava.C.ConnectionPoolDataSource
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConnectionPoolDataSource.description }}

## Sintaxis
~~~java
public interface ConnectionPoolDataSource extends CommonDataSource
~~~

## Métodos
* [createPooledConnectionBuilder()](/Java/ConnectionPoolDataSource/createPooledConnectionBuilder)
* [getLoginTimeout()](/Java/ConnectionPoolDataSource/getLoginTimeout)
* [getLogWriter()](/Java/ConnectionPoolDataSource/getLogWriter)
* [getPooledConnection()](/Java/ConnectionPoolDataSource/getPooledConnection)
* [setLoginTimeout()](/Java/ConnectionPoolDataSource/setLoginTimeout)
* [setLogWriter()](/Java/ConnectionPoolDataSource/setLogWriter)

## Ejemplo
~~~java
{{ site.data.Java.C.ConnectionPoolDataSource.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConnectionPoolDataSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
