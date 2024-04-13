---
title: PersistentMBean
permalink: /Java/PersistentMBean/
date: 2021-01-11
key: Java.P.PersistentMBean
category: Java
tags: ['java se', 'javax.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PersistentMBean.description }}

## Sintaxis
~~~java
public interface PersistentMBean
~~~

## Métodos
* [load()](/Java/PersistentMBean/load)
* [store()](/Java/PersistentMBean/store)

## Ejemplo
~~~java
{{ site.data.Java.P.PersistentMBean.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PersistentMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
