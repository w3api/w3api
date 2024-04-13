---
title: DataFlavor.tryToLoadClass()
permalink: /Java/DataFlavor/tryToLoadClass/
date: 2021-01-11
key: Java.D.DataFlavor
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataFlavor.metodos valor="tryToLoadClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static Class<?> tryToLoadClass(String className, ClassLoader fallback)
~~~

## Parámetros
* **ClassLoader fallback**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader fallback" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Clase Padre
[DataFlavor](/Java/DataFlavor/)

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
