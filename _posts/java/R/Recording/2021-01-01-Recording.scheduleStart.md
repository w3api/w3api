---
title: Recording.scheduleStart()
permalink: /Java/Recording/scheduleStart/
date: 2021-01-11
key: Java.R.Recording
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Recording.metodos valor="scheduleStart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void scheduleStart(Duration delay)
~~~

## Parámetros
* **Duration delay**,  {% include w3api/param_description.html metodo=_dato parametro="Duration delay" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[Recording](/Java/Recording/)

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
