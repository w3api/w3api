---
title: SecureClassLoader
permalink: /Java/SecureClassLoader/
date: 2021-01-11
key: Java.S.SecureClassLoader
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SecureClassLoader.description }}

## Sintaxis
~~~java
public class SecureClassLoader extends ClassLoader
~~~

## Constructores
* [SecureClassLoader()](/Java/SecureClassLoader/SecureClassLoader/)

## Métodos
* [defineClass()](/Java/SecureClassLoader/defineClass)
* [getPermissions()](/Java/SecureClassLoader/getPermissions)

## Ejemplo
~~~java
{{ site.data.Java.S.SecureClassLoader.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
