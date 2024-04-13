---
title: DynStructOperations
permalink: /Java/DynStructOperations/
date: 2021-01-11
key: Java.D.DynStructOperations
category: Java
tags: ['java se', 'org.omg.DynamicAny', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DynStructOperations.description }}

## Sintaxis
~~~java
public interface DynStructOperations extends DynAnyOperations
~~~

## Métodos
* [current_member_kind()](/Java/DynStructOperations/current_member_kind/)
* [current_member_name()](/Java/DynStructOperations/current_member_name/)
* [get_members()](/Java/DynStructOperations/get_members/)
* [get_members_as_dyn_any()](/Java/DynStructOperations/get_members_as_dyn_any/)
* [set_members()](/Java/DynStructOperations/set_members/)
* [set_members_as_dyn_any()](/Java/DynStructOperations/set_members_as_dyn_any/)

## Ejemplo
~~~java
{{ site.data.Java.D.DynStructOperations.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DynStructOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
