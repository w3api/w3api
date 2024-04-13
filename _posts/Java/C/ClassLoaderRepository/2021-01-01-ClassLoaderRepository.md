---
title: ClassLoaderRepository
permalink: /Java/ClassLoaderRepository/
date: 2021-01-11
key: Java.C.ClassLoaderRepository
category: Java
tags: ['java se', 'javax.management.loading', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassLoaderRepository.description }}

## Sintaxis
~~~java
public interface ClassLoaderRepository
~~~

## Métodos
* [loadClass()](/Java/ClassLoaderRepository/loadClass/)
* [loadClassBefore()](/Java/ClassLoaderRepository/loadClassBefore/)
* [loadClassWithout()](/Java/ClassLoaderRepository/loadClassWithout/)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassLoaderRepository.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ClassLoaderRepository.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
