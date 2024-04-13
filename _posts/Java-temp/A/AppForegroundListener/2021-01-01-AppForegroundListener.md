---
title: AppForegroundListener
permalink: /Java/AppForegroundListener/
date: 2021-01-11
key: Java.A.AppForegroundListener
category: Java
tags: ['java se', 'java.awt.desktop', 'java.desktop', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AppForegroundListener.description }}

## Sintaxis
~~~java
public interface AppForegroundListener extends SystemEventListener
~~~

## Métodos
* [appMovedToBackground()](/Java/AppForegroundListener/appMovedToBackground)
* [appRaisedToForeground()](/Java/AppForegroundListener/appRaisedToForeground)

## Ejemplo
~~~java
{{ site.data.Java.A.AppForegroundListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AppForegroundListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
