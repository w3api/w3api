---
title: Connector.BooleanArgument
permalink: /Java/Connector/BooleanArgument/
date: 2021-01-11
key: Java.C.Connector.BooleanArgument
category: Java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Connector.BooleanArgument.description }}

## Sintaxis
~~~java
public static interface Connector.BooleanArgument extends Connector.Argument
~~~

## Métodos
* [booleanValue()](/Java/Connector/BooleanArgument/booleanValue)
* [isValid()](/Java/Connector/BooleanArgument/isValid)
* [setValue()](/Java/Connector/BooleanArgument/setValue)
* [stringValueOf()](/Java/Connector/BooleanArgument/stringValueOf)

## Ejemplo
~~~java
{{ site.data.Java.C.Connector.BooleanArgument.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Connector.BooleanArgument.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
