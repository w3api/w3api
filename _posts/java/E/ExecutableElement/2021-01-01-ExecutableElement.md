---
title: ExecutableElement
permalink: Java/ExecutableElement
date: 2021-01-11
key: JavaJava.E.ExecutableElement
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExecutableElement.description }}

## Sintaxis
~~~java
public interface ExecutableElement extends Element, Parameterizable
~~~

## Métodos
* [getDefaultValue()](/Java/ExecutableElement/getDefaultValue)
* [getParameters()](/Java/ExecutableElement/getParameters)
* [getReceiverType()](/Java/ExecutableElement/getReceiverType)
* [getReturnType()](/Java/ExecutableElement/getReturnType)
* [getSimpleName()](/Java/ExecutableElement/getSimpleName)
* [getThrownTypes()](/Java/ExecutableElement/getThrownTypes)
* [getTypeParameters()](/Java/ExecutableElement/getTypeParameters)
* [isDefault()](/Java/ExecutableElement/isDefault)
* [isVarArgs()](/Java/ExecutableElement/isVarArgs)

## Ejemplo
~~~java
{{ site.data.Java.E.ExecutableElement.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutableElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
