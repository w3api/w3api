---
title: AttachProvider
permalink: /Java/AttachProvider/
date: 2021-01-11
key: Java.A.AttachProvider
category: Java
tags: ['java se', 'com.sun.tools.attach.spi', 'jdk.attach', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AttachProvider.description }}

## Sintaxis
~~~java
public abstract class AttachProvider extends Object
~~~

## Constructores
* [AttachProvider()](/Java/AttachProvider/AttachProvider/)

## Métodos
* [attachVirtualMachine()](/Java/AttachProvider/attachVirtualMachine)
* [listVirtualMachines()](/Java/AttachProvider/listVirtualMachines)
* [name()](/Java/AttachProvider/name)
* [providers()](/Java/AttachProvider/providers)
* [type()](/Java/AttachProvider/type)

## Ejemplo
~~~java
{{ site.data.Java.A.AttachProvider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttachProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
