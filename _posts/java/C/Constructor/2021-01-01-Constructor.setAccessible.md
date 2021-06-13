---
title: Constructor.setAccessible()
permalink: /Java/Constructor/setAccessible/
date: 2021-01-11
key: Java.C.Constructor
category: Java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Constructor.metodos valor="setAccessible" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setAccessible(boolean flag)
~~~

## Parámetros
* **boolean flag**,  {% include w3api/param_description.html metodo=_dato parametro="boolean flag" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [InaccessibleObjectException](/Java/InaccessibleObjectException/)

## Clase Padre
[Constructor](/Java/Constructor/)

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
