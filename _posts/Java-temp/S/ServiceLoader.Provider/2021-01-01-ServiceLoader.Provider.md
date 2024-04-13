---
title: ServiceLoader.Provider
permalink: /Java/ServiceLoader/Provider/
date: 2021-01-11
key: Java.S.ServiceLoader.Provider
category: Java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ServiceLoader.Provider.description }}

## Sintaxis
~~~java
public static interface ServiceLoader.Provider<S> extends Supplier<S>
~~~

## Métodos
* [get()](/Java/ServiceLoader/Provider/get)
* [type()](/Java/ServiceLoader/Provider/type)

## Ejemplo
~~~java
{{ site.data.Java.S.ServiceLoader.Provider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServiceLoader.Provider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
