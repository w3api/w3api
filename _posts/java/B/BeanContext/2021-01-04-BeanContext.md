---
title: BeanContext
permalink: Java/BeanContext
date: 2021-01-04
key: JavaJava.B.BeanContext
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BeanContext.description }}

## Sintaxis
~~~java
public interface BeanContext extends BeanContextChild, Collection, DesignMode, Visibility
~~~

## Campos
* [globalHierarchyLock](/Java/BeanContext/globalHierarchyLock)

## Métodos
* [addBeanContextMembershipListener()](/Java/BeanContext/addBeanContextMembershipListener)
* [getResource()](/Java/BeanContext/getResource)
* [getResourceAsStream()](/Java/BeanContext/getResourceAsStream)
* [instantiateChild()](/Java/BeanContext/instantiateChild)
* [removeBeanContextMembershipListener()](/Java/BeanContext/removeBeanContextMembershipListener)

## Ejemplo
~~~java
{{ site.data.Java.B.BeanContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
