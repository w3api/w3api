---
title: ThreadGroup.setDaemon()
permalink: Java/ThreadGroup/setDaemon
date: 2021-01-11
key: JavaJava.T.ThreadGroup
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadGroup.metodos valor="setDaemon" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setDaemon(boolean daemon)
~~~

## Parámetros
* **boolean daemon**,  {% include w3api/param_description.html metodo=_dato parametro="boolean daemon" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[ThreadGroup](/Java/ThreadGroup/)

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
