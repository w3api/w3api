---
title: ScreenSleepListener
permalink: /Java/ScreenSleepListener/
date: 2021-01-11
key: Java.S.ScreenSleepListener
category: Java
tags: ['java se', 'java.awt.desktop', 'java.desktop', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ScreenSleepListener.description }}

## Sintaxis
~~~java
public interface ScreenSleepListener extends SystemEventListener
~~~

## Métodos
* [screenAboutToSleep()](/Java/ScreenSleepListener/screenAboutToSleep)
* [screenAwoke()](/Java/ScreenSleepListener/screenAwoke)

## Ejemplo
~~~java
{{ site.data.Java.S.ScreenSleepListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScreenSleepListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
