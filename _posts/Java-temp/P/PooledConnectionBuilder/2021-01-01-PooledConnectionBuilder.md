---
title: PooledConnectionBuilder
permalink: /Java/PooledConnectionBuilder/
date: 2021-01-11
key: Java.P.PooledConnectionBuilder
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PooledConnectionBuilder.description }}

## Sintaxis
~~~java
public interface PooledConnectionBuilder
~~~

## Métodos
* [build()](/Java/PooledConnectionBuilder/build)
* [password()](/Java/PooledConnectionBuilder/password)
* [shardingKey()](/Java/PooledConnectionBuilder/shardingKey)
* [superShardingKey()](/Java/PooledConnectionBuilder/superShardingKey)
* [user()](/Java/PooledConnectionBuilder/user)

## Ejemplo
~~~java
{{ site.data.Java.P.PooledConnectionBuilder.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PooledConnectionBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
