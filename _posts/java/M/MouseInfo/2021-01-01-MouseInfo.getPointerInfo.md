---
title: MouseInfo.getPointerInfo()
permalink: /Java/MouseInfo/getPointerInfo/
date: 2021-01-11
key: Java.M.MouseInfo
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseInfo.metodos valor="getPointerInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static PointerInfo getPointerInfo() throws HeadlessException
~~~

## Excepciones
[HeadlessException](/Java/HeadlessException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[MouseInfo](/Java/MouseInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
