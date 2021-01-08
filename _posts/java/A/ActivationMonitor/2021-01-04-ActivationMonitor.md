---
title: ActivationMonitor
permalink: Java/ActivationMonitor
date: 2021-01-04
key: JavaJava.A.ActivationMonitor
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.ActivationMonitor.description }}

## Sintaxis
~~~java
public interface ActivationMonitor extends Remote
~~~

## Métodos
* [activeObject()](/Java/ActivationMonitor/activeObject)
* [inactiveGroup()](/Java/ActivationMonitor/inactiveGroup)
* [inactiveObject()](/Java/ActivationMonitor/inactiveObject)

## Ejemplo
~~~java
{{ site.data.Java.A.ActivationMonitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationMonitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
