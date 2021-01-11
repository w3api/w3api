---
title: TypeBasedGuardingDynamicLinker
permalink: Java/TypeBasedGuardingDynamicLinker
date: 2021-01-11
key: JavaJava.T.TypeBasedGuardingDynamicLinker
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TypeBasedGuardingDynamicLinker.description }}

## Sintaxis
~~~java
public interface TypeBasedGuardingDynamicLinker extends GuardingDynamicLinker
~~~

## Métodos
* [canLinkType()](/Java/TypeBasedGuardingDynamicLinker/canLinkType)

## Ejemplo
~~~java
{{ site.data.Java.T.TypeBasedGuardingDynamicLinker.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeBasedGuardingDynamicLinker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
