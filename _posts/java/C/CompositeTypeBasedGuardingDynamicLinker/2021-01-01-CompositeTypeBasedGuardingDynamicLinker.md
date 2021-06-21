---
title: CompositeTypeBasedGuardingDynamicLinker
permalink: /Java/CompositeTypeBasedGuardingDynamicLinker/
date: 2021-01-11
key: Java.C.CompositeTypeBasedGuardingDynamicLinker
category: Java
tags: ['java se', 'jdk.dynalink.linker.support', 'jdk.dynalink', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompositeTypeBasedGuardingDynamicLinker.description }}

## Sintaxis
~~~java
public class CompositeTypeBasedGuardingDynamicLinker extends Object implements TypeBasedGuardingDynamicLinker
~~~

## Constructores
* [CompositeTypeBasedGuardingDynamicLinker()](/Java/CompositeTypeBasedGuardingDynamicLinker/CompositeTypeBasedGuardingDynamicLinker/)

## Métodos
* [canLinkType()](/Java/CompositeTypeBasedGuardingDynamicLinker/canLinkType)
* [optimize()](/Java/CompositeTypeBasedGuardingDynamicLinker/optimize)

## Ejemplo
~~~java
{{ site.data.Java.C.CompositeTypeBasedGuardingDynamicLinker.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CompositeTypeBasedGuardingDynamicLinker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
