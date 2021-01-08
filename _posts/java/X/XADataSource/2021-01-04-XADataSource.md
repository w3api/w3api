---
title: XADataSource
permalink: Java/XADataSource
date: 2021-01-04
key: JavaJava.X.XADataSource
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XADataSource.description }}

## Sintaxis
~~~java
public interface XADataSource extends CommonDataSource
~~~

## Métodos
* [createXAConnectionBuilder()](/Java/XADataSource/createXAConnectionBuilder)
* [getLoginTimeout()](/Java/XADataSource/getLoginTimeout)
* [getLogWriter()](/Java/XADataSource/getLogWriter)
* [getXAConnection()](/Java/XADataSource/getXAConnection)
* [setLoginTimeout()](/Java/XADataSource/setLoginTimeout)
* [setLogWriter()](/Java/XADataSource/setLogWriter)

## Ejemplo
~~~java
{{ site.data.Java.X.XADataSource.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XADataSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
