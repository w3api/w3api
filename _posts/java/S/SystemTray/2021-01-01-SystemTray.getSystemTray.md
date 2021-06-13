---
title: SystemTray.getSystemTray()
permalink: /Java/SystemTray/getSystemTray/
date: 2021-01-11
key: Java.S.SystemTray
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SystemTray.metodos valor="getSystemTray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SystemTray getSystemTray()
~~~

## Excepciones
[HeadlessException](/Java/HeadlessException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SystemTray](/Java/SystemTray/)

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
