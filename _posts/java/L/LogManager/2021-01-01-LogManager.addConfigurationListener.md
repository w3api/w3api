---
title: LogManager.addConfigurationListener()
permalink: Java/LogManager/addConfigurationListener
date: 2021-01-11
key: JavaJava.L.LogManager
category: java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogManager.metodos valor="addConfigurationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LogManager addConfigurationListener(Runnable listener)
~~~

## Parámetros
* **Runnable listener**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable listener" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LogManager](/Java/LogManager/)

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
