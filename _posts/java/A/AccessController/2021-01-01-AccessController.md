---
title: AccessController
permalink: Java/AccessController
date: 2021-01-11
key: JavaJava.A.AccessController
category: java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AccessController.description }}

## Sintaxis
~~~java
public final class AccessController extends Object
~~~

## Métodos
* [checkPermission()](/Java/AccessController/checkPermission)
* [doPrivileged()](/Java/AccessController/doPrivileged)
* [doPrivilegedWithCombiner()](/Java/AccessController/doPrivilegedWithCombiner)
* [getContext()](/Java/AccessController/getContext)

## Ejemplo
~~~java
{{ site.data.Java.A.AccessController.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AccessController.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
