---
title: DynValueOperations
permalink: /Java/DynValueOperations/
date: 2021-01-11
key: Java.D.DynValueOperations
category: Java
tags: ['java se', 'org.omg.DynamicAny', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DynValueOperations.description }}

## Sintaxis
~~~java
public interface DynValueOperations extends DynValueCommonOperations
~~~

## Métodos
* [current_member_kind()](/Java/DynValueOperations/current_member_kind/)
* [current_member_name()](/Java/DynValueOperations/current_member_name/)
* [get_members()](/Java/DynValueOperations/get_members/)
* [get_members_as_dyn_any()](/Java/DynValueOperations/get_members_as_dyn_any/)
* [set_members()](/Java/DynValueOperations/set_members/)
* [set_members_as_dyn_any()](/Java/DynValueOperations/set_members_as_dyn_any/)

## Ejemplo
~~~java
{{ site.data.Java.D.DynValueOperations.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DynValueOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
