---
title: DynUnionOperations
permalink: /Java/DynUnionOperations/
date: 2021-01-11
key: Java.D.DynUnionOperations
category: Java
tags: ['java se', 'org.omg.DynamicAny', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DynUnionOperations.description }}

## Sintaxis
~~~java
public interface DynUnionOperations extends DynAnyOperations
~~~

## Métodos
* [discriminator_kind()](/Java/DynUnionOperations/discriminator_kind)
* [get_discriminator()](/Java/DynUnionOperations/get_discriminator)
* [has_no_active_member()](/Java/DynUnionOperations/has_no_active_member)
* [member()](/Java/DynUnionOperations/member)
* [member_kind()](/Java/DynUnionOperations/member_kind)
* [member_name()](/Java/DynUnionOperations/member_name)
* [set_discriminator()](/Java/DynUnionOperations/set_discriminator)
* [set_to_default_member()](/Java/DynUnionOperations/set_to_default_member)
* [set_to_no_active_member()](/Java/DynUnionOperations/set_to_no_active_member)

## Ejemplo
~~~java
{{ site.data.Java.D.DynUnionOperations.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DynUnionOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
