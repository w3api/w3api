---
title: NashornException.getScriptFrames()
permalink: Java/NashornException/getScriptFrames
date: 2021-01-04
key: JavaJava.N.NashornException
category: java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NashornException.metodos valor="getScriptFrames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static StackTraceElement[] getScriptFrames(Throwable exception)
~~~

## Parámetros
* **Throwable exception**,  {% include w3api/param_description.html metodo=_data parametro="Throwable exception" %}

## Clase Padre
[NashornException](/Java/NashornException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NashornException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
