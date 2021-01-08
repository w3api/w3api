---
title: ActivationSystem
permalink: Java/ActivationSystem
date: 2021-01-04
key: JavaJava.A.ActivationSystem
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.ActivationSystem.description }}

## Sintaxis
~~~java
public interface ActivationSystem extends Remote
~~~

## Campos
* [SYSTEM_PORT](/Java/ActivationSystem/SYSTEM_PORT)

## Métodos
* [activeGroup()](/Java/ActivationSystem/activeGroup)
* [getActivationDesc()](/Java/ActivationSystem/getActivationDesc)
* [getActivationGroupDesc()](/Java/ActivationSystem/getActivationGroupDesc)
* [registerGroup()](/Java/ActivationSystem/registerGroup)
* [registerObject()](/Java/ActivationSystem/registerObject)
* [setActivationDesc()](/Java/ActivationSystem/setActivationDesc)
* [setActivationGroupDesc()](/Java/ActivationSystem/setActivationGroupDesc)
* [shutdown()](/Java/ActivationSystem/shutdown)
* [unregisterGroup()](/Java/ActivationSystem/unregisterGroup)
* [unregisterObject()](/Java/ActivationSystem/unregisterObject)

## Ejemplo
~~~java
{{ site.data.Java.A.ActivationSystem.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationSystem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
