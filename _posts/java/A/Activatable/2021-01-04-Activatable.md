---
title: Activatable
permalink: Java/Activatable
date: 2021-01-04
key: JavaJava.A.Activatable
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.Activatable.description }}

## Sintaxis
~~~java
public abstract class Activatable extends RemoteServer
~~~

## Constructores
* [Activatable()](/Java/Activatable/Activatable/)

## Métodos
* [exportObject()](/Java/Activatable/exportObject)
* [getID()](/Java/Activatable/getID)
* [inactive()](/Java/Activatable/inactive)
* [register()](/Java/Activatable/register)
* [unexportObject()](/Java/Activatable/unexportObject)
* [unregister()](/Java/Activatable/unregister)

## Ejemplo
~~~java
{{ site.data.Java.A.Activatable.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Activatable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
