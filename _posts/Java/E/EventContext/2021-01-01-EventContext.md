---
title: EventContext
permalink: /Java/EventContext/
date: 2021-01-11
key: Java.E.EventContext
category: Java
tags: ['java se', 'javax.naming.event', 'java.naming', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EventContext.description }}

## Sintaxis
~~~java
public interface EventContext extends Context
~~~

## Campos
* [OBJECT_SCOPE](/Java/EventContext/OBJECT_SCOPE/)
* [ONELEVEL_SCOPE](/Java/EventContext/ONELEVEL_SCOPE/)
* [SUBTREE_SCOPE](/Java/EventContext/SUBTREE_SCOPE/)

## Métodos
* [addNamingListener()](/Java/EventContext/addNamingListener/)
* [removeNamingListener()](/Java/EventContext/removeNamingListener/)
* [targetMustExist()](/Java/EventContext/targetMustExist/)

## Ejemplo
~~~java
{{ site.data.Java.E.EventContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
