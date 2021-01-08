---
title: DataFlavor.tryToLoadClass()
permalink: Java/DataFlavor/tryToLoadClass
date: 2021-01-04
key: JavaJava.D.DataFlavor
category: java
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
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **ClassLoader fallback**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader fallback" %}

## Clase Padre
[DataFlavor](/Java/DataFlavor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataFlavor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
