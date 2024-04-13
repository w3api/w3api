---
title: BeanContextEvent
permalink: /Java/BeanContextEvent/
date: 2021-01-11
key: Java.B.BeanContextEvent
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BeanContextEvent.description }}

## Sintaxis
~~~java
public abstract class BeanContextEvent extends EventObject
~~~

## Constructores
* [BeanContextEvent()](/Java/BeanContextEvent/BeanContextEvent/)

## Campos
* [propagatedFrom](/Java/BeanContextEvent/propagatedFrom)

## Métodos
* [getBeanContext()](/Java/BeanContextEvent/getBeanContext)
* [getPropagatedFrom()](/Java/BeanContextEvent/getPropagatedFrom)
* [isPropagated()](/Java/BeanContextEvent/isPropagated)
* [setPropagatedFrom()](/Java/BeanContextEvent/setPropagatedFrom)

## Ejemplo
~~~java
{{ site.data.Java.B.BeanContextEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
