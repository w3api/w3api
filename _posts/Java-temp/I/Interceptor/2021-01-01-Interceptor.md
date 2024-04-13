---
title: Interceptor
permalink: /Java/Interceptor/
date: 2021-01-11
key: Java.I.Interceptor
category: Java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.Interceptor.description }}

## Sintaxis
~~~java
public interface Interceptor extends InterceptorOperations, Object, IDLEntity
~~~

## Ejemplo
~~~java
{{ site.data.Java.I.Interceptor.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.Interceptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
