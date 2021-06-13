---
title: PathSearchingVirtualMachine
permalink: /Java/PathSearchingVirtualMachine/
date: 2021-01-11
key: Java.P.PathSearchingVirtualMachine
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PathSearchingVirtualMachine.description }}

## Sintaxis
~~~java
public interface PathSearchingVirtualMachine extends VirtualMachine
~~~

## Métodos
* [baseDirectory()](/Java/PathSearchingVirtualMachine/baseDirectory)
* [bootClassPath()](/Java/PathSearchingVirtualMachine/bootClassPath)
* [classPath()](/Java/PathSearchingVirtualMachine/classPath)

## Ejemplo
~~~java
{{ site.data.Java.P.PathSearchingVirtualMachine.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PathSearchingVirtualMachine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
