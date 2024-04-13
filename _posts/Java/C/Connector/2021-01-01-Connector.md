---
title: Connector
permalink: /Java/Connector/
date: 2021-01-11
key: Java.C.Connector
category: Java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Connector.description }}

## Sintaxis
~~~java
public interface Connector
~~~

## Métodos
* [defaultArguments()](/Java/Connector/defaultArguments/)
* [description()](/Java/Connector/description/)
* [name()](/Java/Connector/name/)
* [transport()](/Java/Connector/transport/)

## Ejemplo
~~~java
{{ site.data.Java.C.Connector.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Connector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
