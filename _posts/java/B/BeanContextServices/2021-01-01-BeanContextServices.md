---
title: BeanContextServices
permalink: Java/BeanContextServices
date: 2021-01-11
key: JavaJava.B.BeanContextServices
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BeanContextServices.description }}

## Sintaxis
~~~java
public interface BeanContextServices extends BeanContext, BeanContextServicesListener
~~~

## Métodos
* [addBeanContextServicesListener()](/Java/BeanContextServices/addBeanContextServicesListener)
* [addService()](/Java/BeanContextServices/addService)
* [getCurrentServiceClasses()](/Java/BeanContextServices/getCurrentServiceClasses)
* [getCurrentServiceSelectors()](/Java/BeanContextServices/getCurrentServiceSelectors)
* [getService()](/Java/BeanContextServices/getService)
* [hasService()](/Java/BeanContextServices/hasService)
* [releaseService()](/Java/BeanContextServices/releaseService)
* [removeBeanContextServicesListener()](/Java/BeanContextServices/removeBeanContextServicesListener)
* [revokeService()](/Java/BeanContextServices/revokeService)

## Ejemplo
~~~java
{{ site.data.Java.B.BeanContextServices.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextServices.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
