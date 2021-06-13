---
title: ModuleFinder
permalink: Java/ModuleFinder
date: 2021-01-11
key: JavaJava.M.ModuleFinder
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.ModuleFinder.description }}

## Sintaxis
~~~java
public interface ModuleFinder
~~~

## Métodos
* [compose()](/Java/ModuleFinder/compose)
* [find()](/Java/ModuleFinder/find)
* [findAll()](/Java/ModuleFinder/findAll)
* [of()](/Java/ModuleFinder/of)
* [ofSystem()](/Java/ModuleFinder/ofSystem)

## Ejemplo
~~~java
{{ site.data.Java.M.ModuleFinder.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleFinder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
