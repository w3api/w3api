---
title: StandardMBean
permalink: Java/StandardMBean
date: 2021-01-04
key: JavaJava.S.StandardMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StandardMBean.description }}

## Sintaxis
~~~java
public class StandardMBean extends Object implements DynamicMBean, MBeanRegistration
~~~

## Constructores
* [StandardMBean()](/Java/StandardMBean/StandardMBean/)

## Métodos
* [cacheMBeanInfo()](/Java/StandardMBean/cacheMBeanInfo)
* [getCachedMBeanInfo()](/Java/StandardMBean/getCachedMBeanInfo)
* [getClassName()](/Java/StandardMBean/getClassName)
* [getConstructors()](/Java/StandardMBean/getConstructors)
* [getDescription()](/Java/StandardMBean/getDescription)
* [getImpact()](/Java/StandardMBean/getImpact)
* [getImplementation()](/Java/StandardMBean/getImplementation)
* [getImplementationClass()](/Java/StandardMBean/getImplementationClass)
* [getMBeanInfo()](/Java/StandardMBean/getMBeanInfo)
* [getMBeanInterface()](/Java/StandardMBean/getMBeanInterface)
* [getParameterName()](/Java/StandardMBean/getParameterName)
* [postDeregister()](/Java/StandardMBean/postDeregister)
* [postRegister()](/Java/StandardMBean/postRegister)
* [preDeregister()](/Java/StandardMBean/preDeregister)
* [preRegister()](/Java/StandardMBean/preRegister)
* [setImplementation()](/Java/StandardMBean/setImplementation)

## Ejemplo
~~~java
{{ site.data.Java.S.StandardMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
