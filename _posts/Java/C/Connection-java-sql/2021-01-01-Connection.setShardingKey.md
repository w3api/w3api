---
title: Connection.setShardingKey()
permalink: /Java/Connection-java-sql/setShardingKey/
date: 2021-01-11
key: Java.C.Connection-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="setShardingKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void setShardingKey(ShardingKey shardingKey) throws SQLException
default void setShardingKey(ShardingKey shardingKey, ShardingKey superShardingKey) throws SQLException
~~~

## Parámetros
* **ShardingKey shardingKey**,  {% include w3api/param_description.html metodo=_dato parametro="ShardingKey shardingKey" %}
* **ShardingKey superShardingKey**,  {% include w3api/param_description.html metodo=_dato parametro="ShardingKey superShardingKey" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
