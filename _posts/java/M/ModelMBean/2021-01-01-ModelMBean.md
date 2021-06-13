---
title: ModelMBean
permalink: Java/ModelMBean
date: 2021-01-11
key: JavaJava.M.ModelMBean
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.ModelMBean.description }}

## Sintaxis
~~~java
public interface ModelMBean extends DynamicMBean, PersistentMBean, ModelMBeanNotificationBroadcaster
~~~

## Métodos
* [setManagedResource()](/Java/ModelMBean/setManagedResource)
* [setModelMBeanInfo()](/Java/ModelMBean/setModelMBeanInfo)

## Ejemplo
~~~java
{{ site.data.Java.M.ModelMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModelMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
