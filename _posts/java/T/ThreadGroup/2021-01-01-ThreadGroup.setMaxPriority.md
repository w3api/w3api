---
title: ThreadGroup.setMaxPriority()
permalink: /Java/ThreadGroup/setMaxPriority/
date: 2021-01-11
key: Java.T.ThreadGroup
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadGroup.metodos valor="setMaxPriority" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setMaxPriority(int pri)
~~~

## Parámetros
* **int pri**,  {% include w3api/param_description.html metodo=_dato parametro="int pri" %}

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
