---
title: RMIClassLoaderSpi.getClassAnnotation()
permalink: /Java/RMIClassLoaderSpi/getClassAnnotation/
date: 2021-01-11
key: Java.R.RMIClassLoaderSpi
category: Java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIClassLoaderSpi.metodos valor="getClassAnnotation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String getClassAnnotation(Class<?> cl)
~~~

## Parámetros
* **Class&lt;?&gt; cl**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> cl" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RMIClassLoaderSpi](/Java/RMIClassLoaderSpi/)

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
