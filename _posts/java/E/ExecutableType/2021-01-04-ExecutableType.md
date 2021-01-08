---
title: ExecutableType
permalink: Java/ExecutableType
date: 2021-01-04
key: JavaJava.E.ExecutableType
category: java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExecutableType.description }}

## Sintaxis
~~~java
public interface ExecutableType extends TypeMirror
~~~

## Métodos
* [getParameterTypes()](/Java/ExecutableType/getParameterTypes)
* [getReceiverType()](/Java/ExecutableType/getReceiverType)
* [getReturnType()](/Java/ExecutableType/getReturnType)
* [getThrownTypes()](/Java/ExecutableType/getThrownTypes)
* [getTypeVariables()](/Java/ExecutableType/getTypeVariables)

## Ejemplo
~~~java
{{ site.data.Java.E.ExecutableType.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutableType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
