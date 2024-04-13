---
title: BeanContextChildSupport
permalink: /Java/BeanContextChildSupport/
date: 2021-01-11
key: Java.B.BeanContextChildSupport
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BeanContextChildSupport.description }}

## Sintaxis
~~~java
public class BeanContextChildSupport extends Object implements BeanContextChild, BeanContextServicesListener, Serializable
~~~

## Constructores
* [BeanContextChildSupport()](/Java/BeanContextChildSupport/BeanContextChildSupport/)

## Campos
* [beanContext](/Java/BeanContextChildSupport/beanContext/)
* [beanContextChildPeer](/Java/BeanContextChildSupport/beanContextChildPeer/)
* [pcSupport](/Java/BeanContextChildSupport/pcSupport/)
* [rejectedSetBCOnce](/Java/BeanContextChildSupport/rejectedSetBCOnce/)
* [vcSupport](/Java/BeanContextChildSupport/vcSupport/)

## Métodos
* [addPropertyChangeListener()](/Java/BeanContextChildSupport/addPropertyChangeListener/)
* [addVetoableChangeListener()](/Java/BeanContextChildSupport/addVetoableChangeListener/)
* [firePropertyChange()](/Java/BeanContextChildSupport/firePropertyChange/)
* [fireVetoableChange()](/Java/BeanContextChildSupport/fireVetoableChange/)
* [getBeanContext()](/Java/BeanContextChildSupport/getBeanContext/)
* [getBeanContextChildPeer()](/Java/BeanContextChildSupport/getBeanContextChildPeer/)
* [initializeBeanContextResources()](/Java/BeanContextChildSupport/initializeBeanContextResources/)
* [isDelegated()](/Java/BeanContextChildSupport/isDelegated/)
* [releaseBeanContextResources()](/Java/BeanContextChildSupport/releaseBeanContextResources/)
* [removePropertyChangeListener()](/Java/BeanContextChildSupport/removePropertyChangeListener/)
* [removeVetoableChangeListener()](/Java/BeanContextChildSupport/removeVetoableChangeListener/)
* [serviceAvailable()](/Java/BeanContextChildSupport/serviceAvailable/)
* [serviceRevoked()](/Java/BeanContextChildSupport/serviceRevoked/)
* [setBeanContext()](/Java/BeanContextChildSupport/setBeanContext/)
* [validatePendingSetBeanContext()](/Java/BeanContextChildSupport/validatePendingSetBeanContext/)

## Ejemplo
~~~java
{{ site.data.Java.B.BeanContextChildSupport.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextChildSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
