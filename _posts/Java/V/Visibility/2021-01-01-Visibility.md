---
title: Visibility
permalink: /Java/Visibility/
date: 2021-01-11
key: Java.V.Visibility
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.Visibility.description }}

## Sintaxis
~~~java
public interface Visibility
~~~

## Métodos
* [avoidingGui()](/Java/Visibility/avoidingGui)
* [dontUseGui()](/Java/Visibility/dontUseGui)
* [needsGui()](/Java/Visibility/needsGui)
* [okToUseGui()](/Java/Visibility/okToUseGui)

## Ejemplo
~~~java
{{ site.data.Java.V.Visibility.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.Visibility.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
