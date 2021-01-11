---
title: AccessibleObject.setAccessible()
permalink: Java/AccessibleObject/setAccessible
date: 2021-01-10
key: JavaJava.A.AccessibleObject
category: java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessibleObject.metodos valor="setAccessible" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setAccessible(boolean flag)
public static void setAccessible(AccessibleObject[] array, boolean flag)
~~~

## Parámetros
* **AccessibleObject[] array**,  {% include w3api/param_description.html metodo=_dato parametro="AccessibleObject[] array" %}
* **boolean flag**,  {% include w3api/param_description.html metodo=_dato parametro="boolean flag" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [InaccessibleObjectException](/Java/InaccessibleObjectException/)

## Clase Padre
[AccessibleObject](/Java/AccessibleObject/)

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
