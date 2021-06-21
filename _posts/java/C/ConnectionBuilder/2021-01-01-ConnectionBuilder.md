---
title: ConnectionBuilder
permalink: /Java/ConnectionBuilder/
date: 2021-01-11
key: Java.C.ConnectionBuilder
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConnectionBuilder.description }}

## Sintaxis
~~~java
public interface ConnectionBuilder
~~~

## Métodos
* [build()](/Java/ConnectionBuilder/build)
* [password()](/Java/ConnectionBuilder/password)
* [shardingKey()](/Java/ConnectionBuilder/shardingKey)
* [superShardingKey()](/Java/ConnectionBuilder/superShardingKey)
* [user()](/Java/ConnectionBuilder/user)

## Ejemplo
~~~java
{{ site.data.Java.C.ConnectionBuilder.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ConnectionBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
