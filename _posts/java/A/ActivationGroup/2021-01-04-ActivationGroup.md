---
title: ActivationGroup
permalink: Java/ActivationGroup
date: 2021-01-04
key: JavaJava.A.ActivationGroup
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.ActivationGroup.description }}

## Sintaxis
~~~java
public abstract class ActivationGroup extends UnicastRemoteObject implements ActivationInstantiator
~~~

## Constructores
* [ActivationGroup()](/Java/ActivationGroup/ActivationGroup/)

## Métodos
* [activeObject()](/Java/ActivationGroup/activeObject)
* [createGroup()](/Java/ActivationGroup/createGroup)
* [currentGroupID()](/Java/ActivationGroup/currentGroupID)
* [getSystem()](/Java/ActivationGroup/getSystem)
* [inactiveGroup()](/Java/ActivationGroup/inactiveGroup)
* [inactiveObject()](/Java/ActivationGroup/inactiveObject)
* [setSystem()](/Java/ActivationGroup/setSystem)

## Ejemplo
~~~java
{{ site.data.Java.A.ActivationGroup.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationGroup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
