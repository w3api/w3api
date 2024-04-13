---
title: ExecutionEnv
permalink: /Java/ExecutionEnv/
date: 2021-01-11
key: Java.E.ExecutionEnv
category: Java
tags: ['java se', 'jdk.jshell.spi', 'jdk.jshell', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExecutionEnv.description }}

## Sintaxis
~~~java
public interface ExecutionEnv
~~~

## Métodos
* [closeDown()](/Java/ExecutionEnv/closeDown/)
* [extraRemoteVMOptions()](/Java/ExecutionEnv/extraRemoteVMOptions/)
* [userErr()](/Java/ExecutionEnv/userErr/)
* [userIn()](/Java/ExecutionEnv/userIn/)
* [userOut()](/Java/ExecutionEnv/userOut/)

## Ejemplo
~~~java
{{ site.data.Java.E.ExecutionEnv.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutionEnv.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
