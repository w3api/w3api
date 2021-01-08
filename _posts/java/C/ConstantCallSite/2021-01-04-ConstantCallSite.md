---
title: ConstantCallSite
permalink: Java/ConstantCallSite
date: 2021-01-04
key: JavaJava.C.ConstantCallSite
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConstantCallSite.description }}

## Sintaxis
~~~java
public class ConstantCallSite extends CallSite
~~~

## Constructores
* [ConstantCallSite()](/Java/ConstantCallSite/ConstantCallSite/)

## Métodos
* [dynamicInvoker()](/Java/ConstantCallSite/dynamicInvoker)
* [getTarget()](/Java/ConstantCallSite/getTarget)
* [setTarget()](/Java/ConstantCallSite/setTarget)

## Ejemplo
~~~java
{{ site.data.Java.C.ConstantCallSite.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConstantCallSite.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
