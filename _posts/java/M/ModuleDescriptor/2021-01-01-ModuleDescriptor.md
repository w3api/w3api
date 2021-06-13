---
title: ModuleDescriptor
permalink: /Java/ModuleDescriptor/
date: 2021-01-11
key: Java.M.ModuleDescriptor
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.ModuleDescriptor.description }}

## Sintaxis
~~~java
public class ModuleDescriptor extends Object implements Comparable<ModuleDescriptor>
~~~

## Métodos
* [compareTo()](/Java/ModuleDescriptor/compareTo)
* [equals()](/Java/ModuleDescriptor/equals)
* [exports()](/Java/ModuleDescriptor/exports)
* [hashCode()](/Java/ModuleDescriptor/hashCode)
* [isAutomatic()](/Java/ModuleDescriptor/isAutomatic)
* [isOpen()](/Java/ModuleDescriptor/isOpen)
* [mainClass()](/Java/ModuleDescriptor/mainClass)
* [modifiers()](/Java/ModuleDescriptor/modifiers)
* [name()](/Java/ModuleDescriptor/name)
* [newAutomaticModule()](/Java/ModuleDescriptor/newAutomaticModule)
* [newModule()](/Java/ModuleDescriptor/newModule)
* [newOpenModule()](/Java/ModuleDescriptor/newOpenModule)
* [opens()](/Java/ModuleDescriptor/opens)
* [packages()](/Java/ModuleDescriptor/packages)
* [provides()](/Java/ModuleDescriptor/provides)
* [rawVersion()](/Java/ModuleDescriptor/rawVersion)
* [read()](/Java/ModuleDescriptor/read)
* [requires()](/Java/ModuleDescriptor/requires)
* [toNameAndVersion()](/Java/ModuleDescriptor/toNameAndVersion)
* [toString()](/Java/ModuleDescriptor/toString)
* [uses()](/Java/ModuleDescriptor/uses)
* [version()](/Java/ModuleDescriptor/version)

## Ejemplo
~~~java
{{ site.data.Java.M.ModuleDescriptor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
