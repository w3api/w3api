---
title: PooledConnection
permalink: /Java/PooledConnection/
date: 2021-01-11
key: Java.P.PooledConnection
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PooledConnection.description }}

## Sintaxis
~~~java
public interface PooledConnection
~~~

## Métodos
* [addConnectionEventListener()](/Java/PooledConnection/addConnectionEventListener)
* [addStatementEventListener()](/Java/PooledConnection/addStatementEventListener)
* [close()](/Java/PooledConnection/close)
* [getConnection()](/Java/PooledConnection/getConnection)
* [removeConnectionEventListener()](/Java/PooledConnection/removeConnectionEventListener)
* [removeStatementEventListener()](/Java/PooledConnection/removeStatementEventListener)

## Ejemplo
~~~java
{{ site.data.Java.P.PooledConnection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PooledConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
