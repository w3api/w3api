---
title: NamingEnumeration
permalink: Java/NamingEnumeration
date: 2021-01-11
key: JavaJava.N.NamingEnumeration
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.N.NamingEnumeration.description }}

## Sintaxis
~~~java
public interface NamingEnumeration<T> extends Enumeration<T>
~~~

## Métodos
* [close()](/Java/NamingEnumeration/close)
* [hasMore()](/Java/NamingEnumeration/hasMore)
* [next()](/Java/NamingEnumeration/next)

## Ejemplo
~~~java
{{ site.data.Java.N.NamingEnumeration.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NamingEnumeration.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
