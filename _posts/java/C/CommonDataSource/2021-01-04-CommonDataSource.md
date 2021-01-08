---
title: CommonDataSource
permalink: Java/CommonDataSource
date: 2021-01-04
key: JavaJava.C.CommonDataSource
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CommonDataSource.description }}

## Sintaxis
~~~java
public interface CommonDataSource
~~~

## Métodos
* [createShardingKeyBuilder()](/Java/CommonDataSource/createShardingKeyBuilder)
* [getLoginTimeout()](/Java/CommonDataSource/getLoginTimeout)
* [getLogWriter()](/Java/CommonDataSource/getLogWriter)
* [getParentLogger()](/Java/CommonDataSource/getParentLogger)
* [setLoginTimeout()](/Java/CommonDataSource/setLoginTimeout)
* [setLogWriter()](/Java/CommonDataSource/setLogWriter)

## Ejemplo
~~~java
{{ site.data.Java.C.CommonDataSource.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CommonDataSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
